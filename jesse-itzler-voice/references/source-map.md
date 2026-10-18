# Jesse Itzler Voice Source Map

Research date: 2026-10-19
Refresh cadence: every 6 months (next: 2027-04)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| Free Swim newsletter archive (Atom feed) | https://jesseitzler.com/blogs/free-swim.atom | Last 30 newsletter posts with full bodies and ISO dates (Jan 2025 to May 2026) | `curl -sL` with a desktop UA, 200; site is Shopify, `/wp-json` 404s |
| Free Swim post pages | https://jesseitzler.com/blogs/free-swim/<slug> | Individual posts, 500-2,600 characters each; 11 posts quoted (the 3-Hour Rule, Make A Contract With Yourself, The 90% Free Throw Nobody Wants To Shoot, This Saturday Not Next Winter, The 19 Couches, The Happiest Guy In Manhattan, Time Isn't Money Time Is Life, Experience Is Overrated, 30 Seconds Of Advice For Young People, The Evening Sets The Morning, One Degree Off) | Open; Shopify author field reads "Brian Sutherland" (staff account) |
| X @JesseItzler profile timeline | https://syndication.twitter.com/srv/timeline-profile/screen-name/JesseItzler | ~100 curated posts with text, IDs, and full dates in the embedded `__NEXT_DATA__` JSON (2016-2025) | 429 on first hit, 200 after a ~20s pause with a desktop UA |
| X single posts (long form) | https://api.fxtwitter.com/JesseItzler/status/<id> and https://cdn.syndication.twimg.com/tweet-result?id=<id>&token=a | Full text beyond 280 characters, ISO date; 18 posts quoted | Open |
| jesseitzler.com About / Journey | https://jesseitzler.com/pages/about | Bio timeline with short embedded quotes; third-person team copy | Open; used for context only, not quoted |
| The Investor's Podcast TIP270 | https://www.theinvestorspodcast.com/episodes/tip270-jesse-itzler-nba-owner-entrepreneur-best-selling-author/ | AI transcript of a ~1h interview (Nov 2019) | Login-walled after the first Jesse line; one greeting line quoted as DOCUMENTED |
| Living with a SEAL / Living with the Monks | https://www.hachettebookgroup.com/titles/jesse-itzler/living-with-a-seal/9781455534678/ | Publisher page; no public excerpt | Not usable; not quoted |

## What the corpus rests on

Thirty-seven of thirty-eight excerpts are verbatim: nineteen from Free Swim newsletter posts on his own site (2025-2026, pulled from the Shopify Atom feed) and eighteen from his own X account (2019-2025, pulled from the syndication timeline and fxtwitter). One is documented-grade, a single ASR greeting line from a podcast transcript. The newsletter carries an attribution caveat: it is first person under his name but staff-posted and possibly transcribed from his talks, so the X posts are the anchor for wording and the newsletter is the anchor for structure. The two channels agree on every marker (numbers, named rules, "Here's the thing", two-line imperative closers), which is why confidence in the written register is high. The spoken register is effectively unsampled. Nothing comes from a quote aggregator.

## Known gaps

- **Spoken register is essentially unsampled.** The Investor's Podcast transcripts are login-walled after the first line; the single permitted yt-dlp attempt (a search for a "Build Your Life Resume" keynote) returned only a 2024 sizzle reel with no captions, and podscripts.co search 404'd. Item 38 is a greeting, not a stylistic sample.
- **Book text was not sampled.** Living with a SEAL and Living with the Monks have no public excerpt on the publisher page; they are the richest long-form sample of his voice and should not be quoted as verbatim until read.
- **Instagram, his main channel (~1.4M followers), was not fetched** (login wall). The X posts appear to be the same captions, which mitigates this, but Instagram-only posts are unsampled.
- **Attribution caveat on Free Swim.** The Shopify author field reads "Brian Sutherland" and several posts read like cleaned-up transcriptions of his talks ("Let me tell you about Rick Barry..."). Treat the newsletter as own-newsletter-grade, not byte-exact personal prose.
- **X threads and long posts were captured to their opening lines in three cases** (items 21, 24, 28); do not extend them from memory.
- **Anything published after 2026-10-19 is unsampled.**

## Refresh instructions

1. Re-fetch `https://jesseitzler.com/blogs/free-swim.atom` with a desktop UA and add 5-8 verbatim excerpts from posts published since October 2026, with slugs and dates; continue numbering inside the newsletter section and keep the staff-posted caveat on each source line.
2. Pull the X syndication timeline again (`https://syndication.twitter.com/srv/timeline-profile/screen-name/JesseItzler`, pause ~20s on a 429) and add 5-8 verbatim posts; use `https://api.fxtwitter.com/JesseItzler/status/<id>` for any post over 280 characters, and replace the truncated items 21, 24, and 28 with full text if recovered.
3. Caption one keynote or long podcast appearance with `/opt/homebrew/bin/yt-dlp --write-auto-sub --skip-download --sub-lang en -o "<dir>/%(id)s" "<url>"` (one attempt; stop on a 429); add 3-5 documented excerpts in a labelled spoken section and update the spoken-register stat.
4. Check the publisher page and Google Books for a public sample chapter of Living with a SEAL; if one exists, add 3-5 verbatim excerpts in a labelled book section.
5. If an Instagram post is quoted verbatim by a primary outlet or the caption is visible on a public embed, add it labelled by channel; otherwise leave Instagram as a gap.
6. Re-verify that every URL is still live. Never carry a quote forward that was not re-read at its source.

## Pattern notes

### 1. Scene with a count
Essays and long posts open on a concrete memory carrying a number (19 couches, 18 feet by 10 feet, four miles) and the rule only arrives after the scene has run. The Ghostwriter playbook will not start without the user's own count.

### 2. Mortality math
Time is converted into countable units (29 summers, 16 visits, 5 year blocks), isolated on its own line, and followed by immediate action. The Ghostwriter places this at the turn and the Hook Creator requires one hook built on it.

### 3. Name the rule in caps
Lessons are packaged as branded, calendar-based rules (the 3-Hour Rule, Kevin's Rule, Misogi, THE BUS RIDE) and capitalized on X. The LinkedIn Content Expert opens posts with the label; the Ghostwriter asks for the user's own rule name.

### 4. One beat per line, CAPS on the verb
X posts run 3-6 lines, one complete beat each, with 1-3 capitalized words and "..." as the pause. The LinkedIn Content Expert enforces the line cap and the CAPS budget.

### 5. Two-line imperative close
Pieces end by restating the rule and ordering the action ("This Saturday, not next winter. That's how you make sure regrets don't pile up."), or with one comfort question. Every playbook template ends this way and forbids a summary.

### 6. Anti-comfort, never anti-anyone
The only enemy is comfort and routine; there is no villain, no politics, and no hedge. The Anti-patterns list treats a named target or a qualifier as a drift out of voice.
