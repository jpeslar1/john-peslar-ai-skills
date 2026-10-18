# Sara Blakely Voice Source Map

Research date: 2026-10-18
Refresh cadence: every 6 months (next: 2027-04)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| LinkedIn profile and public posts (sarablakely27) | https://www.linkedin.com/in/sarablakely27/ and https://www.linkedin.com/in/sarablakely27/recent-activity/all/ | Her own written posts 2019-2026: Spanx origin stories, Blackstone sale, Sneex launches, #MondayMugshot motivation, FSU commencement | Open; post pages render full text server-side (curl with a browser user agent; text in the description meta tag) |
| LinkedIn post: Blackstone sale announcement (Oct 21 2021) | https://www.linkedin.com/posts/sarablakely27_entrepreneur-spanx-activity-6856961257753444353-mDLf | Longest single written piece; "cared the most", "one butt at a time", "I'll just know" | Open |
| LinkedIn post: #BuildYourEmpire (Sep 19 2019) | https://www.linkedin.com/posts/sarablakely27_entrepreneur-business-buildyourempire-activity-6579731880034258944-3Qng | Quoted-pressure-then-reversal structure | Open |
| LinkedIn post: Spanx 19th anniversary (Oct 17 2019) | https://www.linkedin.com/posts/sarablakely27_entrepreneur-business-activity-6590603808496238592-mGRM | Prop-scene origin story; "I was every department!" | Open |
| LinkedIn post: #GetRidiculous (Sep 1 2021) | https://www.linkedin.com/posts/sarablakely27_getridiculous-entrepreneur-theunexpected-activity-6838840714340782080-p2tt | "Define yourself!" moral; intelligence doesn't have to look a certain way | Open |
| LinkedIn post: Sneex Ballerina letter (Mar 31 2026) | https://www.linkedin.com/posts/sarablakely27_we-launched-sneex-in-2024-to-rewrite-the-activity-7444760479052427264-FWE9 | Brand-letter register, signed "Xo, Sara Blakely / Founder, SNEEX" | Open |
| LinkedIn post: FSU commencement (Jun 4 2026) | https://www.linkedin.com/posts/sarablakely27_sara-blakely-florida-state-university-2026-activity-7468380788451987458-Oy17 | "What you don't know can be your greatest asset" | Open |
| LinkedIn post: #MondayMugshot rock bottom (Oct 5 2026) | https://www.linkedin.com/posts/sarablakely27_mondaymugshot-mondaymotivation-activity-7512875447039270913-DeON | Most recent sampled post; gratitude-for-rock-bottom register | Open |
| Stanford GSB "View From The Top" talk (YouTube, c. 2018) | https://www.youtube.com/watch?v=TPURpzGPMxQ | 46-minute interview: fax-machine years, humor as tactic, "start small, think big, scale fast", "hire your weaknesses" | Open video; DOCUMENTED (auto-captions saved locally at research time) |
| Forbes "Betting On Yourself" interview (YouTube, 2024-2025) | https://www.youtube.com/watch?v=b8ka0qVGipA | Sneex, the 10x rule, mindset tapes since age 16 | Open video; DOCUMENTED (auto-captions) |
| Instagram @sarablakely | https://www.instagram.com/sarablakely | Highest-volume channel; same captions as LinkedIn plus more personal content | Login-walled; not fetched |
| Fortune, "6 unhinged things…" (Dec 23 2025) | https://fortune.com/article/6-unhinged-things-spanx-founder-sara-blakely-did-shaped-success-of-1-2-billion-empire/ | Confirms an Instagram list post exists; journalist summary, not quotes | Open; secondary, not used for quotes |

## What the corpus rests on

Twenty-five of thirty-three excerpts are verbatim from her own public LinkedIn posts, spanning 2019 to October 2026, fetched as full page text with dates decoded from each post's activity ID. Eight are documented-grade auto-captions from two long interviews on official channels (Stanford GSB, Forbes). Nothing comes from a quote aggregator. Because her Instagram captions are largely cross-posted to LinkedIn, the written sample covers her dominant register despite Instagram being unfetched. Confidence in wording is high for items 1-25 and moderate for 26-33.

## Known gaps

- **Instagram not fetched directly.** The "6 unhinged things" list post (cited by Fortune) and the 2024 Sneex launch caption exist but their exact text was not obtained. A logged-in human can copy them in minutes.
- **No commencement or keynote transcript.** The FSU 2026 speech is linked from her LinkedIn post as video; it could be captioned with yt-dlp if a speech register is wanted.
- **No Masterclass or How I Built This transcript.** The NPR transcript located was the host intro, not the interview. Not required given LinkedIn coverage.
- **Spoken excerpts are auto-captions.** Some passages in the source are garbled; the quoted ones were chosen where the ASR is clean, and one slip is flagged inline.
- **Anything published after 2026-10-18 is unsampled.**

## Refresh instructions

1. Re-fetch https://www.linkedin.com/in/sarablakely27/recent-activity/all/ with a browser user agent; open each new post permalink and copy the description meta tag text. Decode the date from the activity ID (top bits are a millisecond timestamp). Add 5-10 verbatim excerpts, continuing the numbering.
2. If Instagram access is available, add a "Short-form (Instagram)" section for captions that were not cross-posted.
3. Caption the FSU commencement video with `yt-dlp --write-auto-sub --skip-download --sub-lang en`; add 3-5 documented excerpts in a speech-register subsection.
4. Re-verify that every URL is still live. Never carry a quote forward that was not re-read at its source.

## Pattern notes

### 1. Prop scene, then moral
Every origin and milestone post opens on a physical object (pantyhose, license plate, cardboard sign) and closes on a one-line imperative. The Ghostwriter playbook interviews for the user's prop first.

### 2. Quoted pressure, then reversal
What people kept saying is quoted, then reversed in one line ("Oh, and I built my empire too. 👊"). Used for resilience content.

### 3. Humor as tactic
Self-deprecating body humor is deliberate; she credits the fax-machine years for teaching that a laugh buys thirty seconds. One joke per post, before the moral.

### 4. Cared the most
Wins are credited to caring and persistence, never to knowledge or network. This is the humility mechanism that keeps milestone posts from reading as brags.

### 5. Ellipsis and exclamation rhythm
Punctuation is the cadence: ellipses as pauses, multiplied exclamation marks at peaks, emoji at line ends. Flat punctuation is the clearest off-voice tell.

### 6. Reader turn
Posts end with a question that invites a story back or a tag ask; community engagement is built into the closer, not bolted on.
