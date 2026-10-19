# Wes Kao Voice Source Map

Research date: 2026-10-19
Refresh cadence: every 6 months (next: 2027-04)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| Wes Kao's Newsletter (Substack) | https://newsletter.weskao.com/api/v1/archive?sort=new&limit=40 ; https://newsletter.weskao.com/api/v1/posts/<slug> | Bi-weekly essays 2023-2026 on managing up, executive communication, rigorous thinking; every post checked is `audience: everyone`; full `body_html` | Open JSON |
| "Defensible, but not good" (Jul 22 2026) | https://newsletter.weskao.com/p/defensible-but-not-good | The flat distinction opener; "We MUST use our judgment." | Open |
| "Avoid ASAP and other high-strung, non-specific words" (Jan 21 2026) | https://newsletter.weskao.com/p/avoid-asap-and-high-strung-words | The Slack DM hypothetical; "blast radius"; over-communicating as the right amount | Open |
| "Observe, assert, and validate (OAV)" (Oct 15 2025) | https://newsletter.weskao.com/p/observe-assert-and-validate-oav | Operator #1 versus Operator #2; "Asking how you can help is not as thoughtful as it seems" | Open |
| "15 principles for managing up" (Oct 25 2023) | https://newsletter.weskao.com/p/15-principles-for-managing-up | The canonical script pair with the no-sign and check-mark labels; the black-and-white-to-color realization | Open |
| Her "top posts" list (older canonical essays re-hosted) | https://www.weskao.com/articles links to /p/rigorous-thinking, /p/start-right-before-you-get-eaten-by-the-bear, /p/how-to-be-concise, /p/why-high-performers-make-assertions, /p/strategy-not-self-expression | Her named frameworks, many marked "originally published 2015-2020, expanded" | Open JSON via the same API |
| LinkedIn posts (logged-out permalinks) | https://www.linkedin.com/posts/weskao_... and /feed/update/urn:li:activity:<id> links embedded in her newsletter HTML | Short framework posts 2020-2023: bugs into features, simplify first, context, the bear story, the Substack launch | Open with a desktop UA; her profile page lists only others' posts about her, so permalinks came from WebSearch and newsletter embeds |
| weskao.com (Squarespace blog) | https://www.weskao.com/blog/spiky-point-of-view-lets-get-a-little-controversial | 2020 essay defining "spiky point of view" with eight of her own | Open HTML; `datePublished` 2020-07-10 |
| Lenny's Podcast episode page (Apr 6 2025) | https://www.lennysnewsletter.com/p/become-a-better-communicator-specific | Topic list only; transcript behind the paid tier | Not usable for excerpts |
| Maven course page | https://maven.com/wes-kao/executive-communication-influence | Course positioning copy | Not excerpted (sales copy) |
| Lenny's Podcast audio, "Become a better communicator: Specific frameworks to improve your clarity, influence, and impact" (2025-04-06) | https://www.lennysnewsletter.com/p/become-a-better-communicator-specific (MP3 via the show RSS, https://api.substack.com/feed/podcast/10845.rss) | About 45 minutes of her answering at length: sales then logistics, concision as economy of words, blast radius, signposting, excessive formatting, speaking accurately; items 101-110 (spoken, documented) | The RSS enclosure MP3 is free although the page transcript is paywalled; transcribed with MAI-Transcribe-2 via OpenRouter (minutes 5-50, past the intro and ads, $0.075) |

## What the corpus rests on

Thirty-four of thirty-four excerpts are verbatim from channels she writes herself: twenty-four from her Substack newsletter (2023-2026, including re-hosted canonical essays) via the Substack API, six from her own LinkedIn posts (2020-2023) read at logged-out permalinks, and four from her 2020 essay on weskao.com. Nothing comes from a quote aggregator and nothing is documented-grade; there is no spoken sample. The newsletter register is deeply covered and carries the structural habits (read time, Part I / Part II, Do this today, the standing sign-off); the LinkedIn register rests on older posts; the original blog is thin by design because it redirects to Substack. Confidence in wording is high for all 34 items. Items 101-110 were added afterwards as a documented-grade spoken sample: her 2025 Lenny's Podcast interview, machine-transcribed with speaker diarization.

## Known gaps

- **Spoken register rests on one episode.** Items 101-110 come from her 2025 Lenny's Podcast interview, machine-transcribed from the free RSS audio (the page transcript is still paywalled), so the wording is documented grade, not verbatim. Other interviews (In Depth, Productea, Success Story) and any live teaching from her course are untranscribed; one host-led episode is a thin sample.
- **Recent LinkedIn is unsampled.** Her profile page exposes only third-party posts mentioning her, not her own `/posts/weskao_...` permalinks; the six posts here came from WebSearch hits and `feed/update/urn:li:activity` links embedded in her newsletter HTML, all 2020-2023. Her 2024-2026 LinkedIn posts were not sampled.
- **The original blog is thin.** weskao.com now redirects its articles list to Substack; only one Squarespace-hosted essay (2020) remains directly fetchable, so the third source contributes four excerpts. The Substack archive compensates.
- **No book.** She has not published one; do not cite one as a source.
- **Anything published after 2026-10-19 is unsampled.**

## Refresh instructions

1. Pull `https://newsletter.weskao.com/api/v1/archive?sort=new&limit=40` and `/api/v1/posts/<slug>` for issues published since October 2026; add 5-8 verbatim excerpts with dates, confirm `audience: everyone`, and note any that are marked as expanded reworks of older essays.
2. Search `site:linkedin.com/posts weskao` with topic words (managing up, assertion, concise, feedback) and scan newer newsletter HTML for `urn:li:activity` links to harvest 2024-2026 permalinks; add 4-6 verbatim posts with dates decoded from the activity ID or JSON-LD.
3. Check whether a public transcript of a podcast appearance exists (podscripts.co or the show's own transcript page); if a video exists, caption it with `yt-dlp --write-auto-sub --skip-download --sub-lang en "<url>"` and add 3-5 documented excerpts under a new "Documented excerpts (ASR captions)" heading, then update the spoken-register stat.
4. Re-fetch `https://www.weskao.com/blog/spiky-point-of-view-lets-get-a-little-controversial` to confirm it is still live; if more Squarespace-era essays resurface, add 2-3 verbatim excerpts.
5. If she publishes a book, add a labelled section only from a publisher sample or public excerpt page.
6. Transcribe another long episode (ideally her 2025 In Depth (First Round) interview) from its RSS enclosure MP3, not YouTube: `python3 scripts/voice-dna/transcribe.py "<mp3-url>" --out /private/tmp/claude-501/stt/wes-kao --start-min 2 --max-min 45 --budget 0.15` (MAI-Transcribe-2 via OpenRouter, OPENROUTER_API_KEY in the environment, about $0.10 per hour). Identify the speaker label in each 20-minute chunk from context, then add 6-10 documented excerpts continuing from item 111.
7. Re-verify that every URL is still live. Never carry a quote forward that was not re-read at its source.

## Pattern notes

### 1. Name the concept
The idea gets a short label that becomes the title ("Strategy, not self-expression", "Defensible, but not good", "Observe, assert, and validate"). The Ghostwriter and Newsletter Writer playbooks open with the concept name and the LinkedIn playbook leads with it.

### 2. Two operators
The weak and the strong version are staged as two people speaking, followed by "Which operator do you think adds more value?" The Ghostwriter playbook uses this as its default opener.

### 3. The script pair
The line to retire and the line to use, both written as complete pasteable sentences under her no-sign and check-mark labels. Every playbook requires at least one; the Output Format returns the pairs first.

### 4. Define the opposite
The failure mode is named as precisely as the virtue (rigorous versus lazy thinking, defensible versus good, "Do this" versus "Don't do that"). The Newsletter Writer's Part I is built on this split.

### 5. Kindness as mechanism
Rules are justified by the effort they save the recipient ("If you can save your recipient a mental step, you're doing a kind thing"). The Anti-patterns treat a rule without this rationale as off-voice.

### 6. Cut to the bear, then do this today
Stories start at their last ten seconds and essays end with one concrete action and the standing sign-off. The Ghostwriter and Newsletter Writer playbooks both close on a "Do this today" block.
