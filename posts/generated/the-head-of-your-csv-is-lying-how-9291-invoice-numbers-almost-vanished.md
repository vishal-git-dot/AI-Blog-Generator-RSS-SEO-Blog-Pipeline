---
title: "The head of your CSV is lying: how 9,291 invoice numbers almost vanished"
slug: "the-head-of-your-csv-is-lying-how-9291-invoice-numbers-almost-vanished"
author: "Ahmed Abdeltawab"
source: "devto_python"
published: "Sat, 15 Aug 2026 06:19:41 +0000"
description: "Real transaction data is never clean — and the worst part is that it looks clean. This is a short story from a real dataset (UCI Online Retail: 541,909 e-com..."
keywords: "rows, numbers, data, invoiceno, every, one, what, they"
generated: "2026-08-15T06:47:15.229211"
---

# The head of your CSV is lying: how 9,291 invoice numbers almost vanished

## Overview

Real transaction data is never clean — and the worst part is that it looks clean. This is a short story from a real dataset (UCI Online Retail: 541,909 e-commerce transactions) about the quietest way to destroy data: silent type coercion. All numbers below come verbatim from an executed notebook. The head looks perfect Peek at the first rows of the file and InvoiceNo parses as clean integers — 100% parse rate, full confidence. Any type-inference step, mine included, would call it int64 and move on. Measure the whole file instead of the head, and the number drops to ~98%. The other 2%: invoice numbers starting with "C" — which in this dataset marks a cancellation . Coerce the column to numeric and every one of them becomes NaN : Invoice numbers destroyed by numeric coercion: 9,291 DextraLoaderWarning: load: ambiguous decision(s): column 'InvoiceNo': ambiguous - float64 at parse_rate=0.98 An entire class of business events — silently gone. No exception, no crash. That's what makes coercion the quietest bug in data work: the pipeline succeeds . Why those 9,291 rows matter They are not noise. They are the returns side of the business : cancelled orders worth 8.4% of everything sold. Lose them and every revenue number downstream is quietly wrong. One example of what they catch: the dataset's apparent #1 bestseller, "PAPER CRAFT, LITTLE BIRDIE" (168,470 GBP), is a phantom — a single 80,995-unit order entered at 09:15 and fully cancelled at 09:27 the same morning. Only the preserved cancellation rows expose it. The genuine bestseller is a cake stand. The fix: identifiers are labels, not quantities No library can know that "InvoiceNo" is an ID — that's domain knowledge. What a tool can do is disclose its guess and hand you a replayable plan you can correct: naive , plan = dx . load ( CSV_PATH , return_params = True ) # warns: ambiguous at 0.98 plan [ " columns " ][ " InvoiceNo " ][ " dtype " ] = " object " # invoices are labels plan [ " columns " ][ " StockCode " ][ " dtype " ] = " object " # product codes too df = dx . load ( CSV_PATH , params = plan ) # deterministic replay Cancellation invoices preserved: 9,288 InvoiceNo values lost: 0 The correction is now documented, versionable code — not a mystery cell someone ran once. Three habits this taught me Never trust the head of a file. The first rows parse clean at 100%; the truth lives in the full-file parse rate. Measure every cell. Declare identifiers explicitly. Invoice numbers, product codes, phone numbers, zip codes — they look numeric and they are not. One schema line prevents the whole class of bug. Split, don't delete. The final frame here is three frames: sales (530,104 rows, 97.8%), returns (9,288, 1.7%), oddities (2,517, 0.5%). Deleted rows can't answer questions later; split rows can — the returns table is where the phantom bestseller was caught. Try it The full walkthrough — from messy CSV to a business decision, every step printing what it did and why — is published fully executed on Kaggle: Rescuing 9,291 invoices from coercion (pydextra) . It runs on pydextra ( pip install pydextra , MIT), a small library I built around one idea: every function prints a one-line Decision: explaining what it did and why. To be transparent: it's a personal educational-practical project, not a replacement for pandas — pandas is the engine underneath. GitHub: https://github.com/ahmedabdeltawab602-collab/dextra Docs: https://ahmedabdeltawab602-collab.github.io/dextra/ Previous article — data leakage, same AUC, hidden lie: https://dev.to/ahmedabdeltawab/an-adversarial-review-found-11-real-defects-in-my-python-library-best-decision-i-made-2h85 Data: Chen, D. (2015). Online Retail. UCI Machine Learning Repository. DOI 10.24432/C5BW33, CC BY 4.0.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ahmedabdeltawab/the-head-of-your-csv-is-lying-how-9291-invoice-numbers-almost-vanished-3891

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
