#!/usr/bin/env python3
"""Generate <slug>-voice/references/voice-corpus.md from a research file.

Usage: python3 scripts/voice-dna/gen_corpus.py <config.json>

Config keys:
  research       path to the research markdown (needs a `## Excerpts` block of
                 items shaped `N. > quote` (one or more `>` lines) followed by an
                 indented source line)
  out            output path for voice-corpus.md
  name           display name
  prov           provenance paragraph
  punct          punctuation paragraph, or "" to omit
  breaks         {item_number: "## Section heading"} inserted before that item
  stats          list of derived-stat bullets
  research_date  YYYY-MM-DD (default: today)
  first_heading  heading emitted before the first item (default '## Verbatim excerpts')
  end_marker     optional string that ends the excerpt block early
  extra          optional list of lines appended before the stats

Prints the number of items written; compare it to the research file's count.
"""
import datetime, json, re, sys


def gen(research, out, name, prov, punct, breaks, stats, research_date=None,
        first_heading='## Verbatim excerpts', end_marker=None, extra=None):
    src = open(research).read()
    start = src.index('## Excerpts')
    end = len(src)
    for m in ['## Voice patterns', '## Gaps']:
        if m in src[start:]:
            end = min(end, src.index(m, start))
    if end_marker and end_marker in src[start:end]:
        end = src.index(end_marker, start)
    ex = src[start:end]
    # The lookahead keeps continuation `>` lines inside the quote instead of
    # mistaking the second quote line for the source line.
    items = re.findall(r'\n\s*(\d+)\. > (.*?)\n[ \t]+(?![ \t>])([^\n]*?)\n', ex, re.S)
    date = research_date or datetime.date.today().isoformat()
    lines = [f'# {name} Voice Corpus', '', f'Research date: {date}', '',
             "The excerpts below are short quotations from public posts, articles, and talks, "
             "included under fair use for style analysis and attribution. They are third-party "
             "content and NOT covered by this repository's MIT license.", '',
             f'**Provenance note.** {prov}', '']
    if punct:
        lines += [f'**Punctuation note.** {punct}', '']
    lines += [first_heading, '']
    for n, q, s in items:
        q = ' / '.join(l.strip().lstrip('> ').strip() for l in q.split('\n') if l.strip())
        if int(n) in breaks:
            lines += [breaks[int(n)], '']
        lines += [f'{n}. "{q}"', f'    {s.strip()}', '']
    if extra:
        lines += extra
    lines += ['## Derived stats (honest estimates from this corpus)', ''] + [f'- {s}' for s in stats] + ['']
    open(out, 'w').write('\n'.join(lines))
    return len(items)


if __name__ == '__main__':
    cfg = json.load(open(sys.argv[1]))
    cfg['breaks'] = {int(k): v for k, v in cfg.get('breaks', {}).items()}
    print(gen(**cfg))
