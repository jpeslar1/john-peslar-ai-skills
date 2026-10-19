# George Mack Voice Source Map

Research date: 2026-10-19
Refresh cadence: every 6 months (next: 2027-04)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| george-mack.com essays index | https://www.george-mack.com/ | 5 polished essays, "Steal this thought" pull-quotes, his one-line self-description ("the 1% of ideas that change how you see the other 99%") | Open static HTML (georgemack.com redirects to www.george-mack.com); no dates on page |
| "The Adults Don't Exist" | https://www.george-mack.com/posts/adults-dont-exist | Mozart and Jobs cascade, Adult Syndrome coinage, "Does it make them less impressive? No." | Open; undated |
| "Normal is forgotten. Only weird survives." | https://www.george-mack.com/posts/normal-is-forgotten-only-weird-survives | "Normal was" cascade, the normal paradox, 17 teaspoons / $104,755 / 30lbs | Open; undated |
| "How to get lucky (without being rich)" | https://www.george-mack.com/posts/how-to-get-lucky-without-being-rich | Thought experiment hook, Luck razor, poker vs. roulette, 1% vs. 99% | Open; undated |
| "How to solve any problem" | https://www.george-mack.com/posts/the-most-powerful-idea-ive-found | Dead vs. alive problem, giga problem | Open; undated |
| "How to spot high agency people" | https://www.george-mack.com/posts/how-to-spot-high-agency-people | "You can never guess their opinion" example list | Open; undated |
| highagency.com, "High Agency in 30 Minutes" | https://www.highagency.com | ~45 KB essay by Mack: jail-cell question, suitcase wheels, the tap, the tricycle, bad news / good news, "what I wish I read at 18" | Open static HTML; undated on page, announced on X 2025-03-24 |
| X @george__mack (threads) | https://threadreaderapp.com/user/george__mack | ~21 unrolled threads Jul 2023-May 2025: high agency razors, cognitive biases as superpowers, Trojan Horses, life as a video game, dream-client ads | Open; root tweets verified via `https://api.fxtwitter.com/i/status/<id>`; mid-thread tweets from Thread Reader unrolls |
| X single tweets embedded on his site | https://twitter.com/george__mack/status/1661426260327759902 ; https://twitter.com/george__mack/status/1374050973866418184 | Vrba thread hook (2023-05-24), Ngannou thread hook (2021-03-22, not excerpted) | fxtwitter returns full text and date |
| LinkedIn posts | https://www.linkedin.com/in/george-mack (profile lists 7 own-post permalinks) | Oct-Nov 2025: funniest ads of the week, most creative ad copy of all time, Apple AirTag idea, the adprofessor.com CTA | Permalinks render logged out with a desktop UA; text in meta description, date in JSON-LD |
| Modern Wisdom #1111, "The Hidden Cost Of Overthinking Everything" (2026-06-15), audio | https://traffic.megaphone.fm/SIXMSB9616834279.mp3 (feed: https://feeds.megaphone.fm/SIXMSB5088139739) | Spoken register: items 101-108 from minutes 3-48 (British temperament, AI, frivolous spending, history thought experiments, rumination) | RSS enclosure, transcribed with `scripts/voice-dna/transcribe.py` (MAI-Transcribe-2 via OpenRouter, $0.075 for 45 min); documented grade, diarization merges voices in places |
| Ad Professor | https://adprofessor.com | His agency; ad teardowns and the destination of every LinkedIn CTA | NOT fetched this round |

## What the corpus rests on

All 34 excerpts are verbatim from channels he writes himself: 15 from five essays on george-mack.com, 6 from the highagency.com essay, 10 from his own X account (root tweets re-fetched and dated via fxtwitter or via tweet IDs embedded on his own site, mid-thread razors via Thread Reader unrolls), and 3 from LinkedIn post permalinks (Oct 2025). Nothing comes from a quote aggregator. The essay register, the thread register, and the LinkedIn ad-teardown register are all covered and read as one voice with one sales-forward variant. The spoken sample is one podcast conversation (items 101-108, documented machine transcript). Confidence in wording is high for every item; confidence in dating is high for X and LinkedIn and low for the site essays, which carry no publication date. The research file's verdict line counts 30 excerpts; the file itself numbers 34, and all 34 were carried into the corpus.

## Known gaps

- **Site essays are undated.** george-mack.com pages carry no publication date in the HTML; they are dated only by site liveness at research time. Date them via the Wayback CDX API if a refresh needs chronology.
- **X sample is Thread Reader's curation.** The syndication timeline endpoint was rate-limited, so only ~21 curated unrolls plus two tweet IDs embedded on his site were reachable. His weekly "0.1% of ideas" threads and standalone tweets were not pulled. Mid-thread items were not re-fetched individually.
- **Spoken sample is thin.** Items 101-108 cover one loose two-way chat with Chris Williamson (Modern Wisdom #1111, June 2026), documented grade from a diarized machine transcript in which the two British voices sometimes merge, so only single-speaker lines were used. His interview-format appearances where he explains ideas at length (Modern Wisdom #801, #919, #1124; Infinite Loops) remain unsampled, so the spoken stats are provisional.
- **Ad Professor and any newsletter were not fetched.** The agency register is inferred from three LinkedIn posts only.
- **The Ngannou tweet (2021-03-22) was located but not excerpted**; his pre-2023 X voice is otherwise unsampled.
- **Anything published after 2026-10-19 is unsampled.**

## Refresh instructions

1. Re-fetch `https://www.george-mack.com/` and each `/posts/<slug>` page; add 3-5 verbatim excerpts from any new essay and continue the numbering in the essay section. Run `curl -s "http://web.archive.org/cdx/search/cdx?url=george-mack.com/posts/*&output=json&fl=timestamp,original&collapse=urlkey"` to assign first-seen dates to the undated essays and record them in the corpus source lines.
2. Pull the X syndication timeline (`https://syndication.twitter.com/srv/timeline-profile/screen-name/george__mack`) when it is not rate-limited, or re-run Thread Reader (`https://threadreaderapp.com/user/george__mack`); verify each root via `https://api.fxtwitter.com/i/status/<id>` and add 5-8 verbatim posts, including at least one weekly ideas thread.
3. Re-fetch the LinkedIn profile `https://www.linkedin.com/in/george-mack` with a desktop UA, collect new permalinks, read text from `<meta name="description">` and the date from JSON-LD; add 2-4 posts to the LinkedIn section.
4. Fetch `https://adprofessor.com` and, if a newsletter exists, its archive; if the copy is first-person, add a labelled "Ad Professor" verbatim section and extend the Contrarian Take Generator with ad-copy principle examples.
5. Widen the spoken sample: take an MP3 from an official RSS feed (for example Modern Wisdom #1124 or #919 from https://feeds.megaphone.fm/SIXMSB5088139739) and run `python3 scripts/voice-dna/transcribe.py "<mp3-url>" --out /private/tmp/claude-501/stt/george-mack-voice --start-min 3 --max-min 45 --budget 0.15` with `OPENROUTER_API_KEY` set; Williamson's sponsor reads identify his label in each 20-minute chunk, quote only single-speaker lines, and add 6-10 documented items to the spoken section.
6. Re-verify that every URL is still live. Never carry a quote forward that was not re-read at its source.

## Pattern notes

### 1. Forced-choice scene
Essays open on a vivid situation with one decision and then interrogate the choice ("Who do you call? Why did you choose this person?"). The Hook Creator and Ghostwriter both lead with this or with a constrained thought experiment.

### 2. Example cascade
Three to five two-sentence miniatures from history or statistics come before any conclusion (Mozart, Jobs, blackened teeth, suitcase wheels, 17 teaspoons). The Ghostwriter's first section is the cascade; every example is [VERIFY]-flagged unless cited.

### 3. Coin the label
Once the pattern is visible he names it and defines it in one sentence (Adult Syndrome, Luck razor, Trojan Horses, the normal paradox). The Ghostwriter coins one label per piece; the Contrarian Take Generator offers the label as the replacement for the term it attacks.

### 4. Inversion turn
Sections end on a one-line reframe that flips the premise ("High agency states you're a tap."; "Assume everything is a game of skill."). All three playbooks make the turn the last line of a section.

### 5. Razor as rule
Threads are numbered one-line decision rules with a one-line mechanism ("Gas shrinks to the size of the container."). The Ghostwriter's third section and the Contrarian Take Generator's problem list use this shape.

### 6. Verify this
He undercuts his own authority and tells the reader to check, including his own tweets. Every playbook closes on the undercut, which also keeps ghostwritten copy honest about borrowed examples.
