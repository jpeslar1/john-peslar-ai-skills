# 30MPC Source Map (Armand Farrokh and Nick Cegelski)

Research date: 2026-09-09
Refresh cadence: every 6 months (next: 2027-03)

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

## What was actually fetched

Three full newsletter issues and one blog index were pulled as raw text from 30mpc.com on 2026-09-09. The site is server-rendered and scrapes cleanly, so refreshing is cheap. Two of the three issues carry Armand Farrokh's byline and one carries Nick Cegelski's, which is why the corpus can distinguish their registers.

## Known gaps

- **The book was not read.** Cold Calling Sucks (And That's Why It Works) is the canonical long-form source for the cold call system. One newsletter issue in the corpus is an abridged excerpt from it, which is the closest this corpus gets.
- **No podcast transcript.** The two-host banter is a real part of the brand voice and is entirely absent here. The skill's register notes are inferred from written prose. Pull one episode transcript on refresh.
- **Screenshots not captured.** Their newsletters embed the actual email images inline, and the fetched text says only "let's look at how all 3 get woven into a cold email" where the image sits. The before-and-after email bodies themselves are therefore under-sampled. Read two issues in a browser on refresh and transcribe the email images.
- **No LinkedIn corpus.** Their short-form register lives behind a login wall.
- **Statistics need re-checking.** The 300M cold calls and 3x problem-language figures came from a running sentence in one issue. Confirm the exact numbers and the study source before republishing them.

## Refresh instructions

1. Re-fetch the newsletter archive and pull any issue published since this research date.
2. Open two before/after issues in a browser and transcribe the embedded email screenshots.
3. Pull one podcast transcript for the spoken and two-host register.
4. Confirm the four-part cold email structure and the Triple T attribution to Jason Bay, episode 577.
5. Re-verify any statistic before it goes into client-facing enablement material.
