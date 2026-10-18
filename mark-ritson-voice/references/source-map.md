# Mark Ritson Voice Source Map

Research date: 2026-10-19
Refresh cadence: every 6 months (next: 2027-04)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| Marketing Week columnist index | https://www.marketingweek.com/mark-ritson/ | ~80 column permalinks, 2019-2025 | Public; links extractable from the HTML |
| Ignore anyone who tells you to forget about targeting (2025-02-19) | https://www.marketingweek.com/ritson-ignore-anyone-targeting/ | The targeting defence; shitfuckery, digital mineshaft, 92% not advertising | Public via curl with a desktop UA, full body |
| Three things make Coca-Cola better at marketing than anyone (2025-03-31) | https://www.marketingweek.com/ritson-coca-cola-better-marketing/ | The column-about-nothing opener; boring excellence register | Public via curl |
| Liquid Death's fame shows how badly marketers neglect product (2024-07-22) | https://www.marketingweek.com/ritson-liquid-death-product/ | Incumbent's-number deflation; midfielders vs Manchester United | Public via curl |
| Are we witnessing the end of the CMO? No, and stop asking (2024-01-19) | https://www.marketingweek.com/ritson-end-cmo-no/ | Unpopular-perspective opener; barista and kombucha; As. We. Know. It. | Public via curl |
| Facebook's Horizon Workrooms sucks ass (2021-08-24) | https://www.marketingweek.com/mark-ritson-facebook-horizon-workrooms-sucks-ass/ | Fad takedown with rhetorical-question volley | Public via curl |
| Three axioms and three questions that summarise all of brand strategy (2021-01-21) | https://www.marketingweek.com/mark-ritson-brand-strategy-marketing/ | His framework piece: First Axiom, diagnosis first, financial-year question | Public via curl |
| Good purpose, bad purpose (2022-01-17) | https://www.marketingweek.com/mark-ritson-good-purpose-bad-purpose/ | Left-footed footballers analogy; purpose dogma critique | Public via curl |
| The seven things marketers need to know in order to answer The Question (2021-07-30) | https://www.marketingweek.com/mark-ritson-answer-question-marketers/ | "The Question" framing | Public via curl |
| Three things you need for a marketing strategy worthy of a brief (2022-07-08) | https://www.marketingweek.com/ritson-strategy-brief-three-questions/ | Casanova analogy; dogshit briefs | Public via curl |
| The cure for impostor syndrome is simpler than you think (2022-06-16) | https://www.marketingweek.com/mark-ritson-impostor-syndrome-cure/ | Flat imperative close | Public via curl |
| Seven reasons why TV's doubters are wrong (2019-08-07) | https://www.marketingweek.com/mark-ritson-seven-reasons-tv-doubters-wrong/ | "Look at the bar chart" register; first six paragraphs only | Paywalled after paragraph 6 ("Please log-in or subscribe"); Wayback is the fallback |
| LinkedIn posts by Mark Ritson (four permalinks) | https://www.linkedin.com/posts/markritson_marketing-activity-7161519116539953153-ZMFS and three others in the corpus | Short-form register; Mini MBA promotion; Distinctiveness vs Differentiation | Public logged-out with a desktop UA; post text in the page's description meta tag, date in JSON-LD |
| Ritson's 10 marketing hacks to help small businesses go big (2021-10-21) | https://www.marketingweek.com/ritson-10-marketing-hacks/ | Journalist write-up of his Festival of Marketing talk; spoken register | Public via curl; DOCUMENTED (reporter's transcription) |

## What the corpus rests on

Thirty-two of thirty-five excerpts are verbatim from his own writing: twenty-eight from eleven Marketing Week columns under his byline (2019-2025) and four from his own LinkedIn posts (2020-2024). Three excerpts are documented-grade direct quotes from a 2021 live talk as recorded by a Marketing Week journalist, and are labelled so in the corpus. Nothing comes from a quote aggregator. Confidence in wording is high for items 1-32 and moderate for 33-35. The written column register is sampled deeply across six years; the spoken register rests on a single secondary write-up.

## Known gaps

- **Pre-2020 columns are paywalled server-side.** The 2019 TV column truncated after paragraph six; only its visible paragraphs are quoted. Wayback (`web.archive.org/web/2024/<url>`) was not tested because every post-2020 fetch returned in full.
- **No podcast or video ASR sample.** Uncensored CMO, the Marketing Week podcast, and his Marketing Week video segments were not sampled, and yt-dlp was not attempted. The Festival of Marketing write-up stands in for the spoken register, so the spoken-vs-written note in the corpus is inferred from one secondary source.
- **Mini MBA in Marketing course material was not sampled.** It is behind enrolment; the LinkedIn promotion post is the only course-adjacent text.
- **LinkedIn sample is thin.** Four permalinks were located via web search; his /recent-activity/ feed is login-walled, so the short-form sample is not a chronological crawl.
- **Cited studies are his citations, not independently checked.** Ofcom, Gartner, Peckham's Formula, Braun and Schwartz, and the Field and Binet work appear as he reports them; treat figures as his published claims.
- **Anything published after 2026-10-19 is unsampled.**

## Refresh instructions

1. Re-fetch https://www.marketingweek.com/mark-ritson/ and pull any column published since 2025-03-31 with `curl -A "Mozilla/5.0" <url>`; add 5-8 verbatim excerpts and extend the Marketing Week section numbering.
2. For any pre-2020 column that truncates at "Please log-in or subscribe", try `https://web.archive.org/web/2024/<url>` before giving up on it.
3. Add a spoken sample: `yt-dlp --write-auto-sub --skip-download --sub-lang en -o "<slug>/%(id)s" <Uncensored CMO or Marketing Week YouTube URL>` once; if it returns HTTP 429, use the show's published transcript page instead. Label the result documented and update the spoken-register stat.
4. Widen the LinkedIn sample with further `site:linkedin.com/posts markritson` searches; read each permalink's description meta tag and JSON-LD date with a desktop UA.
5. Re-verify every URL in the Primary sources table is live before carrying any quote forward.

## Pattern notes

### 1. Evidence paragraph, expletive clause
A measured paragraph built on a chart or a figure is detonated by one short profane sentence ("It is shitfuckery. And of the highest possible order."). The Contrarian Take Generator requires the number before it permits the swear.

### 2. Fragment staircase
Verdicts arrive as one- to four-word sentences ("Nothing new. But they were all just excellent. Flawless."). All three playbooks close on a fragment chain or a flat imperative rather than a summary.

### 3. The incumbent's number
A hyped brand's figure is placed beside the boring giant's ($263m vs Coke every 72 hours). The Contrarian Take Generator uses it as the deflation move.

### 4. One absurd analogy per argument
Left-footed footballers, midfielders vs Manchester United, the fired barista. The Ghostwriter playbook asks for an analogy from the user's own world so the move transfers without the costume.

### 5. Diagnosis, strategy, tactics
The order is restated in nearly every strategy piece and the fad is shown to have skipped a step. It is the structural spine of the Ghostwriter and Newsletter playbooks.

### 6. Sneer quotes and the meta-aside
Vendor jargon sits in single quotes ('precision', 'hyper-targeted') and the columnist breaks frame once ("if that's OK with you?"). Both are capped at a few uses per piece to avoid the over-imitation tell.
