# Byron Sharp Voice Source Map

Research date: 2026-10-19
Refresh cadence: every 6 months (next: 2027-04)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| Byron Sharp blog (WordPress) | https://byronsharp.wordpress.com/ | 159 posts 2010-2020, 10-1,400 words each: polemics on loyalty, differentiation, brand equity, modelling, digital hype; 27 verbatim excerpts | Open. `https://public-api.wordpress.com/rest/v1.1/sites/byronsharp.wordpress.com/posts/?number=100&fields=ID,date,title,URL,content` returns full bodies (the site's own /wp-json is disabled) |
| "True Brand Loyalty – it doesn't matter" (7 Aug 2013) | https://byronsharp.wordpress.com/2013/08/07/true-brand-loyalty-it-doesnt-matter/ | Blog post reproducing "a footnote from How Brands Grow" verbatim; the only public book text found (items 3-4) | Open via the blog; Google Books and publisher samples not fetchable |
| X @ProfByron | https://x.com/ProfByron | ~100 short posts 2018-2023: one-line laws on availability, search, segmentation, ROI, brand purpose; 8 verbatim excerpts | `curl https://syndication.twitter.com/srv/timeline-profile/screen-name/ProfByron` (parse `__NEXT_DATA__`); full text per post via `cdn.syndication.twimg.com/tweet-result?id=<id>&token=a`. Rate-limits after 2-3 hits |
| In The Black (CPA Australia), "Business academic Byron Sharp says marketers are doing it all wrong" (1 Dec 2015) | https://web.archive.org/web/20160714155106/http://intheblack.com/articles/2015/12/01/business-academic-byron-sharp-says-marketers-are-doing-it-all-wrong | Long interview with ~15 direct quotes; the only spoken sample; DOCUMENTED (journalist transcription), 4 excerpts | Live URL is 404; the Wayback copy fetches cleanly |
| Ehrenberg-Bass "News and Insights" (marketingscience.info) | https://marketingscience.info/news-and-insights/ | Pointer pages to WARC interviews and podcasts (e.g. "Byron Sharp on the legacy of How Brands Grow") | Open, but bodies are 1-2 paragraph summaries linking to paywalled WARC. Not used for excerpts |
| WARC author page | https://www.warc.com/NewsAndOpinion/Author/Byron%20Sharp | Bylined WARC responses (to Ritson 2016, to Tom Morton 2022) | Paywalled; not fetched. Candidate for Wayback in a later pass |

## What the corpus rests on

Thirty-five of thirty-nine excerpts are verbatim from channels he writes himself: twenty-seven from his own WordPress blog (2010-2020), pulled as full post bodies through the wordpress.com public API with his double spaces, spaced question marks, and typos intact, and eight from his own X account (2019-2021) read from the syndication endpoint. Two of the blog items are a footnote he reproduced from How Brands Grow, so the book register is represented by his own hand. Four are documented-grade: direct quotes attributed to him by a journalist in one 2015 interview, the only spoken sample. Nothing comes from a quote aggregator. The blog is the main written channel and is rich; the X register is thinner but consistent with it. Confidence in wording is high for items 1-35 and moderate for 36-39. Both sampled channels are dormant (blog since 2020, X since 2023), so the corpus describes his established register rather than his current output.

## Known gaps

- **The books were not sampled.** No fetchable text of How Brands Grow or How Brands Grow Part 2 exists beyond the one footnote on the blog; publisher samples and Google Books previews did not respond to curl. Do not quote the books as verbatim. A later pass could try archive.org lending snippets or Ehrenberg-Bass open-access report PDFs.
- **WARC responses are paywalled.** His bylined replies to Ritson (2016) and Tom Morton (2022) were not fetched; Wayback was not tried for those URLs.
- **One spoken sample, and it is journalist transcription.** No podcast transcript was captured; Ehrenberg-Bass pointer pages reference Marketing Today (Alan Fraser, 2017) and Let's Talk Marketing (Adam Fraser) episodes, and podscripts.co was not checked. Use items 36-39 for stance and idiom, not exact wording.
- **Both sampled channels are dormant.** The blog stopped in September 2020 and X in 2023; his current channel appears to be LinkedIn, which was not searched this round. Any register shift since 2023 is unsampled.
- **X dates are partly inferred.** Dates for posts not individually fetched were decoded from snowflake IDs rather than read from the API.
- **Anything published after 2026-10-19 is unsampled.**

## Refresh instructions

1. Re-pull the blog through `https://public-api.wordpress.com/rest/v1.1/sites/byronsharp.wordpress.com/posts/?number=100&fields=ID,date,title,URL,content` (and `&offset=100` for the rest); if any post is newer than September 2020, add 3-5 verbatim excerpts and continue the blog section numbering.
2. Search LinkedIn for "Byron Sharp" with a desktop UA and WebSearch `"Byron Sharp on LinkedIn"`; if post permalinks render logged out, add 6-10 verbatim posts as a new labelled section and note whether the register has shifted.
3. Try Wayback for the WARC responses (`https://web.archive.org/web/2016*/warc.com*Sharp*`); if a bylined reply is captured, add 3-5 verbatim excerpts under a "WARC bylined responses" heading; these would strengthen the Objection Handling Expert playbook.
4. Caption one podcast appearance with `yt-dlp --write-auto-sub --skip-download --sub-lang en "<url>"` (or check podscripts.co for Marketing Today / Let's Talk Marketing); add 3-5 documented excerpts and update the spoken-register stat.
5. Check `https://marketingscience.info/` for open-access Ehrenberg-Bass reports with his byline; add 2-4 verbatim excerpts if found, labelled as institute publications.
6. Re-verify that every URL is still live or still archived. Never carry a quote forward that was not re-read at its source.

## Pattern notes

### 1. Orthodoxy restated, then negated
Posts open by stating the received wisdom in its own words and flip it in the next sentence; titles are often the contrarian claim itself. The Contrarian Take Generator and the Ghostwriter both start here.

### 2. Premise, evidence, dismissal
Paragraphs are two to four flat sentences closed by a 2-6 word verdict ("Dangerously simplistic.", "that's it.", "Wow."). Every playbook ends its template on a verdict line rather than a summary.

### 3. Show me the evidence, then reframe
The universal reply asks for the pattern across many brands, then reframes the cherished metric as an effect of market share ("attitudes improve, but mostly after we gain market share"). The Objection Handling Expert is built from these two moves.

### 4. Concede the mundane, deny the magic
Programmatic is useful automation but not targeting magic; segmentation is fine but targeting to exclude is not. The Objection Handling Expert uses this to answer "but it works".

### 5. Analogy to a real science and the hip pocket
He borrows from Popper, Einstein, Mendel, chaos theory, and the Roman chickens to show what evidence looks like, and names the consultant's financial interest as the reason the fad persists. The Contrarian Take Generator allows one of each per piece, aimed at types, never at a person's character.

### 6. One-line laws and "X is not Y"
On X he compresses to "Search is physical availability." and "mental availability is not awareness"; parenthetical asides and scare quotes carry the sarcasm in longer prose. The Ghostwriter closes on the law; the override converts his spaced en dashes to full stops, colons, or parentheses.
