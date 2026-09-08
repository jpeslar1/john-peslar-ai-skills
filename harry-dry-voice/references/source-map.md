# Harry Dry Source Map

Research date: 2026-09-09
Refresh cadence: every 6 months (next: 2027-03)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| Marketing Examples, copywriting hub | https://marketingexamples.com/copywriting | The rule set. Index of every copywriting lesson. | Open, JavaScript-rendered |
| 17 tips for great copywriting | https://marketingexamples.com/copywriting/tips | The canonical rule names | Open |
| 7 practical ways to write copy that converts | https://marketingexamples.com/copywriting/conversion | Before/after examples and the call-to-value idea | Open |
| Psychology of persuasion | https://marketingexamples.com/copywriting/psychology-of-persuasion | The Blair Warren 27 words (attribute to Warren) | Open |
| Adjectives lesson | https://marketingexamples.com/copywriting/adjectives | The adjective rule, verbatim line | Open |
| Copywriting is math | https://marketingexamples.com/copywriting/math | Objection handling, social proof, actionable outcomes | Open |
| Roast My Homepage | https://marketingexamples.com/roast | His teardown format applied live | Open |
| Newsletter | https://marketingexamples.com/newsletter | Format contract: 3 examples, 2 tips, 1 tweet, Mondays | Open, signup |
| X account | https://x.com/harrydry | One-line copy tips, the shortest form of the voice | Open, rate-limited |
| How I Write interview (David Perell) | howiwrite.substack.com | The three laws and the delete-key rules in his own spoken words | Open |

## Scraping notes

- **marketingexamples.com is client-rendered.** A plain HTTP fetch returns a head-only document with a JavaScript bundle and no body text. Use a rendering fetch tool, or the site's own RSS if one is exposed, when refreshing this corpus.
- The page-reading tool used here reliably returns headings and short quoted lines but paraphrases longer prose. That is why the corpus is heavier on rule names than on running paragraphs.

## Known gaps

- **No long-form prose sample.** Everything captured is headings, rules, and one-line examples. His actual connective prose between examples is under-sampled. Fix this on refresh by reading two or three full lesson pages in a rendering browser and transcribing the connective sentences.
- **X corpus not captured.** His one-line tips on X are the purest form of the voice and were not harvested. X requires auth for bulk reading.
- **Newsletter archive not captured.** Issues go to subscribers; only the format description was captured.
- **Interview lines are second-hand.** Items 28-31 in the corpus come from a writeup of the How I Write conversation, not from the audio. Verify before quoting.

## Refresh instructions

1. Open three lesson pages in a rendering browser and transcribe the connective prose, not just the headings.
2. Pull 15 to 20 recent one-line tips from https://x.com/harrydry for the compressed register.
3. Confirm the newsletter format contract is still three examples, two tips, one tweet.
4. Re-check that every brand example held in the corpus is still live on the site. He rotates examples.
5. Never carry a brand example into client copy without confirming the brand actually ran that line.
