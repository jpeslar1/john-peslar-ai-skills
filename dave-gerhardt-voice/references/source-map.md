# Dave Gerhardt Source Map

Research date: 2026-09-09
Refresh cadence: every 6 months (next: 2027-03)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| Exit Five articles (his byline) | https://exitfive.com/articles | The long-form corpus. Bylined, dated, practitioner-facing. | Open, server-rendered, scrapes cleanly |
| Marketing Is Broken | https://exitfive.com/articles/marketing-is-broken-why-youre-so-busy-and-still-not-getting-anything-done/ | Busy mode versus builder mode, performative productivity | Open |
| How to Lead a High Functioning Marketing Org | https://exitfive.com/articles/how-to-lead-a-high-functioning-marketing-org/ | The calendar audit, zombie meetings, async to inform | Open |
| Personal site | https://davegerhardt.com/ | His own bio wording and positioning | Open |
| Exit Five newsletter | exitfive.com | The recurring issue format | Signup |
| Exit Five podcast | exitfive.com/podcast | Spoken register, interview style | Open |
| Book: Founder Brand (2021) | print | The founder-brand thesis. Lines in the corpus are `documented` from summaries. | Purchase |
| LinkedIn | linkedin.com/in/davegerhardt | His best-known register: short, opinionated, marketer-to-marketer posts | Public post permalinks render logged out; profile feed itself is a login wall |
| Exit Five community | exitfive.com | Where the audience anecdotes and quotes come from | Paid membership |

## What was actually fetched

Two full Exit Five articles carrying his byline, plus his personal site, were pulled as raw text on 2026-09-09. The site is server-rendered and scrapes cleanly.

## What was fetched on 2026-09-09

- Three of his own public LinkedIn post permalinks, pulled as raw server-rendered HTML with a plain fetch script, logged out, no login and no bypass: "Sometimes you need to go backward to go forward" (activity 7166042639358742528), "What was your path into marketing?" (activity 7055134980871446528), and "Hey I'm Dave Gerhardt" (activity 7378371732056883200). All three scraped cleanly with full post text, reaction counts, and comments visible in the logged-out HTML. 10 short excerpts drawn from them are now in `voice-corpus.md` as items 30-39, labeled `verified`.
- YouTube captions were not pulled this session. `yt.py tx` returned `IpBlocked` from `youtube_transcript_api` (this machine's IP is rate-limited by YouTube) on the first attempt; per the session's instructions this was not retried. `yt.py search` still works and returned candidate videos (a B2B Vault masterclass, an Exit Five interview, an OnBrand talk) but none were transcribed.
- Attempts to find a third-party article quoting a Gerhardt LinkedIn post verbatim with a screenshot or blockquote did not turn up a usable `documented` source distinct from the LinkedIn permalinks themselves; the direct logged-out fetch made that route unnecessary for this pass.

## Known gaps

- **His LinkedIn register is now sampled, but thinly.** 10 excerpts across 3 posts (items 30-39), all fetched logged out from his own public permalinks this session. That is enough to see the pattern (flat opening line, short paragraphs, a self-deprecating aside, a plain-spoken close) but it is not the 20-30 post sample the original refresh instructions called for. Treat the LinkedIn Content Expert playbook as evidence-backed now, not purely inferred, but still thin.
- **X/Twitter is not captured at all.** No X posts were fetched or searched this session. If he has a distinct short-form register there separate from LinkedIn, it remains unknown.
- **Bylined does not mean solely written.** Exit Five publishes bylined articles that may involve editorial support. Treat these as house-plus-Gerhardt rather than as pure personal voice.
- **Founder Brand was not read.** Items 40 to 42 come from third-party summaries and are labeled `documented`.
- **No podcast transcript.** His interview register, which is a large part of his public presence, is absent. YouTube captions are currently blocked from this machine (see above); this was not the reason podcast audio specifically wasn't pulled, but it forecloses one route to it.
- **Article sample is still narrow.** Two Exit Five articles, both from July 2025, both about meetings and productivity. His positioning, brand, and demand-gen arguments are under-sampled.

## Refresh instructions

1. Capture 15 to 20 more recent LinkedIn posts (beyond the 3 already sampled) and expand the short-form section. Public permalinks render logged out via a plain HTTP fetch with a standard browser User-Agent; no login or bypass is needed. Try `SCRATCH/fetch.py <permalink>` first.
2. Pull three more Exit Five articles on different topics, especially brand versus demand and positioning.
3. Retry YouTube captions (`yt.py tracks` / `yt.py tx`) from a different IP if the 429/IpBlocked persists; otherwise pull one podcast transcript by another route for the spoken and interview register.
4. If any Founder Brand line is going into client copy, verify against the book.
5. Search X for his posts; if a scriptable public route exists without login, sample 15-20 short posts there.
6. Re-verify any third-party research statistic at its original source before republishing.
