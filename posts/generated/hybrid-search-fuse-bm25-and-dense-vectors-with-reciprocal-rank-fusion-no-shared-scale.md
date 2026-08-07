---
title: "Hybrid Search: Fuse BM25 and Dense Vectors With Reciprocal Rank Fusion (No Shared Scale)"
slug: "hybrid-search-fuse-bm25-and-dense-vectors-with-reciprocal-rank-fusion-no-shared-scale"
author: "Devanshu Biswas"
source: "devto_ai"
published: "Fri, 07 Aug 2026 18:52:11 +0000"
description: "Modern retrieval has two great tools that are each half-blind. Lexical search (BM25) matches actual words: unbeatable on exact keywords, product codes, error..."
keywords: "doc, score, dense, rank, each, but, code, both"
generated: "2026-08-07T19:04:02.698462"
---

# Hybrid Search: Fuse BM25 and Dense Vectors With Reciprocal Rank Fusion (No Shared Scale)

## Overview

Modern retrieval has two great tools that are each half-blind. Lexical search (BM25) matches actual words: unbeatable on exact keywords, product codes, error IDs, and rare technical terms — but literal, so it can't tell that "sign in" and "log in" mean the same thing, and a pure paraphrase with no shared words scores zero . Dense vector search matches meaning: it embeds query and documents and ranks by cosine, so it sails through synonyms and paraphrase — but it smears rare tokens into a fuzzy semantic average, so it can rank a generic "error" article above the one doc that names your exact error code. Neither is strictly better. They miss different things. Hybrid search runs both and fuses the two ranked lists. BM25: idf, saturating tf, length-norm BM25 sums, over each query term in the doc: an idf (rare terms count more), a tf that saturates via k1 (the 5th "password" barely beats the 4th), and a length penalty via b . A rare code like X0-2231 gets a huge idf, so the one doc containing it rockets to the top. import math N = len ( corpus ); avgdl = sum ( len ( d ) for d in docs_tok ) / N def idf ( t ): # BM25 idf, non-negative n = sum ( t in set ( d ) for d in docs_tok ) return math . log ( 1 + ( N - n + 0.5 ) / ( n + 0.5 )) def bm25 ( q_tok , d , k1 = 1.5 , b = 0.75 ): score , dl = 0.0 , len ( d ) for t in set ( q_tok ): f = d . count ( t ) if not f : continue score += idf ( t ) * ( f * ( k1 + 1 )) / ( f + k1 * ( 1 - b + b * dl / avgdl )) return score The dense side embeds text into a vector where meaning, not spelling, decides closeness, then ranks by cosine — so "sign in" lands next to "log in," but a rare exact code blurs into a generic error vector. The two blind spots are symmetric Print the top-3 of each and the failure is mirror-image: BM25 finds the code doc but misses the paraphrase; dense finds the paraphrase but ranks a generic error doc over the exact-code one. Each list is half right. No single ordering puts both true answers on top. RRF: fuse by rank, not by score Reciprocal Rank Fusion throws the scores away — they live on incompatible scales (BM25 is 0–tens, cosine is 0–1) — and adds 1/(k + rank) across every list a doc appears in. A doc ranked #1 anywhere earns a big vote; being decent in both also adds up; a doc a list never retrieved simply contributes 0 from that list. def rrf ( rankings , k = 60 ): score = {} for ranked in rankings : # e.g. [lex, dense] for rank , doc in enumerate ( ranked , start = 1 ): score [ doc ] = score . get ( doc , 0 ) + 1.0 / ( k + rank ) return sorted ( score , key = score . get , reverse = True ) fused = rrf ([ lex , dense ], k = 60 ) # the code doc (BM25 #1) and the login doc (dense #1) BOTH surface. Because each true answer was #1 in one list, each earns a top 1/(k+1) vote and both float up. Small k lets a rank-1 hit dominate; large k flattens the votes so agreement across lists matters more. The alternative, and the normalize trap You can fuse the scores directly with α·BM25 + (1−α)·dense — but without a min-max normalize, BM25's raw magnitude bulldozes cosine no matter what α you pick. Normalize each list to 0–1 first and α becomes a real dial. A weighted sum can outperform RRF once you carefully normalize and tune α — but that calibration is exactly what RRF lets you skip by using only ranks. This is the real shape: Weaviate, Elasticsearch/OpenSearch, Qdrant, Milvus, and pgvector all ship native BM25+vector hybrid with RRF built in. Hybrid fixes recall (both answers get retrieved); a reranker after it fixes precision (the best one lands at #1) before the LLM reads a word. Try the live engine — flip queries, fusion methods, and the normalize toggle: https://dev48v.infy.uk/ai/days/day57-hybrid-search.html

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dev48v/hybrid-search-fuse-bm25-and-dense-vectors-with-reciprocal-rank-fusion-no-shared-scale-3i94

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
