# Ross Simmonds Voice Source Map

Research date: 2026-10-19
Refresh cadence: every 6 months (next: 2027-04)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| rosssimmonds.com blog (WordPress REST API) | https://rosssimmonds.com/wp-json/wp/v2/posts?per_page=40 | 40+ long-form essays 2024-2026 with dates: distribution gospel, hiring, annual reviews, AI search | Open; `?slug=<slug>&_fields=date,link,title,content` returns the full HTML body |
| "The Power of Distribution: Why You Should Promote Your Content More" (Dec 4 2024) | https://rosssimmonds.com/blog/power-distribution/ | The cliche flip, the golden rule (twice as much time promoting), repetition is not spam | Open |
| "What I Watched Happen Over 72 Hours Changed How I Think About Everything" (Jun 10 2026) | https://rosssimmonds.com/blog/production-dead-distribution-wins/ | Obvious-now realization, "Folks.", production gatekeeping is dead, ignore vs. copy | Open |
| "If I Were Starting My Marketing Career Today, Here's What I'd Learn First" (Jul 15 2026) | https://rosssimmonds.com/blog/marketing-career/ | The hill, the backwards 80/20 ratio, "Distribution rules everything around me" | Open |
| "Should You Bet Your Sales Pipeline on… Distribution?" (Jun 11 2026) | https://rosssimmonds.com/blog/sales-pipeline-distribution/ | The 47 brand websites question, "Distribution is where real power lives" | Open |
| "Why I Care More About Curiosity Than Credentials When Hiring" (Jul 3 2026) | https://rosssimmonds.com/blog/curiosity-vs-credentials/ | "The Internet" as professor, curiosity beats credentials | Open |
| "My 2025 Annual Review" (Jan 2 2026) and "What 2025 Taught Me" (Dec 5 2025) | https://rosssimmonds.com/blog/2025-annual-review/ ; https://rosssimmonds.com/blog/2025-reflection/ | Momentum is earned, the flywheel started pulling, "Getting here wasn't easy" | Open |
| X @TheCoolestCool (threads) | https://threadreaderapp.com/user/TheCoolestCool | ~21 unrolled threads 2022-2024: the 90% / 50 visits thread, courage to be unfollowed, content = blog posts, 2023 advice list | Open; root tweet text and date via `https://api.fxtwitter.com/i/status/<id>`; mid-thread tweets from Thread Reader unrolls |
| LinkedIn posts | https://www.linkedin.com/in/rosssimmonds (profile lists 9 own-post permalinks) | Oct 2026 posts: AI search dilemma, 5 stages of grief, Dharmesh Shah at UNBOUND, JA Business Hall of Fame | Permalinks render logged out with a desktop UA; text in meta description, date in JSON-LD |
| Foundation Labs (bylined) | https://foundationinc.co/lab/author/ross-simmonds/ (WP author id 9); article https://foundationinc.co/lab/reddit-still-matters/ (Sep 16 2026) | Agency-register long-form under his byline: hot-take rebuttal, single-metric warning, triad close | HTML renders; WP REST `?author=9` intermittently 503s behind wp-simple-firewall |
| Distribution.ai launch post | https://rosssimmonds.com/blog/distribution-ai/ | Product-launch register (located, not excerpted) | Same WP API |
| The Ross Simmonds Show RSS 64, "How to Win AI Search: YouTube, Reddit, and the New Rules of LLM Visibility" (2026-07-31; cross-posted Nick Standlea Show interview) | https://traffic.megaphone.fm/HS9188321670.mp3 (feed https://feeds.megaphone.fm/create-like-the-greats) | Spoken register: items 101-110; minutes 2-47 transcribed, he is the guest answering one host | Open RSS enclosure; MAI-Transcribe-2 via OpenRouter, $0.075 |
| Book: Create Once, Distribute Forever (2022) | not fetched | Canonical framing of the motto | No public excerpt located; NOT accessed this round |

## What the corpus rests on

All 29 excerpts are verbatim from channels he writes himself: 16 from eight essays on rosssimmonds.com (2024-2026, full bodies via the WordPress REST API with dates), 5 from his own X account (root tweets re-fetched and dated via fxtwitter, mid-thread tweets via Thread Reader unrolls), 5 from LinkedIn post permalinks (October 2026), and 3 from one Foundation Labs article bylined to him on his agency's site. Nothing comes from a quote aggregator. The personal-blog, X, LinkedIn, and agency-byline registers are all covered; two-thirds of the sample is from the last 12 months, so it reflects his current AI-search era voice as well as the decade-old distribution thesis. Ten further documented-grade spoken items (101-110) come from one diarized machine transcript of a podcast interview, added 2026-10-19. Confidence in wording is high for the blog, root-tweet, LinkedIn, and Foundation items and slightly lower for the mid-thread items, which rest on Thread Reader's copy.

## Known gaps

- **X sample is Thread Reader's curation.** The syndication timeline endpoint returned 429 during the run, so only ~21 curated threads (2022-2024) were reachable; standalone tweets and anything on X after 2024 are unsampled. Mid-thread tweets are labeled verbatim on the strength of Thread Reader's API copy and were not re-fetched individually.
- **Spoken sample is one interview.** Items 101-110 come from one guest interview cross-posted to The Ross Simmonds Show (RSS 64, 2026-07-31), about 45 minutes of diarized machine transcript. That covers his long-answer interview register: lists, anaphora, signposts, repeated lines. Still missing: his solo episodes, a keynote, and a second interview to confirm the pet phrases. Wording is documented grade, not verbatim.
- **The book was not accessed.** Create Once, Distribute Forever (2022) has no public excerpt located; the motto is sampled from an X thread closer, not the book.
- **Foundation Labs items are agency-byline.** They are first-person under his name but written for the agency blog; the WP REST author endpoint 503s intermittently, so only one article was sampled.
- **Only 9 LinkedIn permalinks were reachable** (those listed on his profile), all from October 2026; earlier LinkedIn voice is unsampled.
- **Anything published after 2026-10-19 is unsampled.**

## Refresh instructions

1. Re-fetch `https://rosssimmonds.com/wp-json/wp/v2/posts?per_page=40&_fields=date,link,title,slug` and, for each new slug, `?slug=<slug>&_fields=date,link,title,content`; add 5-10 verbatim excerpts with URLs and dates, continuing the numbering in the blog section.
2. Pull the X syndication timeline (`https://syndication.twitter.com/srv/timeline-profile/screen-name/TheCoolestCool`) when it is not rate-limited, or re-run Thread Reader (`https://threadreaderapp.com/user/TheCoolestCool`); verify each root via `https://api.fxtwitter.com/i/status/<id>` and add 5-8 verbatim posts, re-fetching the mid-thread items individually if the single-tweet endpoint (`https://cdn.syndication.twimg.com/tweet-result?id=<id>&token=a`) responds.
3. Re-fetch the LinkedIn profile `https://www.linkedin.com/in/rosssimmonds` with a desktop UA, collect new permalinks, read text from `<meta name="description">` and the date from JSON-LD; add 3-5 posts.
4. Retry `https://foundationinc.co/wp-json/wp/v2/posts?author=9&per_page=10` (it 503s intermittently) or browse `https://foundationinc.co/lab/author/ross-simmonds/`; add 2-3 excerpts to the Foundation Labs section if a new bylined piece exists.
5. Add a second spoken sample (a solo Ross Simmonds Show episode or another long interview) from the show's RSS enclosure: `python3 scripts/voice-dna/transcribe.py "<mp3-url>" --out /private/tmp/claude-501/stt/ross-simmonds --start-min 2 --max-min 45 --budget 0.15`, identify his speaker label per chunk from context, and append 6-10 documented items to the spoken section (no YouTube or yt-dlp).
6. Re-verify that every URL is still live. Never carry a quote forward that was not re-read at its source.

## Pattern notes

### 1. Stat and pivot
Threads and essays open on a number and a two-word verdict ("90% of content… This is a shame."; "That ratio is backwards."). The LinkedIn Content Expert and Ghostwriter both lead with it, and both require the stat to be sourced or [VERIFY]-flagged.

### 2. One-line paragraphs with one-word beats
Roughly half the paragraphs are a single sentence, and a lone word ("Folks.", "Hours.", "Quietly…") marks the turns. The Newsletter Writer tells the story in this rhythm before any lesson appears.

### 3. Triad build
Three parallel fragments with the third one different summarize a case or close a section ("Three different categories. Three different buying contexts. One consistent source."). The Newsletter Writer closes on a triad plus the motto.

### 4. The backwards ratio
He names the common split (80/20 creation to distribution) and calls it backwards, then gives the golden rule. The Newsletter Writer's hill paragraph and the Ghostwriter's middle section use this shape.

### 5. Buying-conversation lens
In AI-search content he separates visibility from the moment a buyer asks for a recommendation and says where the budget leaks. The LinkedIn Content Expert names this mechanism in one plain sentence.

### 6. Motto and PS close
Posts end on the repeated motto ("Create once. Distribute forever."), a "Keep moving. Keep distributing." imperative, or a PS pitch to Foundation or Distribution.ai. Every playbook puts the motto last and confines the pitch to one PS line; ghostwritten copy swaps in the user's motto and offer.
