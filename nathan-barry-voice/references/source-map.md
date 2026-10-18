# Nathan Barry Voice Source Map

Research date: 2026-10-19
Refresh cadence: every 6 months (next: 2027-04)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| nathanbarry.com essays, WordPress REST API | https://nathanbarry.com/wp-json/wp/v2/posts?categories_exclude=34&per_page=100 | 272 non-podcast posts 2013-2026 with full HTML bodies: annual reviews, the long framework essays, and the short 300-word single-idea posts | Open; `content.rendered` is the full body; `?slug=<slug>` fetches one post. Category 34 is podcast show notes (excluded) |
| "Endure long enough to get noticed" (Feb 18 2019) | https://nathanbarry.com/endure/ | The season-three question; "Create consistently. / Be patient for results." | Open HTML |
| "Be a creator, not a critic" (Oct 15 2018) | https://nathanbarry.com/critic/ | The creator-not-critic choice; criticism is "unnecessary" | Open HTML |
| "It doesn't get easier" (May 20 2016) | https://nathanbarry.com/easier/ | The gym-weight analogy; optimizations let you do 50x more | Open HTML |
| "Profit is leverage" (Jan 21 2019) | https://nathanbarry.com/leverage/ | Right revenue vs. any revenue; the monthly 30-minute spending review | Open HTML |
| "Stay in your lane and outlast your competition" (Aug 5 2019) | https://nathanbarry.com/outlast/ | "Nope."; "Even when that movement was a crawl." | Open HTML |
| "The magic of creating" (Nov 20 2019) and "Good things come to those who write" (Mar 11 2019) | https://nathanbarry.com/magic/ , https://nathanbarry.com/good-things/ | The creator's feelings named; highest-paid friends are writers or teachers; writing is teaching | Open HTML |
| "The ladders of wealth creation" (Dec 3 2019) and "The Billion Dollar Creator" (Sep 8 2020) | https://nathanbarry.com/wealth-creation/ , https://nathanbarry.com/billion/ | Jason Fried on money as a skill; Wendy's to $1 million per month; the $1.2 billion blog question; beyond the personal brand | Open HTML |
| "Creator Flywheels" (May 9 2023) and "The Audience Shortcut" (Jul 1 2025) | https://nathanbarry.com/creator-flywheels/ , https://nathanbarry.com/audience-shortcut/ | The South Africa water well; the blank-page scene; "$10,000,017 ... Holy shit."; crowd vs. audience | Open HTML |
| "Single-Axis Fallacy" (Sep 23 2025) and "2024 Review" (Jan 14 2025) | https://nathanbarry.com/single-axis-fallacy/ , https://nathanbarry.com/2024-review/ | The friend who cannot work out; "this is more for me than for you" | Open HTML |
| X @nathanbarry, single posts | https://cdn.syndication.twimg.com/tweet-result?id=<id>&token=a | 8 thread openers and posts 2020-2025 with ISO timestamps: Four Laws, Spotify offer, profit sharing, NRR, the Kit rebrand | Open, no login. The profile timeline endpoint returned 429 this session |
| api.fxtwitter.com long-post fallback | https://api.fxtwitter.com/nathanbarry/status/1963233744384586200 | Full text of long (note_tweet) posts that tweet-result truncates (item 32) | Open JSON |
| threadreaderapp.com user index | https://threadreaderapp.com/user/nathanbarry | Used only to locate thread-opener status IDs (21 threads, Mar 2023-Jun 2024); not cited | Open HTML |
| The Russell Brunson Show, "Shut It Down or Double Down" (Oct 21 2024), podscripts.co transcript | https://podscripts.co/podcasts/the-russell-brunson-show/shut-it-down-or-double-down-nathan-barrys-road-to-45m-with-kit-convertkit | About 70KB machine transcript of a 45-minute presentation plus Q&A; the spoken register (ASR renders his name "Nathan Berry", "street" for "streak") | Open HTML. DOCUMENTED (third-party ASR) |
| The Nathan Barry Show / Billion Dollar Creator (own podcast, 178 episodes) | https://nathanbarry.com/category/podcast/ | Show notes only; no published transcripts | Not used (no transcript text without yt-dlp or Whisper) |

## What the corpus rests on

Thirty-three of thirty-six excerpts are verbatim from channels he writes himself: twenty-five from thirteen essays on nathanbarry.com (2016-2025), pulled through the site's public WordPress REST API, and eight from his own X account, each post fetched individually by status ID with its timestamp (one long post completed through api.fxtwitter.com). Thread openers are quoted only to their first post. Three excerpts are documented-grade: a third-party machine transcript of one guest presentation (Oct 2024), with ASR slips flagged inline. Nothing comes from a quote aggregator. The essay register and the X register are well covered across nine years; the spoken register rests on a single appearance. Confidence in wording is high for items 1-33 and moderate for 34-36.

## Known gaps

- **Recent X posts are thin.** The profile timeline endpoint returned HTTP 429 on first hit, so all eight X excerpts came from individually fetched status IDs located through threadreaderapp's 2023-2024 index and one web search; 2025-2026 posts beyond item 32 are unsampled. Do not extend a thread past its quoted opener from memory.
- **His own podcast was not transcribed.** The Nathan Barry Show / Billion Dollar Creator publishes show notes only and podscripts.co has no show page for it. The only spoken sample is one guest appearance, captured by a third-party ASR; yt-dlp was not attempted this pass.
- **Books were not sampled.** Authority, The App Design Handbook, and Designing Web Applications are paid and no public extract was fetched. The Ladders and Billion Dollar Creator essays cover the same ideas in his own words; do not quote the books as verbatim.
- **LinkedIn was not searched.** His primary channels are the blog and X; a LinkedIn register, if one exists, is not represented.
- **Two original typos are preserved** ("make sure don't" in item 9, "todays" in item 14). They are flagged in the corpus and are not voice features.
- **Named sources beyond Jason Fried are from the research notes.** Jim Collins, Chris Guillebeau, Tim Grahl, and Ryan Delk are cited in the voice-pattern notes as people he credits; only Jason Fried appears in a sampled excerpt.
- **Anything published after 2026-10-19 is unsampled.**

## Refresh instructions

1. Re-fetch `https://nathanbarry.com/wp-json/wp/v2/posts?categories_exclude=34&per_page=20&orderby=date` and add 5-10 verbatim excerpts from essays published since October 2026, with slugs and dates; continue the numbering in the essay section. Confirm the most recent annual review is included.
2. Retry the X timeline (`https://syndication.twitter.com/srv/timeline-profile/screen-name/nathanbarry`) once, off-peak; if it still 429s, harvest new status IDs from `https://threadreaderapp.com/user/nathanbarry` and fetch each via `https://cdn.syndication.twimg.com/tweet-result?id=<id>&token=a`, using `https://api.fxtwitter.com/nathanbarry/status/<id>` for truncated long posts. Add 5-8 verbatim posts.
3. Caption one episode of his own podcast or one more long guest appearance with `yt-dlp --write-auto-sub --skip-download --sub-lang en "<url>"`; add 3-5 documented excerpts with timestamps and update the spoken-register stats. Prefer a solo or presentation episode so the speaker is unambiguous.
4. If a publisher or the author posts a sample chapter of Authority, add 2-3 verbatim lines as a labelled "Book" section; until then keep the books out of the verbatim section.
5. Re-verify that every URL is still live, including the podscripts.co transcript page. Never carry a quote forward that was not re-read at its source.

## Pattern notes

### 1. Scene before the name
Essays open on a concrete moment or a fact that cannot be right (the South Africa water well, the $10,000,017 screenshot, the friend who cannot work out) and introduce the Title Case framework only afterward. The Ghostwriter playbook keeps the first paragraph free of the framework's name.

### 2. The exact figure as proof
Persuasion runs on self-disclosed numbers written to the digit ($6.9 million in profit sharing, 99.8% net revenue retention, less than 5% of annual revenue). The Build-in-Public Writer refuses rounded figures and gives the loss equal space to the win.

### 3. Numbered laws
Principles compress into 3-5 numbered imperatives (the Four Laws of Building Audience, the Ladders, the three laws of a flywheel). The Ghostwriter uses a heading per law in long essays; the Build-in-Public Writer uses one line per step in threads.

### 4. The two-line close
Short essays end on two imperative lines or a single fragment that restates the thesis ("Create consistently. / Be patient for results."; "Even when that movement was a crawl."). The Newsletter Writer template ends on exactly this shape, with no CTA.

### 5. Stat or refusal, then the colon
X openers state a number or a refusal in one or two lines and hand off with "Here's what we did instead:" or "Here's how it works:". The Build-in-Public Writer uses this as its thread opener and caps it at one per post.

### 6. Creator, not critic, with credit
He sides with the creator, reframes rather than attacks, and names the source of every borrowed idea in the sentence that uses it (Jason Fried on money as a skill). Every playbook forbids critic mode and requires inline credit.
