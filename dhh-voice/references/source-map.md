# DHH (David Heinemeier Hansson) Voice Source Map

Research date: 2026-10-19
Refresh cadence: every 6 months (next: 2027-04)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| HEY World Atom feed | https://world.hey.com/dhh/feed.atom | Last 30 posts with full bodies and ISO timestamps (Dec 2025 to Oct 2026 at research time); 13 posts quoted for items 1-21 | `curl -sL` with a desktop UA, 200, no auth |
| HEY World post pages | https://world.hey.com/dhh/<slug> | Any older post; byline and "Month D, YYYY" date in the HTML | Open |
| "Why we're leaving the cloud" (Oct 19 2022) | https://world.hey.com/dhh/why-we-re-leaving-the-cloud-654b47e0 | The cloud-exit polemic: renting versus owning, "insanely beefy servers", "This is not what DARPA designed!" | Open |
| "We have left the cloud" (Jun 23 2023) | https://world.hey.com/dhh/we-have-left-the-cloud-251760fb | Receipts follow-up: $1.5 million per year saved, operations team unchanged | Open |
| "Rails is omakase" (Dec 27 2012) | https://dhh.dk/2012/rails-is-omakase.html | The defining Rails-philosophy essay: the menu, the chefs, "The door is right over there" | Open |
| "The Majestic Monolith" (Feb 29 2016) | https://signalvnoise.com/svn3/the-majestic-monolith/ (mirror: https://m.signalvnoise.com/the-majestic-monolith-29166d022228) | Architecture polemic: "Bzzzzzzzzt!! Wrong!", "Don't distribute your computing!" | Open |
| X @dhh | https://x.com/dhh | Short takes in the same voice; 3 posts quoted (Jul-Oct 2026), IDs harvested from links inside his own HEY posts | `https://cdn.syndication.twimg.com/tweet-result?id=<id>&token=a` returns text and ISO date; profile timeline endpoint 429'd |
| Rails World keynotes and podcasts (e.g. Lex Fridman #474) | https://lexfridman.com/dhh-transcript (404 at research time) | Spoken register | NOT fetched this round |

## What the corpus rests on

All thirty-two excerpts are verbatim and written by him: twenty-one from HEY World posts published in the eleven months before research (pulled from the blog's own Atom feed), four from the two cloud-exit posts on the same blog (2022-2023), two from the Rails is omakase essay on dhh.dk (2012), two from The Majestic Monolith on the Signal v. Noise archive (2016), and three from his own X account (2026). The written register is covered across fourteen years and four channels and is consistent throughout, so confidence in wording and structure is high. No spoken sample was captured, and the X sample is thin. Nothing comes from a quote aggregator; no ghostwriter credit appears on any of the channels.

## Known gaps

- **No spoken-word excerpts.** The Lex Fridman transcript page returned 404 and no yt-dlp caption pull was spent on him. His Rails World 2026 keynote ("put down the pencils") is the ideal spoken sample and remains unsampled; spoken-style output is inferred from the written register.
- **X coverage is thin.** Five posts were located (three quoted), all from 2026, found only through links inside his own HEY posts; the profile timeline endpoint rate-limited. He posts far more on X than this sample suggests, and his short-form rhythm is under-represented.
- **Co-authored books were not pulled.** Rework, Remote, and It Doesn't Have to Be Crazy at Work are shared with Jason Fried, so single-author attribution is unclear; do not quote them as his alone.
- **Pre-2012 Signal v. Noise posts were not sampled.** The archive is open; only The Majestic Monolith (2016) was read.
- **The 2026 HEY World posts dominate the sample** (21 of 32), so the AI-agents and Europe themes are over-represented relative to his full archive; the register itself is stable across eras.
- **Anything published after 2026-10-19 is unsampled.**

## Refresh instructions

1. Re-fetch `https://world.hey.com/dhh/feed.atom` with a desktop UA and add 5-8 verbatim excerpts from posts published since October 2026, with slugs and ISO dates; continue numbering inside the HEY World section.
2. Harvest X status IDs from "See the thread" or x.com links inside new HEY posts and fetch each with `https://cdn.syndication.twimg.com/tweet-result?id=<id>&token=a`; add 5-8 verbatim posts and retry the profile timeline (`https://syndication.twitter.com/srv/timeline-profile/screen-name/dhh`, pause ~20s on a 429).
3. Caption the most recent Rails World keynote or a long podcast appearance with `/opt/homebrew/bin/yt-dlp --write-auto-sub --skip-download --sub-lang en -o "<dir>/%(id)s" "<url>"` (one attempt; stop on a 429); add 3-5 documented excerpts in a labelled spoken section and update the spoken-register stat.
4. Read two or three pre-2012 Signal v. Noise posts by him (byline "DHH") from the archive and add 2-4 verbatim excerpts in the essays section to widen the era coverage.
5. If 37signals publishes a new operations or cost post under his byline, add its receipts to the corpus and refresh the Build-in-Public Writer template's example numbers.
6. Re-verify that every URL is still live. Never carry a quote forward that was not re-read at its source.

## Pattern notes

### 1. Receipt first
Posts open on a dated or unit-bearing number (90% to 1%, $1.5 million per year, half a million dollars of servers) and editorialize in the next sentence. The Contrarian Take Generator and Build-in-Public Writer both refuse to start without a real receipt.

### 2. Settled thesis
The conclusion is stated as already decided, often as the title ("Rails is omakase.", "Redundancy is the engine of progress"). The Contrarian Take Generator uses it as the opener and the Ghostwriter as the headline.

### 3. One governing metaphor
A single image (sushi menu, pencils, sacred cows, the Terminator) is carried from the opening to the last line and often supplies the closing wink. Every playbook limits a piece to one metaphor and asks for it before drafting.

### 4. Setup, then punch
A long sentence lands on a 2-6 word exclamatory one ("That is literally the progress!", "Bzzzzzzzzt!! Wrong!"). The Ghostwriter enforces that each paragraph ends shorter than it began and budgets exclamation marks.

### 5. Strawman in their voice
The standard objection is quoted in the opponent's own words and flattened in a short line ("No, really, it's not."). The Contrarian Take Generator places this step between thesis and metaphor.

### 6. Benediction or dare
Pieces end on one short line that blesses or dares ("What a time to be alive.", "We need you.", "How is next Thursday for you?"), never a summary. Every playbook template ends this way, and the Anti-patterns list flags the recurring closer as an over-imitation tell.
