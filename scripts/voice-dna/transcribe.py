#!/usr/bin/env python3
"""Transcribe a podcast episode with speaker labels through OpenRouter STT.

Usage:
  OPENROUTER_API_KEY=... python3 scripts/voice-dna/transcribe.py <audio-url-or-path> --out DIR
      [--model microsoft/mai-transcribe-2] [--start-min 0] [--max-min 60]
      [--chunk-min 20] [--budget 1.00] [--workers 3]

Downloads the audio (if a URL), re-encodes a mono 16 kHz 32 kbps MP3, splits it
into chunks (OpenRouter's non-OpenAI providers cap uploads at 25 MB and upstream
calls time out at 60 s), and sends each chunk to /api/v1/audio/transcriptions
with diarization on. Writes DIR/chunk-NN.json (raw responses) and
DIR/transcript.md (one line per segment: [hh:mm:ss] cNN-S<speaker>: text).

Speaker numbers are assigned per chunk by the provider, so c01-S0 and c02-S0
are NOT guaranteed to be the same person. Identify the speaker in each chunk
from context before quoting. Machine transcripts are `documented` grade in a
voice corpus, never `verbatim`.
"""
import argparse, base64, concurrent.futures, json, os, shutil, subprocess, sys, time, urllib.request

API = 'https://openrouter.ai/api/v1/audio/transcriptions'
DIARIZE = {
    'microsoft/mai-transcribe-2': {'azure': {'diarization': {'enabled': True}}},
}


def hms(s):
    s = int(s)
    return f'{s // 3600:02d}:{s % 3600 // 60:02d}:{s % 60:02d}'


def fetch(src, out):
    if os.path.exists(src):
        return src
    path = os.path.join(out, 'source' + (os.path.splitext(src.split('?')[0])[1] or '.mp3'))
    if not os.path.exists(path):
        req = urllib.request.Request(src, headers={'User-Agent': 'Mozilla/5.0 (Macintosh) voice-dna-transcribe'})
        with urllib.request.urlopen(req, timeout=300) as r, open(path, 'wb') as f:
            shutil.copyfileobj(r, f)
    return path


def make_chunks(path, out, start_min, max_min, chunk_min):
    dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', path],
                               capture_output=True, text=True, check=True).stdout.strip())
    start, end = start_min * 60, min(dur, (start_min + max_min) * 60)
    chunks, t, i = [], start, 1
    while t < end - 5:
        length = min(chunk_min * 60, end - t)
        cp = os.path.join(out, f'chunk-{i:02d}.mp3')
        if not os.path.exists(cp):
            subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(t), '-t', str(length), '-i', path,
                            '-ac', '1', '-ar', '16000', '-b:a', '32k', cp], check=True)
        chunks.append((i, t, cp))
        t += length; i += 1
    return dur, chunks


def transcribe_chunk(key, model, i, offset, cp, out):
    jp = os.path.join(out, f'chunk-{i:02d}.json')
    if os.path.exists(jp):
        return i, offset, json.load(open(jp))
    body = {'model': model, 'input_audio': {'data': base64.b64encode(open(cp, 'rb').read()).decode(), 'format': 'mp3'},
            'language': 'en', 'response_format': 'verbose_json', 'timestamp_granularities': ['segment']}
    if model in DIARIZE:
        body['provider'] = {'options': DIARIZE[model]}
    last = None
    for attempt in range(3):
        try:
            req = urllib.request.Request(API, data=json.dumps(body).encode(), method='POST',
                                         headers={'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'})
            with urllib.request.urlopen(req, timeout=180) as r:
                data = json.load(r)
            json.dump(data, open(jp, 'w'))
            return i, offset, data
        except urllib.error.HTTPError as e:
            last = f'HTTP {e.code}: {e.read()[:300]!r}'
        except Exception as e:  # network or timeout
            last = repr(e)
        time.sleep(5 * (attempt + 1))
    raise RuntimeError(f'chunk {i} failed: {last}')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('src'); ap.add_argument('--out', required=True)
    ap.add_argument('--model', default='microsoft/mai-transcribe-2')
    ap.add_argument('--start-min', type=float, default=0); ap.add_argument('--max-min', type=float, default=60)
    ap.add_argument('--chunk-min', type=float, default=20); ap.add_argument('--budget', type=float, default=1.0)
    ap.add_argument('--workers', type=int, default=3)
    a = ap.parse_args()
    key = os.environ.get('OPENROUTER_API_KEY') or sys.exit('OPENROUTER_API_KEY is not set')
    os.makedirs(a.out, exist_ok=True)
    path = fetch(a.src, a.out)
    dur, chunks = make_chunks(path, a.out, a.start_min, a.max_min, a.chunk_min)
    print(f'source {dur / 60:.1f} min; transcribing {len(chunks)} chunks from minute {a.start_min:g}', file=sys.stderr)
    results, cost = [], 0.0
    with concurrent.futures.ThreadPoolExecutor(a.workers) as ex:
        futs = [ex.submit(transcribe_chunk, key, a.model, i, off, cp, a.out) for i, off, cp in chunks]
        for f in concurrent.futures.as_completed(futs):
            i, off, data = f.result()
            cost += (data.get('usage') or {}).get('cost') or 0
            results.append((i, off, data))
            if cost > a.budget:
                for g in futs: g.cancel()
                print(f'budget {a.budget} exceeded at ${cost:.4f}; stopping', file=sys.stderr)
                break
    results.sort()
    lines = [f'# Transcript', '', f'Source: {a.src}', f'Model: {a.model} (machine transcript, diarized per chunk; documented grade)',
             f'Range: minute {a.start_min:g} to {a.start_min + sum(1 for _ in results) * a.chunk_min:g}; cost ${cost:.4f}', '']
    for i, off, data in results:
        lines.append(f'## Chunk {i:02d} (starts {hms(off)})'); lines.append('')
        segs = data.get('segments') or [{'start': 0, 'text': data.get('text', ''), 'speaker': None}]
        for s in segs:
            spk = s.get('speaker')
            lines.append(f"[{hms(off + (s.get('start') or 0))}] c{i:02d}-S{spk if spk is not None else '?'}: {s.get('text', '').strip()}")
        lines.append('')
    open(os.path.join(a.out, 'transcript.md'), 'w').write('\n'.join(lines))
    print(json.dumps({'chunks': len(results), 'cost_usd': round(cost, 4), 'transcript': os.path.join(a.out, 'transcript.md')}))


if __name__ == '__main__':
    main()
