# Matt Gray Source Map

Research date: 2026-09-09
Refresh cadence: every 6 months (next: 2027-03)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| founderos.com homepage | https://www.mattgray.com/ | Facts (Founder OS, Content GPS System name, track-record claims) - third-person sales copy, NOT his voice | Open, scrapes cleanly |
| founderos.com blog | https://www.founderos.com/blog | First-person long-form posts, his own byline | Open, scrapes cleanly |
| "How I Built My 7-Fig Brand" | https://www.founderos.com/blog/how-i-built-my-7-fig-brand | The Content GPS explained in his own words, verbatim corpus | Open |
| X / Twitter | https://x.com/matt_gray_ | Primary native short-form channel, ~400K followers, verbatim posts | Open (unauthenticated read works via fetch) |
| LinkedIn | https://www.linkedin.com/in/mattgray1/ | His single largest channel (~900K-2.5M+ followers reported across sources) - short-form native format | Login wall, NOT fetched this session |
| YouTube - Matt Gray | https://www.youtube.com/@realmattgray | His own channel, spoken register, ASR captions only | Open, ASR only (`documented`) |
| "Open Residency" interview | https://www.youtube.com/watch?v=eySbMU08piQ | Third-party long-form interview, spoken register, ASR captions only | Open, ASR only (`documented`) |
| Founder OS newsletter | https://www.founderos.com/newsletter | Weekly newsletter, ~250K+ subscribers per third-party reporting | Not fetched this session - see gaps |
| The Matt Gray Show (podcast) | Apple Podcasts / podscan.fm | His own podcast | Not fetched this session - see gaps |

## What was actually fetched

- `mattgray.com` homepage (already cached from a prior session) - confirmed third-person marketing copy, used only for the "Content GPS System" name and to flag as unreliable for voice.
- `founderos.com/blog/how-i-built-my-7-fig-brand` - fetched clean as readable text via `fetch.py`. First-person, human-authored, supplied the bulk of the verified blog corpus (items 1-10).
- `founderos.com/blog` (index page) - fetched clean, confirmed the blog is server-rendered and other post titles exist, but the two specific post URLs guessed from the index (`compounding-machine-behind-exponential-growth`, `create-competitionless-category`) both 404'd. Did not find the correct slugs before time ran out; this is a real gap, not a refusal.
- `x.com/matt_gray_` (profile page) and one individual status thread (`/status/1874463865641050562`) - both fetched clean as readable text via `fetch.py`, no login wall hit. Supplied items 11-20.
- YouTube search via `yt.py search` surfaced 10 candidate videos (his own channel plus interviews on other channels). Pulled caption tracks for four candidates; all four returned `generated=True` (ASR, no human caption track exists for any of them).
- Two ASR transcripts pulled in full: `iONQNwRHd7Y` ("how to build a profitable personal brand (in just 7 steps)," his own channel) and `eySbMU08piQ` ("Open Residency" interview). Both supplied the `documented` section (items 21-27). ASR text has no punctuation or diarization, so quotes above were lightly punctuated for readability and attribution to Matt Gray was only used where the surrounding question/answer structure made the speaker unambiguous.

## Known gaps

- **No LinkedIn corpus at all.** LinkedIn is reported to be his single largest and most native channel for high-volume short-form content (the assignment brief explicitly flags it as most important), but `linkedin.com/in/mattgray1` sits behind a login wall and was not fetched this session. Every hook pattern and lexicon note below LinkedIn-specific structure in SKILL.md is inferred from his X posts and blog prose, not sampled directly from LinkedIn. This is the single biggest gap in this skill. Fix on refresh: pull his public LinkedIn posts via a logged-in fetch or a third-party LinkedIn export tool.
- **No human-captioned video sampled.** Every video candidate checked (his own channel and two interview channels) came back ASR-only (`generated=True`). His actual spoken cadence, filler words, and pacing are only sampled as approximate `documented` text, not verified.
- **Newsletter (Founder OS) not fetched.** The newsletter is reported to have 250K+ subscribers and is described as containing content not available elsewhere. No newsletter archive URL was located and fetched this session; the blog is used as a proxy for his long-form written voice instead.
- **Podcast (The Matt Gray Show) not fetched.** Found on Apple Podcasts and podscan.fm but no transcript was pulled this session.
- **Track-record numbers are unverified positioning copy.** "8 figures of wealth across 3 companies," "9 figures of wealth," "2.5 million followers," "14 million person community," and similar totals appear only on the third-party-styled homepage or in his own promotional copy, not confirmed against any independent source. Treat any specific wealth/audience-size figure as [VERIFY] before using it in output, per the SKILL.md Output Format rule.
- **Two blog post slugs guessed wrong and were not corrected.** The blog corpus rests on a single fully-fetched post. Re-crawl the blog index for exact slugs on refresh rather than guessing from title text.

## Refresh instructions

1. Re-fetch `founderos.com/blog` and pull 2-3 more posts by exact slug (not guessed) to widen the verified written corpus beyond one post.
2. Get a logged-in or third-party-tool pull of `linkedin.com/in/mattgray1` - this is the highest-priority fix, since LinkedIn is his primary native format per the assignment brief and is currently unsampled.
3. Search again for a human-captioned (non-ASR) video; if none exists, keep the spoken register capped at `documented`.
4. Try to locate and fetch a Founder OS newsletter archive page (search "Founder OS newsletter archive" or check beehiiv/Substack).
5. Re-verify every wealth/follower/subscriber number before it goes into client-facing output; these figures likely change and are currently unverified promotional claims, not confirmed facts.
