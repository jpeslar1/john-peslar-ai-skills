# Kevin Dorsey Voice Source Map

Research date: 2026-10-19
Refresh cadence: every 6 months (next: 2027-04)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| LinkedIn profile (logged out) | https://www.linkedin.com/in/kddorsey3 | Headline plus about 9 recent post permalinks embedded in the public profile HTML | curl, desktop UA, no login |
| LinkedIn post permalinks (16 posts, 2021-09 to 2026-10) | linkedin.com/posts/kddorsey3_... (one URL per corpus item) | Full post text in the `<meta name="description">` tag, datePublished in JSON-LD; items 1-24 | curl, desktop UA; found via the profile page plus WebSearch `"Kevin \"KD\" Dorsey on LinkedIn" site:linkedin.com/posts` |
| Salesloft REVstars interview transcript (Sydney Sloan interviewing KD, PatientPop era) | https://web.archive.org/web/20231204003704/https://www.salesloft.com/revstars-kevin-dorsey-transcript/ | Official host-published Q&A transcript, about 2,000 words of KD speaking; items 25-28 | Live URL 404s; Wayback 2023-12-04 capture works |
| GTM Newsletter (GTMnow / Substack), "The Sales Leadership Framework Behind Multiple $100MM ARR Orgs" | https://thegtmnewsletter.substack.com/p/the-sales-leadership-framework-behind | Podcast write-up quoting KD on BIPSY, the 4Ds, WIGL, and 1:1 structure; items 29-30 (documented) | curl, clean HTML |
| salesleadershipaccelerator.com | https://www.salesleadershipaccelerator.com/newsletter | Program site; the newsletter page is a signup form only, no archive | curl works; no essay text available |
| Live Better Sell Better podcast (KD hosts) | https://podwise.ai/episodes/1284043 (listing) | Episode listings only; transcripts behind login | Not usable this round |
| Exit Five podcast appearance (2022) | https://exitfive.com/podcast/why-every-vp-sales-should-love-copywriting | Show notes only; a "Transcription" heading is present but no text renders | Not usable |

## What the corpus rests on

Twenty-eight of thirty excerpts are verbatim: twenty-four from sixteen of his own LinkedIn posts (2021-2026, fetched logged-out from each permalink, spelling and typos intact, one sponsored #AD post labelled), and four from an official host-published Salesloft interview transcript, which is his spoken voice as the host transcribed it rather than ASR. Two are documented-grade lines a publisher quoted from a podcast in the GTM Newsletter. Nothing comes from a quote aggregator. LinkedIn is both his dominant channel and the only written long-form available, since his Sales Leadership Accelerator site publishes no essays. Confidence in wording is high for items 1-28 and moderate for 29-30; confidence in the register is high, because the sixteen posts span five years and read the same, and the spoken transcript confirms the cadence out loud.

## Known gaps

- **No written long-form beyond LinkedIn.** salesleadershipaccelerator.com publishes no essays or archive; the "newsletter" page is a signup form. Do not quote the newsletter as if sampled.
- **Spoken voice rests on one transcript.** Live Better Sell Better transcripts are behind the podwise login, podscripts.co has no KD episodes indexed, the Exit Five page renders no transcript text, and yt-dlp was not attempted this round. The Salesloft transcript is the only spoken sample.
- **LinkedIn back catalog is a slice.** The logged-out profile exposes about 9 recent posts and WebSearch added about 7 older ones; the /recent-activity/ page login-walls. The 16 posts span 2021-2026 and are consistent, so coverage is adequate but not exhaustive.
- **Two items are publisher-quoted.** The GTM Newsletter lines (items 29-30) are the publisher's transcription and selection from a podcast, labelled documented; quote them as such.
- **Salesloft items are undated.** The interview era is inferred from his PatientPop title (c. 2019) and the Wayback capture date; the day could not be pinned.
- **Framework names outrun the sample.** BIPSY, the 4Ds, and WIGL are named in the GTM write-up and in his own posts (WIGL), but no post in the corpus spells out all of their parts. Do not reconstruct a framework's components from memory; mark them [VERIFY].
- **Anything published after 2026-10-19 is unsampled.**

## Refresh instructions

1. Re-fetch https://www.linkedin.com/in/kddorsey3 logged-out with a desktop UA, collect the embedded post permalinks, and curl each one; take the post text from `<meta name="description">` and the date from JSON-LD. Add 6-10 verbatim excerpts from posts after October 2026 and continue the numbering in the LinkedIn section.
2. Re-run WebSearch `"Kevin \"KD\" Dorsey on LinkedIn" site:linkedin.com/posts` to recover older posts the profile does not expose; prioritize posts that spell out the 3 Is, 3x3, KPIC, 4Ds, or WIGL in full.
3. Caption one Live Better Sell Better episode or a long guest appearance with `yt-dlp --write-auto-sub --skip-download --sub-lang en "<url>"`; add 3-5 documented (ASR) excerpts under a new labelled section and update the spoken-register stat.
4. Check whether https://www.salesleadershipaccelerator.com/newsletter has grown a public archive; if so, add 3-5 verbatim excerpts as a new "newsletter" section and note the register.
5. Re-check the Salesloft transcript at its Wayback URL; if the live page returns, swap the URL and keep the capture as a fallback.
6. Re-verify that every URL is still live. Never carry a quote forward that was not re-read at its source.

## Pattern notes

### 1. Verdict, then reversal
Posts open on a flat claim or a quoted excuse on its own line and undercut it immediately ("'No time to train. We're behind.' The sentence that keeps you behind."). The LinkedIn Content Expert writes this verdict line first and the closing inversion second, before any body.

### 2. The Not-run and the triad
Emphasis comes from parallel fragments ("Not when a slow week finally shows up. Not when the quarter's in the bag.") and three-part chants that recur at the close ("low for info, middle for insights, high for influence"). Every playbook allows one Not-run or one triad per piece, never more.

### 3. Named short frameworks
Lessons are packaged as three-letter or three-by-three frameworks (3 Is, 3x3, KPIC, POE, 4Ds, WIGL) and attached to a story or a rep. The Cold Outreach Writer runs the 3 Is as its research step and refuses to write the top-of-account message until the insight exists.

### 4. Staged objection in caps
He voices the reader's pushback in his own name ("BUT BUT BUT KD THIS TAKES TOO LONG!!!") and answers it in a numbered list. The Objection Handling Expert quotes the objection verbatim on its own line, reverses it, and answers in two or three numbered behaviors.

### 5. Buyer's hat
He switches sides and narrates buying ("This is KD with his buyer hat on"), mocking fake deadlines and asking for empathy with a buyer who has an actual job. The Cold Outreach Writer and Objection Handling Expert use this to critique a tactic from the receiving end instead of lecturing.

### 6. Coach's send-off and the rep shout-out
Nearly every post lands on a two-beat aphorism, then a short imperative ("Be different. Stand out. Let's go.") or a soft "happy to share"; wins are credited to named reps ("Proud of Mr Dane!"). The LinkedIn Content Expert closes every post this way and marks rep names [VERIFY] unless the user supplied them.
