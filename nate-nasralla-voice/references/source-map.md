# Nate Nasralla Voice Source Map

Research date: 2026-10-19
Refresh cadence: every 6 months (next: 2027-04)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| LinkedIn profile (logged out) | https://www.linkedin.com/in/natenasralla | Headline ("Simplifying complex sales for B2B teams moving upmarket... Author of Selling With / Brief & Brilliant") plus 9 recent post permalinks embedded in the HTML | curl, desktop UA, no login |
| LinkedIn post permalinks (16 posts, 2022-10 to 2026-10) | linkedin.com/posts/natenasralla_... (one URL per corpus item) | Full post text in the `<meta name="description">` tag, datePublished in JSON-LD; items 1-25 | curl, desktop UA; profile page plus WebSearch `"Nate Nasralla on LinkedIn" site:linkedin.com/posts` |
| fluint.io blog, "How and Why to Ditch the Old 3X Coverage Ratio Rule" | https://www.fluint.io/post/how-and-why-to-ditch-the-old-3x-coverage-ratio-rule | About 1,500-word bylined essay (Nate Nasralla, Co-Founder @ Fluint); items 26-27 | curl, clean HTML; datePublished 2026-06-24 |
| fluint.io blog, "The Ultimate Mid-Funnel Sales Plays: Top 5 Moves to Unstick Your Deals" | https://www.fluint.io/post/the-ultimate-mid-funnel-sales-plays-top-5-moves-to-unstick-your-deals | Bylined essay, 5 plays in a "Why deals stall / Why this play" structure; items 28-29 | curl; datePublished 2026-06-29 |
| fluint.io blog, "You're Renting a Supercar to do the School Run" | https://www.fluint.io/post/youre-renting-a-supercar-to-do-the-school-run | Bylined essay on model routing for RevOps, product-marketing heavy (Olli Mesa); item 30 | curl; datePublished 2026-07-15 |
| fluint.io, "Selling With" preview page | https://www.fluint.io/post/selling-with | Book landing copy in his voice (4 sentences); the rest is a gated early-reader list; item 31 | curl; no chapter text |
| fluint.io, "Brief & Brilliant: Book Preview" | https://www.fluint.io/post/brief-and-brilliant-book-preview | Second book's one-paragraph pitch; gated preview | curl; no chapter text; not excerpted |
| Selling With (book, 2023-11-08) | Audible and Goodreads listings only | Publisher blurb; no Look Inside or Google Books preview text found | Not usable for excerpts |
| The Caliber Show, "How to Create Champions That Sell For You When You're Not There" (2026-05-29, host Chris Orlob) | https://podcasts.apple.com/us/podcast/how-to-create-champions-that-sell-for-you-when-youre/id1696635955?i=1000770198640 (audio via the show RSS, https://anchor.fm/s/e5967874/podcast/rss) | About 29 minutes on champion building: the three I's, potential versus kinetic energy, co-drafting the problem statement, simple sound bites; items 101-110 (spoken, documented) | RSS enclosure (m4a) transcribed with MAI-Transcribe-2 via OpenRouter (minutes 1-30, $0.048); the ASR renders Fluint as "Fluent", so no line naming the company was quoted |

## What the corpus rests on

All thirty-one excerpts are verbatim and written by him, from two channels: twenty-five from sixteen of his own LinkedIn posts (2022-2026, nine of them from the month before the research date, fetched logged-out with his slash lists, arrows, asterisks, and apostrophe plurals intact), five from three bylined fluint.io essays (June-July 2026), and one from his own landing copy for Selling With. Nothing comes from a quote aggregator and nothing is documented-grade. LinkedIn is the dominant channel and the native voice; the fluint.io essays are the same author in a more edited, product-tied register and should be quoted as essays. Confidence in wording is high throughout; confidence that the essay register is unedited by his team is moderate, and there is no spoken sample at all. Items 101-110 were added afterwards as a documented-grade spoken sample: one 2026 podcast interview, machine-transcribed with speaker diarization.

## Known gaps

- **No book text.** Selling With (2023) and Brief & Brilliant have no public excerpt; Amazon Look Inside and Google Books previews were not reachable, and the fluint.io "preview" pages are gated early-reader forms. Only his own landing-page pitch copy is quoted (item 31). Do not quote either book as verbatim.
- **Long form is thin and product-tied.** The 2026 fluint.io posts are the only bylined long-form found; several are heavily product-marketing (Loop, Olli Mesa) and may be team-edited. Older fluint.io posts ("The One Page Business Case", "Selling With") are template and download landing pages with 3-4 lines of copy.
- **Spoken register rests on one episode.** Items 101-110 come from one 2026 interview (The Caliber Show), machine-transcribed and diarized, so the wording is documented grade, not verbatim. His many 2022-2025 guest spots (30MPC, B2B Power Hour, The Learning Culture Podcast) and his keynotes remain untranscribed; one host-led conversation is a thin sample, and the keynote register he describes in items 5-6 is still unsampled.
- **LinkedIn 2024-2025 is thin.** Nine posts came from the last 30 days via the profile page and seven older posts via search; only two posts fall in the 2024-2025 window. The /recent-activity/ page login-walls.
- **Credited stories are not his.** The Splunk business-case program (item 22) is Doug May's story quoted by Nasralla, and the Rolls-Royce headline (item 9) is Ogilvy's; the corpus keeps his framing, not the originals.
- **Anything published after 2026-10-19 is unsampled.**

## Refresh instructions

1. Re-fetch https://www.linkedin.com/in/natenasralla logged-out with a desktop UA, collect the embedded post permalinks, and curl each one; take the text from `<meta name="description">` and the date from JSON-LD. Add 6-10 verbatim excerpts from posts after October 2026 and continue the numbering in the LinkedIn section.
2. Re-run WebSearch `"Nate Nasralla on LinkedIn" site:linkedin.com/posts` with 2024 and 2025 date terms to thicken that window; prioritize posts that spell out a full business-case template or a champion-enablement script.
3. Check https://www.fluint.io/blog for new bylined essays and add 2-3 verbatim excerpts per essay under the essays section, noting how product-tied each one is.
4. Search again for a Selling With sample chapter (Amazon Look Inside, Google Books, a publisher PDF, or a Substack excerpt); if found, add a labelled "book excerpt" section and extend the Newsletter Writer playbook with the book register.
5. Caption one podcast appearance (30MPC or Revenue Builders) with `yt-dlp --write-auto-sub --skip-download --sub-lang en "<url>"`; add 3-5 documented (ASR) excerpts under a new labelled section and replace the inferred spoken-register stat with a sampled one.
6. Transcribe another long episode (ideally a 30MPC or B2B Power Hour guest spot) from its RSS enclosure MP3, not YouTube: `python3 scripts/voice-dna/transcribe.py "<mp3-url>" --out /private/tmp/claude-501/stt/nate-nasralla --start-min 2 --max-min 45 --budget 0.15` (MAI-Transcribe-2 via OpenRouter, OPENROUTER_API_KEY in the environment, about $0.10 per hour). Identify the speaker label in each 20-minute chunk from context, then add 6-10 documented excerpts continuing from item 111.
7. Re-verify that every URL is still live. Never carry a quote forward that was not re-read at its source.

## Pattern notes

### 1. Frame, colon, list
A framing sentence with a count ends in a colon, then the lesson arrives as "1/ 2/ 3/" items, "(1) (2)" parentheticals, or "→" arrows, sometimes drawn as a text diagram. The LinkedIn Content Expert writes the framing line first and lists in slash numbering.

### 2. Hedged confidence, worked math
He hedges where honesty needs it ("IMO," "probably," "I mean, if...") and then shows a formula or a score (sales velocity, Stage 1 = 1/5 through 4.5/5, 20% of the activity to dispel 80% of the doubt). The Sales Closer ties every stage to a score or a number and marks unsourced figures [VERIFY].

### 3. Credit first, then add
Borrowed ideas are named before his extension (Ogilvy, Doug May, the Peak-End Rule). The Guardrails require the same crediting and forbid presenting the Splunk or Rolls-Royce stories as the user's own.

### 4. Raise the uncomfortable topic first
Churn reasons on a discovery call, SLIP before EOQ, the skeptic's risk out loud. The Sales Closer opens with the churn-first script and the Objection Handling Expert validates the skeptic instead of overcoming them.

### 5. Buyer-side framing
Deals are decided "when you're not in the room," buyers say "I live here, you don't," and urgency "is always internal." Every playbook forbids manufactured urgency and routes the work through the champion.

### 6. Two-beat contrast and the closing dare
Arguments ride on paired sentences ("Average reps... Standout reps...", "Coverage is an open loop. Your revenue should be a closed one.") and posts end on an open question or a gentle dare ("Give 'em a shot this week."). The Newsletter Writer closes on the aphorism plus question; no playbook ends on a hard CTA.
