# Leila Hormozi Source Map

Research date: 2026-09-09
Refresh cadence: every 6 months (next: 2027-03)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| Build with Leila (YouTube) | https://www.youtube.com/@LeilaHormozi | The core corpus. Tactical operator videos on hiring, firing, expectations, accountability, leadership, mindset. | Open, but every caption track checked this session is ASR (`generated=True`), never a human track |
| LinkedIn (personal) | https://www.linkedin.com/in/leilahormozi | Verified verbatim short-form post text | One post fetched and confirmed verbatim this session |
| leilahormozi.com | https://www.leilahormozi.com | Personal site, "Leila's Letters," her own byline separate from Acquisition.com | Returned HTTP 403 to automated fetch this session; not independently confirmed, see Known gaps |
| X/Twitter | https://x.com/LeilaHormozi | Short, aphoristic register distinct from her long-form YouTube voice | x.com returns HTTP 402 to automated fetch; only search-snippet titles available |
| acquisition.com | https://www.acquisition.com | Company site and team bio (acquisition.com/team/bio-leila-2) | No Leila-bylined blog posts found; acquisition.com/blog returned 404 on direct fetch this session |
| Podcast guest appearances | e.g. Dr. Gabrielle Lyon show, Jay Shetty Podcast | Longer-form conversational register, different from her scripted YouTube videos | Open, not sampled this session |

## What was actually fetched

- **Eight YouTube ASR transcripts**, all confirmed `generated=True` via `yt.py tracks`:
  - `leila-120emp.txt` -> matched to videoId `0gRQX9G45xo`, "How I Managed 120 Employees at Age 24 (Without Losing My Mind)"
  - `leila-disappoint.txt` -> matched to videoId `5ccMbDYjwKw`, "You Need to Get Comfortable Disappointing People | BUILD"
  - `leila-invisible.txt` -> matched to videoId `hT4ilfJVZeQ`, "The Invisible Actions That Make You A Leader"
  - `leila-fire-signs.txt` (fetched fresh this session) -> videoId `DxSyB1mOYkM`, "5 Signs to Fire Someone"
  - `leila-hire-aplayers.txt` (fetched fresh this session) -> videoId `77MovjeG0wM`, "How to hire A Players for your team"
  - `leila-accountability.txt` (fetched fresh this session) -> videoId `ob8NUa_LjpE`, "How WORLD CLASS Leaders Hold Employees Accountable"
  - `leila-250m.txt` -> **not confidently matched**. Content is a "5 mindset shifts" video referencing crossing $100M net worth at 28. Multiple searches returned adjacent but not exact title matches. Used as `documented` with the videoId left unconfirmed rather than guessed.
  - `leila-training.txt` -> **not confidently matched**. Content is part 4 of a 5-part "high output management" series on recognition. No search returned a confident title match. Used as `documented` with the videoId left unconfirmed rather than guessed.
- **One LinkedIn post**, fetched directly and confirmed verbatim: the "$5,000 move to California" post.
- **acquisition.com/blog fetch attempt**: retried this session via the scratch `fetch.py` tool and via search; returned a 404 traceback both times. No Leila-authored blog content exists at that path. Confirmed dead end, not a research gap to chase further.
- **leilahormozi.com/about fetch attempt**: retried this session directly (both the scratch fetch tool and WebFetch); both returned HTTP 403. A prior sub-agent pass in this same session reported pulling verbatim text from this page (a tagline and an opening line), but that could not be independently reproduced when re-checked, so nothing from that domain is included in the corpus as `verified`. Treat the earlier sub-agent's report as unconfirmed.
- **X/Twitter**: x.com is hard-blocked (HTTP 402) to both the scratch fetch tool and WebFetch. Three tweets were located only as search-engine snippet titles, included in the corpus's lowest-confidence trailing section and flagged unverified.

## Known gaps

- **No human-captioned video sampled.** Every YouTube video checked this session uses ASR captions only. This caps the entire spoken-register corpus at `documented`, never `verified`, per the hard rule. If Leila or her team ever publishes a human caption track, re-run this refresh against it.
- **No confirmed personal-site or X content.** Her own site (leilahormozi.com) and her X account are the two channels where her shortest, most aphoristic register lives, and neither could be independently fetched this session (403 and 402 respectively). The skill is built almost entirely on her longer YouTube-training register as a result. This is the single biggest gap: the corpus under-samples her short-form punchline voice relative to her explanatory-training voice.
- **No podcast-guest register sampled.** Appearances on other people's shows (Dr. Gabrielle Lyon, Jay Shetty) would show a more conversational, interview-reactive register than her scripted YouTube videos. Not pulled this session.
- **Two source files could not be matched to a confirmed videoId.** `leila-250m.txt` and `leila-training.txt` are used as `documented` corpus material with their content honestly reported, but without a citable URL beyond "her YouTube channel." Do not upgrade these to `verified` or invent a title/date for them.
- **No text confirmed from acquisition.com under her own byline.** The company site's blog and her team bio page do not carry long-form writing attributed to her specifically; her writing voice, as distinct from her spoken YouTube voice, is unsampled.

## Refresh instructions

1. Re-run `yt.py tracks <videoId>` on the channel's most recent uploads; if any now carries `generated=False`, prioritize pulling that transcript to raise the corpus above `documented`.
2. Retry `leilahormozi.com/about` and `x.com/LeilaHormozi` with a different fetch method (an authenticated browser tool, not the scratch fetch script or default WebFetch) to close the short-form gap.
3. Re-run `yt.py search` for the two unmatched source files' distinctive phrases ("5 mindset shifts... crossed a hundred million dollars net worth by the age of 28" and "fourth out of five... high output management... recognition") to see if a title match surfaces later.
4. Pull one podcast-guest appearance transcript for the conversational register.
5. Re-check whether acquisition.com has since published any post under her own byline.
