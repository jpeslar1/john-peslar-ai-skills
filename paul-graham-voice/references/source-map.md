# Paul Graham Voice Source Map

Research date: 2026-10-19
Refresh cadence: every 6 months (next: 2027-04)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| paulgraham.com essay index | https://paulgraham.com/articles.html | Every essay 2001-2026 in plain HTML, with a month-and-year dateline at the top of each | `curl -sL` with a desktop UA fetches cleanly; strip tags |
| "Do Things that Don't Scale" (Jul 2013) | https://paulgraham.com/ds.html | Canonical startup-advice essay: founders make startups take off, the Collison installation, delight users | Open |
| "How to Do Great Work" (Jul 2023) | https://paulgraham.com/greatwork.html | Longest recent essay; recipe structure, the three qualities of work worth choosing | Open |
| "Superlinear Returns" (Oct 2023) | https://paulgraham.com/superlinear.html | The received saying denied; "a feature of the world, not an artifact of rules we've invented" | Open |
| "Founder Mode" (Sep 2024) | https://paulgraham.com/foundermode.html | Most-circulated recent essay; anecdote as argument, founder mode versus manager mode, encouraging close | Open |
| "Writes and Write-Nots" (Oct 2024), "Good Writing" (May 2025), "The Right Kind of Stubborn" (Jul 2024) | https://paulgraham.com/writes.html , https://paulgraham.com/goodwriting.html , https://paulgraham.com/persistence.html | Craft-of-writing and character essays; the hedged prediction; "Obstinate people are so annoying" | Open |
| "How to Earn a Billion Dollars" (Jun 2026), "Making Startups Powerful" (Sep 2026) | https://paulgraham.com/earn.html , https://paulgraham.com/powerful.html | Newest essays; the first is his own write-up of an Oxford Union talk | Open |
| "What We Look for in Founders" (Oct 2010), "Mean People Fail" (Nov 2014), "Life is Short" (Jan 2016), "Is It Worth Being Wise?" (Feb 2007) | https://paulgraham.com/founders.html , https://paulgraham.com/mean.html , https://paulgraham.com/vb.html , https://paulgraham.com/wisdom.html | Older essays for era coverage: determination over intelligence, 52 weekends, the one-line definition | Open |
| Hacker News comments by `pg` | https://news.ycombinator.com/threads?id=pg (API: https://hacker-news.firebaseio.com/v0/user/pg.json) | His own short written replies with second-level timestamps; 2 quoted | Firebase JSON API, no auth |
| X @paulg | https://x.com/paulg | Short-form register | NOT fetched: syndication timeline 429'd twice and no status IDs were located |
| The Social Radars, "Paul Graham, Founder, Y Combinator" (2026-03-19), audio | https://episodes.captivate.fm/episode/b276d1a8-7281-4220-816b-693244c7f3df.mp3 (feed: https://feeds.captivate.fm/thesocialradars/) | Spoken register: items 101-110 from minutes 1-46 (YC growth, Hacker News stress, office hours, Demo Day vertebrae, Sam Altman) | RSS enclosure, transcribed with `scripts/voice-dna/transcribe.py` (MAI-Transcribe-2 via OpenRouter, $0.075 for 45 min); documented grade |

## What the corpus rests on

All twenty-six excerpts are verbatim and written by him: twenty-four from thirteen essays on paulgraham.com spanning February 2007 to September 2026, read from the plain public HTML, and two from his own Hacker News comments (2019 and 2024) read from the public Firebase API. The essays are the overwhelmingly dominant channel and the comments confirm that the register does not change at short length, so confidence in wording and structure is high. The corpus has no X posts, and its spoken sample is one podcast conversation (items 101-110, documented machine transcript); short-form output is still inferred from the essay register. Nothing comes from a quote aggregator, and no ghostwriter credit exists anywhere on the site.

## Known gaps

- **No X posts.** The @paulg syndication timeline returned "Rate limit exceeded" on two attempts and no x.com/paulg/status IDs surfaced via search, so his short-form register is unsampled. Fix: feed known status IDs into `https://cdn.syndication.twimg.com/tweet-result?id=<id>&token=a`, which worked for other handles this run.
- **Spoken sample is thin.** Items 101-110 cover 45 minutes of one relaxed conversation with his wife and longtime colleague (The Social Radars, March 2026), documented grade from a diarized machine transcript; it is retrospective storytelling, not argument. A formal talk or an adversarial interview (for example Conversations with Tyler, 2023) is still unsampled, and How to Earn a Billion Dollars remains a written-up talk rather than a transcript.
- **Famous lines not re-read this pass are not in the corpus.** Only the thirteen essays listed above were fetched; well-known sentences from other essays must be re-read at paulgraham.com before being quoted as verbatim.
- **Essays are dated by month and year only.** That is how he publishes them; the corpus carries the same precision.
- **Footnotes and the Notes sections were not excerpted.** The research notes describe them as carrying his wryest asides; the corpus has no sample of that sub-register.
- **Anything published after 2026-10-19 is unsampled.**

## Refresh instructions

1. Re-fetch `https://paulgraham.com/articles.html` with a desktop UA, open any essay newer than September 2026, and add 5-8 verbatim excerpts with month-year datelines and URLs; continue numbering inside the essays section.
2. Locate 5-8 @paulg status IDs (from links in his essays, Hacker News threads, or WebSearch for "x.com/paulg/status") and fetch each with `https://cdn.syndication.twimg.com/tweet-result?id=<id>&token=a`; add them in a labelled X section and add a short-form stat.
3. Caption one long interview or talk with `/opt/homebrew/bin/yt-dlp --write-auto-sub --skip-download --sub-lang en -o "<dir>/%(id)s" "<url>"` (one attempt; stop on a 429); add 3-5 documented excerpts in a labelled spoken section.
4. Excerpt 2-3 footnotes from the Notes sections of the fetched essays to sample the aside sub-register, and note it in the stats.
5. Pull 3-5 more `pg` comments from `https://hacker-news.firebaseio.com/v0/user/pg.json` (submitted IDs, then `/v0/item/<id>.json`) to widen the short-form sample.
6. Re-verify that every URL is still live. Never carry a quote forward that was not re-read at its source.
7. For more spoken register, take an MP3 from an official RSS feed (for example Conversations with Tyler, Aug 2023, https://rss.libsyn.com/shows/137081/destinations/850607.xml) and run `python3 scripts/voice-dna/transcribe.py "<mp3-url>" --out /private/tmp/claude-501/stt/paul-graham-voice --start-min 2 --max-min 45 --budget 0.15` with `OPENROUTER_API_KEY` set; identify his speaker label in each 20-minute chunk from context and add 6-10 documented items to the spoken section.

## Pattern notes

### 1. Thesis in sentence one
Essays open on a dateline and a plain declarative thesis, often beginning "Actually" when a belief is being corrected; an opening anecdote pivots to its question within four sentences. The Ghostwriter and Newsletter Writer templates both start with the dateline and the thesis line.

### 2. Calibrated certainty
The strongest claim carries its own uncertainty ("I feel fairly confident about this one", "as far as I know", "remarkably few"). Every playbook requires calibration on the central claim and forbids hedging trivial ones.

### 3. Small arithmetic
Points land on a tiny checkable calculation ("52 weekends with your 2 year old"; "half as good... no customers"). The Contrarian Take Generator uses arithmetic in place of rebuttal.

### 4. Named case, coined term
Abstractions are replaced by a company and a founder (the Collison installation), and new ideas are flagged once in quotation marks ("founder mode") then used bare. The Ghostwriter allows one coinage per essay and one named case per section.

### 5. The received saying, denied
A saying the reader has actually heard is quoted, granted good intent, and shown to be rarely true. The Contrarian Take Generator opens on this move.

### 6. Aphoristic close, Notes below
Essays end on one proverb-like sentence and move caveats and wry asides into numbered Notes with a thanks line. The Ghostwriter template reproduces the structure; the Anti-patterns list flags footnotes longer than the essay as a tell.
