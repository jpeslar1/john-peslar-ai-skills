#!/usr/bin/env python3
"""Register built voice skills in the voice-dna plugin.

Usage: python3 scripts/voice-dna/register_voice.py slug="Display Name" [slug="Display Name" ...]

For each slug (without the -voice suffix): adds ./<slug>-voice to the voice-dna
plugin's skills and keywords in .claude-plugin/marketplace.json, appends the
display name to the plugin description, creates plugins/voice-dna/skills/<slug>-voice,
then runs scripts/sync-agent-skills.sh. Idempotent. README rows are still manual.
"""
import json, os, subprocess, sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def main(args):
    pairs = [a.split('=', 1) for a in args]
    for slug, _ in pairs:
        if not os.path.isfile(f'{REPO}/{slug}-voice/SKILL.md'):
            sys.exit(f'missing {slug}-voice/SKILL.md')
    path = f'{REPO}/.claude-plugin/marketplace.json'
    m = json.load(open(path))
    vd = [x for x in m['plugins'] if x['name'] == 'voice-dna'][0]
    names = [n for _, n in pairs if n not in vd['description']]
    if names:
        vd['description'] = vd['description'].replace('. Each skill', ', ' + ', '.join(names) + '. Each skill', 1)
    for slug, _ in pairs:
        if f'./{slug}-voice' not in vd['skills']:
            vd['skills'].append(f'./{slug}-voice')
        if slug not in vd['keywords']:
            vd['keywords'].append(slug)
        link = f'{REPO}/plugins/voice-dna/skills/{slug}-voice'
        if not os.path.islink(link):
            os.symlink(f'../../../{slug}-voice', link)
    open(path, 'w').write(json.dumps(m, indent=2, ensure_ascii=False) + '\n')
    print('voices registered:', len(vd['skills']))
    out = subprocess.run(['bash', f'{REPO}/scripts/sync-agent-skills.sh'], capture_output=True, text=True, cwd=REPO)
    print((out.stdout.strip().splitlines() or [''])[-1])


if __name__ == '__main__':
    main(sys.argv[1:])
