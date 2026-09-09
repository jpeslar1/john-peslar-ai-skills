# Chris Orlob Source Map

Research date: 2026-09-09
Refresh cadence: every 6 months (next: 2027-03)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| pclub.io / Caliber blog | https://www.pclub.io/blog | Current long-form register, 2023-2026, byline-confirmed posts | Open, server-rendered, scrapes cleanly |
| Sales Discovery Training | https://www.pclub.io/blog/sales-discovery-training | Discovery mechanics, current vocabulary | Open |
| Master C-Suite Selling | https://www.pclub.io/blog/cant-sell-to-c-suite-executives | Executive-selling stats and steps | Open |
| Overcoming Pricing Objections | https://www.pclub.io/blog/overcoming-price-objections | Negotiation and price-objection register | Open |
| How To Run a Flawless SaaS Product Demo | https://www.pclub.io/blog/saas-product-demo | Demo structure, current version (fetched for confirmation, not deeply excerpted) | Open |
| Gong.io blog (archived) | web.archive.org captures of gong.io/blog/* | His 2019-era Gong Labs data posts, the source of the "N million calls analyzed" register | Wayback Machine only; the live gong.io blog no longer carries these under his byline |
| YouTube: pclub.io channel | videos -Fgt5R6bhAY, A4KdGq4SMR4, OMPXf4FL9WM | Spoken register, ASR only | Open, auto-generated captions |
| LinkedIn | linkedin.com/in/chrisorlob | Primary current short-form/carousel register | Login wall, not fetched |
| pclub.io / Caliber homepage | https://www.pclub.io | Company positioning, course/community offer language | Open |

## What was actually fetched

- `gong.txt` (via Wayback Machine `fetch.py`): three concatenated blog posts. Two are Chris Orlob bylines and were used - "The 11 Best Discovery Call Tips for Sales" (March 28, 2019, captured 2019-09-15) and "7 Elements of 'Insanely' Persuasive Sales Product Demos" (February 1, 2019, captured 2019-08-25). The third, "The Ultimate Guide to Asking Sales Questions," is byline Devin Reed, not Chris Orlob, and was deliberately excluded from the corpus.
- Four pclub.io/Caliber blog posts fetched live with `fetch.py` and confirmed byline "by Chris Orlob" in the rendered text: `sales-discovery-training` (8/5/25), `cant-sell-to-c-suite-executives` (updated 5/21/26, originally June 2023), `overcoming-price-objections` (2/13/24), `saas-product-demo` (12/12/23, used only to confirm current demo-structure claims, not deeply excerpted). The site is server-rendered and scraped cleanly.
- Three YouTube videos, all confirmed ASR (`generated=True`) via `yt.py tracks`: `-Fgt5R6bhAY` (cost-of-inaction training clip), `A4KdGq4SMR4` (four-question urgency-building training, includes his Gong origin story), `OMPXf4FL9WM` (nine bad habits keeping SaaS sellers off the leaderboard). Full transcripts pulled and sliced; all quotes from these are `documented`, not `verified`, per the ASR rule.
- `WebSearch` was used only to find pclub.io blog article URLs (Google does not index the blog's internal links cleanly through the plain fetch), not to harvest quotes.

## Known gaps

- **No verified LinkedIn corpus.** Chris Orlob is LinkedIn-heavy and the spec calls out his "carousel/listicle energy" specifically, but linkedin.com sits behind a login wall and was not fetched. The LinkedIn playbook in SKILL.md is inferred from his long-form listicle habits (exact-count titles, numbered claims-as-headers, stat-per-claim), not from sampled LinkedIn posts. This is the single biggest gap. Fix on refresh by pulling a signed-in LinkedIn export or a public post mirror if one becomes fetchable.
- **No podcast or stage-talk corpus.** He is reportedly a frequent guest on sales podcasts and speaks at events; none were sampled. His spoken cadence here comes only from two YouTube training videos, both scripted "free training" monologues rather than conversational podcast appearances.
- **No book.** Unlike April Dunford, Chris Orlob has not (as of this research date) published a book under his own name. There is no equivalent "documented, from secondary summaries" book section in this corpus because there is no book to summarize.
- **Gong-era posts are archive-only.** The live gong.io blog no longer serves these 2019 posts under his byline (confirmed via Wayback Machine capture dates); if Gong has since removed or reattributed them, that is worth re-checking on refresh.
- **Stat provenance is his claim, not independently audited.** Figures like "39% less," "28% more," "54.3% vs 31%," and "3,000,000 demos analyzed" are Gong Labs data as reported by him in his own posts. No independent replication was attempted; treat these as his published claims, not verified external research.
- **pclub.io rebrand in progress.** The blog now displays as "Caliber (formerly pclub.io)" in its header while URLs still resolve under pclub.io. Confirm on refresh whether the domain or brand name has fully changed.

## Refresh instructions

1. Re-check whether pclub.io has fully rebranded to Caliber (new domain, new URLs) and update links if so.
2. Re-fetch the pclub.io/Caliber blog index and pull any Chris Orlob byline post published since August 2026.
3. Attempt a LinkedIn pull again (signed-in export, or check if a public mirror is fetchable) to close the carousel/short-form gap - this is the top priority for the next refresh.
4. Search for a podcast appearance or conference talk transcript to add a conversational (non-scripted) spoken register.
5. Re-verify the Gong Labs stats cited in this corpus are still the numbers he uses; some blog posts (e.g. the C-suite piece) are explicitly dated as periodically "updated," so check for revised figures.
6. Confirm whether the 2019 Wayback-only Gong.io posts have reappeared live or been formally retired/reattributed.
