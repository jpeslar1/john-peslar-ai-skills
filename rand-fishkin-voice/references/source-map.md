# Rand Fishkin Voice Source Map

Research date: 2026-10-19
Refresh cadence: every 6 months (next: 2027-04)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| SparkToro blog, author=Rand (WordPress REST) | https://sparktoro.com/blog/wp-json/wp/v2/posts?author=2&per_page=40 | ~40 bylined posts 2025-2026: zero-click research write-ups, rants (SEO acronyms, AI jobs, Google's "digital enclosure"), 5-Minute Whiteboard posts with his own pasted transcripts | Open; full bodies in `content.rendered` |
| "In a Zero-Click World, Traffic is a Terrible Goal" (Jun 11 2025) | https://sparktoro.com/blog/in-a-zero-click-world-traffic-is-a-terrible-goal/ | Number-then-verdict opener; "Period."; "Traffic is a vanity metric." (pasted whiteboard transcript) | Open |
| "Seriously, please stop with the new acronyms" (May 29 2025) | https://sparktoro.com/blog/its-still-seo-search-everywhere-optimization/ | "It's a day ending in Y"; "Really Rand?"; Search Everywhere Optimization credited to Ashley Liddell | Open |
| "AI will replace all the jobs! Is Just Tech Execs Doing Marketing" (Jun 1 2025) | https://sparktoro.com/blog/ai-will-replace-all-the-jobs-is-just-tech-execs-doing-marketing/ | "let's walk through the logic together"; raining-on-the-parade disclaimer | Open |
| "Inimitable Product is the New Make Great Content" (May 25 2026) | https://sparktoro.com/blog/inimitable-product-is-the-new-make-great-content/ | "Google's plan is elegant, simple, and evil"; "They want to be the web." | Open |
| "The Final Chapter of My First Startup" (Oct 26 2023) | https://sparktoro.com/blog/the-final-chapter-of-my-first-startup/ | 17K-character memoir epilogue to Lost and Founder: "$371,000.", the revenge motive, the non-VC funding model, Chill Work | Open |
| LinkedIn posts (logged-out permalinks) | https://www.linkedin.com/in/randfishkin exposes `/posts/randfishkin_...` links | October 2026 rants: BOALIR, "THE data", the Reddit objection, Alertmouse | Open with a desktop UA; full text in the page body plus JSON-LD `datePublished` |
| Moz Blog Whiteboard Friday archive (2007-2018) | https://moz.com/blog/why-good-unique-content-needs-to-die-whiteboard-friday | 2015 spoken register ("Howdy, Moz fans"); official Speechpad transcript under "Video transcription" | Open HTML; DOCUMENTED (third-party transcription) |
| SparkToro 5-Minute Whiteboard videos (YouTube) | embedded in the blog posts above | Current spoken register; he pastes the transcript into the post body himself | Transcript inside the post = verbatim-as-published |
| Lost and Founder (Portfolio, 2018) | not fetched | Book voice; public excerpts exist via publisher and press | Not pulled this round |
| X @randfish | https://cdn.syndication.twimg.com/tweet-result?id=<id>&token=a | Would give the short-form register | Timeline endpoint rate-limited this session; no status IDs harvested |

## What the corpus rests on

Twenty-six of twenty-nine excerpts are verbatim from channels he writes or publishes himself: seventeen from bylined SparkToro blog posts (2025-2026, three of them whiteboard transcripts he pasted in), four from his 2023 memoir epilogue on sparktoro.com, and five from his own LinkedIn posts read at logged-out permalinks. Three are documented-grade: a Speechpad transcription of a 2015 Moz Whiteboard Friday, published by Moz. Nothing comes from a quote aggregator. The essay, research write-up, memoir, and LinkedIn registers are covered, and two eras of spoken register are present (2015 as documented, 2025 as author-published). Confidence in wording is high for items 1-26 and moderate for 27-29. The short-form X register is the one hole.

## Known gaps

- **No X excerpts.** The syndication profile-timeline endpoint was rate-limited at first call and no @randfish status IDs were harvested from his blog embeds this session. LinkedIn covers the short-form register for now.
- **Lost and Founder was not fetched.** The 2023 "Final Chapter" epilogue on SparkToro stands in for the book voice; do not quote the book as verbatim. Publisher excerpt pages or Google Books previews are the next source.
- **Moz-era transcripts are third-party.** The Whiteboard Friday transcripts are Speechpad transcriptions, so items 27-29 are labeled documented even though Moz published them officially; his 2025 SparkToro whiteboard transcripts, which he pastes into his own posts, are treated as verbatim-as-published.
- **LinkedIn discovery is manual.** WebSearch does not surface his post permalinks; the working method was reading `/posts/randfishkin_...` links out of the logged-out profile HTML. Only October 2026 posts were sampled, so older LinkedIn tone is unsampled.
- **Stat provenance is his claim, not independently audited.** The 68% zero-click figure (Similarweb clickstream), <0.5% AI referral traffic, and the 1/5th-of-Americans AI usage figure are his published readings of third-party panels; re-verify before republishing.
- **Anything published after 2026-10-19 is unsampled.**

## Refresh instructions

1. Re-fetch `https://sparktoro.com/blog/wp-json/wp/v2/posts?author=2&per_page=40` and add 5-8 verbatim excerpts from posts published since October 2026; continue the numbering in the SparkToro section and mark any pasted whiteboard transcript as such.
2. Fetch `https://www.linkedin.com/in/randfishkin` with a desktop user agent, harvest fresh `/posts/randfishkin_...` permalinks, and add 4-6 verbatim posts with dates from JSON-LD or the activity ID.
3. Retry the X timeline once the rate limit resets (`https://syndication.twitter.com/srv/timeline-profile/screen-name/randfish`) or harvest status IDs from his blog embeds, then pull each with `https://cdn.syndication.twimg.com/tweet-result?id=<id>&token=a`; add a labelled "Verbatim excerpts (X posts)" section.
4. Look for a publisher excerpt or Google Books preview of Lost and Founder; add 3-5 verbatim excerpts under a labelled book section if the text is public.
5. Caption one recent 5-Minute Whiteboard or a podcast appearance with `yt-dlp --write-auto-sub --skip-download --sub-lang en "<url>"` only if the transcript is not already pasted into the post; otherwise prefer his pasted text.
6. Re-verify the panel statistics he cites (zero-click share, AI referral share) against the current SparkToro research posts, since he updates them yearly.
7. Re-verify that every URL is still live. Never carry a quote forward that was not re-read at its source.

## Pattern notes

### 1. The number, then the verdict
A sourced statistic opens the piece and a one-line judgment follows ("you're about to have a terrible, horrible, no-good year"; "Traffic is a vanity metric."). The Newsletter Writer and Contrarian Take Generator playbooks both open this way.

### 2. The verdict slam
Long evidentiary paragraphs end on a one-word paragraph ("Period.", "Nope."). Every playbook allows one slam per section and forbids stacking them.

### 3. Walk the logic together
He announces the walkthrough, admits it may be dry, and then does it step by step with each source named. The Contrarian Take Generator requires the promise and the sourced steps before the harsh verdict.

### 4. Evil with a mechanism, stake disclaimed
Moral words ("evil", "theft") arrive inside a sentence that lists exactly how, and he disclaims his own stake first ("this is hardly my fight"). The Ghostwriter playbook places the disclaimer before the harshest paragraph.

### 5. Open the books
Exact dollars, dates, board-room roles, and admitted motives ("Revenge isn't the healthiest of motivating emotions, but it damn sure is an effective one"). The Build-in-Public Writer will not start without the user's own figure and motive.

### 6. Folksy heat, warm close
"Marketing friends", "sure as heck", "frickin'", a jokey acronym, then "Good luck, friends" and a p.s. crediting someone. All four playbooks end on the warm sign-off rather than a CTA.
