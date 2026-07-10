---
title: "Vector search kept missing rootstock codes, so I went hybrid"
slug: "vector-search-kept-missing-rootstock-codes-so-i-went-hybrid"
author: "Kantemir Satibalov"
source: "devto_python"
published: "Fri, 10 Jul 2026 07:48:43 +0000"
description: "Grounded RAG in production (8 Part Series) I stopped trusting generic LLMs for horticulture — so I built a grounded assistant on ~500 scientific articles 68 ..."
keywords: "vector, search, query, scores, eval, top, coming, soon"
generated: "2026-07-10T09:45:24.781749"
---

# Vector search kept missing rootstock codes, so I went hybrid

## Overview

Grounded RAG in production (8 Part Series) I stopped trusting generic LLMs for horticulture — so I built a grounded assistant on ~500 scientific articles 68 questions before a single token: eval-first RAG Vector search kept missing rootstock codes, so I went hybrid — you are here Scientific articles aren't FAQ-shaped: chunking a 500-article corpus — coming soon Gate the answer, not just the retrieval: verifying LLM output against sources — coming soon Go for the product, Python for the models: anatomy of a two-service RAG — coming soon Hardening a side project like it's production (and the outage that caused) — coming soon One RAG platform, swappable domains: what 500 articles taught me about product shape — coming soon When the eval suite first ran against pure vector search, the failures clustered in one place: exact identifiers . Rootstock codes like "SK-4", cultivar names, dosage lines. Embeddings are great at "this paragraph is about slope planting" and terrible at "this exact token matters more than the topic." A typical miss looked like this — vector search returned paragraphs about rootstocks, but not the cultivar token the eval expected: The fix wasn't a bigger model. It was accepting that I needed two retrievers with opposite failure modes, and a principled way to merge them. The pipeline query └─ glossary expansion (synonyms appended) ├─ Chroma vector search (multilingual-e5-small), top-16, filtered by crop └─ BM25 per-crop index, top-16 └─ RRF merge → candidates └─ cross-encoder rerank (bge-reranker-base) — only for some categories └─ per-article diversification → top-8 fragments Every stage exists because a specific eval failure demanded it. Layer by layer: Embeddings: intfloat/multilingual-e5-small . Multilingual because the corpus is Russian and queries can be either language. One non-obvious gotcha: e5 models require query: / passage: prefixes at query and index time. Without them similarity scores quietly degrade — no error, just worse ranking. I subclassed the embedding wrapper so the prefixes can't be forgotten. BM25, one index per crop. Classic lexical scoring over tokenized chunks. This is what catches "SK-4" — the exact token is either in the chunk or it isn't. The indexes are built at reindex time and persisted alongside the vector store, so a container restart doesn't silently drop the lexical half (an early bug the eval caught: exact-code questions failing while everything else passed). RRF merge. Reciprocal Rank Fusion is embarrassingly simple — each list contributes 1 / (k + rank) per document, sum, sort (k=60): def rrf_merge ( rankings , k = 60 ): scores = {} for ranking in rankings : for rank , chunk_id in enumerate ( ranking ): scores [ chunk_id ] = scores . get ( chunk_id , 0.0 ) + 1.0 / ( k + rank + 1 ) return [ cid for cid , _ in sorted ( scores . items (), key = lambda x : - x [ 1 ])] I tried score normalization schemes first. RRF won because it needs no calibration between BM25 scores and cosine similarities — it only trusts ranks — and it's ten lines you can hold in your head. Conditional reranking. A cross-encoder ( BAAI/bge-reranker-base ) reads the query and each candidate together and re-scores the top candidates. It measurably improves ranking for dense technical questions — and costs real CPU time. So it's category-gated: the question classifier (rule-based, config-driven) tags questions as rootstock , disease , variety , fertilizer , relief , or general , and only the complex categories pay the reranker tax. "When should I water?" doesn't need a cross-encoder. Glossary expansion. A curated JSON of domain synonyms; if the query contains a known term, its synonyms are appended to the search string. This is where user vocabulary meets literature vocabulary — the colloquial disease name pulls in Marssonina spellings the embeddings alone ranked too low. Curated beats automatic here: the glossary is small, reviewable, and each entry exists because a real query missed. Diversification. Top-ranked chunks tend to come from the same article. The last step caps fragments per source before returning the top-8, so the LLM sees multiple studies instead of one article shredded eight ways. What I didn't do Fine-tune embeddings. Tempting, but the eval said ranking was mostly fine once lexical search covered the identifier cases. Not worth the MLOps overhead yet. LLM query rewriting. Adds latency and a failure mode to the cheap half of the system. The glossary covers the actual observed misses deterministically. A vector DB migration. Chroma with a persistent local directory is unglamorous and entirely sufficient at ~14.5k chunks. The interesting problems were above the storage layer. Results With the full stack, the 68-question suite passes at 100% retrieval, and — the part I care about more — hit_rate@3 stays high enough that the LLM's context isn't padded with near-misses (apple suite: MRR 0.938, hit@3 0.953). With --fast (reranker off) it still passes 68/68 today, which tells me the reranker is currently insurance rather than load-bearing. I keep it because insurance is what you want the week a new corpus batch lands.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/kantik001/vector-search-kept-missing-rootstock-codes-so-i-went-hybrid-37li

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
