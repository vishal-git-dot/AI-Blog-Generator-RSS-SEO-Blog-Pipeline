---
title: "Hybrid Search for RAG: Why Your Vector Search Misses "TS-999" (and the 20-Line Fix)"
slug: "hybrid-search-for-rag-why-your-vector-search-misses-ts-999-and-the-20-line-fix"
author: "M.T.Ramkrushna"
source: "devto_python"
published: "Mon, 19 Oct 2026 03:39:27 +0000"
description: "A user types: "How do I fix error TS-999?" Your RAG app runs a vector search, pulls five chunks about error codes in general , and the model writes a confide..."
keywords: "search, your, vector, int, chunks, exact, you, query"
generated: "2026-10-19T04:06:19.788070"
---

# Hybrid Search for RAG: Why Your Vector Search Misses "TS-999" (and the 20-Line Fix)

## Overview

A user types: "How do I fix error TS-999?" Your RAG app runs a vector search, pulls five chunks about error codes in general , and the model writes a confident, useless answer. The one doc that literally says "TS-999" never made it into the prompt. That is not a model problem. It is a retrieval problem, and it has a boring, reliable fix: hybrid search . Why pure vector search misses exact matches Embeddings are great at meaning. "Reset my password" and "I can't log in" land close together, which is exactly what you want. But embeddings compress text into a point in space. Rare, exact tokens get blurred in that compression: Error codes and ticket IDs ( TS-999 , INC-4821 ) SKUs, part numbers, invoice numbers Function and config names ( max_retries , PG_POOL_SIZE ) Names of people, products, and internal tools To an embedding model, TS-999 and TS-998 look almost identical. To your user, they are completely different problems. Anthropic's Contextual Retrieval write-up uses this exact example: an embedding model "might find content about error codes in general, but could miss the exact 'TS-999' match." Keyword search finds it instantly. The fix: run both searches, then fuse the rankings Hybrid search means you run two retrievers on every query: BM25 (keyword search). Scores chunks by exact term matches, weighted by how rare the term is. It is the classic search-engine ranking function and it loves IDs and jargon. Vector search (semantic). Scores chunks by meaning. It handles paraphrases, synonyms, and vague questions. Then you merge the two ranked lists. The simplest merge that works well is Reciprocal Rank Fusion (RRF) : score(chunk) = Σ 1 / (k + rank_in_list) You add up the score from each list the chunk appears in. k is a constant, usually 60 , from the original RRF paper by Cormack, Clarke and Büttcher (SIGIR 2009) . Elasticsearch uses the same default for its rank_constant in its RRF docs . The nice part: RRF only looks at ranks , not raw scores. You never have to figure out how a BM25 score of 14.2 compares to a cosine similarity of 0.81. A minimal Python version This uses rank_bm25 for keyword search and whatever vector search you already have. from rank_bm25 import BM25Okapi chunks = load_chunks () # list[str] bm25 = BM25Okapi ([ c . lower (). split () for c in chunks ]) def keyword_search ( query : str , n : int = 50 ) -> list [ int ]: scores = bm25 . get_scores ( query . lower (). split ()) return sorted ( range ( len ( chunks )), key = lambda i : scores [ i ], reverse = True )[: n ] def vector_search ( query : str , n : int = 50 ) -> list [ int ]: ... # your existing embedding search, returning chunk indices in rank order def rrf ( * ranked_lists : list [ int ], k : int = 60 ) -> list [ int ]: fused : dict [ int , float ] = {} for ranked in ranked_lists : for rank , idx in enumerate ( ranked , start = 1 ): fused [ idx ] = fused . get ( idx , 0.0 ) + 1.0 / ( k + rank ) return sorted ( fused , key = fused . get , reverse = True ) def hybrid_search ( query : str , top_k : int = 10 ) -> list [ str ]: ids = rrf ( keyword_search ( query ), vector_search ( query )) return [ chunks [ i ] for i in ids [: top_k ]] In production you usually don't hand-roll BM25. Postgres full-text search, Elasticsearch/OpenSearch, and vector databases like Weaviate ship hybrid search built in. The logic is the same. How much does it help? In Anthropic's experiments across codebases, fiction, and papers, combining embeddings with BM25 beat embeddings alone, and adding context to chunks plus BM25 cut top-20 retrieval failures by 49% (5.7% to 2.9%). Adding a reranker on top cut failures by 67% (5.7% to 1.9%). Source: Introducing Contextual Retrieval . Your numbers will differ. That's why the next section matters. A practical rollout plan Collect 30–50 real queries from logs, and make sure some contain IDs, codes, or exact names. Label the right chunk for each query. Measure recall@10 for vector-only search. That's your baseline. Add BM25 + RRF and measure again. Look especially at the ID-heavy queries. Optionally add a reranker (retrieve ~50–150, rerank, keep the top 10–20). Keep the eval set in the repo so the next "small retrieval tweak" can't silently undo it. When you can skip it Your queries are all fuzzy, natural-language questions with no IDs or jargon. Your knowledge base is small enough to just put in the prompt (Anthropic suggests under ~200k tokens is worth trying first). Everyone else: if your users ever type a code, a name, or a number, give them keyword search back. TL;DR Vector search is great at meaning and bad at exact tokens. BM25 is great at exact tokens and bad at meaning. Run both, merge with Reciprocal Rank Fusion (k = 60), and measure recall on real queries. References Anthropic, Introducing Contextual Retrieval (Sep 2024) Cormack, Clarke, Büttcher, Reciprocal Rank Fusion outperforms Condorcet and individual Rank Learning Methods (SIGIR 2009) Elastic, Reciprocal rank fusion docs Weaviate, Hybrid search docs rank_bm25 on GitHub What's in your retrieval stack today: vector-only, or hybrid?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/m_t_ramkrushna/hybrid-search-for-rag-why-your-vector-search-misses-ts-999-and-the-20-line-fix-koa

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
