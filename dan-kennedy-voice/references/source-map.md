# Dan Kennedy Source Map

Research date: 2026-09-09
Refresh cadence: every 6 months (next: 2027-03)

## Authorship caveat, read before refreshing

magneticmarketing.com publishes Kennedy's methodology under the Magnetic Marketing brand, which has changed hands. Its blog posts carry no personal byline. They are written in his doctrine and in a close approximation of his register, and they are the best freely accessible prose in this style, but they cannot be assumed to be his personal writing. This corpus labels them `documented`, not `verified`, and calls them house register throughout. As of this revision, dankennedy.com 301-redirects to magneticmarketing.com, confirming the two are now the same operation, which reinforces rather than resolves the caveat.

**This gap is now partly closed, not fully closed.** Items 36-49 in the corpus are `verified`: personally bylined entrepreneur.com pieces, two of them explicit excerpts from his own named books. See "What was fetched on 2026-09-09" below. The house register (items 1-25) is unchanged and still unconfirmed as his personal writing.

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| Magnetic Marketing blog | https://magneticmarketing.com/blog | The doctrine in the house register. Dated posts on pricing, copy length, direct response versus awareness. | Open, server-rendered, scrapes cleanly |
| How You're Pricing Yourself Into Destruction | https://magneticmarketing.com/blog/how-youre-pricing-yourself-into-destruction | Price as positioning, the discount trap, the punch-sentence rhythm | Open |
| Stop Counting Words. Start Counting Sales. | https://magneticmarketing.com/blog/stop-counting-words-start-counting-sales | Copy length doctrine and the five questions | Open |
| Magnetic Marketing site copy | https://magneticmarketing.com/ | Live examples of the offer-and-bonus-stack format the doctrine teaches | Open |
| Dan S. Kennedy author page, entrepreneur.com | https://www.entrepreneur.com/author/dan-s-kennedy | Index of individually bylined contributor pieces and book excerpts under his name | Open, server-rendered, scrapes cleanly |
| Discover the Power of "Blind" Advertising (excerpt, No B.S. Direct Marketing) | https://www.entrepreneur.com/growing-a-business/discover-the-power-of-blind-advertising-new-excerpt/313318 | Verbatim book text under his byline, personal register on brand-suppression tactics | Open |
| Here's an Ad that Sucks. Here's How to Fix It. (excerpt, The Best of No B.S.) | https://www.entrepreneur.com/marketing/heres-an-ad-that-sucks-heres-how-to-fix-it/432342 | Verbatim book text, a sustained real-ad teardown in first person | Open |
| The No. 1 Trait I Look For When Deciding to Do Business With Someone | https://www.entrepreneur.com/leadership/the-no-1-most-powerful-personal-discipline-in-the-world/478850 | First-person contributor essay, not a book excerpt, on punctuality as an integrity test | Open |
| No B.S. Direct Marketing for Non-Direct Marketing Businesses | book | The ten rules. Currently `documented` from summaries only for the rules list; partially corroborated in prose by the verified excerpt above. | Purchase |
| No B.S. series (Price Strategy, Time Management, Marketing to the Affluent, and others) | books | The wider doctrine and further personal prose register | Purchase |
| No B.S. Inner Circle newsletter | nobsinnercircle.com | The print newsletter format he built the business on | Paid |
| Magnetic Marketing podcast | magneticmarketing.com | Spoken register | Open |

## What was fetched on 2026-09-09

- Re-confirmed the two magneticmarketing.com blog URLs already in the corpus (unchanged; not re-quoted).
- `https://www.dankennedy.com` -> 301 redirect to `https://magneticmarketing.com/`, confirming the domains are now one operation. `https://www.dankennedy.com/blog/` returns 404.
- `https://www.entrepreneur.com/author/dan-s-kennedy` fetched directly: an index of contributor pieces bylined to him, spanning marketing, time management, and presentations.
- `https://www.entrepreneur.com/growing-a-business/discover-the-power-of-blind-advertising-new-excerpt/313318` fetched directly: explicitly framed as "the following excerpt is from Dan S. Kennedy's book No B.S. Direct Marketing." Scraped cleanly. Three excerpts pulled (corpus items 36-38).
- `https://www.entrepreneur.com/marketing/heres-an-ad-that-sucks-heres-how-to-fix-it/432342` fetched directly: explicitly framed as excerpted from his book The Best of No B.S., published Aug 17, 2022. Scraped cleanly. Six excerpts pulled (corpus items 39-44).
- `https://www.entrepreneur.com/leadership/the-no-1-most-powerful-personal-discipline-in-the-world/478850` fetched directly: a first-person contributor essay, not marked as a book excerpt, published Sept 4, 2024. Scraped cleanly. Five excerpts pulled (corpus items 45-49).
- YouTube caption route was not usable this session: `yt.py tracks` succeeded but `yt.py tx` returned `IpBlocked` (HTTP 429-class YouTube IP block) on the first attempt. Not retried, per the session's tooling constraint. No spoken-register material was added this session as a result; see Known gaps.

## Known gaps

- **The house register (items 1-25) is still unconfirmed as personal writing.** This revision did not change that; it made the label honest instead of leaving it implied. Closing this gap fully means either the blog begins carrying personal bylines, or it gets dropped in favor of confirmed sources.
- **The ten rules (items 26-35) are still second-hand.** Unchanged this revision. Wording varies between sources and between editions.
- **No full book was read cover to cover.** The two "verified" book excerpts are single passages each, chosen and framed by Entrepreneur's editors, not a representative sample of either book. Do not treat items 36-44 as covering the full range of his book-length prose.
- **No print newsletter sample.** The Inner Circle newsletter is the format that built the business and is the natural reference for the Newsletter Writer playbook. It is paid and was not sampled.
- **No spoken register.** He is a well-known speaker and the platform register differs from the written one. YouTube transcript access was blocked this session (see above); this gap is unchanged from the prior revision, not newly discovered.
- **Only three personally bylined pieces sampled.** The entrepreneur.com author index lists more; this revision pulled the three most useful for pricing, advertising teardown, and personal-standards content, matching the existing playbooks. A refresh could add more from the same author index at low cost.

## Refresh instructions

1. Pull additional pieces from `https://www.entrepreneur.com/author/dan-s-kennedy` beyond the three sampled here, particularly anything on presentations or time management, to broaden the verified personal-register section.
2. Read one full No B.S. title, ideally No B.S. Price Strategy or No B.S. Direct Marketing in full, and replace items 26-35 (the ten rules) with cited quotations from the actual text, dropping the summary-based `documented` label for that section.
3. If access to an Inner Circle issue is available, document the print newsletter structure for the Newsletter Writer playbook.
4. Re-check whether magneticmarketing.com has begun carrying personal bylines. If it has, promote those posts out of the house-register section and into the verified section, and update the authorship caveat.
5. Retry `yt.py tracks` / `yt.py tx` on a Dan Kennedy speaking clip once the IP block has cleared, to add a spoken-register sample.
6. Re-verify any response rate or case result before it goes into client-facing copy.
