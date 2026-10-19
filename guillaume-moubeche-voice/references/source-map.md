# Guillaume Moubeche Voice Source Map

Research date: 2026-10-19
Refresh cadence: every 6 months (next: 2027-04)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| X @GuillaumeMbh timeline | https://syndication.twitter.com/srv/timeline-profile/screen-name/GuillaumeMbh | 99 posts with full text and dates in the embedded `__NEXT_DATA__` JSON; mostly Jan-Jun 2022 daily aphorisms, the Oct 2021 $10M milestone, Aug 2023 threads, one 2025 post | Rate-limits (429, 20-byte body) after 1-2 hits per handle; a retry with a Linux UA worked. Raw JSON saved at research time |
| lempire blog, "$0 to $10,000,000 in ARR bootstrapped" (26 Oct 2021) | https://web.archive.org/web/20211205163606/https://blog.lempire.co/0-to-10m-in-arr-bootstrapped/ | 15-minute bylined essay: founding scene, the "Note:" disclaimer, growth circle of love, founders clash | Wayback only (live blog.lempire.com is gone) |
| lempire blog, "$6m ARR in 3 years bootstrapped" (12 Apr 2021) | https://web.archive.org/web/20220331200339/https://blog.lempire.com/6-million-dollars-arr-in-3-years-bootstrapped/ | 10-minute essay: multiple acquisition channels, #CheapFrenchBastard, "to master something, teach it" | Wayback |
| lempire blog, "0 to $4m ARR in less than 3 years" (1 Jan 2021) | https://web.archive.org/web/20221125202139/https://blog.lempire.com/0-to-4m-arr-in-3-years-bootstrapped/ | 13-minute essay: lemlist family, "Communities die, families prosper." | Wayback |
| lempire blog, "From $0 to $150M valuation in 3.5 years" (30 Nov 2021) | https://web.archive.org/web/20220222134909/https://blog.lempire.com/from-0-to-150m-valuation-in-3-5-years/ | 8-minute essay: no loans, no investors, the $30M round declined, profitable from day 1 | Wayback |
| lempire blog, "From 0 to exit in 18 months with a side project" (29 Sep 2020) | https://web.archive.org/web/20240221075035/https://blog.lempire.com/from-0-to-exit-in-18-months/ | 12-minute essay on the lempod sale; read for register, not excerpted | Wayback |
| Indie Hackers, "From $0 to $22M ARR in 5 years. Here's a peek at Guillaume Moubeche's finances." (July 2023) | https://www.indiehackers.com/post/from-0-to-22m-arr-in-5-years-heres-a-peek-at-guillaume-moubeche-s-finances-d24f03e880 | Written Q&A by James Fleischmann; his typed answers labelled "Guillaume:"; DOCUMENTED (publisher-formatted) | Live page is a Cloudflare challenge; the Wayback copy (20250905223837) opens |
| LinkedIn (profit-led-growth / guillaumemoubeche-a026541b2) | https://www.linkedin.com/posts/profit-led-growth_when-i-started-lemlist-in-2018-i-had-very-activity-7118516870697086976-cr3v | Should be his main short-form channel | BLOCKED: every permalink serves the login page, both profile handles authwall; third-party pages report the profile was banned. Not sampled |
| Book The $150M Secret (2022) and guillaume-moubeche.com newsletter | https://guillaume-moubeche.com/ | Book and newsletter register | BLOCKED: 502 / connection reset; no 2025 Wayback snapshot. Not sampled |
| Podcast: Bootstrapping to $45M ARR: Guillaume Moubeche on scaling efficiently without any VC trade-offs, Making The Grade, 2026-04-02 | https://podcasts.apple.com/us/podcast/bootstrapping-to-%2445m-arr-guillaume-moubeche-on-scaling/id1827033461?i=1000758773865 (MP3: https://cdn.simplecast.com/media/audio/transcoded/28d7c161-abf2-443d-aae1-c100575b06f2/cabf3285-350b-4a94-b15d-8c83e2d25729/episodes/audio/group/86c3843e-a019-4af8-b711-18576076a35c/group-item/6a9778df-5bd6-4598-bf7d-d3e6c4bdca51/128_default_tc.mp3) | Spoken register in English: 45 transcribed minutes (00:02 to 00:47) of a guest interview on bootstrapping, hiring, ads, and outbound (the ASR renders the host's name for him as "Graham"); items 101-110, documented-grade | Open RSS enclosure; transcribed with MAI-Transcribe-2 via OpenRouter (diarized; speaker identified per 20-minute chunk from context) |

## What the corpus rests on

Twenty-five of twenty-seven excerpts are verbatim from channels he writes himself: fifteen from his own X account (2021-2023), read from the syndication timeline's embedded JSON with emoji and non-native phrasing intact, and ten from five bylined founder essays on the lempire blog (2020-2021), read from Wayback captures. Two are documented-grade: his typed answers in a written Indie Hackers Q&A, publisher-formatted. Nothing comes from a quote aggregator. The short-form and long-form written registers are both covered, but the short-form sample is X, not LinkedIn, which the roster treats as his native channel; he states in the $10M essay that he posted on LinkedIn and Twitter in parallel, so the register is believed to transfer, but no LinkedIn text was read. No spoken sample exists. Confidence in wording is high for items 1-25 and moderate for 26-27; confidence that the X register equals his LinkedIn register is moderate and unverified. Added 2026-10-19: items 101-110 are documented-grade spoken excerpts from one 2026 English podcast interview (machine transcript); the written counts above are unchanged.

## Known gaps

- **LinkedIn was not sampled.** All post permalinks are login-walled and both profile handles authwall; third-party sources report the profile was banned. The LinkedIn Content Expert playbook is inferred from X. Never quote a LinkedIn post of his, and flag LinkedIn-specific output as inferred-register when precision matters.
- **No book or newsletter text.** The $150M Secret and guillaume-moubeche.com were unreachable (502) with no Wayback snapshot; do not quote either.
- **Spoken sample is one English episode.** Items 101-110 come from one April 2026 interview (45 transcribed minutes, machine transcript, documented-grade). One episode is thin: his other English appearances and his YouTube vlog are unsampled, and his French-language interviews are out of scope for this English-only skill.
- **The X sample is the syndication endpoint's curated 99 posts**, weighted to Jan-Jun 2022 daily posting and Aug 2023 threads; 2024-2026 is nearly absent (one Feb 2025 post on negotiation leverage). His current register may have shifted.
- **The lempod exit essay was read but not excerpted**; the side-project and exit register is thin in the corpus.
- **Indie Hackers items are publisher-formatted.** The words are his typed answers, but paragraphing is the interviewer's; label them documented.
- **Anything published after 2026-10-19 is unsampled.**

## Refresh instructions

1. Retry LinkedIn with an authenticated session or a desktop UA against `https://www.linkedin.com/in/guillaumemoubeche-a026541b2` and the `profit-led-growth` post permalinks; if any render, add 8-12 verbatim LinkedIn posts as a new labelled section and promote the LinkedIn Content Expert playbook from inferred to sampled in SKILL.md Guardrails.
2. Pull the X syndication timeline again (`curl -A "Mozilla/5.0 (X11; Linux x86_64)" https://syndication.twitter.com/srv/timeline-profile/screen-name/GuillaumeMbh`, parse `__NEXT_DATA__`) and add 5-8 posts from 2024-2026; fetch single posts via `https://cdn.syndication.twimg.com/tweet-result?id=<id>&token=a` if the timeline is thin.
3. Check `https://guillaume-moubeche.com/` and `https://web.archive.org/web/2026*/guillaume-moubeche.com*`; if the newsletter or a book sample is live, add 3-5 verbatim excerpts as a labelled section.
4. Caption one English podcast appearance or his own YouTube channel with `yt-dlp --write-auto-sub --skip-download --sub-lang en "<url>"`; add 3-5 documented excerpts and fill the spoken-register stat.
5. Re-read the lempod exit essay (Wayback 20240221075035) and add 2-3 verbatim excerpts if the Ghostwriter playbook needs the side-project register.
6. For the spoken register, pick a long-form episode with a direct MP3 in its RSS feed (find it with `curl -s "https://itunes.apple.com/search?term=<name>&entity=podcastEpisode&limit=25"`, field `episodeUrl`; no YouTube), then run `python3 /Users/johnpeslar/dev/john-peslar-ai-skills/scripts/voice-dna/transcribe.py "<mp3-url>" --out /private/tmp/claude-501/stt/guillaume-moubeche --start-min 2 --max-min 45 --budget 0.15` with `OPENROUTER_API_KEY` exported (about $0.10 per 60 minutes). Speaker numbers reset per chunk, so identify his label in each chunk from context, then add 6-10 documented excerpts to the spoken section, continuing from the highest item number. Use English-language episodes only (Sales Players, January 2024, is a second candidate).
7. Re-verify that every URL is still live or still archived. Never carry a quote forward that was not re-read at its source.

## Pattern notes

### 1. Milestone arithmetic
Nearly every opener is a before/after number pair with the time span and the funding status ("$1000" to "$10M in ARR", "6 people ... $1M / 34 people ... $10M", "21 months ... 1 month"). The Build-in-Public Writer will not start without the user's own pair.

### 2. The two-line contrast joke
Funded party vs bootstrapper, or $10 client vs $100,000 client, in two parallel lines with the punchline on the second and mild profanity only there. The LinkedIn Content Expert uses it as one of four short-post forms.

### 3. French self-deprecation beside the biggest number
"#CheapFrenchBastard", the $5 Uniqlo t-shirt, "what the fuck is this french guy talking about" sit next to $10M and $150M. Every playbook places one self-own near the largest figure and requires the user's own trait, not his.

### 4. Parallel lines with one variable
Year-by-year reactions, planner vs doer, easy vs hard, repeated with one word changed per line. The LinkedIn Content Expert builds its body from this; the Ghostwriter uses "1-" numbered sections the same way.

### 5. Growth is love, family not community
Named coinages (growth circle of love, lemlist family, "Communities die, families prosper.") carry the stance that passion and customer obsession beat hacks. The Ghostwriter keeps one stance paragraph and credits the coinages.

### 6. The disclaimer and the moral
Essays carry a "Note:" that the lessons are his own and not a recipe; posts close on a one-line imperative with a heart or rocket ("Ignore the doubters", "Be patient ..."). The Ghostwriter inserts the note near the top; the short-form playbooks end on the moral.
