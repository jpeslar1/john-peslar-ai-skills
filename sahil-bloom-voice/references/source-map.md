# Sahil Bloom Source Map

Research date: 2026-09-09
Refresh cadence: every 6 months (next: 2027-03)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| Newsletter | https://www.sahilbloom.com/newsletter | The core corpus. Weekly Curiosity Chronicle essays and the Friday Five roundup format. | Open, but the site is a Webflow build with heavy cart/nav/CMS-placeholder chrome around the real article text |
| The Scarlet Robe Effect | https://www.sahilbloom.com/newsletter/the-scarlet-robe-effect | Named-effect essay format, the Bought Status Test | Open |
| Why You Need to Subtract: The Vasa Effect | https://www.sahilbloom.com/newsletter/why-you-need-to-subtract-the-vasa-effect | Second named-effect essay, sourcing Klotz's research | Open |
| The Traffic Jam Theory of Success | https://www.sahilbloom.com/newsletter/the-traffic-jam-theory-of-success | Third named-effect essay, current AI-era register | Open |
| 9 Harsh Truths Nobody Told You About Success | https://www.sahilbloom.com/newsletter/9-harsh-truths-nobody-told-you-about-success | Numbered-list essay format | Open |
| Stop Making a 5-Year Plan (Do This Instead) | https://www.sahilbloom.com/newsletter/stop-making-a-5-year-plan-do-this-instead | The Adjacent Possible, mentor-question hook | Open |
| It Was Just a Game of Catch | https://www.sahilbloom.com/newsletter/it-was-just-a-game-of-catch | Pure personal-memory essay, no named framework | Open |
| The Hidden Debt of Convenience | https://www.sahilbloom.com/newsletter/the-hidden-debt-of-convenience | Scroll-stop-observation hook, borrowed quotes credited by name | Open |
| Why You Need a Side Quest in Life | https://www.sahilbloom.com/newsletter/why-you-need-a-side-quest-in-life | Cited-study hook (inattentional blindness study) | Open |
| The Friday Five (Two Wolves edition) | https://www.sahilbloom.com/newsletter (archive) | Short-form five-part roundup format, distinct from the long essay shape | Open |
| The 5 Types of Wealth (2025) | book | The full five-type framework, only sampled here through the Talks at Google interview and his own site references | Purchase |
| Talks at Google interview | https://www.youtube.com/watch?v=NegTHmVuepk | Spoken register, human caption track (generated=False), his own words on the five types and his personal turning point | Open, YouTube |
| X / Twitter | x.com/SahilBloom | Short-form register, current takes and threads | Not fetched this session |

## What was actually fetched

Nine newsletter posts were pulled as raw text from sahilbloom.com/newsletter via a prior session's fetch, cached at `SCRATCH/raw/sb-*.txt`, and read in full this session with the CMS boilerplate, shopping-cart chrome, and repeated Webflow placeholder text ("What's a Rich Text element?") identified and skipped. The real article text starts consistently after that filler on each page and scrapes cleanly once isolated. One YouTube video, "Sahil Bloom | The 5 Types of Wealth | Talks at Google" (videoId NegTHmVuepk), was confirmed via `yt.py tracks` to have a human (generated=False) English caption track, and the full transcript was pulled via `yt.py tx` and cached at `SCRATCH/voicetx/sahil-talksatgoogle-NegTHmVuepk.txt`. Because that caption track is human-authored rather than ASR, his spoken turns from it are treated as `verified`, not `documented`.

## Known gaps

- **The book itself was not read.** The 5 Types of Wealth is behind purchase. Everything about the five-type framework in this skill comes from his own newsletter references to it and his spoken explanation in the Talks at Google interview, not the book text itself. Verify chapter-level detail against the book before teaching it as his exact structure.
- **No X/Twitter corpus.** His short-form thread register is a real and distinct part of the voice (hooks compressed to a single tweet, thread-unrolled frameworks) and is not sampled here. The LinkedIn Content Expert playbook is inferred from his newsletter's short-line rhythm rather than from sampled short-form posts. Fix on refresh.
- **Only one spoken source.** One Talks at Google interview is the entire spoken corpus. His podcast-guest appearances (Nick Bare, James Altucher, SuperPsyched) were found in search but not fetched. More spoken samples would strengthen confidence that the interview register generalizes.
- **Newsletter sample skews mid-to-late 2026 with one outlier from March 2025.** Eight of nine posts are from July through September 2026, clustered in a two-month window. This is a narrow time slice; his tone earlier in the newsletter's run (2021-2023, before the book's success) is not sampled and may differ.
- **No secondary summaries were used or needed.** Unlike the April Dunford exemplar, no `documented` or `sketch` tier was required for this corpus; every item traces to a verbatim primary fetch. This is a strength, not a gap, but it means the corpus has not been cross-checked against a second observer's account of his style.

## Refresh instructions

1. Re-fetch https://www.sahilbloom.com/newsletter and pull any essay published since September 2026 that introduces a new named framework.
2. Pull at least one X/Twitter thread for the short-form register, and one additional podcast appearance transcript (Nick Bare, James Altucher, or SuperPsyched were found in search but not fetched this session).
3. If the book The 5 Types of Wealth becomes available to read directly, verify the chapter-level structure against the summary currently sourced only from the Talks at Google interview.
4. Confirm the newsletter subscriber count and any other cited statistics (800,000+ subscribers as of this research date) are still current before quoting them in generated copy.
5. Check whether any newer named effect has emerged as his signature move continues; the pattern (historical or scientific anecdote to named framework) is durable and should keep producing fresh examples worth adding.
