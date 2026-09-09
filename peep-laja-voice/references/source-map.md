# Peep Laja Source Map

Research date: 2026-09-09
Refresh cadence: every 6 months (next: 2027-03)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| CXL blog (via Wayback Machine) | https://cxl.com/blog/author/peep-laja/ | Long-form posts on CRO, prioritization, agency/process rants, personal reading habits | Live site is Cloudflare-gated; Wayback Machine captures scrape cleanly |
| CXL author page | https://cxl.com/blog/author/peep-laja/ | Bio and a partial rolling list of post titles/teasers | Same Cloudflare gate; a 2025 Wayback capture of the author page listed post excerpts |
| LinkedIn | https://www.linkedin.com/in/peeplaja/ | Short-form register, current takes, real dialogue-style anecdotes | Login wall shown but post content still rendered on direct fetch |
| X (Twitter) | https://x.com/peeplaja | Shortest-form register, one-idea posts, dash lists | Scrapes cleanly on direct fetch of status URLs |
| Wynter | https://www.wynter.com | Current company positioning and blog index | Live site scrapes cleanly, but content is Wynter marketing copy, not confirmed personal authorship by Laja; not used for verbatim corpus |
| Podcast appearances (YouTube) | see below | Spoken register, framework explanations | ASR-only captions (`generated=True`) on all three sampled videos |

## What was actually fetched

**Cloudflare-dead, confirmed this session:** `pl/cxl.html` (cached from a prior session) returns a Cloudflare "Just a moment..." challenge page for a direct `cxl.com` request. Live cxl.com is not scrapeable with the plain fetch tool. Confirmed dead again on 2026-09-09 by inspecting the file: it is a Cloudflare challenge shell, not content.

**Wayback Machine, confirmed working this session:** direct-timestamp Wayback URLs (`https://web.archive.org/web/<14-digit-timestamp>/<url>`, timestamp taken from the CDX API, not a bare year) scrape cleanly and return full article text with byline. Five cxl.com posts were pulled this way and verified as Peep Laja's own byline before use:
- `https://web.archive.org/web/20191209160547/https://cxl.com/blog/better-way-prioritize-ab-tests/` (PXL post, by: Peep Laja)
- `https://web.archive.org/web/20200921133527/https://cxl.com/blog/working-hard-doesnt-matter-if-you-dont-know-what-youre-doing-rant/` (Rant, by: Peep Laja)
- `https://web.archive.org/web/20210112160808/https://cxl.com/blog/speero-agency/` (Speero announcement, by: Peep Laja)
- `https://web.archive.org/web/20200923043548/https://cxl.com/blog/introducing-pep-show/` (Pe:p Show intro, by: Peep Laja)
- `https://web.archive.org/web/20200426214940/https://cxl.com/blog/best-business-books-of-2011-imho/` (book list, by: Peep Laja)

One additional CXL post was fetched and explicitly REJECTED for the corpus: `https://web.archive.org/web/20200804030116/https://cxl.com/blog/conversion-optimization-myths/` ("10 Conversion Optimization Myths that Just Won't Go Away") is byline "By: Derek Gleason", not Peep Laja. It surfaced in search results attributed loosely to him; the byline check on the fetched page caught the misattribution before it entered the corpus.

A bare-year Wayback URL (e.g. `/web/2020/https://cxl.com/...`) does NOT reliably return article content; it returns the Wayback calendar-picker page. Always resolve an exact 14-digit timestamp via the CDX API first: `http://web.archive.org/cdx/search/cdx?url=<path>&output=json&limit=5`.

**LinkedIn and X, confirmed working this session:** four LinkedIn post URLs and three X status URLs fetched directly (no Wayback needed) returned full post text past the login-wall shell. Used in the corpus:
- linkedin.com/posts/peeplaja_people-want-to-put-you-in-a-box... (2021, box/positioning post)
- linkedin.com/posts/peeplaja_copy-is-often-where-great-messaging-strategy... (2024, copy vs. strategy)
- linkedin.com/posts/peeplaja_years-ago-i-hired-an-analyst-and-asked-him... (2023, data dialogue anecdote)
- x.com/peeplaja/status/1757425134795620376 (planning-as-procrastination)
- x.com/peeplaja/status/1795908976074281122 (fetched, media-companies take; not used in final corpus, available for refresh)
- x.com/peeplaja/status/1762463189042708789 (fetched, message-market fit / product-market fit; not used in final corpus, available for refresh)
One additional LinkedIn URL was fetched and not used: linkedin.com/posts/peeplaja_the-classic-marketing-wisdom-says-that-you... (2022, channel-strategy post referencing lemlist/Guillaume Moubeche) - available for refresh, held back only for space.

**Wynter.com:** the homepage and `/blog` index both scrape cleanly (no Cloudflare gate, unlike cxl.com), giving current company positioning copy and article titles. This is Wynter's marketing copy, not confirmed as Peep Laja's own sentence-level authorship, so it was NOT used as a verbatim personal-voice source. It is useful context for what Wynter as a company argues (message testing, B2B message layers), which lines up with his personal framework in the corpus.

**Podcast transcripts (cached from a prior session, re-verified this session):** `yt.py tracks` was re-run on all three cached video IDs and confirmed `generated=True` (ASR, no human caption track) for all three:
- `EvACl2xdC7s` - guest describes him as founder of "Conversion XL," now "Winter" (Wynter); blogging-in-2024 discussion.
- `VfoKbF1FPXE` - Growth Colony (Australia B2B podcast), host Alex Hipwell, "Peplia"/"Pv" transcription of "Peep Laja"; USP/differentiation discussion.
- `yqH72GQSku4` - SaaS Inbound podcast; Wynter as message-testing platform, "bootstrapped to over $2M ARR," four-layer messaging framework.
All quotes drawn from these are labeled `documented` per the ASR rule, not `verified`.

## Known gaps

- **cxl.com live site is fully Cloudflare-gated.** Every direct fetch attempt (this session and the prior cached one) hits a "Just a moment..." challenge page. The entire verbatim CXL corpus here comes from Wayback Machine snapshots, not the live site. If Wayback ever de-indexes these captures, the corpus cannot be refreshed the same way.
- **wynter.com is scrapeable but was deliberately not used for verbatim quotes.** The company blog and homepage are current marketing copy, most likely written or edited by a content team, not confirmed sentence-by-sentence as his own writing. Using it risked misattributing house copy as his personal voice, so it was excluded from the corpus entirely rather than labeled `documented` and included.
- **No confirmed access to a full CXL newsletter issue.** He is reported (via podcast, ASR) to send a personal newsletter ("What's on my mind"), referenced on the Speero post's sidebar CTA, but no actual issue was located or fetched this session.
- **No book-length source.** He has not published a book under his own name comparable to Dunford's Obviously Awesome; his written corpus is blog posts, social posts, and interviews only. This is accurately reflected, not a gap to fix.
- **ARR and client numbers are secondhand.** The "$2M ARR" Wynter figure and any specific client names mentioned in podcast appearances come from a podcast host's framing or ASR transcription, not from his own published financials. Flagged `documented` and [VERIFY] in the skill's Guardrails; do not repeat as fact without independent confirmation.
- **Sample skews CXL-era (2011-2021) for long-form, 2021-2024 for short-form.** No verbatim Wynter-era (2022-2026) long-form writing was found, since Wynter does not appear to publish personal-byline long-form posts the way CXL did. The voice profile may under-represent how his register has evolved as a SaaS founder versus a CRO-agency operator. Confirm on refresh.

## Refresh instructions

1. Re-check whether cxl.com's Cloudflare gate has lifted; if it has, prefer live fetches over Wayback for currency.
2. Re-run the CDX API query for each cxl.com URL above and re-fetch the latest available capture's exact timestamp (do not reuse a bare year).
3. Re-run `yt.py search "Peep Laja <topic>" 8` for newer podcast appearances and check `yt.py tracks <videoId>` for a human caption track before assuming ASR-only.
4. Re-fetch linkedin.com/in/peeplaja and x.com/peeplaja for posts from the last 6 months; both scraped cleanly this session without needing login.
5. Re-check wynter.com for a personal-byline blog post (not company marketing copy) before adding any Wynter-era item as verbatim.
6. Confirm the "$2M ARR" figure and any client names against a source he has personally published (not a podcast host's paraphrase) before using them as fact anywhere client-facing.
