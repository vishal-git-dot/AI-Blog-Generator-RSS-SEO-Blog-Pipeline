---
title: "I Built a Production RAG System on My M1 Mac for $0"
slug: "i-built-a-production-rag-system-on-my-m1-mac-for-0"
author: "Alex Bogle"
source: "devto_ai"
published: "Wed, 10 Jun 2026 04:09:35 +0000"
description: "I Built a Production RAG System on My M1 Mac for $0 Most RAG tutorials stop at "it answers questions." But answering questions is table stakes. The real ques..."
keywords: "rag, all, system, answers, you, ollama, mac, source"
generated: "2026-06-10T04:15:10.543230"
---

# I Built a Production RAG System on My M1 Mac for $0

## Overview

I Built a Production RAG System on My M1 Mac for $0 Most RAG tutorials stop at "it answers questions." But answering questions is table stakes. The real question is: are the answers actually correct? I built a RAG pipeline that doesn't just retrieve and generate — it evaluates whether its own answers are faithful to the source material and relevant to the question. All running locally on an M1 Mac with 16GB RAM. Zero cloud cost. What I Built A full RAG system with three layers most tutorials skip: Retrieval — Upload PDFs or paste text, get chunked and embedded into a local vector store Generation — Ask questions, get streaming answers backed by retrieved context with source citations Evaluation — Run an automated test suite that scores every answer for faithfulness and relevance using an LLM-as-judge, then logs all metrics to MLflow for experiment tracking Why Evaluation Matters Anyone can build a RAG that produces plausible-sounding answers. The hard part is knowing whether those answers are grounded in the source material or just confident hallucinations. My evaluation pipeline measures three things: Faithfulness (1-5): Is the answer actually supported by the retrieved chunks? Or is the LLM making stuff up? Relevance (1-5): Does the answer match the ground truth reference for the given question? Retrieval Accuracy (%): What percentage of key terms from the reference answer actually appear in the retrieved chunks? All three metrics get logged to MLflow, so you can compare different chunk sizes, overlap values, and model choices across runs. Architecture The whole stack runs locally: FastAPI backend with async streaming responses ChromaDB as the vector store (embedded, no separate server) all-MiniLM-L6-v2 (sentence-transformers) for embeddings — 80MB, fast on CPU qwen3:4b (Ollama) for generation — 2.5GB, no API keys needed MLflow for experiment tracking — params, metrics, all logged Vanilla HTML/CSS/JS frontend — dark theme, chat UI, PDF upload, eval controls Why Not Ollama Embeddings? I started with Ollama's /api/embeddings endpoint using nomic-embed-text. On my M1 Mac, it was painfully slow — 30+ seconds per embedding call. Switched to sentence-transformers running the same all-MiniLM-L6-v2 model locally in-process. First call loads the model in ~2 seconds. Subsequent embeddings: ~18ms each. Night and day. The Code The entire project is open source. Key files: rag_engine.py — Chunking, embedding, vector storage, retrieval llm_client.py — Ollama client with sync and streaming generation evaluator.py — LLM-as-judge scoring for faithfulness and relevance tracker.py — MLflow experiment tracking wrapper app.py — FastAPI routes tying it all together seed.py — Sample data seeding script Tests are fully mocked — no Ollama or model files required. Full suite runs in ~30 seconds. What I Learned Evaluation is not optional. If you can't measure answer quality, you're shipping a chatbot, not a system. Local-first is viable. Everything runs on a $1,200 laptop. No cloud credits, no API keys, no vendor lock-in. Streaming matters for UX. SSE streaming makes the UI feel responsive even when the LLM takes a few seconds to generate. Mock your external dependencies. Tests that call real LLMs are slow and flaky. Mock the HTTP layer, test your logic. Try It Yourself The repo includes a seed script with sample data so you can go from clone to running in under 5 minutes. Just need Python 3.9+ and Ollama with qwen3:4b. git clone https://github.com/SaintChris/rag-eval-system.git cd rag-eval-system/backend python3 -m venv venv && source venv/bin/activate pip install -r requirements.txt python3 seed.py python3 run.py Open http://localhost:8001/docs for the interactive API docs. What's Next This is Project 1 of 5 in my portfolio rebuild. Next up: a Hermes MLOps case study showing how I run a 6-agent AI system with 22K+ requests, 52 tests, and $0 cloud spend — all on this same M1 Mac. If you're building RAG systems and not evaluating them, you're flying blind. Build the eval pipeline first. Everything else follows.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/saintchris_21/i-built-a-production-rag-system-on-my-m1-mac-for-0-5cn8

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
