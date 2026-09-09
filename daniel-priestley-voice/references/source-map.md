# Daniel Priestley Source Map

Research date: 2026-09-09
Refresh cadence: every 6 months (next: 2027-03)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| Dent Global blog | https://www.dent.global/blog | The core written corpus. Listicle posts on business growth stages, personal brand, referrals, and pitching. | Open, but the live page renders body text through a per-letter JS animation that breaks a plain HTTP fetch's word spacing; a Wayback Machine snapshot of the same URL renders clean. |
| 9 Business Growth Stages | https://www.dent.global/business-growth-entrepreneurs/ | The 9-stage framework (Start-Up, Wilderness, Struggling Boutique, Lifestyle Boutique, Performance...), Revenue Per Person concept | Open (fetched via Wayback snapshot 20260519181833) |
| 21 Ways to Boost Your Profile and Personal Brand | https://www.dent.global/personal-brand-profile/ | The S.A.L.T. method (Social, Awards, Live events, Traditional media), personal-brand voice register | Open, fetched cleanly on a direct request this session |
| 9 Ways to Generate More Referral Partners | https://www.dent.global/get-more-referrals/ | Referral-partner system, his sourced-statistic opening pattern | Open (fetched via Wayback snapshot 20260208050137) |
| Is Raising Investment the Right Move for Your Business? | https://www.dent.global/raising-investment/ | Fetched and read, then EXCLUDED from the corpus - the post is explicitly bylined "This article was written by James Church of Robot Mascot," a Dent-affiliated guest author, not Daniel Priestley. Kept here only as a flag against reuse. | Open |
| Key Person of Influence (book, 2010/revised) | book | The 5 P's framework (Pitch, Publish, Product, Profile, Partnership) | Purchase - not read this session |
| Oversubscribed (book, 2015) | book | Demand-creation and scarcity framework | Purchase - not read this session |
| 24 Assets (book, 2018) | book | Asset-building framework | Purchase - not read this session |
| YouTube - "Daniel Priestley \|\| Key Person Of Influence" channel and guest appearances (Diary of a CEO, SaaS Academy, Mindvalley Talks, Smart Passive Income) | youtube.com | Spoken register, faster and more compressed than the blog | Open, but this session hit an IP block from the transcript API after the first successful `tracks` call (see below) |
| danielpriestley.com | https://www.danielpriestley.com | Author site, likely duplicates or supplements the Dent Global blog | Attempted; not confirmed reachable this session, not used in the final corpus |

## What was actually fetched

- Three Dent Global blog posts were fetched and used for the verbatim corpus (items 1-18): business-growth-entrepreneurs, personal-brand-profile, get-more-referrals. The live site renders body copy through a per-letter-span animation that a plain HTTP GET reproduces literally (one space-separated character per token), which made a direct `fetch.py` pull on two of the three unusable; the same pages were pulled clean from Wayback Machine snapshots instead. personal-brand-profile fetched clean directly.
- A fourth post, raising-investment, was fetched and read, then excluded once its byline showed it was ghostwritten by a Dent-affiliated third party, not Daniel Priestley himself.
- One cached ASR transcript of a spoken interview appearance (topic: starting and scaling a business, waiting-list validation, the Rolex example) was reused from a prior research pass in this repo's scratchpad. Its exact video ID/URL was not reconfirmed this session.
- `yt.py search` returned a working list of his own YouTube channel and guest-appearance videos, and one `yt.py tracks` call against a Key Person of Influence-channel video succeeded (subtitles disabled on the first video tried; a second returned all `generated=True` caption tracks, i.e. ASR only, confirming no human-captioned track was available for that video). A follow-up `yt.py tx` call to actually pull that transcript hit `IpBlocked` from the youtube-transcript-api (the same rate-limit condition noted in the assignment as having killed a prior attempt). No fresh transcript was pulled this session as a result.

## Known gaps

- **No book text.** Key Person of Influence, Oversubscribed, and 24 Assets are all unread for this build. The 5 P's (Pitch, Publish, Product, Profile, Partnership), the demand-creation mechanics in Oversubscribed, and the specific asset list in 24 Assets are referenced in SKILL.md only as named concepts from public secondary descriptions, not sampled as his running prose. Do not present book passages as quotations; none are in this corpus.
- **The spoken/ASR item's exact source is unconfirmed.** Items 19-23 are real ASR-transcribed lines cached from a prior session, but this session could not re-locate and re-verify the exact video ID because of a YouTube transcript API IP block encountered mid-session. Treat items 19-23 as `documented` only. Top priority on refresh: re-run `yt.py search` for his Diary of a CEO-style interview appearances, find the matching video by content, and confirm the caption-track type with `yt.py tracks`.
- **No confirmed human-captioned (generated=False) track found.** Every caption track checked this session was `generated=True` (ASR). There is currently no `verified` spoken item in this corpus; every spoken register example is `documented`.
- **LinkedIn and X short-form not sampled.** His current short-form register (LinkedIn posts, the X account referenced in search results) lives behind login walls or was not directly fetched this session. The LinkedIn Content Expert playbook is inferred from his long-form listicle habits, not from sampled short posts. Fix on refresh.
- **danielpriestley.com not confirmed reachable.** The corpus relies entirely on dent.global; his personal author site was attempted but not successfully pulled this session.
- **Sample skews 2023.** All three verbatim blog posts are from April-August 2023. Confirm the vocabulary, the S.A.L.T. and 9-stage frameworks, and the cited statistics are still current on refresh - Dent Global's product portfolio (ScoreApp, Vidonary) referenced on the site's homepage has changed over time and framework language may shift too.

## Refresh instructions

1. Re-run `yt.py search` for "Daniel Priestley Diary of a CEO", confirm which video matches the cached ASR excerpt (the "zero to a million" / Rolex waiting-list content), and re-cite items 19-23 against a real video ID and date once found.
2. Pull at least one fresh, unexpired `yt.py tracks` + `yt.py tx` pair for a `verified` or a cleanly-dated `documented` spoken item; retry later if IP-blocked again.
3. Re-fetch the Dent Global blog index for any post published since August 2023 not yet in this corpus, preferring the Wayback Machine snapshot route if the live per-letter animation still breaks plain-text fetches.
4. Attempt danielpriestley.com directly again; if it is a client-rendered SPA, note that honestly rather than treating a thin scrape as complete.
5. Do not reuse the "Is Raising Investment" post's content as Priestley's voice; it is ghostwritten by James Church of Robot Mascot under the Dent Global byline.
6. If any book (Key Person of Influence, Oversubscribed, 24 Assets) is read, replace the secondary-description references to the 5 P's and related frameworks with short cited quotations and drop them from "referenced but unsampled" status.
