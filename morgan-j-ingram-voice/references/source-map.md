# Morgan J Ingram Voice Source Map

Research date: 2026-10-19
Refresh cadence: every 6 months (next: 2027-04)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| LinkedIn post permalinks (12 posts, 2020-03 to 2023-11) | linkedin.com/posts/morganjingram_... (one URL per corpus item) | Full post text in the `<meta name="description">` tag, datePublished in JSON-LD; items 1-15 | curl, desktop UA; found via WebSearch `"Morgan J Ingram on LinkedIn" site:linkedin.com/posts`. Fetching linkedin.com/in/morganjingram logged out returned a different person's profile, so permalinks came from search, not the profile page |
| HubSpot Sales Blog, "Master in Sales" column: "Mastering the Art of Cold Calling" | https://blog.hubspot.com/sales/master-in-sales-cold-calling | About 2,500-word bylined guide: PLA opener, value-prop formula, PAQ objection handling; items 16-19 | curl, clean HTML; "Written by: Morgan J Ingram", updated 2024-08-20 |
| HubSpot Sales Blog: "My 10-Step Process for Nailing Prospecting on LinkedIn, According to AMP's CEO" | https://blog.hubspot.com/sales/master-in-sales-linkedin-prospecting | Bylined 10-step LinkedIn prospecting process, blank-connection-request data, the 76% nudge; items 20-23 | curl; updated 2025-03-27 |
| HubSpot Sales Blog: "Using Video to Accelerate Your Sales Pipeline: Morgan Ingram's Master in Sales Series Part 1" | https://blog.hubspot.com/sales/morgan-ingram-video-sales | Bylined video-selling guide: movie-trailer analogy, 10-30-10, stand up; items 24-25 | curl; updated 2024-10-04 |
| 30MPC newsletter guest issue, "10-30-10 LinkedIn Voice Notes" by Morgan Ingram | https://www.30mpc.com/newsletter/club-fundamentals-10-30-10-linkedin-voice-notes | Short guest-written issue in first person with the full voice-note script; items 26-27 | curl, clean HTML; dated 2023-07-28 |
| X / @morganjingram | https://x.com/morganjingram/status/1821547290819023048 | Thread opener on LinkedIn voice notes; item 28 (first post only) | `cdn.syndication.twimg.com/tweet-result?id=...&token=a` and api.fxtwitter.com both return text and an ISO date; the profile timeline endpoint was rate-limited |
| amp-creative.com | https://amp-creative.com | Listed as his company site; host returns no HTTP response. "AMP Creative" in web results is an unrelated Dallas firm | Dead |
| YouTube @morganjingram | https://www.youtube.com/@morganjingram | Video library; captions not pulled (yt-dlp 429 risk, written corpus sufficient) | Not used |

## What the corpus rests on

All twenty-eight excerpts are verbatim and written by him, across four channels: fifteen from twelve of his own LinkedIn posts (2020-2023, several of them captions of his own coaching videos), ten from three bylined HubSpot "Master in Sales" columns (2024-2025, passed through HubSpot's editors), two from a guest issue he wrote for the 30MPC newsletter (2023), and one X thread opener (2024). Nothing comes from a quote aggregator and nothing is documented-grade; there are no ASR captions. The LinkedIn posts are the native voice and the HubSpot columns are the same voice in long form with editorial polish. Confidence in wording is high throughout; confidence that the HubSpot fillers ("folks," "I know, big shocker") are his rather than an editor's is moderate.

## Known gaps

- **No owned-site material.** amp-creative.com does not respond at all, so no essays from his company site; his newsletter (ampup.live/email, per his X post) has no public archive found.
- **X thread is truncated to its opener.** Only the first post of the 2024-08-08 thread was retrievable (syndication and fxtwitter return single tweets; the timeline-profile endpoint was already rate-limited this session). Do not extend the thread from memory.
- **LinkedIn coverage ends at 2023-11.** The logged-out profile fetch served an unrelated person, so no profile-embedded recent posts; the twelve posts came from search-indexed permalinks. Nothing from his 2024-2026 LinkedIn feed is in the corpus; the 2024-2025 HubSpot columns fill the recency gap in written form only.
- **No spoken transcript.** YouTube captions were not pulled under the yt-dlp 429 constraint, and no podcast transcript was sampled. The posts caption his own videos in his own words, so the written cadence is a fair proxy, but spoken-register claims are inferred.
- **HubSpot copy is editor-touched.** The em dashes and some connective fillers in items 16-25 may be HubSpot's house style rather than his; quote those items as his edited register.
- **Anything published after 2026-10-19 is unsampled.**

## Refresh instructions

1. Re-run WebSearch `"Morgan J Ingram on LinkedIn" site:linkedin.com/posts` and curl each new permalink with a desktop UA; take the text from `<meta name="description">` and the date from JSON-LD. Add 6-10 verbatim excerpts from 2024-2026 posts to close the recency gap and continue the numbering in the LinkedIn section.
2. Retry https://www.linkedin.com/in/morganjingram logged out; if it now serves his own profile, harvest the embedded recent post permalinks.
3. Check https://blog.hubspot.com/sales for new "Master in Sales" columns under his byline and add 2-4 verbatim excerpts per column, labelled editor-touched.
4. Caption one of his own YouTube videos or a long podcast appearance with `yt-dlp --write-auto-sub --skip-download --sub-lang en "<url>"`; add 3-5 documented (ASR) excerpts under a new labelled section and replace the inferred spoken-register stat with a sampled one.
5. If an authenticated X session is available, pull the full 2024-08-08 voice-note thread and replace item 28's opener with the complete text, noting the change; check whether ampup.live/email has grown a public archive.
6. Re-verify that every URL is still live. Never carry a quote forward that was not re-read at its source.

## Pattern notes

### 1. Label, colon, tactic
Posts open with a capitalized label and a colon ("COLD CALLING TIP:", "Prospecting Tip:") or a struggle question, then state one tactic in one line. The LinkedIn Content Expert writes this label line first.

### 2. The staged objection
He voices the reader's pushback in their own words, often with an emoji ("'Yeah.. but I'm just an SDR' 😳", "Hold up Morgan.. I don't have time for practice.."), then flips it with a flat "Yes" or "It works." The Objection Handling Expert uses the same move for rep objections and PAQ for prospect objections.

### 3. Named frameworks with exact timings
Every tactic becomes a short acronym or numeric pattern with seconds attached (PLA, PAQ, 10-30-10, wait 1.5 seconds, 50-second videos). The Cold Outreach Writer refuses to leave a step untimed.

### 4. Self-sourced numbers as proof
Confidence arrives as a number he measured ("almost 76% of the time," "5-10 personalized videos a year," "20-30 meetings per month") framed as "I am only reporting the data." Every playbook marks unverified figures [VERIFY] because the register depends on the test being real.

### 5. Friction removal
Voicemails tell the prospect not to call back, the nudge is one line, the CTA is interest-based, and the video sells the meeting, not the solution. The No-Reply Follow-Up Expert diagnoses friction before adding touches.

### 6. The failure credential and the question to the room
First-person stumbles (the airport rejection, the shaking first video, the missed quota) are told in short lines and converted into effort; nearly every post ends on a question ("What would you add? 👇🏾"). The LinkedIn Content Expert closes every post with the question and requires the stumble to be the user's own.
