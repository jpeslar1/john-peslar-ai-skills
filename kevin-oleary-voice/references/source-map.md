# Kevin O'Leary Source Map

Research date: 2026-08-24; primary-source re-verification and refresh 2026-10-18
Refresh cadence: every 6 months (next: 2027-04)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| O'Leary Ventures | https://olearyventures.com/ | Public positioning, current fund/venture messaging | Open |
| X profile | https://x.com/kevinolearytv | Short-form register, current takes | Login wall |
| Shark Tank (ABC, 2009 onward) and Dragons' Den (CBC) | public quote archives: IMDb, screenrant.com, thesharktankepisodes.com | On-air verdict lines, catchphrases ("you're dead to me") | Open, secondary archives |
| Cold Hard Truth (2011) and sequels | book | Money-personified doctrine, public excerpts only | Purchase, accessed via secondary quote pages |
| Interview archives | CNBC (negotiation, investing); aggregated quote pages graciousquotes.com, brainyquote.com, etfdb.com, awakenthegreatnesswithin.com | Widely quoted lines, negotiation philosophy | Open, secondary archives |

## Public positioning

O'Leary's public arc: SoftKey/The Learning Company founder (sold to Mattel for billions in 1999), Dragons' Den and Shark Tank investor, and chairman of O'Leary Ventures with public positions in funds, wine, and crypto ventures. His public persona, Mr. Wonderful, is a self-aware pantomime villain: theatrical bluntness in service of capital discipline, with the meanness framed as the most honest kindness in the room.

## What the corpus rests on

The corpus rests almost entirely on secondary quote-aggregator sites (graciousquotes.com, screenrant.com, thesharktankepisodes.com, etfdb.com, awakenthegreatnesswithin.com), plus one primary CNBC interview page for the negotiation items (20, 21). Confidence is moderate: these are widely republished lines, consistent across multiple aggregators, but the original primary context (an ABC or CBC broadcast timestamp, a book page number, an X post URL) was not independently fetched and confirmed by Claude this session.

## Re-verification and refresh (2026-10-18)

All 21 first-pass items were checked against primary sources: 4 verified (items 3 and 14 on his own X posts with shorter wording; 20 and 21 exact at CNBC https://www.cnbc.com/2020/10/29/kevin-oleary-how-to-make-the-best-deals-when-negotiating.html), 17 not found, 1 flagged as a cross-corpus duplicate with no primary trace (item 2). The refresh added 28 primary items (101-128): 17 verbatim X posts from @kevinolearytv (2021-2025, fetched through X's syndication endpoint by ID with fxtwitter for full text) and 11 documented from two own-channel "Ask Mr. Wonderful" episodes ("How I Made My First Million Dollars Part 1", "How to Get Rich Investing in Things You LOVE") and one CNBC segment ("Nvidia Has Some Big Challenges Ahead"). The corpus now has dated, permalinked posts and a spoken register for the first time.

## Known gaps

- **No spoken register sampled.** Every excerpt is a written transcription pulled from quote-aggregator sites, not a video Claude watched or a human caption track. O'Leary's native register (Shark Tank, Dragons' Den, CNBC hits) is spoken; this corpus documents what he said, not how he delivered it.
- **Sourced from secondary aggregators, not primary transcripts.** Most items trace to graciousquotes.com, screenrant.com, or similar pages rather than an ABC/CBC transcript or an X post Claude fetched directly. Treat every item as `documented`, not `verified`.
- **Books never read directly.** Cold Hard Truth and its sequels are named as a source, but no corpus item is attributed to them directly; the "royalty deal logic" pattern rests on interview summaries, not the books themselves.
- **No live X corpus.** x.com/kevinolearytv is named as a source but no post from it appears in the corpus. His current (2026) short-form register is not sampled.
- **"Money as soldiers" has no primary trace.** The skill's Money personified hook and Signature Move 1 rest on aggregator lore; keep them labelled as such until a permalink or caption track surfaces.
- **"You're dead to me" (item 16) is attested but unverifiable**: Shark Tank clips carry no caption tracks.
- **Items 4-8, 11-13, 15, 17-19 remain unverified** as worded.
- **Books never read directly.**
- **Anything published after 2026-10-18 is unsampled.**

## Refresh instructions

To update: pull recent posts from `https://x.com/kevinolearytv`, new Shark Tank season quote roundups, and current O'Leary Ventures messaging (his topics rotate through crypto, energy, and small-business advocacy). Add 5-10 dated verbatim excerpts to `voice-corpus.md`, re-estimate the derived stats, and check whether new catchphrases have joined the canon alongside the established ones. Prioritize pulling from a primary transcript or an X post directly, so new items can be labeled `verified` rather than `documented`.

## Pattern notes

### 1. Money personified

Capital as soldiers sent to war who must come home with prisoners. This is the master metaphor; the skill uses it for investment discipline and opportunity cost.

### 2. Royalty deal logic

His signature structure: recoup capital through per-unit royalties until made whole, then step down. The skill translates this into pricing and negotiation structures generally.

### 3. Verdict-first delivery

Judgment stated before reasoning, as theater. The skill opens pieces with the cold verdict.

### 4. Anti-sentiment economics

Feelings priced at zero; fear and greed as the only two diagnoses. The skill uses this in objection handling and contrarian takes.

### 5. The self-aware villain

The persona works because he is visibly enjoying it. The skill's anti-pattern list guards the wink: cruelty without mischief is parody.

### 6. Mutual-discomfort negotiation

His stated negotiation ideal: both sides feel they left something on the table. The skill says this truth out loud in closes to build trust.
