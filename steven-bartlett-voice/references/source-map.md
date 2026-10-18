# Steven Bartlett Voice Source Map

Research date: 2026-10-18
Refresh cadence: every 6 months (next: 2027-04)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| @StevenBartlett on X | https://x.com/StevenBartlett | 99 original posts 2018-2025: the 2018-2019 two-paragraph aphorism era, then 2023-2025 episode promos and personal announcements; the only own-hand writing fetched | Public via syndication.twitter.com (rate-limited; long posts truncated at ~280 characters, marked in the corpus) |
| Happy Sexy Millionaire publisher page (Hachette UK, Yellow Kite, 2021) | https://www.hachette.co.uk/titles/steven-bartlett/happy-sexy-millionaire/9781529394856/ | First-person opening passage of the book ("As an 18-year-old, Black, broke, lonely…") | Public blurb; publisher-quoted, no full extract |
| DOAC YouTube: "6 BEST Pieces Of Business Advice That Made Me Millions \| E103" (Oct 25 2021) | https://www.youtube.com/watch?v=ls9be-9C-uk | 27-minute solo Q&A: focus, time as currency, the someday shelf, "there's gonna become a day" | Open video; DOCUMENTED (auto-captions, lowercase, no punctuation; "sunday shelf" ASR slip flagged) |
| Behind The Diary YouTube: "You're procrastinating 80% of your time (here's how I fixed it)" (Aug 3 2025) | https://www.youtube.com/watch?v=bzVuNxEVScs | 24-minute direct-to-camera vlog: "I'm going to be honest. I'm pissed off."; "stay with me guys" | Open video; DOCUMENTED (auto-captions, YouTube-punctuated; "Olirri" = O'Leary) |
| TEDxLondon: "Entrepreneurs should follow their instincts" (c. 2017) | https://www.youtube.com/watch?v=Dri_W3dvd6Y | 13-minute scripted origin talk: report card at 15, Wallpark, Social Chain | Open video; DOCUMENTED (auto-captions) |
| BBC Maestro: "Steven Bartlett on quitting" (course launched 2024) | https://www.youtube.com/watch?v=W2x46AYxh8E | 9-minute clip: "quitting is for winners", the quitting framework | Open video; DOCUMENTED (auto-captions) |
| Forbes Australia interview (Alexandra York, Apr 20 2025) | https://www.forbes.com.au/news/30-under-30/why-the-diary-of-a-ceo-founder-turned-down-100m-podcast-deal/ | 16 direct quotes on independence, "dragged or driven", the bulldozer | Public; DOCUMENTED (journalist-transcribed) |
| BusinessCloud: "TV Dragon responds to Social Chain sale" (Feb 6 2023) | https://businesscloud.co.uk/news/tv-dragon-responds-to-social-chain-sale/ | His Feb 2023 tweets on the 2019 board disagreement and resignation | Public; DOCUMENTED (journalist-reproduced tweet fragments) |
| Steven's Newsletter (Substack) | https://stevenbartlett.substack.com | Exists ("My 5 thoughts") but the archive returns no posts | Not usable |
| stevenbartlett.com News & Stories | https://stevenbartlett.com | Third-person PR copy, not his voice | Public; not used |
| The Diary Of A CEO: The 33 Laws (Penguin, 2023) | Publisher pages only | Blurb copy only ("Strategy changes like the seasons.") | Paywalled; no extract |

## What the corpus rests on

Twenty-two of thirty-six excerpts are verbatim: twenty X posts pulled directly from the syndication timeline (complete for 2018-2019, truncated at roughly 280 characters for the 2023-2025 long posts, each truncation marked) and two sentences of his book's opening as quoted on the publisher's page. Fourteen are documented-grade: seven ASR captions from solo videos on his own channels, three ASR captions from a TEDx talk and a BBC Maestro clip, and four journalist-transcribed quotes. Nothing comes from a quote aggregator. The written sample is X-only, which is a real limit: the aphorism register is well covered, the long-form register is inferred from truncated openers and spoken material. Confidence in wording is high for items 1-22 and moderate for 23-36.

## Known gaps

- **No own-channel long-form writing is fetchable.** The Substack has zero posts, stevenbartlett.com is third-person PR, LinkedIn is behind login, and no publisher extract exists for The 33 Laws. The Ghostwriter playbook's long-form shape is inferred from truncated X openers and solo-video cadence; flag long-form output as inferred-register when precision matters.
- **Long X posts are truncated.** The 2024-2025 essays on creator advice, the Forbes independence decision, and his parents cut off at about 280 characters in the syndication endpoint. Full text needs an authenticated X session. Do not extend them from memory.
- **Spoken excerpts are auto-captions.** The 2021 video has no punctuation; names are misrecognised (Olirri for O'Leary, Barlett, wallp Park for Wallpark); "someday shelf" is heard as "sunday shelf" once. Use for cadence and stance, not exact wording.
- **Book text is publisher-quoted.** Items 1-2 are his words as the publisher chose to quote them; the sentence in item 2 continues beyond the excerpt. Nothing else from either book was sampled.
- **Journalist quotes are secondhand.** Forbes Australia and BusinessCloud lines (items 33-36) are his words as printed by a reporter, including two fragments joined as printed.
- **The 2020 Social Chain resignation post was not captured** beyond its opening line; Provoke Media, Hollywood Reporter, and Yorkshire Evening Post returned 403 or paywall.
- **Anything published after 2026-10-18 is unsampled.**

## Refresh instructions

1. Pull the X syndication timeline again (`https://syndication.twitter.com/srv/timeline-profile/screen-name/StevenBartlett`) and add 5-8 new verbatim posts with status URLs; mark any truncation. If an authenticated session is available, replace the truncated 2024-2025 posts (items 15, 17, 18, 19, 20, 21, 22) with full text and note the change.
2. Check https://stevenbartlett.substack.com for published issues; if any exist, add a "Newsletter" verbatim section and consider adding the Newsletter Writer playbook that was dropped in this build.
3. Caption one new solo Behind The Diary video with `yt-dlp --write-auto-sub --skip-download --sub-lang en "<url>"`; add 3-5 documented excerpts and update the spoken-register stats.
4. If a publisher or retailer posts a sample chapter of The 33 Laws, add it as a labelled publisher-quoted section; until then keep both books out of the verbatim sections except items 1-2.
5. Re-verify that every URL is still live. Never carry a quote forward that was not re-read at its source.

## Pattern notes

### 1. Claim, blank line, reframe
The 2018-2019 posts are two visual blocks: a flat provocation, then the humane truth ending in a short imperative ("Focus on that.", "then let someone down."). The LinkedIn Content Expert and Hook Creator playbooks require the reframe under every provocation.

### 2. Confession opener
Spoken and written pieces start with an admission of state ("I'm just going to go ahead and say it...", "I'm going to be honest. I'm pissed off.", "WOW! Today was one of the most surreal days of my career!") followed by a promise of the honest answer. The Ghostwriter playbook opens here.

### 3. Disadvantages before the pivot
The same biographical list recurs across book, X, and stage: 18, Black, broke, lonely, insecure, drop-out, bankrupt family; the $100 mic; the bedroom podcast nobody listened to. The Ghostwriter interviews for the user's own true list and refuses to borrow his.

### 4. Named frameworks walked as decision trees
The someday shelf, the quitting framework, second priority, signal versus noise: a label, then "if… then" steps. Advice content in every playbook names the framework before explaining it.

### 5. Delegated brag
Metrics appear via third parties ("Apple said…", "Forbes…") or a video title (80%), never in the first person. The Signature Move "delegate the brag" governs any number in output.

### 6. Reverence and gratitude
Guests are "legend" and "absolute honour"; milestones end on thanks to god kids, friends, and supporters; health is "a temporary loan." The emotional-register fix for a cocky draft is a gratitude line.
