# Ship 30 (Nicolas Cole and Dickie Bush) Voice Source Map

Research date: 2026-10-19
Refresh cadence: every 6 months (next: 2027-04)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| Ship 30 for 30 blog / Start Writing Online newsletter archive (173 posts, Webflow) | https://www.ship30for30.com/blog and https://www.ship30for30.com/sitemap.xml | Weekly co-bylined essays ("Dickie Bush & Nicolas Cole") plus solo-bylined posts; author shown in `class="author"`; no publish date on the page, sitemap `lastmod` only | Open HTML; curl with a desktop UA, text extracted locally |
| "10 Hard Lessons From Writing Online For 15+ Years" (lastmod 2024-09-11) | https://www.ship30for30.com/post/10-hard-lessons-from-writing-online-for-15-years | Co-authored: Dickie's 9-month blog nobody read; the brutal truth about going viral; the two-years-ago reader | Open HTML. Undated, last modified |
| "Clear vs. Clever" (lastmod 2022-06-26) | https://www.ship30for30.com/post/clear-vs-clever-a-quick-guide-to-avoid-the-1-mistake-in-writing | Co-authored: "If the reader is confused, they're going."; the five-words test; "Boom. Done." | Open HTML. Undated, last modified |
| "What Is Digital Writing? 7 Rules To Live By" (lastmod 2021-11-02) | https://www.ship30for30.com/post/what-is-digital-writing-7-rules-to-live-by | Co-authored: the 47-tabs-open reader; "You can't steer a stationary ship"; "Hemingway's era is over."; "Hit publish. Then hit publish again." | Open HTML. Undated, last modified |
| "How To Write Viral Twitter Thread Hooks (With 6 Clear Examples)" (lastmod 2022-10-23) | https://www.ship30for30.com/post/how-to-write-viral-twitter-thread-hooks-with-6-clear-examples | Dickie Bush solo: the hook anatomy, twisting the knife, the "silent controversial opinion" | Open HTML. Undated, last modified |
| "20 Quotes From The Art and Business of Online Writing" (lastmod 2022-06-27) | https://www.ship30for30.com/post/20-quotes-from-the-art-and-business-of-online-writing-by-nicolas-cole | Nicolas Cole solo: his own list of lines from his 2020 book; the only book text sampled | Open HTML. Undated, last modified; the post's "1 year anniversary" line matches a 2021-08-30 X post |
| X @dickiebush, single posts | https://cdn.syndication.twimg.com/tweet-result?id=<id>&token=a | 7 posts 2021-2023 with ISO dates: the 41,438-like Twitter features thread, the $120,000 college hook, the Mr. Beast study, the Monthly Review, the 732-follower origin post | Open, no login; IDs harvested from embeds on ship30for30.com posts and dickiebush.com/threads. Profile timeline endpoint was rate-limited |
| X @Nicolascole77, single posts | https://cdn.syndication.twimg.com/tweet-result?id=<id>&token=a | 4 posts 2021-2023: 500 business books, Worst Writing Advice, the five-step writer income ladder, "Small words ruin sentences" | Same endpoint; same rate-limit note |
| Dickie Bush Substack ("Dickie's Digest") | https://dickiebush.substack.com | Personal essays 2025: 22 inconvenient truths, 9 scaling lessons, the 4-month rut, 8 years of journaling | Substack API: `/api/v1/archive?sort=new` and `/api/v1/posts/<slug>` return full `body_html`; all `audience: everyone` |
| Nicolas Cole, The Art & Business of Writing (Substack) | https://artandbiz.substack.com | Long free essays 2024-2026: 8 brutal truths ("Dear Writer,"), $20M course lessons, document the journey, the First $1 Roadmap | Same Substack API, free posts |
| Write With AI (Substack, Cole and Bush) | https://writewithai.substack.com | Paid newsletter; a few free co-bylined posts | Archive JSON open; most posts `only_paid`; not used for excerpts |
| Nicolas Cole on Medium | https://medium.com/feed/@nicolascole77 | Daily 2026 essays on ghostwriting income, full bodies in RSS | Located, not excerpted; the Substack covers the same voice and era |
| nicolascole.com | https://www.nicolascole.com/ | Hub linking books, Substacks, and three blog posts | Open HTML (Webflow); not excerpted |

## What the corpus rests on

All thirty-eight excerpts are verbatim and each carries its speaker: eleven co-authored items from the Ship 30 for 30 blog and Start Writing Online archive bylined "Dickie Bush & Nicolas Cole", fifteen Dickie Bush items (one solo-bylined Ship 30 post, seven X posts fetched individually by status ID, and his 2025 Substack essays), and twelve Nicolas Cole items (four X posts, his 2024-2026 Substack essays, and his own on-blog list of quotes from his 2020 book). Blog text was read from the live Webflow pages, Substack text from the public API with full bodies, and X text from the syndication tweet-result endpoint with timestamps. Nothing comes from a quote aggregator and no documented-grade material was needed. Written registers (co-authored newsletter, X hooks, solo Substack letters) are covered for both writers; there is no spoken sample. Confidence in wording is high for all thirty-eight items; confidence in first-publication dates for the Ship 30 blog posts is low because the pages carry no date.

## Known gaps

- **No spoken material.** No podcast or video transcript of either writer was collected; yt-dlp was not attempted and podscripts.co was not probed for the Ship 30 "Digital Writing Podcast" or Cole's "Dear Writer" audio. Do not describe how either of them talks on a podcast.
- **Ship 30 blog posts are undated on the page.** Dates given are sitemap `lastmod` values, which may be later than first publication (the "10 Hard Lessons" post has a 2024-09-11 lastmod but reads as older). Cite them as "undated, last modified".
- **The X sample skews to greatest hits.** The profile timeline endpoint returned "Rate limit exceeded" for both handles, so tweet IDs came only from embeds on ship30for30.com and dickiebush.com/threads; the sample is their best-performing 2021-2023 threads, not everyday posts, and thread openers are quoted only to their first post.
- **The 2020 book is represented only through Cole's own 20-quote list.** No fuller text of The Art and Business of Online Writing is publicly accessible; do not quote the book beyond those lines.
- **Write With AI is paywalled** (`only_paid`) and was not used; the co-authored AI-writing register is unsampled.
- **Cole's Medium feed and nicolascole.com were located but not excerpted.** The Substack covers the same voice and era.
- **Ritual newsletter lines ("Ahoy and happy Monday!", "Chat next week!", the location stamps) come from the research notes**, not from a numbered excerpt; the corpus has the "We have a saying in Ship 30 for 30" line but not a full ritual open or close.
- **Anything published after 2026-10-19 is unsampled.**

## Refresh instructions

1. Re-fetch `https://www.ship30for30.com/sitemap.xml`, diff against the 173 known post URLs, and read any new posts with a desktop UA; add 5-8 verbatim excerpts tagged co-authored or by the solo byline shown in `class="author"`. Add one full ritual opener and closer from a recent newsletter issue as numbered items so the crew register is quoted, not just noted.
2. Pull both Substack archives (`https://artandbiz.substack.com/api/v1/archive?sort=new`, `https://dickiebush.substack.com/api/v1/archive?sort=new`) and fetch new free posts via `/api/v1/posts/<slug>`; add 3-5 verbatim excerpts per writer with dates.
3. Retry the X timeline endpoint (`https://syndication.twitter.com/srv/timeline-profile/screen-name/dickiebush` and `.../Nicolascole77`) once, off-peak, to sample everyday posts rather than embedded hits; fall back to `https://cdn.syndication.twimg.com/tweet-result?id=<id>&token=a` for individual IDs. Add 3-5 posts per writer.
4. Caption one episode of the Ship 30 podcast or a long guest appearance by each writer with `yt-dlp --write-auto-sub --skip-download --sub-lang en "<url>"`; add 3-5 documented excerpts per speaker under a new "Documented excerpts (ASR)" heading and add a spoken-register line to the stats.
5. If a publisher sample chapter of The Art and Business of Online Writing or of Cole's later books appears, add it as a labelled "Book" section; until then keep book text limited to Cole's own quote list.
6. Re-verify that every URL is still live and that each speaker tag still matches the byline on the page. Never carry a quote forward that was not re-read at its source.

## Pattern notes

### 1. The four-line hook
Bold declarative, credibility number, knife twist, colon promise ("College completely failed in teaching me how to write. / So I spent over 500 hours... / But unlike college, these won't cost you $120,000. / Here they are for free:"). The Hook Creator generates against this anatomy and the LinkedIn Content Expert compresses it to two lines plus the colon.

### 2. One idea per line, stems stacked
Lines are a sentence or less and rhythm comes from repeating a stem ("That means nights. / That means weekends."; "And my first $100. / And my first $1,000."). The Ghostwriter places one stacked stem at the peak of every piece and treats a two-idea line as an error.

### 3. Clear, not clever
Confusion loses the reader; the test is saying what the thing is in five words or less ("Sales Analytics For Creators. Boom. Done."). Every playbook runs the five-words test before drafting and bans puns and jargon.

### 4. The silent controversial opinion
Cole's hook form is the thing everyone thinks and nobody says ("They should have been blog posts."); Dickie names the move in his hook breakdown. The Hook Creator requires at least two per batch.

### 5. The receipt and the miss
Both writers prove with their own exact figures and disclose failure plainly (the 732-follower tweet, the $1M per month target missed, the 4-month rut, the webinar that never ran itself). The Ghostwriter asks for the user's own receipt and miss before writing.

### 6. Two speakers, one brand
Cole writes stern letters ("Dear Writer,") from an origin story; Bush writes energetic frameworks from a study plus habit evangelism; the crew voice is nautical and ritual. Every playbook declares the register (Cole, Bush, or co-authored) in the draft header and refuses to blur them.
