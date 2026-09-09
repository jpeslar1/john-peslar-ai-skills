# Sam Parr Source Map

Research date: 2026-09-09
Refresh cadence: every 6 months (next: 2027-03)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| How to write like The Hustle | https://thehustle.co/write-like-hustle-boring-stuff-writing-no-one-talks | The documented method, in his own words, signed by him. The single best source for this voice. | Open |
| The Hustle author page | https://thehustle.co/author/sam-parr | Index of pieces carrying his byline | Open, HubSpot-hosted, heavy nav chrome in the HTML |
| The Hustle newsletter archive | https://thehustle.co/newsletters | Daily issues in the house voice he created | Open |
| Hampton blog | https://joinhampton.com/blog | Current-era founder profiles in a related house voice. Not his byline. | Open |
| My First Million | thehustle.co and podcast platforms | His spoken register, the riffing, the idea generation | Open |
| X account | https://x.com/thesamparr | Short-form register, one-line business observations | Open, rate-limited |

## What was actually fetched

One full article, signed "Sam, CEO of The Hustle", was pulled as raw text from thehustle.co on 2026-09-09. It supplied the entire verbatim corpus (items 1-30). Two Hustle newsletter URLs from 2020 were also fetched but returned mostly navigation chrome rather than issue bodies.

## Spoken sources fetched (2026-09-09)

Four YouTube videos were pulled via `yt.py tx` and used for items 31-50 in `voice-corpus.md`. All four carry auto-generated (ASR) caption tracks only, so every excerpt drawn from them is `documented`, not `verified`, even where the speaker is unambiguous.

| Video | Channel | videoId | Caption track | Format |
|---|---|---|---|---|
| Sam Parr from The Hustle Explains his Content Strategy | My First Million | BsLf5hE2yS8 | auto | Solo conference talk, single speaker |
| How To Build a Media Empire with Sam Parr | Ryan Hawk | Q52-zcDSvlk | auto | One-on-one interview |
| Sam Parr on how to grow on Twitter, selling a company, and the best social media platforms to choose | Kopywriting Kourse (Neville Medhora) | nW6UChjM88I | auto | Two-person conversation |
| Sam Parr On The Inspiration, Story & Grind Behind The Hustle | KevinandFredTV | w8TFNhxgGuM | auto | One-on-one interview |

Every excerpt taken from the two-person and interview videos was checked against the raw transcript text and kept only where the surrounding exchange makes Sam Parr unambiguously the speaker of the full quoted line; ambiguous lines were dropped rather than guessed.

## Known gaps

- **No newsletter issue bodies.** The Hustle archive on thehustle.co is now HubSpot-hosted and the fetched pages returned navigation rather than issue text. The daily-brief voice, which is what most readers mean by "The Hustle voice", is therefore still not sampled. This is the top priority on refresh.
- **The Hustle voice is a house voice.** It was written by a team and, by his own account, sometimes published under pen names. Distinguish his personal byline from the house style when refreshing.
- **No X corpus.** His short-form business observations are not captured.
- **Hampton profiles are not his byline.** The Hampton blog was reviewed for house style only and no lines from it are in the corpus.
- **Spoken register is now sampled but ASR-only.** Items 31-50 cover a solo conference talk, two interviews, and one co-hosted conversation, all through auto-generated captions with no human caption track and no speaker diarization. Treat exact wording as approximate; re-verify any figure before republishing. No human-captioned (verified-tier) video was found for him.

## Refresh instructions

1. Pull five full Hustle daily issues from the archive by rendering the pages, and add a house-voice section to the corpus, clearly separated from his personal byline.
2. Pull the Soylent article he cites as his running example. It is the piece the whole craft article refers to.
3. Capture 20 to 30 X posts for the compressed register.
4. Check whether any of the four YouTube videos above (or a new one) has since gained a human caption track, which would let those excerpts be upgraded to `verified`.
5. Re-verify the subscriber counts and any dollar figures before they appear in client-facing copy.
