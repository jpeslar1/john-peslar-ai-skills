# April Dunford Source Map

Research date: 2026-09-09; LinkedIn and newsletter refresh 2026-10-18
Refresh cadence: every 6 months (next: 2027-04)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| Blog | https://www.aprildunford.com/blog | The core corpus. Long-form posts on positioning, competition, storytelling, sales pitch. | Open, plain HTML, scrapes cleanly |
| Quickstart Guide to Positioning | https://www.aprildunford.com/post/a-quickstart-guide-to-positioning | The definition, the war story, the five components | Open |
| Positioning and Competition | https://www.aprildunford.com/post/positioning-and-competition | Competitive alternatives, status quo, phantom competitors, no-decision rate | Open |
| Storytelling vs Positioning | https://www.aprildunford.com/post/storytelling-vs-positioning | The positioning-before-story argument | Open |
| Positioning vs Strategy vs Vision | https://www.aprildunford.com/post/positioning-vs-strategy-vs-vision | Sales pitch versus investor pitch | Open |
| Obviously Awesome (2019) | book | The full ten-step methodology | Purchase |
| Sales Pitch (2023) | book | The pitch structure summarised in the corpus as `documented` | Purchase |
| LinkedIn (aprildunford) | https://www.linkedin.com/in/aprildunford/ and 13 post permalinks cited in the corpus (items 101-127) | Short-form register: one-line aphorisms and emoji-bulleted newsletter teasers, 2023-2024 and 2026 | Post permalinks and the profile render logged out with a desktop user agent (full text plus JSON-LD datePublished); only the activity feed is login-walled |
| Newsletter (Substack, since 2023) | https://aprildunford.substack.com/ | Long-form 2025-2026 essays; "differentiated value", pessimistic product thinking, positioning in the age of AI (items 128-134) | Open; use the Substack JSON API (/api/v1/posts/<slug>) when a page fails to parse |
| mtpcon London 2026 talk (YouTube) | https://www.youtube.com/watch?v=O9FCRvlJcSs | Spoken register, "Everything has changed except for the fundamentals of positioning" | Open video; caption pull hit HTTP 429 twice on 2026-10-18, not yet sampled |
| Talks | BoS USA, SaaStr, Lenny's Podcast | Spoken register, timing, the jokes | Open, video |

## What was actually fetched

Six blog posts were pulled as raw text from aprildunford.com on 2026-09-09. Four of them supplied the verbatim corpus. The site is server-rendered and scrapes cleanly with a plain HTTP fetch, so refreshing this corpus is cheap. On 2026-10-18, 27 LinkedIn excerpts (13 permalinks, 2023-2024 and 2026) and 7 Substack newsletter excerpts (2025-2026) were added as items 101-134, all verbatim; the short-form register is now sampled, not inferred.

## Known gaps

- **Neither book was read.** Both Obviously Awesome and Sales Pitch are behind purchase. Items 29 to 33 in the corpus are from third-party summaries and are labeled `documented`. The ten-step methodology in Obviously Awesome is referenced in this skill only through the five components published on the blog.
- **LinkedIn 2024-2025 is thin.** The 2023 set came from search-surfaced permalinks and the 2026 set from the profile's latest nine posts; posts between February 2024 and March 2026 were reached only through the newsletter.
- **No spoken corpus.** Her stage timing and the jokes are a real part of the voice and are not captured here. The mtpcon London 2026 caption pull was rate-limited (HTTP 429 twice); re-run `yt-dlp --write-auto-sub --skip-download --sub-lang en https://www.youtube.com/watch?v=O9FCRvlJcSs` later.
- **Second edition of Obviously Awesome (2026, 100,000 copies sold) not read.** The newsletter now labels the five components Competitive Alternatives, Distinct Capabilities, Differentiated Value, Best-Fit Customers, Market Category; the 2021 blog labels in items 1-28 may be superseded.
- **X not sampled** (syndication endpoint 429). Unknown whether she posts actively.
- **Lenny's Newsletter guest post (Mar 2026) is paywalled**; the roadblocks framework is captured only through her LinkedIn summary.
- **Anything published after 2026-10-18 is unsampled.**
- **Long-form sample skews 2020-2021** (items 1-28); the 2025-2026 newsletter items confirm the thesis is unchanged and the vocabulary has shifted toward "differentiated value" and an AI frame.

## Refresh instructions

1. Re-fetch the blog index and pull any post published since 2021 that is not in this corpus.
2. Pull one talk transcript for the spoken register.
3. Confirm the 20 to 30 percent no-decision figure is still the number she cites, and update if she has revised it.
4. If any `documented` Sales Pitch item is going into client-facing material, check it against the book, not against a summary.
5. Check whether the five components have grown a sixth (trends is discussed in Obviously Awesome as an optional component).
