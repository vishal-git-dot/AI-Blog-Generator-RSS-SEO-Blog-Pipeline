---
title: "My Favorite Constant in Retrieval Is 60. Nobody Tunes It. That's the Point."
slug: "my-favorite-constant-in-retrieval-is-60-nobody-tunes-it-thats-the-point"
author: "Vinicius Fagundes"
source: "devto_python"
published: "Sun, 02 Aug 2026 03:00:00 +0000"
description: "Reciprocal rank fusion merges two ranked lists — say, BM25 results and vector-search results over your chargeback cases — into one. It has exactly one parame..."
keywords: "rank, doc, scores, list, two, results, one, not"
generated: "2026-08-02T03:28:39.839730"
---

# My Favorite Constant in Retrieval Is 60. Nobody Tunes It. That's the Point.

## Overview

Reciprocal rank fusion merges two ranked lists — say, BM25 results and vector-search results over your chargeback cases — into one. It has exactly one parameter, k . And the answer is just... 60. Not tuned per dataset. Not learned. Sixty, from the original paper, works essentially everywhere. The entire algorithm: def rrf ( rankings : list [ list [ str ]], k : int = 60 ) -> list [ tuple [ str , float ]]: """ Each ranking is a list of doc IDs, best first. Score = sum of 1/(k + rank). """ scores = {} for ranking in rankings : for rank , doc in enumerate ( ranking , start = 1 ): scores [ doc ] = scores . get ( doc , 0 ) + 1 / ( k + rank ) return sorted ( scores . items (), key = lambda x : - x [ 1 ]) # Fraud case search, two retrievers disagreeing: bm25_top = [ " CB-1041 " , " CB-1250 " , " CB-1102 " ] # keyword hits: rule ID matched dense_top = [ " CB-1203 " , " CB-1041 " , " CB-1288 " ] # semantic hits: similar pattern for doc , score in rrf ([ bm25_top , dense_top ]): print ( f " { doc } : { score : . 4 f } " ) CB-1041: 0.0325 <- ranked #1: the case BOTH retrievers liked CB-1203: 0.0164 CB-1250: 0.0161 CB-1102: 0.0156 CB-1288: 0.0156 Notice what it just did without being told: the case both retrievers agreed on floated to the top, and the two scoring scales — BM25's unbounded scores, cosine's 0-to-1 — never had to be reconciled, because ranks don't care about scales. Why 60 works everywhere: at k=60, the difference between rank 1 and rank 3 matters, but the difference between rank 40 and rank 50 is noise — which is exactly the shape of trust you should have in any retriever. The constant encodes an epistemics, not a dataset. I think about this every time I watch a team burn a sprint tuning fusion weights per query type. Twenty years of information retrieval research, and one of its most robust results is a knob you never touch. Some of the best engineering is knowing which knobs don't need turning. I'm Vinicius Fagundes — principal data engineer and MBA lecturer in São Paulo. I build fraud and risk analytics pipelines for e-commerce through vf-insights.com .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/fagundesv/my-favorite-constant-in-retrieval-is-60-nobody-tunes-it-thats-the-point-4857

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
