# Nick Huber Source Map

Research date: 2026-09-09
Refresh cadence: every 6 months (next: 2027-03)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| Sweaty Startup blog | https://www.sweatystartup.com/blog/ | The long-form corpus. Story-led essays on sales, operating, hiring, delayed gratification. | Open, server-rendered, scrapes cleanly |
| Life is sales | https://www.sweatystartup.com/blog/life-is-sales | His sales method and the Ithaca scene | Open |
| Why skilled operators beat passionate founders | https://www.sweatystartup.com/blog/why-skilled-operators-beat-passionate-founders | The operator thesis and the parallel-professions run | Open |
| These skills virtually guarantee success | https://www.sweatystartup.com/blog/these-skills-virtually-guarantee-success | Delayed gratification, plus the newsletter promo-block format | Open |
| The Sweaty Startup (book) | Publisher excerpt at porchlightbooks.com | The boring-opportunity thesis in book prose | Excerpt open, book purchase |
| X account | https://x.com/sweatystartup | The provocative short-form register. Threads, one-liners, the fights. | Open, rate-limited, bulk reading needs auth |
| LinkedIn | linkedin.com/in/sweatystartup | Same short-form register for a business audience | Public post permalinks render logged out; profile feed itself is a login wall |
| Sweaty Startup podcast | sweatystartup.com/podcasts | Spoken register, deal detail | Open |
| Deal breakdowns | sweatystartup.com | Real numbers on real acquisitions | Open, some gated |

## What was fetched on 2026-09-09

- Five of his own public LinkedIn post permalinks, pulled as raw server-rendered HTML with a plain fetch script, logged out, no login and no bypass: "Self storage development DOES NOT pencil right now" (activity 7125504267162947584), "I bought a self storage facility in October 2020..." (activity 7090743891250872321), "When we built our self storage facility from the ground up..." (activity 7087440984325722112), "Linkedin is full of BAD BUSINESS ADVICE" (activity 6953097335631417345), "The 'never give up' advice is bullshit" (activity 7043667772425347073), and "10 things I've changed my mind on recently" (activity 7025823215629320192). All scraped cleanly with full post text visible in the logged-out HTML. 13 short excerpts from these are now in `voice-corpus.md` as items 39-51, labeled `verified`.
- A broader search surfaced additional public LinkedIn posts, including one built on "the worst thing you can do as an entrepreneur is hire a social justice warrior" and one on family/gender-role framing. Both were deliberately excluded from the corpus. Per this session's editorial instruction, this corpus samples his contrarian, receipts-and-numbers register (bad advice, boring business, changed-my-mind reversals) and not his culture-war/inflammatory register, even though the latter is also public and also short-form. This is a deliberate scope choice, stated here openly, not a claim that the excluded material doesn't exist.
- YouTube captions were not pulled this session. `yt.py tx` returned `IpBlocked` from `youtube_transcript_api` on the first attempt (this machine's IP is currently rate-limited by YouTube); per this session's instructions it was not retried.
- X/Twitter was not fetched. Search located his handle and a few status URLs but no scriptable, unauthenticated route to bulk post text was used or attempted beyond a discovery search.

## Known gaps

- **The short-form register is now sampled, but only on LinkedIn, and only the contrarian-not-inflammatory slice of it.** 13 excerpts across 5 posts (items 39-51), all fetched logged out from his own public permalinks this session. That is enough to confirm the caps-for-emphasis, profanity-on-ideas-not-people, and numbered-list patterns seen in his long-form, but it undersamples relative to the 20-30 post target, and it deliberately leaves out his more inflammatory public material (see above). Do not claim the "provocative short-form register" gap is fully closed: what's closed is the boring-business-contrarian slice of it.
- **X is completely uncaptured.** Zero posts pulled from X this session. If his X voice differs from his LinkedIn voice in degree of provocation, that difference is unknown here.
- **No deal-breakdown numbers with full commentary captured beyond the two LinkedIn number-posts already in the corpus (items 40-41).** The Build-in-Public playbook has real sampled examples now but still no full multi-post deal walkthrough with expense-line detail.
- **No podcast transcript.** The spoken register is under-sampled. YouTube captions are currently blocked from this machine (see above), which forecloses one possible route.
- **Company roster shifts.** He runs and invests in several businesses and the promo block changes. Do not hardcode a company name into generated copy; the corpus deliberately names only what appeared in the fetched posts.

## Refresh instructions

1. Pull 15 to 20 more recent LinkedIn posts (beyond the 5 already sampled) via `SCRATCH/fetch.py <permalink>`, logged out, no login needed for public permalinks.
2. Pull 20 to 30 recent short posts from X for the provocative register, if a scriptable unauthenticated route is found; otherwise note it stays gated.
3. When selecting new short-form posts, keep applying the editorial filter above: contrarian and blunt is in scope, bigoted or harassing content is not, and any close call gets logged in this file rather than silently included or silently dropped.
4. Pull one complete deal breakdown with its numbers.
5. Retry YouTube captions from a different IP if the 429/IpBlocked persists; otherwise pull one podcast transcript by another route.
6. Confirm the newsletter promo-block format is still top-of-issue with a divider.
7. Re-check the blog index for posts published since this research date.
8. Never carry his company names or figures into client copy without re-verifying them on his live properties.
