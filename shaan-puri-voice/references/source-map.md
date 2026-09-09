# Shaan Puri Voice Source Map

Research date: 2026-09-09
Refresh cadence: every 6 months (next: 2027-03)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| One Minute Blog | https://www.shaanpuri.com/blog | The core written corpus, short newsletter-style posts | Open, scrapes cleanly with a plain HTTP fetch |
| Individual posts used | https://www.shaanpuri.com/p/&lt;slug&gt; (see corpus for exact slugs) | Verbatim excerpts, dated | Open |
| My First Million | YouTube channel "My First Million", also mfmpod.com | Spoken register, banter with Sam Parr, longer stories | Open, video with mostly auto-generated captions |
| X / Twitter | x.com/ShaanVP | Short-form takes, current register | Open but not sampled this pass |
| shaan-puri-founder-brain (this repo) | /Users/johnpeslar/dev/john-peslar-ai-skills/shaan-puri-founder-brain/ | The companion THINKING skill; read for scope boundary, not for corpus text | Local |

## What was actually fetched

Nine "One Minute Blog" posts were already cached in the scratchpad from a prior scrape of shaanpuri.com (`raw/sp-*.txt`) and were read in full this session: big-mario-marketing, excuses, finding-your-thing, mispriced-assets, proximity-is-power, shamelessly-cloning, stop-working-so-hard, triangle-of-talent, underdo-the-competition. The pages scrape cleanly as plain server-rendered HTML with the post text, a date line, and the "-Uncle Shaan" sign-off intact; each also carries a duplicated share-card render of the same post further down the page, which was ignored as noise.

One YouTube video was pulled for spoken register: "7 things Bezos, MrBeast & Thiel do that you don't" (My First Million channel, videoId jZT04e4yBb0). Its only available caption track is `en, generated=True`, i.e. ASR, so every excerpt from it is labeled `documented` in the corpus, not `verified`.

## Known gaps

- **No X/Twitter corpus.** His short-form takes on x.com/ShaanVP were not sampled. The newsletter is longer-form than his tweets, so the Hook Creator playbook is inferred from newsletter hook lines rather than from sampled tweets. Fix on refresh.
- **No human-captioned podcast episode found.** Every My First Million caption track checked in this pass was ASR-only. All spoken-register excerpts are `documented`, not `verified`. If a future episode has a human track, re-pull and upgrade.
- **Only one MFM episode sampled.** A single video is a thin base for spoken cadence; his podcast register varies by co-host energy and topic. Pull 2-3 more episodes on refresh, ideally ones with a human caption track.
- **Sample skews 2024-2025 newsletter posts.** No pre-2024 material and no post published after August 2025 was in the cache. Confirm his current vocabulary and OMB format are unchanged before relying on this corpus long-term.
- **No direct verification of exact post URLs.** URL slugs in the corpus are the site's evident `/p/<slug>` pattern inferred from the post title; re-fetch shaanpuri.com/blog on refresh to confirm each slug resolves before republishing a link.

## Refresh instructions

1. Re-fetch https://www.shaanpuri.com/blog and pull any post published since August 2025 that is not in this corpus; confirm the nine existing slugs still resolve.
2. Pull 2-3 additional My First Million episodes via `yt.py search` and `yt.py tracks`, preferring any with `generated=False`.
3. Sample x.com/ShaanVP for short-form register if a fetch path becomes available; note the access method used.
4. Re-verify the named frameworks (mispriced assets, Triangle of Talent, shamelessly cloning, underdo the competition) are still described the same way; update the corpus if he has revised or renamed one.
5. Confirm the `shaan-puri-founder-brain` skill's scope has not shifted in a way that changes this skill's boundary statement.
