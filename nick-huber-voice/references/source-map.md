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
| LinkedIn | linkedin.com/in/nickhuber | Same short-form register for a business audience | Login wall |
| Sweaty Startup podcast | sweatystartup.com/podcasts | Spoken register, deal detail | Open |
| Deal breakdowns | sweatystartup.com | Real numbers on real acquisitions | Open, some gated |

## Known gaps

- **The short-form provocative register is not captured.** Everything in the corpus is long-form blog or book prose, which is calmer and more measured than the X and LinkedIn posts he is best known for. The Contrarian Take Generator playbook is therefore built on his stated positions rather than on sampled short posts. This is the single most important gap to close on refresh.
- **No deal-breakdown numbers captured.** The Build-in-Public playbook describes the shape but has no sampled example with real figures. Pull one full deal breakdown on refresh.
- **No podcast transcript.** The spoken register is under-sampled.
- **Company roster shifts.** He runs and invests in several businesses and the promo block changes. Do not hardcode a company name into generated copy; the corpus deliberately names only what appeared in the fetched posts.

## Refresh instructions

1. Pull 20 to 30 recent short posts from X for the provocative register and add a short-form section to the corpus.
2. Pull one complete deal breakdown with its numbers.
3. Confirm the newsletter promo-block format is still top-of-issue with a divider.
4. Re-check the blog index for posts published since this research date.
5. Never carry his company names or figures into client copy without re-verifying them on his live properties.
