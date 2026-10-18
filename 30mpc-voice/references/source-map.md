# 30MPC Source Map (Armand Farrokh and Nick Cegelski)

Research date: 2026-09-09; spoken-register enrichment 2026-10-18
Refresh cadence: every 6 months (next: 2027-04)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| 30MPC newsletter archive | https://www.30mpc.com/newsletter | The core corpus. Weekly tactical issues, bylined, dated, script-heavy. | Open, server-rendered, scrapes cleanly |
| Triple T issue | https://www.30mpc.com/newsletter/how-to-write-outbound-messages-that-cut-through-using-triple-t | Outbound message framework and the buzzword ban list | Open |
| Cold call opener issue | https://www.30mpc.com/newsletter/i-book-1-in-3-cold-calls-with-this-opener | The opener script and the origin war story. Abridged from the book. | Open |
| Cold email before/after | https://www.30mpc.com/newsletter/3-cold-emails-that-cut-through-the-noise-before-vs-after | The teardown format and the four-part email structure | Open |
| Blog | https://www.30mpc.com/blog | Longer reports: objections, negotiation scripts, discovery questions | Open |
| Book: Cold Calling Sucks (And That's Why It Works) | print / audio | The long-form version of the cold call system | Purchase |
| Podcast: 30 Minutes to President's Club | 30mpc.com/podcast | Spoken register, guest frameworks, the banter between the two hosts | Open |
| LinkedIn (Armand Farrokh, Nick Cegelski) | linkedin.com | Short-form register, one-tactic posts | Login wall |
| Podcast RSS feed (Megaphone) | https://feeds.megaphone.fm/30mpc | 660 episodes with official show notes and direct MP3 enclosures; the reliable route to audio when YouTube captions are blocked | Open |
| #540 Cold Call Masterclass: The Perfect Script (Jan 20 2026, both hosts) | https://traffic.megaphone.fm/THMPC6303200218.mp3 | Full script performed live; "heard the name tossed around" opener; "just so no one from my team calls you again" | Open MP3; DOCUMENTED (whisper-1 ASR) |
| #517 The Secret to Handling Nasty Cold Call Objections (Oct 28 2025, Nick solo) | https://traffic.megaphone.fm/THMPC2396260973.mp3 | The ASPCA coffee-shop story; the Mr. Miyagi method | Open MP3; DOCUMENTED |
| #558 The 5 Data-Backed Cold Call Scripts to Overcome Any Objection (Mar 24 2026, host not named) | https://traffic.megaphone.fm/THMPC8103117140.mp3 | Five objections, each as a ring-ring role-play | Open MP3; DOCUMENTED |
| 30mpc.com newsletter index | https://www.30mpc.com/newsletter | Newer issues ("How To Build Your Warm Lead Engine in Sales Navigator") not yet in the corpus | Open |

## What was actually fetched

Three full newsletter issues and one blog index were pulled as raw text from 30mpc.com on 2026-09-09. The site is server-rendered and scrapes cleanly, so refreshing is cheap. Two of the three issues carry Armand Farrokh's byline and one carries Nick Cegelski's, which is why the corpus can distinguish their registers.

## Spoken enrichment (2026-10-18)

YouTube caption downloads returned HTTP 429, so three SELL episodes were pulled as MP3 from the official Megaphone RSS feed and transcribed with OpenAI whisper-1. Items 101-130: 26 documented spoken (11 Armand, 9 Nick, 6 host-unconfirmed) and 4 verbatim show-notes lines. The spoken register is now sampled for the first time.

## Known gaps

- **Spoken items are machine ASR, not human-verified.** Whisper does not diarize; episode #558 never names its host. Known slips: "Arman" for Armand, "heard her name tossed around" for "heard my name". Re-check against audio before client-facing use.
- **LEAD co-host Mark Kosoglow is not sampled**; only SELL episodes were pulled.
- **Newsletter refresh not done**; the 30mpc.com index is undated and alphabetical.
- **The book (Cold Calling Sucks) is still unread.**
- **Anything published after 2026-10-18 is unsampled.**
- **The book was not read.** Cold Calling Sucks (And That's Why It Works) is the canonical long-form source for the cold call system. One newsletter issue in the corpus is an abridged excerpt from it, which is the closest this corpus gets.
- **Screenshots not captured.** Their newsletters embed the actual email images inline, and the fetched text says only "let's look at how all 3 get woven into a cold email" where the image sits. The before-and-after email bodies themselves are therefore under-sampled. Read two issues in a browser on refresh and transcribe the email images.
- **No LinkedIn corpus.** Their short-form register lives behind a login wall.
- **Statistics need re-checking.** The 300M cold calls and 3x problem-language figures came from a running sentence in one issue. Confirm the exact numbers and the study source before republishing them.

## Refresh instructions

0. For spoken material, prefer the RSS route: `curl -s https://feeds.megaphone.fm/30mpc` to list enclosures, download the MP3, transcribe (whisper-1 or local Whisper), label `documented`. Retry `yt-dlp --write-auto-sub --skip-download --sub-lang en` only if the 429 has cleared.
1. Re-fetch the newsletter archive and pull any issue published since this research date.
2. Open two before/after issues in a browser and transcribe the embedded email screenshots.
3. Pull one podcast transcript for the spoken and two-host register.
4. Confirm the four-part cold email structure and the Triple T attribution to Jason Bay, episode 577.
5. Re-verify any statistic before it goes into client-facing enablement material.
