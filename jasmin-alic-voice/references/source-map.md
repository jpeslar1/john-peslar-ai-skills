# Jasmin Alic Voice Source Map

Research date: 2026-10-19
Refresh cadence: every 6 months (next: 2027-04)

Identity note: LinkedIn handle is `alicjasmin` (not `jasminalic`); display name "Jasmin Alić"; signs as "Coach J" or "Jay"; site is hey-jay.com (heyjay.co and jasminalic.com are empty shells); community is Link Up (linkupbyjasmin.com).

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| LinkedIn profile (logged out) | https://www.linkedin.com/in/alicjasmin | Leaks ~3 recent own-post permalinks plus ~10 posts by others mentioning him | Renders with a desktop UA (200, 548 KB). `grep -oE 'linkedin\.com/posts/alicjasmin_[^"?&]+'` |
| LinkedIn post permalinks (15 posts, Nov 2022 to Oct 2026) | e.g. https://www.linkedin.com/posts/alicjasmin_my-linkedin-strategy-hasnt-changed-in-5-activity-7516082879920111617-ckSd | Full post text in `<meta name="description">` and the attributed-text block; `datePublished` in JSON-LD (date also equals activity ID >> 22 as ms epoch); 27 verbatim excerpts | Open with a desktop UA. Found via WebSearch `"Jasmin Alić on LinkedIn" <topic>` (the diacritic and the "on LinkedIn" title phrase surface post pages; `site:` operators do not) |
| hey-jay.com/resources ("My best LinkedIn posts. All in one place.") | https://www.hey-jay.com/resources | ~9,800 words of his own Jan-Mar 2023 LinkedIn posts republished on his Squarespace site, dated; 3 verbatim excerpts | Open; plain HTML |
| PDF: "1-Minute Commenting Course" | https://www.hey-jay.com/s/Learn-How-to-Comment-Better-In-60-Seconds-Hey-Jay.pdf | His commenting playbook as a 454-word carousel; 1 verbatim excerpt (slide text flattened) | Open; `pdftotext -layout` |
| PDF: "LinkedIn's #1 Copywriting Hack" (Dear son / Love, Dad) | https://www.hey-jay.com/s/LinkedIns-1-Copywriting-Hack.pdf | His signature copy technique as a 240-word carousel; 1 verbatim excerpt | Open; `pdftotext -layout` |
| Podcast appearances (not fetched) | Kickoff Sessions #228 https://www.buzzsprout.com/1499203/episodes/15348999 ; The Futur https://www.thefutur.com/content/2025-linkedin-strategies-that-create-real-growth-w-jasmin-alic ; Real Business Connections https://realbusinessconnections.com/podcast/heyjay/ | Spoken register; would be documented (ASR) | Not attempted this round; podscripts.co untested for these shows |
| Podcast: #325 Jasmin Alic - The LinkedIn Content System to Scale to $30,000/Month, Kickoff Sessions, 2026-02-15 | https://podcasts.apple.com/us/podcast/325-jasmin-al%C3%ADc-the-linkedin-content-system-to-scale/id1541531544?i=1000749828689 (MP3: https://www.buzzsprout.com/1499203/episodes/18685654-325-jasmin-alic-the-linkedin-content-system-to-scale-to-30-000-month.mp3) | Spoken register: 45 transcribed minutes (00:02 to 00:47) of a guest interview on AI writing, commenting, profile CTAs, his paid community, and Linkbound; items 101-109, documented-grade | Open RSS enclosure; transcribed with MAI-Transcribe-2 via OpenRouter (diarized; speaker identified per 20-minute chunk from context) |

## What the corpus rests on

All thirty-two excerpts are verbatim from channels he writes himself: twenty-seven from fifteen of his own LinkedIn post permalinks (November 2022 to October 2026), read from the logged-out permalink pages with arrows, scare quotes, and emoji intact; three from early-2023 LinkedIn posts he republished on hey-jay.com; and two from self-published PDF carousels on the same site. Nothing is documented-grade and nothing comes from a quote aggregator. The LinkedIn register, which is his native and only sampled channel, is covered across four years, with the 2023 archive and two October 2026 posts as the anchors. No spoken sample exists. Confidence in wording is high for all 32 items; confidence that the sample reflects his 2024 to mid-2025 output is moderate, because that stretch is thin. Added 2026-10-19: items 101-109 are documented-grade spoken excerpts from one 2026 podcast interview (machine transcript); the written counts above are unchanged.

## Known gaps

- **Spoken sample is one episode.** Items 101-109 come from one February 2026 Kickoff Sessions interview (#325; 45 transcribed minutes, machine transcript, documented-grade). One episode is thin: the three appearances listed above (#228, The Futur, Real Business Connections) are still untranscribed, and solo or live-video speech is unsampled.
- **2024 and most of 2025-2026 are thin.** WebSearch surfaces older indexed posts and the logged-out profile leaks only the three most recent, so the bulk of permalinks are 2023 plus two October 2026 posts. Habits that changed in between (for example the "Coach J" sign-off, first seen from 2025) are dated from the sample, not from a complete archive.
- **Larger carousels were not retrieved.** The "27 proven writing tips" 34-page document and other LinkedIn document posts do not expose slide text in the permalink meta; only the two PDFs hosted on hey-jay.com were read.
- **Link Up community content and his newsletter were not fetched.** The community and email registers are unsampled.
- **His self-reported stats are unverified.** The -20% and -30% hook figures, 2M views a month, and 380,000 followers are his own disclosures, carried as his claims; nothing here independently checks them.
- **Anything published after 2026-10-19 is unsampled.**

## Refresh instructions

1. Re-fetch `https://www.linkedin.com/in/alicjasmin` with a desktop UA, grep the three newest `alicjasmin_` permalinks, and read each permalink's `<meta name="description">` and JSON-LD `datePublished`; add 5-8 verbatim posts and continue the LinkedIn section numbering.
2. Run WebSearch for `"Jasmin Alić on LinkedIn" 2025` and `"Jasmin Alić on LinkedIn" 2026` to fill the thin years; add 4-6 posts from 2024-2025 so the register is continuous.
3. Caption one podcast appearance with `yt-dlp --write-auto-sub --skip-download --sub-lang en "<url>"` (The Futur episode is the most likely to have a video), or check podscripts.co for Kickoff Sessions #228; add 3-5 documented excerpts under a labelled "Documented excerpts (podcast ASR)" heading and fill the spoken-register stat.
4. Check `https://www.hey-jay.com/resources` for new republished posts and `https://www.hey-jay.com/s/` for new PDFs; add 2-4 verbatim excerpts from any new carousel.
5. If a newsletter signup or archive appears on hey-jay.com or linkupbyjasmin.com, add 2-3 verbatim excerpts as a labelled newsletter section and note whether the Ghostwriter playbook needs an email register.
6. For the spoken register, pick a long-form episode with a direct MP3 in its RSS feed (find it with `curl -s "https://itunes.apple.com/search?term=<name>&entity=podcastEpisode&limit=25"`, field `episodeUrl`; no YouTube), then run `python3 /Users/johnpeslar/dev/john-peslar-ai-skills/scripts/voice-dna/transcribe.py "<mp3-url>" --out /private/tmp/claude-501/stt/jasmin-alic --start-min 2 --max-min 45 --budget 0.15` with `OPENROUTER_API_KEY` exported (about $0.10 per 60 minutes). Speaker numbers reset per chunk, so identify his label in each chunk from context, then add 6-10 documented excerpts to the spoken section, continuing from the highest item number. The Futur episodes (January 2024, December 2024, September 2025) are the next candidates and have RSS MP3s.
7. Re-verify that every URL is still live. Never carry a quote forward that was not re-read at its source.

## Pattern notes

### 1. The fixed post skeleton
One-line hook under 45 characters, a parenthetical second line, a numbered list of one-liners with ↳ examples, a quotable power ending, a repost ask in parentheses, and a one-question P.S. The LinkedIn Content Expert template is this skeleton unchanged.

### 2. Demonstrate the device inside the post
The re-hook post is a re-hook, the pull-quote post is built of pull-quotes, and "(see what I did in this entire post)" names the trick live. The Hook Creator produces one of each named form and the Ghostwriter annotates the technique it uses.

### 3. Dear son, Love Dad
Write the whole piece to one beloved person, then delete the salutation and sign-off; "To whom it may concern" is the failure. The Ghostwriter uses it as the drafting instruction and the Hook Creator as the final test on every line.

### 4. Scare quotes, arrows, and one word in caps
Ordinary words land in quotes ("stay" consistent, the "sauce"), → replaces "then", ↳ indents the example, and one word per post goes to caps. Every playbook caps scare quotes at one per line and emoji at two per post.

### 5. Own-stat with a disclosure line
Percentages and counts are his own and carry "(Those are my stats based on my own 500+ posts)". The playbooks require the user's own numbers with the same disclosure and flag borrowed figures [VERIFY].

### 6. Kindness as the strategy
Comments and DMs over the algorithm, give everything away, support new voices, never cold DM, never negativity in the feed. The emotional-register fix in SKILL.md adds the gift and the "Cheers!" whenever a draft reads cold, and the anti-patterns exclude cold outreach entirely.
