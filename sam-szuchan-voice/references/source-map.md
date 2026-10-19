# Sam Szuchan Voice Source Map

Research date: 2026-10-19
Refresh cadence: every 6 months (next: 2027-04)

Two registers are documented. The 2026 register (structural mini-essays and szuchan.com essays) is the default for every playbook. The 2022-2023 register (LinkedIn hook-craft and growth posts) is a labelled secondary mode used only inside the Hook Creator playbook. Corpus items carry the era in their section headings.

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| LinkedIn profile (logged out), handle samuel-szuchan | https://www.linkedin.com/in/samuel-szuchan/ | Leaks 9 recent own-post permalinks (2026-04-22 to 2026-05-07) plus ~20 posts by others. | Renders with a desktop UA (HTTP 200, ~706 KB). Extract with `grep -oE 'linkedin\.com/posts/samuel-szuchan_[^"?&]+'`. |
| LinkedIn post permalinks (20) | e.g. https://www.linkedin.com/posts/samuel-szuchan_john-kerry-and-dick-cheney-said-the-exact-activity-7458116268848631809-gdoB | Full text in description meta and attributed-text segments; datePublished; date = activity ID >> 22. Nine 2026 mini-essays (current register) and eleven 2022-2023 growth posts (secondary register). Verbatim. | Open with a desktop UA. Older posts found via WebSearch `"Sam Szuchan on LinkedIn" <topic>`. |
| szuchan.com essays | https://szuchan.com/essays/ and https://szuchan.com/rss.xml | 16 essays 2025-11 to 2026-10-14 (7-31 minute reads); 3 fetched in full (Elon, When Paradigms Die, Anthropic writers). Verbatim. | Open static HTML. RSS carries titles, links, and dates only; bodies are 1-2 sentence summaries. |
| szuchan.com about page and manifesto | https://szuchan.com/about/ and https://szuchan.com/manifesto/ | Self-description, the creed lines ("Structure decides before anyone chooses."), a 1,200-word manifesto on Kuhn and Kahneman. Verbatim. | Open. |
| Legacy Substack | https://samszuchan.substack.com/ | Essays 2025-11 to 2026-08 including the "newsletter has moved" note; 3 full posts read. Verbatim. | `/api/v1/posts/<slug>` returns full `body_html`. newsletter.szuchan.com now redirects to szuchan.com and old post slugs 404. |
| X @szuchans | https://x.com/szuchans | One-line aphorisms; 1 fetched. Verbatim. | `cdn.syndication.twimg.com/tweet-result?id=1916117082401575003&token=a`; the timeline endpoint was rate-limited. |
| YouTube: "Sam Szuchan - Linkedin Creator + Influencer", Assembly Marketing, 2024-07-30 | https://www.youtube.com/watch?v=S7A8m79fDu4 | 338-word spoken intro: origin story, Justin Welsh influence, zero-likes start. DOCUMENTED (auto-captions). | Captured by a prior run with yt-dlp auto-subs (local file S7A8m79fDu4.en.vtt). |
| samszuchan.com (roster URL) | https://samszuchan.com | Nothing; a parked Namecheap domain. | Do not cite. His site is szuchan.com. |
| Podcast: 20. Embracing Remote Work and Navigating the Waves of AI with Sam Szuchan, The Estee Show, 2024-03-27 | https://podcasts.apple.com/us/podcast/20-embracing-remote-work-and-navigating-the-waves-of/id1678657399?i=1000650426575 (MP3: https://traffic.libsyn.com/secure/6c2fd474-c72a-4987-9105-1097f14588f1/LANDR-samesteev2-Balanced-Medium.mp3) | Spoken register: 24 transcribed minutes (00:01 to the end) of a guest interview on remote work, AI, ghostwriting, and opinionated content; items 101-110, documented-grade; 2024, between the two written eras | Open RSS enclosure; transcribed with MAI-Transcribe-2 via OpenRouter (diarized; speaker identified per 20-minute chunk from context) |

## What the corpus rests on

Thirty-eight of thirty-nine excerpts are verbatim from channels he writes himself. The current register rests on thirty-one items: eighteen from nine LinkedIn mini-essays published 22 April to 7 May 2026, seven from three full szuchan.com essays (March to May 2026, plus one November 2025 essay also carried on the legacy Substack), two from the legacy Substack, three from the szuchan.com about page and manifesto, and one X post. The secondary register rests on seven items from LinkedIn posts between November 2022 and June 2023. One item is a documented-grade ASR caption from a short podcast intro. Nothing comes from a quote aggregator, and he bylines everything himself. Confidence in wording and structure is high for the 2026 LinkedIn and essay items, which are dense and recent; moderate for the 2023 register, which is sampled from post captions only (carousel slides were never exposed); and low for the spoken register, which is one 338-word intro. Added 2026-10-19: the spoken register now also rests on items 101-110 (one 24-minute 2024 interview, machine transcript), so wording confidence there is moderate, but it still says nothing direct about the current era.

## Known gaps

- **Two registers, one default.** The roster DNA ("hook craftsmanship and clean-format LinkedIn growth") describes the 2022-2023 voice; the current voice is structural essays. This skill defaults to the current register and keeps the old one as a labelled secondary mode in the Hook Creator. Do not blend them.
- **X timeline was rate-limited**; only one tweet was captured directly. A second tweet of his survives verbatim inside the Anthropic essay (item 25) because he reproduced it there.
- **LinkedIn coverage has a hole from mid-2023 to early 2026.** The logged-out profile leaks only the latest ~9 posts and search returns older indexed ones, so the transition years (including the ghostwriting-agency period) are unsampled.
- **Only 3 of 16 szuchan.com essays were fetched in full**; the RSS carries one-line summaries. The 31-minute K-pop essay (2026-10-14) was fetched by a prior run but not excerpted.
- **The legacy essay "How I Built 100k Followers in a Year"** (cited by third parties) is gone: newsletter.szuchan.com and szuchan.com/essays/how-i-built-100k-linkedin-followers both 404. Do not quote it from memory.
- **The spoken sample is two 2024 recordings**: a 338-word podcast intro (item 39) and one 24-minute guest interview (items 101-110, machine transcript). Both predate the late-2025 essay register and neither is long; no 2025-2026 speech is sampled, so spoken output in the current register is still inferred.
- **2023 carousel slide text was never captured** (hook templates, Apple and Amazon principles); only post captions exist. Carousel copy in the secondary mode is inferred.
- **Anything published after 2026-10-19 is unsampled.**

## Refresh instructions

1. Re-fetch https://www.linkedin.com/in/samuel-szuchan/ with a desktop UA and extract new permalinks with `grep -oE 'linkedin\.com/posts/samuel-szuchan_[^"?&]+'`; fetch each permalink and add 5-8 verbatim 2026-register excerpts, continuing the numbering in the current-register LinkedIn section. Confirm the register has not shifted again before adding.
2. Pull https://szuchan.com/rss.xml for new essay URLs, fetch 2-3 essays in full (prioritise the K-pop essay of 2026-10-14 and anything newer), and add 4-6 verbatim excerpts to the essays section.
3. Retry the X syndication endpoint per tweet (`https://cdn.syndication.twimg.com/tweet-result?id=<id>&token=a`) using IDs linked from his essays or about page; add 2-4 aphorisms if found.
4. Caption a longer podcast appearance with `yt-dlp --write-auto-sub --skip-download --sub-lang en "<url>"`; add 3-5 documented excerpts and update the spoken-register stats, which currently rest on one 338-word intro.
5. Search for mid-2023 to 2025 LinkedIn posts via WebSearch `"Sam Szuchan on LinkedIn" <topic>` to close the transition-era hole; if found, add them under a dated heading and note whether they belong to the secondary or current register.
6. For the spoken register, pick a long-form episode with a direct MP3 in its RSS feed (find it with `curl -s "https://itunes.apple.com/search?term=<name>&entity=podcastEpisode&limit=25"`, field `episodeUrl`; no YouTube), then run `python3 /Users/johnpeslar/dev/john-peslar-ai-skills/scripts/voice-dna/transcribe.py "<mp3-url>" --out /private/tmp/claude-501/stt/sam-szuchan --start-min 2 --max-min 45 --budget 0.15` with `OPENROUTER_API_KEY` exported (about $0.10 per 60 minutes). Speaker numbers reset per chunk, so identify his label in each chunk from context, then add 6-10 documented excerpts to the spoken section, continuing from the highest item number. Prefer a 2025-2026 recording so the spoken sample matches the current essay register, and label each item's era by its date.
7. Re-verify that every URL is still live, including that samszuchan.com is still parked and szuchan.com is still his. Never carry a quote forward that was not re-read at its source.

## Pattern notes

### 1. The fact that sounds wrong
Every current-register piece opens on a precise, checkable, slightly absurd fact with no preamble ("John Kerry and Dick Cheney said the exact same sentence, two months apart, in 2004."). The Ghostwriter and LinkedIn Content Expert playbooks will not start without the user's own sourced fact, and the Hook Creator's default mode drafts five variants of it.

### 2. Hold both facts, then name the blind spot
Two true contradictory statements are followed by the claim that the reader's framework cannot hold both ("Western analysis struggles with this because it can only hold one of those facts at a time."). The LinkedIn Content Expert template places this in sentences two to four.

### 3. Long sentence, short verdict
A 25-35 word evidence sentence lands on a 2-5 word judgment ("Same data. Different lens." / "It reroutes."). Both writing playbooks require at least two such pairs and forbid line-per-sentence formatting, which belongs to the 2023 register.

### 4. Refuse the cop-out, read the incentive
He names the easy moral label and rejects it in print ("It would be rhetorically pleasing to call these teenagers 'psychopaths.' But this is an analytic cop-out."), then explains the behaviour as a response to a structure someone else installed. The Ghostwriter playbook requires one explicit refusal per essay.

### 5. The quiet re-angle
The final line is a single paragraph that changes the meaning of the piece and gives no advice ("Someone is paid to tell you that." / "The ballet companies, meanwhile, still need to sell tickets."). Every current-register template ends on it and bans CTAs, questions, and takeaways.

### 6. The 2023 hook register, quarantined
The secondary-mode template (problem, "most advice is generic, vague, and ineffective", "So I'm stepping in.", "Check it out below:", the "(Actually)" title device) is sampled from seven 2022-2023 posts and lives only in the Hook Creator playbook, labelled "2023 mode" in output. The Guardrails and Anti-patterns both forbid blending it with the current register.
