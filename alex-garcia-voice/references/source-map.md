# Alex Garcia Voice Source Map

Research date: 2026-10-19
Refresh cadence: every 6 months (next: 2027-04)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| marketingexamined.com blog (newsletter case-study archive) | https://www.marketingexamined.com/sitemap-0.xml (279 URLs) | 2022-2026 case studies; the first-person ones (content strategy, media funnel, distribution, email teardowns) carry his voice; author and ISO date in each page's `__NEXT_DATA__` | Open HTML; `<script id="__NEXT_DATA__">` has author + date |
| "How I Develop My Content Strategy" (Aug 22 2023) | https://www.marketingexamined.com/blog/how-i-develop-my-content-strategy | Zero-subscribers opener, 3Ps, 90/10/5 mix, snacks and entrees, "Never the other way around." | Open |
| "The Media Funnel" (Sep 12 2024) | https://www.marketingexamined.com/blog/the-media-funnel | Consensus flip, reach vs. impact, forever billboards, "Brand time…" section break | Open |
| "This Brand Does $40M Selling Tape" (Apr 17 2024) | https://www.marketingexamined.com/blog/hostage-tape | Email hooks, "Oh, that's me" shift, The Formula label | Open |
| "How To Extend The Life-Cycle Of Your Content With Strategic Distribution" (Mar 1 2023) | https://www.marketingexamined.com/blog/strategic-content-distribution | Publish-then-crickets opener, shoe drop, buffet simile | Open |
| "How To Convert Customer Objections Into Your Best Ad Hooks" (Feb 28 2023) | https://www.marketingexamined.com/blog/how-to-write-converting-ad-hooks | "Your customers are your best scriptwriters" | Open (author field "alexgarcia_atx") |
| Marketing Examined site-wide footer | https://www.marketingexamined.com (footer on every post) | First-person intro, 200k+ claim, "My Promise" copy | Open |
| X @alexgarcia_atx (threads) | https://threadreaderapp.com/user/alexgarcia_atx | ~21 unrolled threads Oct 2021-Oct 2023: landing pages, copywriting, True Classic and Hostage Tape teardowns, X algorithm, AI tools | Open; root tweet text and date via `https://api.fxtwitter.com/i/status/<id>`; mid-thread tweets from Thread Reader unrolls |
| LinkedIn posts | https://www.linkedin.com/in/alex-garcia-294119159 (profile lists 7 own-post permalinks; `/in/alexgarciaatx` returns HTTP 999) | 2023-2026 posts: social shows, 7 content archetypes, "chief clipping officer", reader-response gratitude | Permalinks render logged out with a desktop UA; text in meta description, date in JSON-LD |
| Founder Stories interview (beehiiv) | https://founderstories.beehiiv.com/p/alex-garcia-marketing-examined | Founding-story interview quotes | Open; NOT fetched this round (would be documented-grade) |
| The Marketing Millennials podcast ep. 64 | https://creators.spotify.com/pod/profile/themarketingmillennials/episodes/64---Alex-Garcia-Gumroad-Growth-Marketing-Examined-e19vuor | Spoken voice | Audio only; NOT fetched; no transcript located |

## What the corpus rests on

All 32 excerpts are verbatim from channels he writes himself: 17 from first-person case studies and the site footer on marketingexamined.com (2023-2026), 10 from his own X account (root tweets re-fetched and dated via fxtwitter, mid-thread tweets via Thread Reader unrolls of the same threads), and 5 from LinkedIn post permalinks (2023-2026). Nothing comes from a quote aggregator. Third-person brand profiles credited to him but reading as staff-written were excluded, so the sample is first-person voice only. The newsletter, X, and LinkedIn registers are all covered and read as one compressed voice. There is no spoken sample. Confidence in wording is high for the case-study, root-tweet, and LinkedIn items and slightly lower for the mid-thread items, which rest on Thread Reader's copy.

## Known gaps

- **No spoken-word source.** Podcasts exist (The Marketing Millennials ep. 64, Founder Stories) but no transcript was fetched and yt-dlp was not attempted. Every voice claim here is about his written register; do not attribute verbal habits to him.
- **Authorship on marketingexamined.com must be judged per post.** Many posts credited "Alex Garcia" are third-person, undated brand profiles that read as staff-written (e.g. the Liquid Death philosophy piece). Only first-person posts were quoted; apply the same test on refresh.
- **X sample is Thread Reader's curation.** The syndication timeline endpoint returned 429 during the run, so only ~21 curated threads (2021-2023) were available; standalone tweets and anything after Oct 2023 on X are unsampled. Mid-thread items were not re-fetched individually.
- **LinkedIn profile slug.** `/in/alexgarciaatx` returns HTTP 999; the working slug is `alex-garcia-294119159`. Only the 7 permalinks listed on the profile were reachable.
- **The 200k+ subscriber figure is his own footer claim**, not independently verified; treat it as his statement when quoting.
- **Anything published after 2026-10-19 is unsampled.**

## Refresh instructions

1. Re-fetch `https://www.marketingexamined.com/sitemap-0.xml`, pick new URLs, and for each check `__NEXT_DATA__` for author and date; quote only posts written in the first person. Add 5-10 verbatim excerpts with URLs and dates, continuing the numbering in the case-study section.
2. Pull the X syndication timeline (`https://syndication.twitter.com/srv/timeline-profile/screen-name/alexgarcia_atx`) when it is not rate-limited, or re-run Thread Reader (`https://threadreaderapp.com/user/alexgarcia_atx`); verify each root tweet via `https://api.fxtwitter.com/i/status/<id>` and add 5-8 verbatim posts.
3. Re-fetch the LinkedIn profile `https://www.linkedin.com/in/alex-garcia-294119159` with a desktop UA, collect new post permalinks, and read text from `<meta name="description">` and the date from JSON-LD; add 3-5 posts.
4. Close the spoken gap: run `yt-dlp --write-auto-sub --skip-download --sub-lang en "<url>"` once on a long interview he appears in (or fetch the Founder Stories page), add 3-5 excerpts under a new "## Documented excerpts" heading, and add a spoken-register bullet to the stats.
5. Re-verify that every URL is still live. Never carry a quote forward that was not re-read at its source.

## Pattern notes

### 1. Proof number, then the reveal
Teardowns open on a result ("turned $3k into $150M") and reveal the brand on its own short line ("The brand? True Classic."). The Newsletter Writer and Hook Creator both start here, and both require the number to be real or [VERIFY]-flagged.

### 2. Fragment chain
One- and two-word sentences enact the behavior they describe ("Post. Post. Post. And post again."; "Tease. Create curiosity. Fomo."). Every playbook caps this at one chain per piece so it stays a pace-setter rather than a tic.

### 3. Framework label
Methods get a name and a one-line definition (3Ps, The Formula, media funnel, snacks and entrees, forever billboards, 7 archetypes). The Newsletter Writer places one label per issue; the LinkedIn Content Expert can use the label itself as the hook.

### 4. Colon promise
Thread roots and LinkedIn hooks end on "Here's how to…:" with the body as the payoff. The Hook Creator and LinkedIn Content Expert both end hooks on the colon rather than on a summary.

### 5. Kicker close
Sections and posts end on a flat, unanswerable line ("Never the other way around."; "Do what you want with this info."; "Just mute the word on your timeline"). All three playbooks make the kicker the final line.

### 6. Operator credential as work done
Authority is stated as time and output, not titles ("Two years of building Marketing Examined"; "I've spent the last year creating social shows for 8-10 figure brands"). The LinkedIn Content Expert puts this in line two; ghostwritten copy must substitute the user's own work.
