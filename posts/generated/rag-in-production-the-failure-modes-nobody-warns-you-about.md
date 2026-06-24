---
title: "RAG in production: the failure modes nobody warns you about"
slug: "rag-in-production-the-failure-modes-nobody-warns-you-about"
author: "Mridul Nagpal"
source: "devto_ai"
published: "Wed, 24 Jun 2026 03:55:15 +0000"
description: "Retrieval-augmented generation looks trivial in a tutorial: embed some documents, drop them in a vector database, stuff the top matches into a prompt, done. ..."
keywords: "you, rag, retrieval, model, real, context, production, data"
generated: "2026-06-24T04:04:51.777643"
---

# RAG in production: the failure modes nobody warns you about

## Overview

Retrieval-augmented generation looks trivial in a tutorial: embed some documents, drop them in a vector database, stuff the top matches into a prompt, done. Then you point it at real company data and real users, and you discover that the demo was the easy 10%. We build RAG systems over private knowledge for companies, and almost every painful bug traces back to the same handful of failure modes. Here they are, and what actually fixes them. 1. Retrieval returns the wrong chunks — and the model uses them anyway The single biggest source of "wrong" RAG answers isn't the LLM. It's retrieval handing it irrelevant or partial context, which the model then summarizes with total confidence. Naive fixed-size chunking splits a table from its header, or a clause from the sentence that negates it. The fix is unglamorous data engineering: chunk on semantic boundaries, not character counts; add a reranking step so the top-k you actually pass is the top-k by relevance, not by raw vector distance; and store enough metadata to filter before you search. Retrieval quality sets the ceiling on everything downstream. 2. The model answers beyond its context Even with perfect retrieval, an LLM will happily fill gaps with plausible invention. In a RAG system that's worse than no answer, because it looks sourced. Force grounding: instruct the model to answer only from the retrieved context and to say "I don't know" when the context doesn't cover it — then verify that with citations that point back to specific chunks. If you can't trace a sentence to a source, treat it as a hallucination, not an answer. 3. The knowledge goes stale, and nobody notices RAG is only as good as the index behind it. Documents change, get duplicated, get deleted — and a pipeline that ingested once at launch quietly serves last quarter's truth. The unsexy work is the ingestion pipeline: incremental re-indexing, de-duplication, and a freshness signal so old content can be down-weighted or expired. 4. You have no evals, so you're guessing "The new embedding model feels better" is not an engineering statement. Without a held-out set of real questions with known-good answers, every change is a coin flip — you fix one query and silently break five. Build an eval set early, measure retrieval hit-rate and answer faithfulness on every change, and treat a regression like a failing test. 5. Latency and cost sneak up on you Embedding the query, searching, reranking, and stuffing a large context into a big model adds up — in both seconds and dollars. Cache embeddings and frequent queries, retrieve fewer-but-better chunks rather than dumping everything, and reserve the largest model for the steps that genuinely need it. The pattern underneath all of these Notice what's missing from that list: clever prompting. Production RAG is a data and retrieval engineering problem wearing an AI costume. The teams whose RAG holds up aren't the ones with the fanciest prompt — they're the ones who treat ingestion, chunking, retrieval, and evaluation as real systems with real tests. That's the lens we bring from years of building data systems at scale before this wave. If you're moving a RAG prototype toward something users can actually trust in production, that's the kind of RAG and knowledge-AI work we do at Krazimo . What's bitten you hardest in a production RAG system? I'll dig into specifics in the comments.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/mridul_nagpal_e33b6be1260/rag-in-production-the-failure-modes-nobody-warns-you-about-62i

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
