#!/usr/bin/env python3
"""Check built voice skills against the house contract.

Usage: python3 scripts/voice-dna/verify_voice.py [--research-dir DIR] slug [slug ...]

Checks: the three files exist; strict-YAML frontmatter with matching name and the
"Not affiliated" line; SKILL.md length and required sections; no em or en dashes
outside quoted lines; source-map sections; corpus item count matches
DIR/<slug>.md when --research-dir is given. Dash hits inside the Punctuation
Override or quoted titles are expected; read them before fixing.
"""
import os, re, sys
import yaml

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REQ = ['## Voice DNA', '### Cadence and rhythm', '### Hook patterns', '### Lexicon', '### Taboo list',
       '### Punctuation and formatting', '### POV and stance', '### Emotional register', '## Signature Moves',
       '## Playbooks', '## Anti-patterns', '## Punctuation Override', '## Guardrails', '## Output Format']


def research_count(path):
    t = open(path).read()
    m = re.search(r'^## Excerpts(.*?)(^## |\Z)', t, re.S | re.M)
    return len(re.findall(r'^\d+\. ', m.group(1), re.M)) if m else -1


def dash_lines(txt):
    return [l for l in txt.splitlines() if ('\u2014' in l or '\u2013' in l)
            and not l.strip().startswith(('>', '"'))]


def check(slug, rdir):
    d = f'{REPO}/{slug}-voice'
    files = ['SKILL.md', 'references/voice-corpus.md', 'references/source-map.md']
    miss = [f for f in files if not os.path.exists(f'{d}/{f}')]
    if miss:
        return f'{slug}: MISSING {miss}'
    sk, co, sm = (open(f'{d}/{f}').read() for f in files)
    probs = []
    try:
        fm = yaml.safe_load(sk.split('---')[1])
        if fm.get('name') != f'{slug}-voice':
            probs.append(f"name={fm.get('name')}")
        if 'Not affiliated' not in fm.get('description', ''):
            probs.append('no affiliation line')
    except Exception as e:
        probs.append(f'YAML FAIL {str(e)[:60]}')
    n = sk.count('\n')
    if not 140 <= n <= 185:
        probs.append(f'SKILL lines={n}')
    probs += [f'missing {r}' for r in REQ if r not in sk]
    for label, txt in [('SKILL', sk), ('source-map', sm)]:
        if dash_lines(txt):
            probs.append(f'{label} dash lines x{len(dash_lines(txt))}')
    ci = len(re.findall(r'^\d+\. ', co, re.M))
    if rdir:
        ri = research_count(f'{rdir}/{slug}.md')
        if ci != ri:
            probs.append(f'corpus items {ci} vs research {ri}')
    if 'Research date:' not in co or 'Research date:' not in sm:
        probs.append('research date missing')
    for sec in ['## Known gaps', 'Anything published after', '## Refresh instructions', '## Pattern notes']:
        if sec not in sm:
            probs.append(f'source-map lacks {sec}')
    pb = re.findall(r'^### (.+)$', sk.split('## Playbooks')[1].split('## Anti-patterns')[0], re.M) if '## Playbooks' in sk else []
    return f'{slug}: lines={n} items={ci} playbooks={pb} ' + ('OK' if not probs else 'CHECK: ' + '; '.join(probs))


if __name__ == '__main__':
    args = sys.argv[1:]
    rdir = None
    if args[:1] == ['--research-dir']:
        rdir, args = args[1], args[2:]
    for s in args:
        print(check(s.removesuffix('-voice'), rdir))
