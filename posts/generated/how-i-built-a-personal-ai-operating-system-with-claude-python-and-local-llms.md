---
title: "How I Built a Personal AI Operating System with Claude, Python, and Local LLMs"
slug: "how-i-built-a-personal-ai-operating-system-with-claude-python-and-local-llms"
author: "Paul Holland"
source: "devto_python"
published: "Fri, 05 Jun 2026 15:08:07 +0000"
description: "Every AI conversation I had vanished the moment I closed the tab. Weeks of research, planning sessions, decision context — gone. So I built a system that fix..."
keywords: "atlas, search, vault, system, every, your, you, skills"
generated: "2026-06-05T15:19:56.043117"
---

# How I Built a Personal AI Operating System with Claude, Python, and Local LLMs

## Overview

Every AI conversation I had vanished the moment I closed the tab. Weeks of research, planning sessions, decision context — gone. So I built a system that fixes that. Atlas OS is an open-source "personal operating system" that wraps Claude Cowork with persistent memory, local RAG search, scheduled automation, and a web dashboard. It turns a stateless chatbot into something that remembers everything and works while you sleep. GitHub: paulholland511/atlas-os | pip install atlas-os The Architecture ┌─────────────────────────────────────────────┐ │ atlas CLI │ │ init · doctor · search · embed · dashboard │ ├──────────┬──────────┬───────────┬───────────┤ │ Vault │ RAG │ Skills │ Backends │ │ Parser │ Engine │ 160+ │ LM Studio│ │ Git Sync│ SQLite │ Market- │ Ollama │ │ Session │ BM25+Vec│ place │ llama.cpp│ │ Capture │ Rerank │ Registry │ OpenAI │ ├──────────┴──────────┴───────────┴───────────┤ │ Obsidian Markdown Vault │ │ (your files, your machine) │ └─────────────────────────────────────────────┘ The entire system is local-first. Your notes, embeddings, and knowledge graph never leave your machine. The "database" is a folder of markdown files. History is plain git. Everything is diffable, portable, and yours. Key Design Decisions Why SQLite for vectors (not Pinecone/Weaviate) I chose sqlite-vec for the vector store because it's zero-config, embeds directly in the process, and needs no running service. For a personal knowledge base with ~10K chunks, the KNN search is fast enough and the operational overhead is zero. There's a NumPy cosine fallback for environments without the C extension. Why hybrid search (not just embeddings) Pure vector search misses exact matches. Pure keyword search misses meaning. Atlas OS fuses both: BM25 scores every chunk by term frequency Vector cosine scores by semantic similarity Reciprocal Rank Fusion merges both ranked lists TF-IDF reranking refines the top results This consistently outperforms either approach alone, especially for a personal vault where you remember words you used but also need conceptual matches. Why Flask (not React) The dashboard ships as part of the Python package — atlas dashboard starts it. No npm install , no build step, no node_modules. Seven panels: system health, audit trail, scheduled tasks, skills, vector store stats, RAG search, and a D3.js knowledge graph. All rendered server-side with Jinja2 and inline CSS. What It Actually Does Day-to-Day The system runs scheduled tasks autonomously: Session capture — every Cowork conversation gets saved as a markdown note in your vault, twice daily. Summaries, key actions, files touched. RAG indexing — semantic chunking + embedding runs incrementally. New notes are searchable within minutes. Email briefings — a morning report lands in your inbox with vault status, pending tasks, and a system health check. Trading research — a multi-agent module writes market briefings into the vault (I use this for crypto research, not financial advice). The Numbers 400+ tests , CI/CD via GitHub Actions 160+ installable skills with a marketplace and registry Pluggable LLM backends — auto-detects LM Studio, Ollama, llama.cpp Append-only audit trail — every autonomous action logged to JSONL Docker support, MIT licensed What I Learned Session persistence is the killer feature. Everything else — RAG, dashboards, skills — only matters because the vault remembers. Without that, you're rebuilding context every session. Hybrid search is worth the complexity. The BM25 + vector + RRF pipeline was the single biggest quality improvement over pure embedding search. Local-first is a real constraint but worth it. No cloud dependencies means the system works offline, on planes, and never leaks data. But it means managing your own embedding server. Git as the sync layer is underrated. Every vault change is a commit. You get free versioning, branching, and conflict detection. The merge conflicts are the hard part (v3.0 roadmap addresses this). What's Next (v3.0) Extension architecture — decouple trading/voice/job modules into optional extras MCP skills — every skill becomes a Model Context Protocol server Security sandbox — AST analysis + runtime isolation for community skills Git hardening — proper merge strategies for concurrent vault access Pluggable vector backends — LanceDB and ChromaDB alongside sqlite-vec The repo is at github.com/paulholland511/atlas-os . Install with pip install atlas-os , run atlas init , and you're up in five minutes. Feedback and contributions welcome.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/paulholland511/how-i-built-a-personal-ai-operating-system-with-claude-python-and-local-llms-56e2

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
