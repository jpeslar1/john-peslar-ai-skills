# Nikita Bier Voice Source Map

Research date: 2026-10-19
Refresh cadence: every 6 months (next: 2027-04)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| X @nikitabier, "everything you need to know" thread (27 posts, 2022-01-12) | https://x.com/nikitabier/status/1481118406749220868 | Dense consumer-app heuristics, one rule per post; items 1-18 | Public via `https://cdn.syndication.twimg.com/tweet-result?id=<id>&token=a`, each thread ID fetched and verified individually; thread IDs located via threadreaderapp.com |
| X @nikitabier, standalone posts 2022-2024 (NYT reply, Gas sale, A/B test, Maltalk, time to value) | https://x.com/nikitabier/status/1709649178735825175 and the other status URLs in the corpus | Aphoristic one-liners and growth lore; items 19-23 | Public via the syndication endpoint |
| X @nikitabier, long posts 2025-2026 (Explode launch, X App Store rank, link reach, repost-factory reply, stepping back, Threads epiphany) | https://x.com/nikitabier/status/2085105586966827343 and the other status URLs in the corpus | Full text of posts over 280 characters; items 24-29 | Public via `https://api.fxtwitter.com/nikitabier/status/<id>` (the syndication endpoint truncates long posts) |
| Lenny's Podcast, "How to consistently go viral: Nikita Bier's playbook for winning at consumer apps" (2024-08-25) | https://www.youtube.com/watch?v=bhnfZhJWCWY | 98-minute spoken interview; items 30-35 | Open video; DOCUMENTED (YouTube auto-captions pulled once with yt-dlp, saved locally at research time; no speaker labels) |
| Lenny's Newsletter episode page | https://www.lennysnewsletter.com/p/how-to-consistently-go-viral-nikita-bier | Episode summary only | Public summary; the official transcript is paywalled and was not used |
| X profile timeline | https://x.com/nikitabier | Chronological feed | Syndication timeline endpoint returned "Rate limit exceeded" during research; status IDs were harvested with `site:x.com nikitabier/status` web searches instead |

## What the corpus rests on

Twenty-nine of thirty-five excerpts are verbatim from his own X posts, every one fetched by status ID from a public X endpoint with the ISO publish date attached: eighteen consecutive posts from the 2022 advice thread and eleven standalone posts and replies spanning 2022-2026, including his X-product era. Six excerpts are documented-grade YouTube auto-captions of one 2024 podcast interview, labelled so in the corpus, with speaker attribution inferred from context. Nothing comes from a quote aggregator or a thread-reader mirror's text (the mirror was used only to locate IDs). Confidence in wording is high for items 1-29 and moderate for 30-35. He is effectively a single-channel writer, so the written register is X and nothing else.

## Known gaps

- **No long-form essay or blog exists.** He has never maintained one, so the written corpus is capped at X post length (the longest fetched is roughly 1,200 characters). Any long-form output in this voice is an extrapolation from his stacked one-line paragraphs.
- **The X sample is search-assembled, not a chronological crawl.** The syndication profile-timeline endpoint was rate-limited for this handle, so standalone posts from 2023-2026 were located by web search and may over-represent his most-shared posts.
- **Official podcast transcript not used.** Lenny's transcript is paywalled; the spoken excerpts are YouTube ASR with no speaker labels. One widely quoted Bier line ("drops 20% for every additional year of age from 13 to 18") was voiced by the host in the interview and its original post was not located, so it is excluded from the verbatim section.
- **Only one spoken source.** Other interviews (podcasts, conference talks) were not sampled; the spoken-register stat rests on a single 98-minute conversation.
- **His X-era posts are company-adjacent.** Items 25-28 were written while he led product at X and describe that company's ranking, link handling, and payouts; they document his register, not neutral facts about X.
- **Anything published after 2026-10-19 is unsampled.**

## Refresh instructions

1. Retry `https://syndication.twitter.com/srv/timeline-profile/screen-name/nikitabier` for a chronological crawl; if still rate-limited, harvest new status IDs with `site:x.com nikitabier/status` searches scoped to the last six months.
2. Fetch each new short post with `curl "https://cdn.syndication.twimg.com/tweet-result?id=<id>&token=a"` and each long post with `curl "https://api.fxtwitter.com/nikitabier/status/<id>"`; add 5-8 verbatim excerpts with ISO dates and extend the standalone section numbering.
3. Add a second spoken sample once: `yt-dlp --write-auto-sub --skip-download --sub-lang en -o "<slug>/%(id)s" <interview URL>`; if it returns HTTP 429, use the show's published transcript page. Label the result documented.
4. Search for the original post behind the "20% per year of age" line; if found at a status URL, add it as verbatim, otherwise keep it out.
5. Re-verify every status URL in the corpus still resolves (deleted posts should be marked, not silently carried forward).

## Pattern notes

### 1. If-then, no why
A product condition and a verdict with no reasoning between ("If your product requires a 'partnership', run."). The Hook Creator makes this the default shape and rejects any hook that needs a "because".

### 2. Quantify the adjective
Every evaluative word becomes a figure with a unit (48 hours, $500 of ads, 7 friends, No. 78). All three playbooks treat a number-free claim as unfinished and route it to [VERIFY].

### 3. The smallest test market
Malta, one high school, one community: the narrowest possible test and its result. The Contrarian Take Generator uses it as the proof slot after the mechanism sentence.

### 4. Credential stack, then news
Two parallel past-tense lines, then the announcement ("Sold my company 5 years ago... Today I sold my company..."). The Build-in-Public Writer opens with it when the track record is real.

### 5. The spite confession and the wink
An unflattering motive stated flat ("Explode is a spite app") and a sign-off that refuses sentiment ("See you on the Timeline"). The Build-in-Public Writer allows the first only when true and requires the second in place of a thanks paragraph.

### 6. Undercut at the close
The thread ends by telling the reader to distrust the thread. The Contrarian Take Generator closes every take this way so the voice never tips into guru register.
