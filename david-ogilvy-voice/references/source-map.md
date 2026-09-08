# David Ogilvy Source Map

Research date: 2026-09-09
Refresh cadence: every 12 months (the corpus is historical and will not drift; next: 2027-09)

## Corpus quality warning

This is the weakest-sourced corpus in the voice-dna collection and it should be treated that way until someone reads the books. Every item is `documented`, meaning widely republished and consistently attributed, but none was verified against a printed page in this build. Ogilvy is one of the most misquoted figures in advertising, and quote sites propagate errors between each other. His own memo says "Check your quotations." Do that before any of these lines appears in client-facing work.

## Primary sources

| Source | What it gives | Access |
|---|---|---|
| Confessions of an Advertising Man (1963) | The register, the reader-respect doctrine, the headline economics | In print, purchase |
| Ogilvy on Advertising (1983) | The rules with examples, the long-copy argument, the picture-and-caption rules | In print, purchase |
| The Unpublished David Ogilvy (1986) | The internal memos, including "How to Write" (1982) | In print, purchase |
| Ogilvy & Mather archive campaigns | The actual advertisements: Rolls-Royce 1958, Hathaway, Schweppes, Dove | Swipe file sites of varying reliability |
| Swipe file archives (e.g. swiped.co) | Scans of the classic ads with full body copy | Open, but verify provenance of any scan |
| Reproductions of the 1982 memo (Open Culture, Farnam Street, and others) | The ten hints, consistently reproduced across sources | Open |

## What was actually fetched

Nothing primary. The corpus was assembled from search results and one quotation aggregator on 2026-09-09. Two attempts to have a page-reading tool reproduce the memo verbatim were declined by that tool on copyright grounds, which is why the memo items are drawn from the fragments that appear consistently across multiple independent reproductions.

## Known gaps

- **No book text.** Both canonical books are unread for this build. The voice fingerprint in SKILL.md is therefore built from aphorisms plus the memo, not from sampled running prose. This is the top priority to fix.
- **No full ad body copy.** The Rolls-Royce ad's headline is captured but not its body, and the body is where the long-copy discipline actually lives. Pull one verified scan and transcribe the body on refresh.
- **Wording variance.** Several items, particularly "If it doesn't sell, it isn't creative", appear in slightly different forms across sources. The corpus records the most common form and flags the variance.
- **Attribution risk.** At least one widely circulated Ogilvy quotation collection includes lines he did not write. Anything not traced to a book, a memo reproduction, or a dated advertisement should be treated as unattributed.

## Refresh instructions

1. Read Ogilvy on Advertising and Confessions of an Advertising Man. Replace the aphorism corpus with short cited quotations including page references, and drop the `documented` labels for anything verified.
2. Transcribe the body copy of two verified classic ads, ideally Rolls-Royce 1958 and one Hathaway or Dove piece, and add a running-prose section to the corpus.
3. Verify the ten hints of the 1982 memo against The Unpublished David Ogilvy.
4. Remove or re-source any line that cannot be traced to a book, a memo, or a dated advertisement.
5. Keep the historical framing note on item 1. It is a 1955 line and should not be presented as live audience guidance.
