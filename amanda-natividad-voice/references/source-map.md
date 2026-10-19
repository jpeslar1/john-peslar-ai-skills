# Amanda Natividad Voice Source Map

Research date: 2026-10-19
Refresh cadence: every 6 months (next: 2027-04)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| SparkToro blog, author=Amanda (WordPress REST) | https://sparktoro.com/blog/wp-json/wp/v2/posts?author=3&per_page=40 | ~40 bylined long-form essays 2025-2026: the zero-click doctrine, "No, I Will Not A/B Test That", "Nobody Is Dying on Hills", the invisible subtweet, Office Hours write-ups | Open; full bodies in `content.rendered` |
| "No, I Will Not A/B Test That" (Apr 21 2025) | https://sparktoro.com/blog/no-i-will-not-a-b-test-that/ | Conviction over testing; "procrastination disguised as optimization"; "Make the change. Move on." | Open |
| "The Case for Zero-Click Content in a Zero-Trust Ecosystem" (Jul 23 2025) | https://sparktoro.com/blog/the-case-for-zero-click-content-in-a-zero-trust-ecosystem/ | "Don't Depend on the Link"; the 4-5 to 1 ratio; the 95% | Open |
| "The Click Is Now Optional. Here's What Isn't." (Jun 9 2026) | https://sparktoro.com/blog/zero-click-search-what-still-works/ | "Hold onto your butts"; good news / bad news opener; 68% zero-click stat credited to Rand | Open |
| "Algorithms Don't Just Happen to Us" (Sep 22 2026) | https://sparktoro.com/blog/algorithms-dont-just-happen-to-us-we-train-them/ | The iced-coffee detour with signposted payoff; the TL;DR line | Open |
| The Menu (Substack, Zero Click Marketing newsletter) | https://amandanat.substack.com/api/v1/archive?sort=new and /api/v1/posts/<slug> | 23 weekly essays Mar-Oct 2026, all free; "Ungate the Argument. Gate the Utility.", "The Work Is Bigger Than the Receipt", "Don't Market More. Matter More." | Open JSON |
| LinkedIn posts (logged-out permalinks) | https://www.linkedin.com/in/amandanat exposes recent `/posts/amandanat_...` links | Short-form posts 2022-2026: the quoted-objection opener, two-types sort, journey arrows, the Flypost study post | Open with a desktop UA; full text in the page body plus JSON-LD `datePublished`; only `/recent-activity/` login-walls |
| X @amandanat single posts | https://cdn.syndication.twimg.com/tweet-result?id=<id>&token=a | Verbatim tweet text plus ISO date; two posts sampled by ID | Open per ID; the profile timeline endpoint was rate-limited this session |
| Zero Click Marketing podcast (she hosts) | https://share.transistor.fm/s/04446b98 | Spoken register; episodes pair with Substack write-ups | This episode not transcribed; one other episode transcribed 2026-10-19 (row below) |
| Zero Click Marketing episode "What If You Can't Prove Your Marketing Worked?" (2026-08-25; replay of her Wistia Talking Too Loud interview) | https://share.transistor.fm/s/3edc1cfa (MP3 https://media.transistor.fm/3edc1cfa/e5d739bd.mp3) | Spoken register: items 101-110, minutes 2-47 transcribed, she is the guest answering two hosts | Open RSS enclosure (feeds.transistor.fm/zero-click-marketing); MAI-Transcribe-2 via OpenRouter, $0.075 |
| Zero Click Marketing (book, co-author Rand Fishkin) | https://amandanat.substack.com/p/pre-order-zero-click-marketing-the | Pre-order announcement only; no excerpt text | Not yet published at research date |

## What the corpus rests on

Thirty of thirty excerpts are verbatim from channels she writes herself: seventeen from bylined SparkToro blog posts (2025-2026) via the WordPress REST API, four from her own Substack The Menu (2026) via the Substack API, seven from her own LinkedIn posts read at logged-out permalinks, and two from her own X account pulled by status ID. Nothing comes from a quote aggregator. Ten further documented-grade spoken items (101-110) come from one diarized machine transcript of a Zero Click Marketing episode, added 2026-10-19. The long-form and LinkedIn registers are well covered; the X register rests on two posts. Confidence in wording is high for all 30 items.

## Known gaps

- **Spoken sample is one episode.** Items 101-110 come from one Zero Click Marketing episode (a replay of her Wistia Talking Too Loud interview, 2026-08-25), about 45 minutes of diarized machine transcript where she answers two hosts. That covers her interview register: long chained answers, hedges, self-repair. Still missing: her solo host episodes (likely more scripted), any keynote, and a second interview to confirm the pet phrases. Wording is documented grade, not verbatim.
- **X sample is two posts.** The syndication profile-timeline endpoint returned "Rate limit exceeded" on the first call; only the two tweets embedded in her SparkToro posts were pulled by ID. The LinkedIn register, which she uses more now, is sampled properly.
- **The book is unsampled.** Zero Click Marketing (with Rand Fishkin) was pre-order only at research time; do not quote it as verbatim.
- **LinkedIn discovery is manual.** WebSearch does not index her post permalinks; the working method was reading `/posts/amandanat_...` links off the logged-out profile page and out of LinkedIn URLs embedded in her blog HTML. Older posts (pre-2022) were not sampled.
- **Research she cites is not independently audited.** The 68% zero-click figure, the 95% out-of-market figure, and the 116,000-post LinkedIn study are Rand Fishkin's and third parties' work as reported by her; treat them as her published claims and re-verify before republishing.
- **Anything published after 2026-10-19 is unsampled.**

## Refresh instructions

1. Re-fetch `https://sparktoro.com/blog/wp-json/wp/v2/posts?author=3&per_page=40` and add 5-8 verbatim excerpts from posts published since October 2026, with URLs and dates; continue the numbering in the SparkToro section.
2. Pull `https://amandanat.substack.com/api/v1/archive?sort=new` and `/api/v1/posts/<slug>` for new issues of The Menu; add 3-5 verbatim excerpts and confirm issues are still `audience: everyone`.
3. Fetch `https://www.linkedin.com/in/amandanat` with a desktop user agent, harvest fresh `/posts/amandanat_...` permalinks, and add 4-6 verbatim posts with dates decoded from the activity ID or JSON-LD.
4. Retry the X timeline once the rate limit resets (`https://syndication.twitter.com/srv/timeline-profile/screen-name/amandanat`) or harvest status IDs from her blog embeds, then pull each with `https://cdn.syndication.twimg.com/tweet-result?id=<id>&token=a`; add 4-6 posts to the X section.
5. Add a second spoken sample (a solo Zero Click Marketing episode or another interview) from the show's RSS enclosure: `python3 scripts/voice-dna/transcribe.py "<mp3-url>" --out /private/tmp/claude-501/stt/amanda-natividad --start-min 2 --max-min 45 --budget 0.15`, identify her speaker label per chunk from context, and append 6-10 documented items to the spoken section (no YouTube or yt-dlp).
6. Check whether Zero Click Marketing has published; if a publisher sample chapter or excerpt page exists, add 3-5 excerpts under a labelled book section and note which co-author's voice the passage reads as.
7. Re-verify that every URL is still live. Never carry a quote forward that was not re-read at its source.

## Pattern notes

### 1. State it, then scope it
A hard opinion in one complete sentence ("most A/B tests are a waste of time"), then the honest boundary ("at least for small and medium-sized businesses"). The LinkedIn Content Expert playbook makes the scope line mandatory in lines two or three.

### 2. The punch and the coined closer
Medium sentences do the arguing; three-word fragments do the turning ("Get seen.", "That's not the point."), and paragraphs end on an aphorism she coins herself. Every playbook ends on a coined line rather than a CTA.

### 3. Parenthetical self-roast
The joke lives in parentheses and the target is herself or the discourse ("(Boom. Self-roast!)", "(gender neutral)"). The Ghostwriter playbook allows exactly one per piece.

### 4. Quoted objection, then answer
She opens by writing the pushback in quotation marks ("But if I do zero-click marketing, how will people go to my website?") and corrects the misreading. The Ghostwriter playbook uses this as its default opener for doctrine pieces.

### 5. Credit in-line
Borrowed research and ideas carry the name of the person inside the sentence (Rand, Jay Acunzo, Talia Wolf). The Newsletter Writer playbook requires the receipt's source to be named in the same block.

### 6. Give before the ask
Four or five pure-value posts before one ask, no gate on the argument, no link as the only mechanism of value. The Newsletter Writer and LinkedIn Content Expert playbooks both enforce the ratio.
