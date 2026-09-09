# Scott Galloway Source Map

Research date: 2026-09-09
Refresh cadence: every 6 months (next: 2027-03)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| No Mercy / No Malice newsletter | https://www.profgalloway.com | The core corpus. Weekly long-form essays on economics, tech power, and generational wealth. | Open, server-rendered, scrapes cleanly |
| Bubble.ai | https://www.profgalloway.com/bubble-ai | AI-market bubble psychology, the stat cascade, the false-equivalence gag | Open |
| Earners vs Owners | https://www.profgalloway.com/earners-vs-owners | The core Earners/Owners framework, tax-burden stats | Open |
| Second Mouse.AI | https://www.profgalloway.com/second-mouse-ai | The renamed-maxim move, parallel-structure lists | Open |
| The Epstein Tax | https://www.profgalloway.com/the-epstein-tax | Wealth-inequality argument, the Gini coefficient analogy | Open |
| Rare Earths | https://www.profgalloway.com/rare-earths | Geopolitical dead-empire analogies, the renamed-analogy thesis line | Open |
| Slow Dopa | https://www.profgalloway.com/slow-dopa | Book-excerpt register, heaviest profanity sample | Open |
| The 'Vcel' Movement | https://www.profgalloway.com/the-vcel-movement | The renamed-euphemism move | Open |
| A Touch Better | https://www.profgalloway.com/a-touch-better | Older (2022) sample, lighter dash count, useful as a register baseline | Open |
| The Algebra of Resistance | https://www.profgalloway.com/the-algebra-of-resistance | Activism-era register (2026), not pulled into the numbered corpus, read for context only | Open |
| Prof G Pod / Pivot | YouTube, Apple Podcasts | Spoken register, cadence, ad-lib profanity | Open, video/audio |
| No Mercy / No Malice book excerpts | Notes on Being a Man, Adrift: America in 100 Charts | Longer narrative register, book-length argument structure | Newsletter excerpts open; full books are purchase |
| LinkedIn / X | linkedin.com/in/profgalloway, x.com/profgalloway | Short-form register, current hot takes | Open but not sampled here |

## What was actually fetched

Nine newsletter posts were pulled as raw text from profgalloway.com this session: `a-touch-better` (Jul 22, 2022), `bubble-ai` (May 24, 2024), `earners-vs-owners` (May 17, 2024), `second-mouse-ai` (Jun 14, 2024), `rare-earths` (Jan 9, 2026), `slow-dopa` (Jan 2, 2026), `the-vcel-movement` (Jan 16, 2026), `the-algebra-of-resistance` (Feb 20, 2026), `the-epstein-tax` (Feb 27, 2026). All nine scraped cleanly with a plain HTTP fetch (site is server-rendered; only nav chrome, share buttons, and reader comments needed stripping). The URL pattern `https://www.profgalloway.com/<slug>` was re-confirmed live during this session by re-fetching `the-epstein-tax`. Eight of the nine posts supplied the verbatim corpus (items 1-31); `the-algebra-of-resistance` was read for register context but no line from it made the numbered corpus. One podcast transcript was pulled via `yt.py tx` for videoId `uNrjrDV9-YQ` ("The Algebra of Wealth: Scott Galloway on How To Get Rich," The Prof G Pod). `yt.py tracks uNrjrDV9-YQ` returned only `en generated=True`, so every line from it is labeled `documented`, not verbatim.

## Known gaps

- **No short-form corpus.** LinkedIn and X are his real short-form register and were not sampled at all. The LinkedIn Content Expert playbook in SKILL.md is inferred from his long-form habits compressed down, not from sampled short posts. This is a real gap; fix on refresh.
- **No human-captioned spoken sample.** Every YouTube caption track checked this session was `generated=True` (ASR). No line of his spoken register in this skill is verified; all four spoken excerpts are `documented` and may contain ASR transcription errors, especially around numbers and proper nouns.
- **Only one podcast episode sampled, and it is a solo monologue segment, not a two-host Pivot-style exchange.** The Pivot co-host banter register (with Kara Swisher) is a materially different mode, more interruption and cross-talk, and is not represented here at all.
- **Neither book was read in full.** Notes on Being a Man and Adrift: America in 100 Charts are both referenced only through newsletter excerpts the author himself published, not the full text. Longer narrative structure from the books is not captured.
- **Sample skews recent (2026) plus two 2024 posts and one 2022 post**, so the corpus is reasonably current, but no 2023 or 2025 posts were pulled; confirm nothing material changed in the interim on refresh.
- **The em-dash count analysis in SKILL.md's Punctuation Override is based only on the nine sampled posts**, not a full-archive count. Treat the "roughly 17 per post" figure as an estimate from this sample, not a verified population statistic.
- **Profanity frequency is eyeballed, not counted systematically.** The corpus shows profanity appearing once or twice per long post across the sample, but this was not run as a rigorous frequency count across his full archive.

## Refresh instructions

1. Re-fetch the newsletter index at profgalloway.com and pull any post published since February 2026 that argues a new named framework (in the pattern of Earners vs Owners, the Donroe Doctrine, the Epstein Tax).
2. Pull at least one Pivot episode transcript to capture the two-host banter register, distinct from the Prof G Pod solo monologue register sampled here.
3. Check whether a human-captioned (generated=False) track exists for any recent Prof G Pod or Pivot episode; if so, replace the documented spoken items with verified ones.
4. Re-run the em-dash count across a larger sample (aim for 15-20 posts) to firm up the Punctuation Override's numeric claim.
5. Pull a short LinkedIn or X sample to build a genuinely sampled short-form playbook instead of an inferred one.
6. Re-verify every [VERIFY]-flagged statistic in generated output against a current source before publishing; several of the sampled numbers (tax rates, market caps, wealth-tax country counts) are time-sensitive and will be stale within the six-month refresh window.
