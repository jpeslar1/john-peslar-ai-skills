# Peter Thiel Voice Source Map

Research date: 2026-10-18
Refresh cadence: every 6 months (next: 2027-04)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| "The Education of a Libertarian" (Cato Unbound, Apr 13 2009, with editor-appended follow-up remarks) | https://www.cato-unbound.org/2009/04/13/peter-thiel/education-libertarian/ | Confessional-political essay; freedom vs democracy inversion; "escape from politics"; race between politics and technology | Open |
| "The Optimistic Thought Experiment" (Policy Review / Hoover, Jan 29 2008) | https://www.hoover.org/research/optimistic-thought-experiment | Long essay on globalization, bubbles, and apocalypse; Luke 17 epigraph; news vs business sections | Open |
| "The Straussian Moment" (in Politics and Apocalypse, Michigan State UP, 2007) | https://gwern.net/doc/philosophy/religion/2007-thiel-thestraussianmoment.pdf | 30-page philosophical essay (Schmitt, Strauss, Girard, 9/11); the longest-form register | Open PDF mirror |
| "The End of the Future" (National Review, Oct 3 2011) | https://www.nationalreview.com/2011/10/end-future-peter-thiel/ | The stagnation thesis in full: travel speed, energy, Woodstock line, "clean tech" | Live page bot-walled (403); read via Wayback https://web.archive.org/web/2020/https://www.nationalreview.com/2011/10/end-future-peter-thiel/ |
| "Competition Is for Losers" (WSJ, Sep 12 2014, adapted from Zero to One) | https://www.wsj.com/articles/peter-thiel-competition-is-for-losers-1410535536 | The business register: monopoly vs competition, Tolstoy inversion, "What valuable company is nobody building?" | Paywalled; read via Wayback https://web.archive.org/web/2015/https://www.wsj.com/articles/peter-thiel-competition-is-for-losers-1410535536 |
| "Against Edenism" (First Things, Jun/Jul 2015) | https://www.firstthings.com/article/2015/06/against-edenism | Theology meets technology; Faust, Malthus, Revelation; "Technology means doing more with less" | Open |
| "Back to the Future" (First Things, Mar 2020, review of Douthat's The Decadent Society) | https://www.firstthings.com/web-exclusives/2020/03/back-to-the-future | 707 vs 737 MAX opener; "radical progress begins with moderation"; the good-aliens parenthetical | Open |
| Blake Masters, CS183 Class 1 notes (Stanford, Apr 2012) | https://blakemasters.tumblr.com/post/20400301508/cs183class1 | 0 to 1 vs 1 to n; "retail sanity, wholesale madness" | Open; DOCUMENTED (student notes, not Thiel's words) |
| Uncommon Knowledge, "Apocalypse Now? Peter Thiel on Ancient Prophecies and Modern Tech" (Hoover Institution, host Peter Robinson, Nov 18 2024; part 1 of 2) | https://uncommonknowledgehoover.podbean.com/e/apocalypse-now-peter-thiel-on-ancient-prophecies-and-modern-tech-uncommon-knowledge-peter-robinson-hoover-institution/ (MP3: https://mcdn.podbean.com/mf/web/y3itknq4t4nr78rw/20241118-UK-Peter-Thiel.mp3) | Interview register, minutes 1-41: Girard and the apocalypse, 1945, AI and existential risk, stagnation, the katechon; items 101-110 | Open RSS MP3 (https://feed.podbean.com/uncommonknowledgehoover/feed.xml); DOCUMENTED (MAI-Transcribe-2 diarized ASR via OpenRouter, $0.067) |
| "Peter Thiel \| Cambridge Union" talk and Q&A (YouTube, uploaded 2024) | https://www.youtube.com/watch?v=bNewfkhhwMo | ~43 min spoken register: stagnation, science as technology's older sibling, wokeness as Christian heresy | Open video; DOCUMENTED (YouTube ASR captions, saved locally at research time) |

## What the corpus rests on

Twenty-eight of thirty-three excerpts are verbatim from seven essays Thiel wrote himself, spanning 2007 to 2020 and five outlets (Cato Unbound, Hoover, a university-press anthology, National Review, WSJ, First Things). Two paywalled or bot-walled pieces were read from Wayback Machine captures of the original articles; the text is his, the access path is archival. Five excerpts are documented-grade (student notes and ASR captions) and are labelled as such in the corpus. Nothing comes from a quote aggregator. Confidence in wording is high for items 1-28 and moderate for 29-33. The 2026-10-19 refresh added items 101-110, documented-grade diarized ASR of one 2024 Uncommon Knowledge interview.

## Known gaps

- **No social channel exists.** Thiel has no active public X or LinkedIn presence. The short-form register in SKILL.md is derived from the WSJ book excerpt, not from posts.
- **Zero to One was sampled only through the WSJ excerpt.** The book's preface, the "contrarian question" chapter, and other widely quoted lines were not fetched from a primary copy. Do not quote them as verbatim from memory.
- **Two live pages are not fetchable without a subscription or a browser.** National Review (Cloudflare wall) and WSJ (paywall) were read via Wayback. A human with access can confirm on the live page.
- **Recent essays not fetched.** The Free Press essay "A Time for Truth and Reconciliation" (2025) and the 2024 First Things pieces ("The Pope and the Antichrist", "Voyages to the End of the World") would add his most recent register. The first fetch attempt used a wrong slug and was not retried.
- **Spoken sample is one talk plus one interview, both ASR.** The Cambridge Union talk (items 31-33) covers his lecture register; items 101-110 (Uncommon Knowledge, Nov 2024) now cover his interview register (the "Well, that's very overdetermined" opener, deadpan asides, "or something like this" tags). Still missing: an official human transcript of any talk, part 2 of the Uncommon Knowledge conversation (Dec 2024), a 2025-2026 interview (Ross Douthat's Interesting Times, Conversations with Tyler), and the Oxford Union talk ("Anti-Anti-Anti-Anti Classical Liberalism", 2023).
- **Anything published after 2026-10-18 is unsampled.**

## Refresh instructions

1. Fetch the First Things and Free Press essays listed under Known gaps; add 5-10 verbatim excerpts with URLs and extend the Verbatim section numbering.
2. Add a 2025-2026 interview from an RSS MP3 (Interesting Times https://feeds.simplecast.com/bS1LZG8m, Conversations with Tyler https://rss.libsyn.com/shows/137081/destinations/850607.xml, or Uncommon Knowledge part 2): `python3 scripts/voice-dna/transcribe.py "<mp3-url>" --out /private/tmp/claude-501/stt/peter-thiel --start-min 2 --max-min 45 --budget 0.15`, identify his speaker label per 20-minute chunk, and add 6-10 documented excerpts continuing from item 111. YouTube captions (yt-dlp) are rate-limited from this Mac; prefer RSS.
3. Re-verify that every open URL is still live. For the Wayback-read pieces, confirm the capture still resolves. Never carry a quote forward that was not re-read at its source.
4. If a primary copy of Zero to One chapter text becomes publicly available (publisher excerpt, author-posted), add it; until then keep the book out of the verbatim section.

## Pattern notes

### 1. Inversion of a commonplace
The thesis sentence reverses the sign of a consensus he has just described fairly ("I no longer believe that freedom and democracy are compatible"; "Business is the opposite"). The Contrarian Take Generator enforces the fair statement before the flip.

### 2. Grand claim, dated receipt
Civilizational openers are paid for within two sentences by a year, a speed, or a named event (977 km/h in 1958; Woodstock three weeks after the moon landing). The skill treats an unpaid abstraction as an error.

### 3. The literal test
"Consider the most literal instance of non-acceleration: We are no longer moving faster." Vague progress claims are tested against their most measurable instance.

### 4. Parenthetical knife
Humor is deadpan, bracketed, and placed at the end of a serious sentence. One or two per essay.

### 5. Both ends are apathy
Extreme optimism and fatalistic pessimism are shown to converge on inaction; the narrow third path (definite optimism, moderation) is proposed. This is the structural turn before his conclusions.

### 6. Theology and finance in one clause
Apocalyptic and scriptural vocabulary is applied literally to markets and technology. The skill keeps this register available but requires the user to be able to stand behind any canonical anchor used.
