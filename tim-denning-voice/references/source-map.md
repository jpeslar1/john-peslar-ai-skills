# Tim Denning Voice Source Map

Research date: 2026-10-19
Refresh cadence: every 6 months (next: 2027-04)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| Substack "Tim Denning" archive API | https://timdenning.substack.com/api/v1/archive?sort=new&limit=20 then https://timdenning.substack.com/api/v1/posts/<slug> | Weekly essays Aug-Oct 2026 with subtitle, date, and full body_html; all free (audience: everyone) | Open |
| Substack: Not being unhinged is quietly costing you everything (Oct 16 2026) | https://timdenning.substack.com/p/not-being-unhinged-is-quietly-costing | Newest sampled piece; "call to arms", Domino's parable, brown-noser confession | Open |
| Substack: I don't want to be rich (Sep 8 2026) | https://timdenning.substack.com/p/i-dont-want-to-be-rich | "Everyone wants to be rich. Except f*cking me."; the verdict stack | Open |
| Substack: Stop f*cking trying to feel confident (Sep 25 2026) | https://timdenning.substack.com/p/stop-fcking-trying-to-feel-confident | "Give me 4 mins."; confidence as action | Open |
| Substack: The quiet life is the most ignored way to succeed (Oct 9 2026) | https://timdenning.substack.com/p/the-quiet-life-is-the-most-ignored | "I'm a millionaire, but most people in my life don't know." | Open |
| timdenning.com (WordPress) | https://timdenning.com/wp-json/wp/v2/posts?per_page=50 | 50 full essays, Feb-Dec 2024; same titles as his paywalled Medium pieces, so they stand in for the Medium register | Open, default curl UA |
| Essay: 16 Harsh Truths About Your Writing (Mar 25 2024) | https://timdenning.com/writing-harsh-truths/ | Credential-by-numbers opener, hashtag rant, 5th-grader headline rule | Open |
| Essay: Why Tim Denning Writes like Sh*t and Is Rich (Apr 29 2024) | https://timdenning.com/tim-denning-is-rich/ | Critic's title turned; "Readers buy humans, not niches." | Open |
| LinkedIn Pulse: I Will Teach You How To Make Your First $10,000 From Writing (Jan 10 2020) | https://www.linkedin.com/pulse/i-teach-you-how-make-your-first-10000-from-writing-tim-denning | Older, calmer, list-driven register; snowball analogy | Renders logged out with a desktop UA |
| X @Tim_Denning single post | https://cdn.syndication.twimg.com/tweet-result?id=1755543316769480953&token=a | One verbatim post with ISO date (Feb 8 2024) | Single posts open per status ID; the timeline endpoint returned 429 |
| Medium @timdenning RSS | https://medium.com/feed/@timdenning | Titles and one-line subtitles only | Bodies paywalled ("Continue reading on ILLUMINATION"); not used for excerpts |
| LinkedIn feed posts (timdenning) | n/a | Short posts | NOT FOUND: WebSearch surfaced no linkedin.com/posts permalinks; profile authwalls |
| Podcast: How writing changed Tim Denning's business life forever (#637), The Small Business Big Marketing Podcast with Tim Reid, 2023-05-22 | https://podcasts.apple.com/us/podcast/how-writing-changed-tim-dennings-business-life-forever-637/id319019197?i=1000613999291 (MP3: https://traffic.omny.fm/d/clips/7a7ebf98-497f-4c50-b05f-ae98000a0713/bdb9761b-a3b9-4250-bfc5-aeb70044e585/c39f8557-7af0-4201-803e-b00a00398007/audio.mp3) | Spoken register: 45 transcribed minutes (00:03 to 00:48) of a guest interview on finding his voice, Medium, platforms, email lists, and community; items 101-110, documented-grade | Open RSS enclosure; transcribed with MAI-Transcribe-2 via OpenRouter (diarized; speaker identified per 20-minute chunk from context) |

## What the corpus rests on

All 26 excerpts are verbatim and written by him: 10 from free weekly Substack essays (August to October 2026), 11 from full essay bodies on timdenning.com (2024, the same pieces he published on Medium), 4 from a 2020 LinkedIn Pulse article, and 1 X post. Nothing comes from a quote aggregator and nothing is documented-grade; there is no ASR material. The long-form essay register is covered across two eras (the calmer 2020 article and the profane, story-led 2024-2026 essays). Short-form LinkedIn is represented only by one X post. Confidence in wording is high for every item. Added 2026-10-19: items 101-110 are documented-grade spoken excerpts from one 2023 podcast interview (machine transcript); the written counts above are unchanged.

## Known gaps

- **No LinkedIn feed posts.** WebSearch returned no `linkedin.com/posts/` permalinks for him and the profile authwalls, so his short-form LinkedIn cadence (half a million followers, by his own count) is represented only by one X post and the long-form Pulse article. The skill therefore carries Newsletter Writer rather than LinkedIn Content Expert.
- **X timeline unsampled.** The syndication timeline endpoint returned 429 on first hit; only one status ID surfaced via search.
- **Medium bodies paywalled.** The timdenning.com essays carry the same titles, so the voice is covered, but Medium-specific formatting (pull quotes, image choices) is not.
- **Spoken sample is one episode.** Items 101-110 come from one 2023 guest interview (45 transcribed minutes, machine transcript, documented-grade). That is thin: it predates the profane 2024-2026 essays, follows one host's questions, and includes no 2025-2026 or solo speech. Spoken-style output beyond what those items show is still inferred.
- **Anything published after 2026-10-19 is unsampled.**

## Refresh instructions

1. Re-pull Substack: `curl -s 'https://timdenning.substack.com/api/v1/archive?sort=new&limit=20'` for slugs and dates, then `curl -s 'https://timdenning.substack.com/api/v1/posts/<slug>'` for `body_html`; convert to text locally. Add 5-10 verbatim excerpts from the newest essays with their subtitles, continuing the numbering.
2. Re-pull the blog: `curl -s 'https://timdenning.com/wp-json/wp/v2/posts?per_page=50'` (default curl UA) and sample any post-2024 essays if the site has resumed publishing.
3. Search for LinkedIn permalinks with WebSearch `"Tim Denning" "on LinkedIn:" <topic>` or `site:linkedin.com/posts timdenning`; fetch each with a desktop UA. If 5 or more short posts are found, add a "LinkedIn posts" section and reconsider adding a LinkedIn Content Expert playbook.
4. For X, collect status IDs from search and fetch each with `curl -s 'https://cdn.syndication.twimg.com/tweet-result?id=<id>&token=a'`; do not hit the timeline endpoint more than once.
5. If a spoken register is wanted, caption a podcast appearance with `yt-dlp --write-auto-sub --skip-download --sub-lang en <url>` and add 3-5 documented excerpts under a "Documented excerpts (ASR captions)" heading, flagged as such.
6. For the spoken register, pick a long-form episode with a direct MP3 in its RSS feed (find it with `curl -s "https://itunes.apple.com/search?term=<name>&entity=podcastEpisode&limit=25"`, field `episodeUrl`; no YouTube), then run `python3 /Users/johnpeslar/dev/john-peslar-ai-skills/scripts/voice-dna/transcribe.py "<mp3-url>" --out /private/tmp/claude-501/stt/tim-denning --start-min 2 --max-min 45 --budget 0.15` with `OPENROUTER_API_KEY` exported (about $0.10 per 60 minutes). Speaker numbers reset per chunk, so identify his label in each chunk from context, then add 6-10 documented excerpts to the spoken section, continuing from the highest item number. Prefer a 2025-2026 episode so the spoken sample matches the current essay era.
7. Re-verify that every URL is still live. Never carry a quote forward that was not re-read at its source.

## Pattern notes

### 1. Confession first
Essays open with a one- or two-line personal declaration of status or failure, then a short story, then the lesson. The Ghostwriter and Newsletter Writer playbooks refuse to start without the user's own admission.

### 2. Headline as thesis, subtitle as twist
Titles are full-sentence claims and subtitles invert or compress them; blog titles are numbered promises with a parenthetical payoff. The Hook Creator pairs every title with an inverting subtitle and runs the 5th-grader test.

### 3. Asterisked profanity and crude imagery
f*ck and sh*t always carry the asterisk, and one deliberately gross metaphor marks the moment of judgment. Every playbook caps the count and the Anti-patterns flag both over- and under-use as tells.

### 4. Receipt, then shrug
Credentials (1B+ views, 7 figures, half a million followers) are restated in nearly every piece and immediately waved off ("This is not a post designed to brag"). The playbooks place this once, early, and the Guardrails mark every number [VERIFY].

### 5. Announced provocation
The contrarian claim is preceded by a warning ("Let's stack up the hate comments right now."). The Ghostwriter and Newsletter Writer place it right before the verdict stack, once per piece.

### 6. Command close
Pieces end on a short order or dare ("Let's change that.", "Nail the headline or go home.") or a compressed aphorism ("Readers buy humans, not niches."). Every playbook template ends this way; a summary paragraph is listed as an anti-pattern.
