# Alex Hormozi Source Map

Research date: 2026-08-24; primary-source re-verification and refresh 2026-10-18; items 8-19 permalink search 2026-10-19
Refresh cadence: every 6 months (next: 2027-04)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| Acquisition.com public site | https://www.acquisition.com/ | Public positioning, portfolio framing | Open |
| X profile | https://x.com/AlexHormozi | Short-form aphorisms | Login wall |
| LinkedIn | https://www.linkedin.com/in/alexhormozi/ | Cross-posted short-form register | Login wall |
| $100M Offers (book, 2021) | public excerpts via Goodreads quote pages | Offer-design aphorisms, value-equation language | Purchase (excerpts Open via Goodreads) |
| $100M Leads (book, 2023) | public excerpts via Goodreads quote pages | Lead-generation definitions and aphorisms | Purchase (excerpts Open via Goodreads) |
| The Game podcast / YouTube channel | his YouTube channel | Long-form spoken register | Open, video |
| Aggregated public quote collections | thecitesite.com, summarypedia.org, startearlytoday.com | Secondary compilations of X posts and book lines; used only to locate a status ID, never as the cited source | Open |

## What the corpus rests on

Primary material carries the corpus. Verbatim: 8 first-pass X posts (items 7-10, 12, 14, 15, 17) and the 2026-10-18 refresh posts (items 101-120; 15 of them currently lack their citation line, see Known gaps), all fetched from X's own syndication endpoint by status ID, plus one acquisition.com quote (item 121). Documented: 12 ASR excerpts from three channel videos (items 122-133) and 8 book lines taken from Goodreads rather than the books (items 1-6, 19, 20). No aggregator-only X quote remains in usable form.

## Re-verification and refresh (2026-10-18)

All 20 first-pass items were checked against his X account, acquisition.com, and his YouTube channel: 1 verified exactly (item 7), 1 partially (item 1, book subtitle only), 18 not found. They remain in the corpus labelled documented and must not be quoted in client copy. The refresh added 33 primary items: 20 dated verbatim X posts pulled by ID through X's syndication endpoint (cdn.syndication.twimg.com/tweet-result?id=<id>&token=a; the profile timeline at syndication.twitter.com/srv/timeline-profile/screen-name/AlexHormozi exposes a curated 100 posts and rate-limits after a few hits), 1 verbatim quote from https://www.acquisition.com/, and 12 documented ASR excerpts from three channel videos (2021 sales talk, 2024, 2026). The corpus now has dated, permalinked X posts and a spoken register for the first time.

## Permalink search for items 8-19 (2026-10-19)

Each of items 8-19 was searched post by post: exact-phrase and variant web searches scoped to x.com (standard and extended), threadreaderapp unrolls, and the profile timeline, with every candidate status ID confirmed through the syndication endpoint for exact text and ISO date. Found and moved to verbatim: 8, 9, 10, 12, 14, 15, 17 (8, 14, 15 and 17 had drifted from the X wording at the aggregator and were corrected). Book line, not X: 19. Not found and tombstoned: 11, 13, 16, 18.

## Known gaps

- **Book lines (items 1-6, 19, 20) cannot be verified without the books.** They come from Goodreads quote pages and reader highlights, stay labelled documented, and are not for client copy. acquisition.com hosts no free chapters.
- **Thread bodies not captured.** The syndication tweet endpoint returns only a thread's root post; the "How to stay poor" (1604865554824642560) and "#mozisms" (1541904282303115265) threads hold dozens more one-liners.
- **Spoken register is YouTube ASR only.** Items 122-133 are auto-caption text (documented, not verbatim) from three videos; no excerpt is drawn from The Game podcast.
- **Item 121's original utterance is not located.** acquisition.com presents it as his words without a date or source.
- **LinkedIn not sampled.** Login wall.
- **Anything published after 2026-10-18 is unsampled.**
- **Derived stats are estimates, not measurements.** The percentages under "Derived stats" (hook-type frequency, one-line-paragraph rate) are labeled estimates in the file itself, not a systematic count.

## Refresh instructions

1. Pull recent posts from `https://x.com/AlexHormozi` and his LinkedIn directly, plus any new book or course launch pages, rather than relying only on aggregator sites.
2. Add 5-10 new verbatim excerpts to `voice-corpus.md` with dates and URLs.
3. Re-estimate the derived stats.
4. Check whether new signature phrases have entered his lexicon; his vocabulary shifts as his businesses shift from gyms to portfolio scale.
5. Pull at least one dated excerpt from The Game podcast (`scripts/voice-dna/transcribe.py` on the show's RSS MP3).

## Pattern notes

### 1. Aphorism as unit of content

His native format is the compressed rule: a claim under 15 words that survives being read flatly. The skill should end every piece on one.

### 2. Math over motivation

Claims are backed with arithmetic: value equations, volume math, exchange rates of time for money. If a piece has no number, it is not finished.

### 3. Definition reframes

He wins arguments by redefining the noun first ("a lead is a person you can contact"). The skill deploys this at the top of educational content.

### 4. Volume gospel

His default prescription is more reps: more calls, more content, more outreach. The skill uses this against trick-seeking questions.

### 5. Give away the paid thing

His CTA posture is anti-CTA: free books, free courses, "I have nothing to sell you". The skill mirrors this in lead magnets and closers.
