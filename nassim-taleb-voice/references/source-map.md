# Nassim Nicholas Taleb Voice Source Map

Research date: 2026-10-18
Refresh cadence: every 6 months (next: 2027-04)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| INCERTO publication on Medium, full-text RSS feed | https://medium.com/feed/incerto | 10 full essays 2020-2024 authored by Taleb ("How I write", "The Masks Masquerade", "No, Covid 19 is not an old person problem", "Safe Heaven", "Bitcoin is the Detector of Imbeciles", "On Christianity", "A Few Things We Don't Quite Get About the Levant", others) | Open via RSS; Medium HTML returns 403 to fetchers |
| "How I write" (Medium, Oct 30 2022) | https://medium.com/incerto/how-i-write-8b495eae0330 | His own stated writing rules: idiosyncrasy, refusing editors, the postcard rule | Open via RSS |
| "The Masks Masquerade" (Medium, Jun 14 2020) | https://medium.com/incerto/the-masks-masquerade-7de897b517b7 | The numbered-error polemic form; class insults; terse imperative close | Open via RSS |
| "No, Covid 19 is not an old person problem" (Medium, Nov 29 2021) | https://medium.com/incerto/no-covid-19-is-not-an-old-person-problem-6968f720d153 | Extend-the-absurdity move; intergenerational argument | Open via RSS |
| "Safe Heaven" (foreword to Mark Spitznagel's Safe Haven; Medium, May 6 2021) | https://medium.com/incerto/safe-heaven-e76392796ef5 | Heroic-persistence register; mirrored asymmetry aphorisms | Open via RSS |
| "Bitcoin is the Detector of Imbeciles" (L'Express interview, translated, republished by Taleb; Medium, Jan 4 2023) | https://medium.com/incerto/bitcoin-is-the-detector-of-imbeciles-e5cc5eeccdbf | Spoken register in translation | Open via RSS; DOCUMENTED |
| EconTalk, "Nassim Nicholas Taleb on the Nations, States, and Scale" (Jul 11 2022; his most recent of ten EconTalk episodes) | https://www.econtalk.org/nassim-nicholas-taleb-on-the-nations-states-and-scale/ (MP3 via https://feeds.simplecast.com/wgl4xEgL) | English spoken register, minutes 1-41: city states, scale and non-linearity, skin in the game for local rulers, Russia vs Venice; items 101-110 | Open RSS MP3; DOCUMENTED (MAI-Transcribe-2 diarized ASR via OpenRouter, $0.067) |
| fooledbyrandomness.com Notebook ("Opacity") | https://fooledbyrandomness.com/notebook.htm | ~165 numbered aphoristic entries, undated; every quote grep-verified against the raw page | Open |
| fooledbyrandomness.com "Reviewing the Reviewers" | https://fooledbyrandomness.com/Reviewers.html | Skin in the game applied to critics | Open |
| fooledbyrandomness.com home | https://fooledbyrandomness.com/ | Index of essays; Technical Incerto (arXiv 2001.10488) | Open |
| X @nntaleb | https://x.com/nntaleb | Daily one-line aphorisms and fights | Not fetchable from this environment (login wall; syndication and mirror endpoints empty) |

## What the corpus rests on

Twenty-five of thirty-one excerpts are verbatim from text Taleb wrote and published on his own channels: five Medium essays read in full through the publication's open RSS feed, and his personal site's notebook and reviewers pages, with every notebook quote confirmed by grep against the raw HTML. Three excerpts are a translated interview he republished himself and are labelled documented. Nothing comes from a quote aggregator. The sample spans his two gears (long polemic, short aphorism) and is current through 2024. Confidence in wording is high for the verbatim items and moderate for the translated ones. The 2026-10-19 refresh added items 101-110, documented-grade diarized ASR of one English EconTalk interview (2022).

## Known gaps

- **X was not sampled.** @nntaleb is a major part of his public voice (daily one-liners, public fights). The X syndication endpoint and four mirror sites returned nothing from this environment. A logged-in human can pull 10-20 posts with permalinks in minutes; add them as a "Short-form (X)" section.
- **The Bed of Procrustes aphorisms were not sampled.** No author- or publisher-posted public excerpt page was located; aggregator quote sites were excluded by rule. Do not quote the book from memory as verbatim.
- **Book text (Fooled by Randomness, The Black Swan, Antifragile, Skin in the Game) was not sampled** beyond what he restates in the essays. Famous book lines must not be quoted as verbatim from memory.
- **Four fetched essays were not excerpted.** "On Christianity", "A Few Things We Don't Quite Get About the Levant", "Maestro Bogomolny", and "Religion, Violence, Tolerance" were pulled in full text at research time and are available for cultural and historical register samples.
- **English spoken sample is one interview.** Items 101-110 are ASR of one 2022 EconTalk episode with a friendly host, so his explanatory spoken register (run-on turns, "okay?" and "you see?" check-ins, parables) is now covered. Still missing: his combative spoken register (Bloomberg, X Spaces, debates), anything 2023-2026 spoken (EconTalk's last Taleb episode is 2022), and a second interview to confirm the tics.
- **Anything published after 2026-10-18 is unsampled.**

## Refresh instructions

1. Re-fetch https://medium.com/feed/incerto; add 5-10 verbatim excerpts from new essays with URLs and dates, continuing the item numbering.
2. If a logged-in export of @nntaleb is available, add a "Short-form (X)" section of 10-20 one-liners with permalinks; this is the highest-value addition.
3. Re-grep fooledbyrandomness.com/notebook.htm for any new entries (the page is undated; compare entry count).
4. Add a second English spoken sample, ideally a 2023-2026 or adversarial interview, from an RSS MP3 (EconTalk feed https://feeds.simplecast.com/wgl4xEgL has ten Taleb episodes, 2007-2022): `python3 scripts/voice-dna/transcribe.py "<mp3-url>" --out /private/tmp/claude-501/stt/nassim-taleb --start-min 2 --max-min 45 --budget 0.15`, identify his speaker label per 20-minute chunk, and add 6-10 documented excerpts continuing from item 111.
5. Re-verify that every URL is still live. Never carry a quote forward that was not re-read at its source.

## Pattern notes

### 1. Stand it on its head
The thesis is an inversion of the received view, stated bluntly ("No, no; it's the exact opposite"). The Contrarian Take Generator opens here.

### 2. Mirrored asymmetry
Aphorisms are two parallel clauses with the second carrying extra weight. The Hook Creator builds every line this way.

### 3. Class, not person
Insults name categories (bureaucrats, hacks, "evidence based" scientists), never private individuals. The skill enforces this as a guardrail.

### 4. Numbered errors with a calculation
Polemics enumerate the opponent's errors and attach a small checkable number to each, then close on an imperative.

### 5. Via negativa
Negative advice (what not to do) outranks positive advice; the sucker problem is preferring the latter. The skill converts recommendations accordingly.

### 6. Idiosyncrasy as policy
He refuses editing, keeps typos, writes postcard-length emails, and says literature "must be idiosyncratic." The skill leaves one deliberate roughness rather than polishing flat.
