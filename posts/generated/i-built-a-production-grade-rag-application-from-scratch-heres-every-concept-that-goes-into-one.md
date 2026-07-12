---
title: "I Built a Production-Grade RAG Application From Scratch — Here's Every Concept That Goes Into One"
slug: "i-built-a-production-grade-rag-application-from-scratch-heres-every-concept-that-goes-into-one"
author: "Suman Nath"
source: "devto_ai"
published: "Sun, 12 Jul 2026 13:35:29 +0000"
description: ""Chat with your documents" sounds simple. Then you actually build it, and you discover that a good RAG system is really seven or eight systems wearing a tren..."
keywords: "rag, embedding, graph, every, one, token, you, chunks"
generated: "2026-07-12T13:38:55.221737"
---

# I Built a Production-Grade RAG Application From Scratch — Here's Every Concept That Goes Into One

## Overview

"Chat with your documents" sounds simple. Then you actually build it, and you discover that a good RAG system is really seven or eight systems wearing a trench coat. I recently finished myRAG — a self-hosted, Dockerized RAG stack (FastAPI + React + Qdrant + PostgreSQL + Neo4j) — and I want to walk through the concepts behind every stage, because each one taught me something. Access the repo here: https://github.com/sumannath/myRAG Document Parsing — garbage in, garbage out Everything starts with turning PDFs, DOCX, and HTML into clean text. I use Docling as a dedicated parsing service: it converts documents into structured Markdown, preserving headings and tables instead of producing a soup of characters. The concept here: your retrieval quality is capped by your parsing quality. No embedding model can recover structure that was destroyed at ingestion. Chunking — the most underrated decision in RAG LLMs can't attend to a 200-page document, so we split it. But chunking is a trade-off: chunks too large dilute the embedding signal; too small lose context. I use recursive chunking (~512 tokens with overlap) so sentences aren't cut mid-thought. The overlap matters — it stops answers from falling into the gap between two chunks. Dense + Sparse Embeddings — two kinds of "similar" This is where most tutorials stop at one embedding model. I index every chunk twice: Dense vectors (Qwen3-Embedding, 4096-dim) capture semantic similarity — "Q3 revenue" matches "third-quarter earnings." Sparse BM25 vectors (computed locally with fastembed) capture lexical similarity — exact keywords, product codes, names that embedding models fumble. The concept: dense retrieval understands meaning, sparse retrieval respects precision. You want both, because users ask both kinds of questions. Hybrid Search with Reciprocal Rank Fusion At query time, Qdrant runs both searches and merges them with RRF (Reciprocal Rank Fusion) — a beautifully simple algorithm that combines ranked lists without needing to normalize incomparable scores. A document ranked well by either method surfaces; one ranked well by both wins. Reranking — a second, smarter opinion Vector search is fast but shallow: it compares a query against chunks that were embedded without knowing the question. A cross-encoder reranker (Cohere rerank via OpenRouter) reads the query and each candidate chunk together and rescores them. Retrieve 10 broadly, rerank to the best 5. This two-stage funnel — cheap recall, expensive precision — is the same pattern search engines have used for decades. Knowledge Graph — RAG that can connect the dots Pure vector RAG struggles with relational questions ("Who reports to the person who founded X?"). During ingestion, an LLM extracts (subject, relation, object) triples from every chunk into Neo4j. At query time, entities are extracted from the question, matched against the graph, and their 1-hop neighborhood is injected into the prompt as structured facts. It's GraphRAG-lite: the vector store answers "what's relevant," the graph answers "how things relate." Conversation Memory + Token Budgeting — respecting the context window Multi-turn chat needs history, but context windows aren't infinite. Two mechanisms: Rolling summarization: after N turns, older exchanges get compressed into a running summary by a small LLM, so long conversations don't eat the prompt. Token budgeting: before generation, the prompt is assembled against a hard token cap — lowest-ranked chunks are dropped first, and the user's question is always protected. The concept: context is a budget, and every token of history you keep is a token of evidence you can't include. Parallelism — the difference between 90 seconds and 15 Ingestion is embarrassingly parallel: embedding API calls, local BM25 encoding, and per-chunk graph extraction are all independent I/O. A shared thread pool fans out embedding sub-batches, runs sparse encoding concurrently with dense calls, and extracts facts from all chunks in parallel. At query time, the graph lookup overlaps with retrieval and reranking. Same hardware, same models — several times faster, purely from overlapping waits. The unglamorous parts that make it "production" Referential integrity: one UUID ties every document across Postgres (metadata), Qdrant (vectors), and Neo4j (facts) — deletes cascade cleanly through all three. Streaming UX: ingestion and chat stream progress over SSE, so the UI shows parsing → chunking → embedding → graph → done live. Auth: every endpoint requires a bearer token; the React build bakes in its key at build time from an env file, keeping secrets out of the login flow entirely. Config as code: one YAML file, zero hardcoded values; secrets live in .env. The takeaway RAG isn't one technique — it's a pipeline of small, well-understood ideas: parse cleanly, chunk thoughtfully, index twice, fuse ranks, rerank deeply, add structure with a graph, budget your tokens, and parallelize the waits. None of these steps is hard alone. The engineering is in making them agree with each other. Happy to share more about any stage — especially hybrid search and the knowledge-graph layer, which delivered the biggest quality jumps. RAG #LLM #GenAI #VectorSearch #KnowledgeGraph #Qdrant #Neo4j #FastAPI #React #OpenSource #AIEngineering

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/sumanpro/i-built-a-production-grade-rag-application-from-scratch-heres-every-concept-that-goes-into-one-3a22

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
