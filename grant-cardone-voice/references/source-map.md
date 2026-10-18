# Grant Cardone Voice Source Map

Research date: 2026-10-18
Refresh cadence: every 6 months (next: 2027-04)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| Entrepreneur.com contributor columns (byline Grant Cardone, 2017-2020) | https://www.entrepreneur.com/author/grant-cardone | 30+ bylined columns on sales, money, mindset; JSON-LD confirms `"author":"Grant Cardone"`; carries "Opinions expressed by Entrepreneur contributors are their own" | Open; raw HTML fetch works without login |
| "Don't Take Advice From Quitters" (Mar 8 2018) | https://www.entrepreneur.com/growing-a-business/dont-take-advice-from-quitters/309626 | Accusing question opener; "Alexander and Napoleon of your own life"; divorce confession turned rule | Open |
| "Why I'm Not Interested in a High Closing Ratio" (Nov 30 2017) | https://www.entrepreneur.com/growing-a-business/why-im-not-interested-in-a-high-closing-ratio/305432 | Write everyone up; swing the bat; known-answer questions; "You have to earn that" | Open |
| "You'll Never Get Rich Playing Defense With Your Money" (Sep 27 2018) | https://www.entrepreneur.com/money-finance/youll-never-get-rich-playing-defense-with-your-money/320655 | Offense vs defense; father died at 10; 95/5 Rule; debt only for income | Open |
| "Be Tough on Yourself" (Jul 12 2018) | https://www.entrepreneur.com/living/be-tough-on-yourself/316186 | Triple frame ("Tell yourself the truth..."); unreasonable as compliment | Open |
| grantcardone.com blog and "Strategy of the Week" (2016-2018) | https://web.archive.org/web/2018*/grantcardone.com/blogs/grantcardone/* | His own posts signed "Be great, GC" | Open via Wayback Machine only; live site Cloudflare-blocks curl and now redirects grantcardone.com/blog to gctv.com and then a HubSpot booking page |
| "5 Things that Will Actually Make You Poor" (Jan 4 2018) | https://web.archive.org/web/20180119230100/https://grantcardone.com/blogs/grantcardone/5-things-that-will-actually-make-you-poor | No silver spoon; "Big think"; the now is the past; Sunday-evening dread | Open via Wayback |
| "Fight Against Obscurity" (Mar 24 2017) | https://web.archive.org/web/20170707192954/https://grantcardone.com/blogs/grantcardone/fight-against-obscurity | Spectators vs users; "Don't worry about pushing too much"; cable-network board line | Open via Wayback |
| "It Takes Courage to Make Money" (Mar 17 2016) | https://web.archive.org/web/20180201215209/https://grantcardone.com/blogs/grantcardone/it-takes-courage-to-make-money | Club-or-bank question; fear list; "10X Balls"; "Be great, GC" sign-off | Open via Wayback |
| @GrantCardone on X (2025-2026) | https://x.com/GrantCardone | Three posts: Bitcoin-denominated real estate, the Global 7500 jet listing, the 700 BTC beach house | Public via `https://cdn.syndication.twimg.com/tweet-result?id=<id>&token=a`; tweet IDs located through Benzinga and Finviz embeds; profile timeline endpoint is IP rate-limited |
| grantcardone.com/quotes ("200+ quotes" download) | https://grantcardone.com/quotes/ | Official quote list | Email-gated download; page itself has no quote text; not used |
| Grant Cardone YouTube (@GrantCardone) | https://www.youtube.com/@GrantCardone | Spoken and stage voice | Captions NOT obtained: yt-dlp returned HTTP 429 on three attempts across two videos |
| The 10X Rule (Wiley, 2011); Sell or Be Sold | https://store.grantcardone.com/collections/allproducts/products/the-10x-rule-book | Book-length voice | Paywalled; Wiley page lists TOC only; "Free Books" are shipping-fee funnels; no official public excerpt found |

## What the corpus rests on

All thirty-one excerpts are verbatim, written under his own byline: nineteen from four Entrepreneur.com columns (2017-2018) whose JSON-LD names him as author, nine from Wayback Machine captures of his own grantcardone.com blog (2016-2018), and three from his own X posts (2025-2026) read from the public syndication JSON. There are zero documented-grade items and zero spoken or ASR items. Nothing comes from a quote aggregator, and the email-gated official quote list was not used. Confidence in wording is high for all 31 items. Confidence in register coverage is high for his 2016-2018 long-form written voice, low for his spoken voice (unsampled), and thin for his 2024-2026 written voice (three X posts).

## Known gaps

- **No spoken sample.** yt-dlp returned HTTP 429 on three separate attempts (two videos, with 30-second-plus cooldowns), so no YouTube captions were obtained. His stage, podcast, and video cadence is unsampled; every cadence note in SKILL.md rests on written passages that mimic speech ("Look, the now is what? It's the past now! Do you get it?"). Label spoken-register claims as inferred.
- **The 10X Rule and Sell or Be Sold not quoted.** No official public excerpt was located; the Wiley page lists the table of contents only and grantcardone.com "Free Books" are shipping-fee funnels. Famous book lines must not be quoted as verbatim from memory. Aggregator quote sites were deliberately not used.
- **Live grantcardone.com unreadable.** Cloudflare blocks non-browser fetches; the official "200+ quotes" list is an email-gated download. Only Wayback snapshots of 2016-2018 posts were readable, and no 2019+ blog posts were captured because the blog was retired and redirected.
- **X sample is three posts.** IDs came from a Finviz and Benzinga article's embeds; the profile timeline endpoint is IP rate-limited. No 2026-Q3 or Q4 posts. The X register (lowercase "i", ampersand, spaced hyphen, emoji strings, listing specs) is therefore a sketch, not a sample.
- **LinkedIn articles and Medium (@grantcardone) not readable** (login wall and Cloudflare 403).
- **Columns are 2017-2018 vintage.** His current long-form written voice (2024-2026) is under-sampled relative to his social and video output.
- **Anything published after 2026-10-18 is unsampled.**

## Refresh instructions

1. Pull captions from two or three of his own YouTube videos, retrying after the rate limit clears and spacing attempts out: `yt-dlp --write-auto-sub --skip-download --sub-lang en --sleep-requests 5 "https://www.youtube.com/watch?v=<id>"`, then strip timestamps. Add 5-8 excerpts as a new "Documented excerpts (ASR captions)" section, continuing the item numbering, and update the Guardrails line in SKILL.md that says no spoken sample exists.
2. Re-fetch https://www.entrepreneur.com/author/grant-cardone and add 5-10 verbatim excerpts from 2019-2020 columns not yet sampled, with URLs and dates.
3. For X, locate recent tweet IDs through news embeds (Benzinga, Finviz, Fortune) and read each via `https://cdn.syndication.twimg.com/tweet-result?id=<id>&token=a`; add 10-15 posts to the short-form section so the X register rests on more than three items.
4. Check whether gctv.com or a successor hosts his current long-form writing with a byline; if so, add a 2024-2026 written section.
5. Search for a publisher-hosted excerpt of The 10X Rule or Sell or Be Sold so famous lines can move from "do not quote" to verbatim.
6. Re-verify that every URL above is still live, including the Wayback captures. Never carry a quote forward that was not re-read at its source.

## Pattern notes

### 1. Accusing question or flat command as the opener
"Where do you get your advice from?" and "If you want money, you've got to get on offense." open columns with the reader already implicated. The Contrarian Take Generator requires one of the two as line one, with no wind-up.

### 2. Triple frame
Three sentences, same frame, escalating ("Tell yourself the truth. Ask for the truth. Hear the truth."). Appears in five of 31 items and is the rule block in every playbook, used once per piece.

### 3. Binary sort
Average vs exceptional, offense vs defense, spectators vs users, soft vs firm, realistic vs big think. The Objection Handling Expert playbook sorts every objection onto the losing side of one binary instead of rebutting it point by point.

### 4. Confession to command
Father dead at 10, the house sold within a month, the divorce, the third strike: one sentence of biography, then the rule it proves. The playbooks allow one such proof per piece and require the user's own biography, not his.

### 5. Write everyone up, swing the bat
The Sales Closer playbook is built on this: refuse to pre-qualify, ask only known-answer questions, measure swings rather than closing ratio, and name the seller's fear as the real objection.

### 6. Register as a deliberate choice
Hot, certain, boastful, hedge-free. It conflicts with careful, qualified outbound and with the operator's own brand ("Avoid when: default John-brand copy"), so every playbook ends with an audience check and the Output Format states whether the register fits the reader.
