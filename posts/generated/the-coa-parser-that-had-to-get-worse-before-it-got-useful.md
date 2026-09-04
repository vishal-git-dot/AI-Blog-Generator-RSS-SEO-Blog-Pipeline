---
title: "The CoA parser that had to get worse before it got useful"
slug: "the-coa-parser-that-had-to-get-worse-before-it-got-useful"
author: "Rajiv Iyer"
source: "devto_python"
published: "Fri, 04 Sep 2026 03:35:02 +0000"
description: "A Certificate of Analysis is a PDF a supplier sends with a shipment saying what they measured and what they got. In a contract manufacturing shop you receive..."
keywords: "not, tensile, had, supplier, label, str, parser, what"
generated: "2026-09-04T03:55:40.883419"
---

# The CoA parser that had to get worse before it got useful

## Overview

A Certificate of Analysis is a PDF a supplier sends with a shipment saying what they measured and what they got. In a contract manufacturing shop you receive a lot of them, and someone has to check the numbers against the specification before the material is released to production. I wrote a parser for this in 2022. It was accurate on about 94% of documents, and it was a bad system. The version running now is accurate on about 78%, and it is a good one. This is the story of the six percentage points I gave away on purpose, and why the number I was optimising was the wrong number. The first version Straightforward pipeline. pdfplumber for text extraction, layout heuristics to find the results table, fuzzy matching to map a supplier's label for a property onto ours — "Tensile", "Tensile Str.", "TS (MPa)" all becoming tensile_strength — then a comparison against the spec table. ALIASES = { " tensile_strength " : { " tensile " , " tensile str " , " ts " , " tensile strength " }, " hardness " : { " hardness " , " hrc " , " rockwell " , " hardness hrc " }, # ~40 more } def canonical ( label : str ) -> str | None : key = re . sub ( r " [^a-z ] " , "" , label . lower ()). strip () for prop , names in ALIASES . items (): if key in names : return prop return best_fuzzy_match ( key , ALIASES ) # <- the problem lived here It worked. I measured it against 200 documents I had hand-checked and got 94% field-level accuracy, which felt like a result worth telling people about. What 94% was hiding The 6% was not evenly distributed, and it was not random. best_fuzzy_match always returned something . Give it a label it had never seen and it would find the nearest neighbour above a similarity floor and hand it back with no indication that it had guessed. Most of the time the nearest neighbour was right, because supplier labels really are similar. Then a supplier changed their template and started reporting "Yield Str." alongside "Tensile Str." We had no alias for yield strength — nobody had sent it before. Fuzzy matching put yield strength into the tensile strength field. Yield is lower than tensile for the steel we buy, so the value looked plausible, sat inside the tensile specification, and passed. Eleven shipments went through before someone in production noticed the tensile numbers had quietly dropped about 15% across one supplier and asked why. Nothing was actually wrong with the material — the real tensile values were fine, we just were not reading them. But for eleven receipts our release records said we had verified a property we had not looked at. Explaining that to a customer auditor is not a conversation you want, and "the algorithm was 94% accurate" is not the mitigating fact it sounds like. The rewrite The change was small and the whole point: def canonical ( label : str ) -> str | None : key = re . sub ( r " [^a-z ] " , "" , label . lower ()). strip () for prop , names in ALIASES . items (): if key in names : return prop return None # unknown is a real answer I deleted the fuzzy matcher. An unrecognised label now returns None , the document goes to a review queue, and a human reads it. Accuracy on documents fell to 78%, because 22% now contain at least one label we do not have an exact alias for and get queued instead of parsed. But the metric changed. It is no longer "how often is the parser right." It is: how often does the parser assert something it has not verified — and that is now zero. Every queued document is also a prompt. If a supplier sends "Yield Str." three times, someone adds the alias and it stops queueing. The alias table has grown from 40 properties to just over 90 in two years, entirely from the queue. The system gets better by being honest about what it does not know, which is not a sentence I expected to write about a regex. The part I would argue about An obvious objection: keep the fuzzy matcher but flag low-confidence matches. Best of both. I tried it. The problem is that a confidence score creates a threshold, and a threshold creates a band of matches that are probably fine, and in practice nobody reviews the probably-fine band. It gets treated as passed. Within a month we were back to the same failure with an extra number attached to it. Exact match or queue is a cruder rule and people actually follow it. From a CMO perspective that matters more than elegance — the system has to work on a Tuesday when the person running it is also doing three other things. Where the 22% actually goes Roughly: 12% — a supplier label we have not seen, first time. Gets an alias, usually never queues again. 6% — scanned PDFs with no text layer. We do not OCR these; the failure modes of OCR on a smudged fax are exactly the confidently-wrong class I removed the fuzzy matcher to avoid. 3% — genuinely unusual formats, one supplier who sends results as prose. 1% — corrupt or truncated files. The 6% scanned ones bother me and I have not solved them. Every OCR pipeline I have tried is happy to give me a digit that is not on the page. The general version If you build parsers over documents someone else controls, the number to watch is not accuracy. It is what your system does when it does not know . A parser that says "I don't know" 22% of the time is auditable. A parser that silently guesses is a liability with good metrics, and you will not find out which one you built until a supplier changes a template. Rajiv Iyer — QA tech lead, contract manufacturing, Bangalore. Opinions my own.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/rajiviyer112/the-coa-parser-that-had-to-get-worse-before-it-got-useful-1gb6

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
