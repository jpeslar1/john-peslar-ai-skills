# Andrew Gazdecki Voice Source Map

Research date: 2026-10-19
Refresh cadence: every 6 months (next: 2027-04)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| X @agazdecki single posts | https://cdn.syndication.twimg.com/tweet-result?id=1709708261065474073&token=a (pattern) | Full post text, ISO created_at, like counts, no login; 19 posts 2021 to Oct 2026 sampled | Open per status ID; the profile timeline endpoint 429s after 2-3 hits |
| fxtwitter status API | https://api.fxtwitter.com/agazdecki/status/<id> | Full text for posts over 280 characters (items 13, 16, 18) | Open |
| X: bootstrapped-to-$10m origin post (Jan 19 2024) | https://x.com/agazdecki/status/1748331162098155611 | The four-line origin credential and the mantra | Open via syndication endpoint |
| X: August scoreboard (Sep 6 2023) | https://x.com/agazdecki/status/1699460491658297551 | Monthly metric stack with hyphen bullets; "We're just getting started!" | Open via syndication endpoint |
| X: $1.1M self-improvement app listing (Sep 28 2026) | https://x.com/agazdecki/status/2104668104555130933 | Chevron metric stack; listing-promo register | Open via fxtwitter |
| LinkedIn posts (agazdecki) | https://www.linkedin.com/posts/agazdecki_two-startup-acquisition-outcomes-3-activity-7153008345547767809-njzX (pattern) | Full post text in the description meta tag, datePublished in JSON-LD; 5 posts 2022-2024 sampled | Permalinks render logged out with a desktop UA (verified 2026-10-19); the /in/agazdecki/ profile authwalls |
| LinkedIn: Two startup acquisition outcomes (Jan 16 2024) | https://www.linkedin.com/posts/agazdecki_two-startup-acquisition-outcomes-3-activity-7153008345547767809-njzX | The signature two-column comparison and neutral verdict | Open |
| Acquire.com blog (WordPress), author id 8 | https://blog.acquire.com/wp-json/wp/v2/posts?author=8&per_page=50 | Bylined posts 2019-2026; only first-person pieces used | Open with default curl UA (a fake Chrome UA gets an HTTP/2 stream error) |
| Blog: Becoming Acquire.com (Jan 5 2023) | https://blog.acquire.com/becoming-acquire-com/ | "Hey there, Andrew here" founder letter on the MicroAcquire to Acquire.com rebrand | Open |
| Blog: Acquire.com Closing Fee From June 2023 (May 17 2023) | https://blog.acquire.com/acquire-closing-fee-june-2023/ | Founder letter; the one en dash in the sample | Open |
| Blog: 5 Ways Bootstrapping Can Make You a Better Business (Dec 18 2019) | https://blog.acquire.com/5-ways-bootstrapping-can-make-you-a-better-business/ | Bizness Apps-era essay; "I couldn't disagree more", "a couple cases of Redbull" | Open |
| Blog: Who Needs Investors? (Dec 13 2019) | https://blog.acquire.com/who-needs-investors-why-many-startups-should-bootstrap-instead/ | "Being broke is a wonderful system" | Open |
| Book: Getting Acquired (2022) | n/a | His memoir of bootstrapping to $10m ARR and selling | Not fetched; no public excerpt located |

## What the corpus rests on

All 30 excerpts are verbatim and written by him: 19 from his own X posts (2021 to October 2026), 5 from public LinkedIn post permalinks (2022 to 2024), and 6 from first-person pieces on the Acquire.com blog (two 2019 Bizness Apps-era essays and two 2023 "Andrew here" founder letters). Nothing comes from a quote aggregator and nothing is ASR. Raw JSON and HTML were saved at research time and re-verified from the saved files, with blog authorship re-checked live. The short-form X register is the deepest-covered; the blog letters are a calmer register and may have had marketing help, so treat them as documented-grade for attribution even though the text is verbatim. Confidence in wording is high for every item.

## Known gaps

- **Book Getting Acquired not sampled.** No public excerpt was fetched; do not quote it as verbatim.
- **No spoken sample.** Podcast appearances, including his own Acquire podcast episodes, were not captioned; all 30 items are written. Spoken-style output is inferred.
- **X sample under-represents 2024-2025.** Items were reached by status IDs that surfaced in search plus a first-pass collection; the profile timeline endpoint 429s, so his high-frequency 2024-2025 posting is thin and several 2026 items are listing promos rather than opinion.
- **Blog byline is shared.** Author id 8 "Andrew Gazdecki" is a house byline on roughly 50 SEO guides (2025-2026). Only the four first-person pieces were used, and even the 2023 letters may have been drafted with marketing help.
- **LinkedIn sample is small.** Five posts, 2022 to 2024, found via permalinks; the profile and activity pages authwall.
- **Anything published after 2026-10-19 is unsampled.**

## Refresh instructions

1. Collect new X status IDs from search (`site:x.com/agazdecki <topic>` or his own LinkedIn cross-posts), then fetch each with `curl -s 'https://cdn.syndication.twimg.com/tweet-result?id=<id>&token=a'`; for posts over 280 characters use `curl -s 'https://api.fxtwitter.com/agazdecki/status/<id>'`. Do not hit the timeline endpoint more than twice per session. Add 5-10 verbatim posts, favoring opinion over listing promos, and continue the numbering.
2. Find new LinkedIn permalinks with WebSearch `"Andrew Gazdecki" "on LinkedIn:" <topic>`; fetch each with a desktop UA and read the text from the description meta tag and the date from the JSON-LD `datePublished`.
3. Re-pull the blog: `curl -s 'https://blog.acquire.com/wp-json/wp/v2/posts?author=8&per_page=50'` (default curl UA) and keep only posts that open in the first person ("Andrew here", "we built our company"); skip the SEO guides.
4. Check whether a public excerpt of Getting Acquired has appeared (publisher page, Amazon preview); if so, add 2-3 excerpts in their own section, labeled as book text.
5. If a spoken register is wanted, caption a podcast appearance with `yt-dlp --write-auto-sub --skip-download --sub-lang en <url>` and add 3-5 documented excerpts under a "Documented excerpts (ASR captions)" heading, flagged as such.
6. Re-verify that every URL is still live, and that the mantras are still in use (he has repeated them since 2022). Never carry a quote forward that was not re-read at its source.

## Pattern notes

### 1. Stack and stop
Every sentence is its own line and the post ends on a two- or three-word verdict ("That's the play."). All three playbooks enforce one sentence per row and a short verdict line.

### 2. Mantra reuse
"For the love of startups this is why @acquiredotcom exists." and "We're just getting started." recur verbatim across years and channels. The Build-in-Public Writer and LinkedIn Content Expert close on the user's own repeated line, and the Anti-patterns flag paraphrasing the mantra as a tell.

### 3. Receipt stack
Metrics arrive as hyphen or chevron bullets, biggest first, followed by a one-line reaction. The Build-in-Public Writer returns the stack first so the user confirms every figure before the copy is written.

### 4. Two outcomes
Parallel stacks (raised vs bootstrapped, ownership, post-tax take) and a neutral verdict argue for bootstrapping without attacking anyone. The Hook Creator and LinkedIn Content Expert use it whenever paths are compared.

### 5. Brand as verb
The company name becomes a past participle for the outcome ("get @acquiredotcom'd"). Playbooks allow it once per exit post; three in one post is an over-imitation tell.

### 6. Sincere, no snark
Warmth toward founders ("hard and lonely", "please surround yourself", "Shout out") is the baseline and the only joke target is his own product. The Emotional register fix and the Taboo list both route a clever or salesy draft back to the flat truism and the shout-out.
