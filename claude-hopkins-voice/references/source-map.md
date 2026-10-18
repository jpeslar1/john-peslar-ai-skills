# Claude Hopkins Voice Source Map

Research date: 2026-10-19
Refresh cadence: every 6 months (next: 2027-04)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| Scientific Advertising (1923), full text, archive.org item `scientific-advertising` (Carl Galletti re-set "original text" edition, 21 chapters) | https://archive.org/download/scientific-advertising/Scientific%20Advertising_djvu.txt (item page https://archive.org/details/scientific-advertising) | Complete book, chapter-numbered; the reason-why and test-everything doctrine; items 1-21 | Open, plain text, 132 KB; public domain |
| My Life in Advertising (Harper & Brothers, 1927), first-edition OCR, archive.org item `mylifeinadvertis0000clau` | https://archive.org/download/mylifeinadvertis0000clau/mylifeinadvertis0000clau_djvu.txt (item page https://archive.org/details/mylifeinadvertis0000clau) | Complete autobiography, Preface plus 19 chapters; Schlitz, Pepsodent, Palmolive case stories; items 22-33 | Open, plain text, 294 KB, clean chapter headings; public domain |
| My Life in Advertising (1927), second scan (Google Books digitization), archive.org item `mylifeinadverti00unkngoog` | https://archive.org/download/mylifeinadverti00unkngoog/mylifeinadverti00unkngoog_djvu.txt | Independent OCR of the same edition, used to cross-check wording | Open, plain text, 302 KB; noisier OCR, some chapter headings lost |
| archive.org metadata for both items | https://archive.org/metadata/scientific-advertising and https://archive.org/metadata/mylifeinadvertis0000clau | Confirms edition, publisher, year, file list | Open JSON |
| John Carlton on Hopkins (secondary, corroborative only) | https://copyblogger.com/copywriting-john-carlton-1/ | Carlton reports reading both books eight times in his first 18 months on Jay Abraham's instruction; confirms the canon status | Open; not excerpted into the corpus |
| Gary Bencivenga on Hopkins (secondary, corroborative only) | http://web.archive.org/web/20140205032807id_/http://www.marketingbullets.com/bullet02.htm | Quotes the "war, minus the venom" passage verbatim and calls Hopkins "the Aristotle of Advertising" | Open via Wayback; not excerpted into the corpus |

Not available: the 1998 NTC combined edition (`mylifeinadvertis00hopk`) and the 1936 reprint (`bwb_S0-DSD-567`) sit in the archive.org lending library and return HTTP 401 on the text file. Project Gutenberg has no Hopkins title.

## What the corpus rests on

All thirty-three excerpts are verbatim from the two books Hopkins wrote himself, both in the public domain: twenty-one from Scientific Advertising (1923), covering fourteen of its twenty-one chapters, and twelve from My Life in Advertising (1927), covering the Preface and nine of nineteen chapters, with the memoir wording cross-checked against a second independent scan. Zero items are documented-grade. Nothing comes from a quote aggregator, a secondary summary, or a modern reprint. Confidence in wording is high throughout; the only caveat is that the Scientific Advertising text is a re-set edition rather than a scan of the 1923 printing. There is no spoken register because none exists.

## Known gaps

- **No spoken-word record exists.** Hopkins died in 1932 and left no recording or transcript. The spoken-vs-written note in the corpus cannot be filled and any claim about his speech is unsupported.
- **Scientific Advertising is a re-set edition, not a first-printing scan.** The archive.org text is Carl Galletti's "original text" edition and carries his page headers (stripped) plus a few OCR slips in passages not quoted ("a carelessness truth" for "a carelessness of truth"; "They site advantages" for "cite"). Every quoted sentence was checked and none of those slips were used. A scan of the 1923 Lord & Thomas printing would be the only upgrade.
- **His actual client copy is not in the corpus.** The Schlitz, Pepsodent, Palmolive, and Puffed Wheat advertisements, the Bissell and Swift letters, and his Lord & Thomas house pieces are summarized in the memoir but not reproduced as full text in either book, and no open swipe-file scan was located. The skill can quote his doctrine but not his ad copy.
- **Chapters read but not excerpted.** Scientific Advertising chapters 9, 11, 14, 16, 17, 19, 20 and My Life in Advertising chapters 3-6, 8-11, 13-16, 18 were read in full and not quoted; cleaned full texts were saved at research time at /private/tmp/claude-501/batch5/claude-hopkins/raw/sa_clean.txt and mla_clean.txt (temporary location, may not survive).
- **His results are self-reported.** Every figure in the corpus (20 percent coupon returns, Schlitz fifth to first, 30 vs 150 percent) is his own account; no independent audit exists.
- **Anything published after 2026-10-19 is unsampled.** For a 1932 death this means only new scans, reprints, or newly surfaced letters.

## Refresh instructions

1. Check archive.org for a scan of the 1923 Lord & Thomas first printing of Scientific Advertising (`https://archive.org/search?query=hopkins+scientific+advertising+1923`); if one appears with a `_djvu.txt`, re-read items 1-21 against it and note any wording differences.
2. Re-fetch both full texts with `curl -L <djvu.txt URL> -o <file>` and confirm the quoted sentences still match character for character; archive.org occasionally re-OCRs items.
3. Search for open swipe-file scans of his Schlitz, Pepsodent, or Palmolive ads (archive.org, Duke's Ad*Access, HathiTrust full view); if found, add a separate "Client copy (scanned ads)" section rather than mixing them with the book excerpts.
4. Add 3-5 excerpts from the unexcerpted chapters (Scientific Advertising ch. 9 "Information", ch. 11 "Individuality", ch. 16 "Leaning on Dealers"; My Life in Advertising ch. 17 on Pepsodent) to widen coverage, keeping the two-section structure.
5. Do not add anything from quote aggregators or modern paraphrase sites; both books are open, so every line can be read at its source.

## Pattern notes

### 1. State the law, then its consequences
A four-word principle ("Advertising is salesmanship.") is followed by three to five short sentences that follow from it. The Ghostwriter playbook builds every doctrinal paragraph this way.

### 2. The traced figure
Every rule is paid for within two sentences by a coupon count, a percentage, or a cost per result. All three playbooks treat an unpaid claim as unfinished and route it to [VERIFY].

### 3. Hey there, Bill Jones
The headline is a shout to one person in a crowd; "people in the mass" is the error. The Hook Creator requires every headline to name the buyer, state a specific, or deny a commonplace.

### 4. Give it a meaning
The fact every competitor shares and none has stated ("a story common to all good brewers, but a story which had never been told") is the campaign. The Ghostwriter makes finding it the mandatory first step.

### 5. The salesman's test and the court of last resort
Every line is judged by whether a salesman would say it at the buyer's door, and every dispute is settled by a keyed test rather than argument. The Objection Handling Expert answers doubt by offering the test instead of the rebuttal.

### 6. Temperate toward rivals, merciless toward waste
"To attack a rival is never good advertising" sits beside "Men spending five dollars to do what one dollar might do." The Objection Handling Expert forbids disparaging a competitor and the Ghostwriter forbids superlatives, while both demand the cost comparison.
