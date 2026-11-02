---
title: "GLiNER2 vs an LLM: I tested both on 640 labelled examples"
slug: "gliner2-vs-an-llm-i-tested-both-on-640-labelled-examples"
author: "Ahmad Dogar"
source: "devto_python"
published: "Mon, 02 Nov 2026 05:15:34 +0000"
description: "My comparison of LLMs, Jev and CDMs was all reading: docs, papers and vendor numbers. It left me wanting something I could run myself. GLiNER2 is that thing...."
keywords: "not, one, haiku, model, invoices, base, str, invoice"
generated: "2026-11-02T05:25:25.625152"
---

# GLiNER2 vs an LLM: I tested both on 640 labelled examples

## Overview

My comparison of LLMs, Jev and CDMs was all reading: docs, papers and vendor numbers. It left me wanting something I could run myself. GLiNER2 is that thing. It is an Apache-2.0 extraction model from Fastino that runs on a CPU, and you give it a schema, not a prompt. So I ran it on this laptop against Claude Haiku 5.5, with 640 labelled examples. I could not find an independent head-to-head for JSON extraction, which is the part I care about most. The short version: GLiNER2 is very fast and fine when the answer is written plainly in the text. Haiku was more accurate on every test but one, and the gap gets wide as soon as a value needs judgment. Percent correct. Entities are F1, and invoices count a note as right only if all four fields are. What I tested News topics: 200 AG News articles, 4 labels. Banking intent: 200 BANKING77 questions, 77 labels. Named entities: 200 CoNLL-2003 sentences, scored on exact type and text. Invoices: 40 notes I wrote myself, 20 easy and 20 hard, with four fields each. The GLiNER2 side ran on an M1 Pro with 16 GB of memory, CPU only, one text at a time. I tried three models: gliner2.5-small-v1 , gliner2.5-base-v1 and GLiNER2.5-Decide , which is the classification specialist. Getting it running takes a few lines: pip install 'gliner2[local]' from gliner2 import AutoExtractor m = AutoExtractor . from_pretrained ( " fastino/gliner2.5-small-v1 " ) print ( m . extract_json ( " Invoice 4471 from Acme Roofing, total due $1,240.50 by 12 March 2026. " , { " invoice " : [ " vendor::str " , " number::str " , " total::str " , " due_date::str " ]}, )) {'invoice': [{'vendor': 'Acme Roofing', 'number': '4471', 'total': '$1,240.50', 'due_date': '12 March 2026'}]} The results All scores from the same samples on one run. Decide was the slowest model and did not clearly beat base on classification, so I would not reach for it based on these two sets. Speed and memory M1 Pro, 16 GB, CPU only, one text at a time. Time grows with the number of labels, which is worth knowing before you hand it a long taxonomy. There is no Haiku column on purpose. I ran Haiku through the Claude Code CLI, and its start-up time would make any latency number meaningless. For cost, the billed tokens at Haiku's list price of $0.10 and $0.50 per million work out to roughly $0.05 to $0.16 per 1,000 calls depending on the task. The CLI may add some tokens of its own, so treat that as an upper estimate. Where it broke The hard invoices show the difference best. These are real shapes of mistake from the base model: Five real misses from the base model. Some of this is not a fair fight. GLiNER2 pulls text out of the input, so it cannot produce $300.00 when that number is not written anywhere. Four of my 20 hard notes need a value like that, so a perfect score was never possible for it. The other misses are a different problem: it picked the wrong value, or filled a field that should have been empty. The last row bothers me most. A model that fills a missing field with something plausible is harder to catch than one that returns nothing. Tuning did not rescue it. Dropping the confidence threshold from 0.5 to 0.3 left the invoice score unchanged and lowered entity F1 from 53.4% to 50.6%. Giving it the same field definitions Haiku got moved hard invoices only from 9 to 10 of 20: schema = { " invoice " : [ " vendor::str::Who issued the invoice " , " invoice_number::str::The current invoice number " , " total_due::str::What is still owed now, after credits and payments " , " due_date::str::The current date it must be paid by " , ]} Same mistakes again My last post quoted a paper finding that LLM fallbacks tend to repeat a cheap model's confident errors. I saw a version of that here. Of Haiku's 33 wrong banking answers, GLiNER2 base got 32 wrong too. On news it was 17 of 20. Some of those are probably ambiguous or debatable labels, and I did not check them one by one, but it means a second model is not a free safety net. How far to trust this I wrote the invoices. Forty notes is small, and I wrote both the notes and Haiku's prompt, so 40 of 40 is not a general claim about Haiku. One run, default settings. I did not fine-tune GLiNER2, which is one of its selling points. Training on your own data could change these numbers. Exact matching is harsh on entities. CoNLL also has a lot of sports tables, which is an odd test for any model. The label wording matters. 35 of base's 61 news errors were science and technology articles labelled business, so better label names might help. No Jev or CDMs here. I did not run them, so this says nothing about how they compare. Which one I would use GLiNER2 base when the value is stated plainly, the volume is high, or the text cannot leave your machine. Check that a missing field stays empty. An LLM when the answer needs reading: balances, superseded dates, or anything where a wrong value costs you money. Small only when memory or speed really is the limit. It lost three easy invoices that base got right. Before switching anything, label 200 of your own examples and run this same comparison. My invoices are not your invoices, and an afternoon of labelling is cheaper than trusting my table. Originally published on my site . More posts and projects at mahmadmanzoor.com .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ahmad_dogar_7d098f5e48f72/gliner2-vs-an-llm-i-tested-both-on-640-labelled-examples-1998

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
