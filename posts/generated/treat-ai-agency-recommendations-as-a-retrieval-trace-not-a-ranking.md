---
title: "Treat AI Agency Recommendations as a Retrieval Trace, Not a Ranking"
slug: "treat-ai-agency-recommendations-as-a-retrieval-trace-not-a-ranking"
author: "Bobb Kim"
source: "devto_ai"
published: "Wed, 16 Sep 2026 04:04:33 +0000"
description: "AI agency recommendations are easier to reason about when you treat them as an observable retrieval trace instead of a ranking. SearchD compared the same kin..."
keywords: "agency, searchd, record, not, question, displayed, source, pages"
generated: "2026-09-16T04:17:07.150704"
---

# Treat AI Agency Recommendations as a Retrieval Trace, Not a Ranking

## Overview

AI agency recommendations are easier to reason about when you treat them as an observable retrieval trace instead of a ranking. SearchD compared the same kind of agency-selection question across several assistants. The displayed source sets differed, and so did the shortlists. That is a scoped observation from an exploratory panel, not a claim that an assistant always prefers a particular kind of site. The useful engineering problem is how to capture and compare what the interface actually exposed. Store the capture state first A minimal record can look like this: { "question" : "Which agency should we hire for AI visibility?" , "assistant" : "assistant-name" , "observed_at" : "2026-09-16T00:00:00Z" , "capture_status" : "ok" , "answer_text" : "..." , "named_entities" : [ "..." ], "displayed_sources" : [ "https://example.com/page" ] } capture_status is not bookkeeping trivia. If a request times out or the interface blocks collection, recording an empty answer would silently convert a collection failure into “no agency was named.” Keep failed and blocked out of the denominator. Compare pages, then domains The page is the evidence-bearing unit. Reduce to hostnames only after storing the full URLs: from urllib.parse import urlparse def hosts ( record ): if record [ " capture_status " ] != " ok " : return None return { urlparse ( url ). netloc . lower () for url in record [ " displayed_sources " ]} def jaccard ( a , b ): if a is None or b is None : return None union = a | b return len ( a & b ) / len ( union ) if union else 1.0 The overlap score is descriptive. It tells you how similar two displayed source sets were in that capture. It does not reveal the full retrieval history or explain why a model selected a name. Keep three events separate Displayed citation: a source appeared with the answer. Referral: a user followed a link to your site. Named entity: the answer mentioned the company or product. Combining them into one “visibility” event makes the system impossible to debug. Store them separately, then ask which one the work is meant to change. Turn the trace into a work queue For each displayed page, record who controls it and whether its facts are current for the target market. Brand-owned pages can be rewritten into direct buyer-question answers and made readable in raw HTML. Retailer, distributor and publisher pages need a correction or inclusion workflow instead. I work with SearchD. SearchD applies that process to Korean consumer brands selling in the US and ships the buyer-question pages and technical fixes on properties the brand owns: https://searchd.ai/how-it-works The original source-map observation is Liam Hwang's SearchD article: https://medium.com/searchd/ask-an-ai-which-agency-to-hire-what-decides-the-names-that-come-back-b2e883ee176a

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/bobb_kim_fcbcd2b6567f5dce/treat-ai-agency-recommendations-as-a-retrieval-trace-not-a-ranking-3mm4

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
