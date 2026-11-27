---
title: "Debugging a RAG app in an interview: split retrieval from generation"
slug: "debugging-a-rag-app-in-an-interview-split-retrieval-from-generation"
author: "Valenx"
source: "devto_ai"
published: "Fri, 27 Nov 2026 20:54:17 +0000"
description: ""How would you build a RAG pipeline?" is the most common AI engineer design question. The usual answer lists parts: vector DB, embeddings, LLM. The step that..."
keywords: "answer, retrieved, hits, rag, split, question, prompt, model"
generated: "2026-11-27T20:56:45.961567"
---

# Debugging a RAG app in an interview: split retrieval from generation

## Overview

"How would you build a RAG pipeline?" is the most common AI engineer design question. The usual answer lists parts: vector DB, embeddings, LLM. The step that gets skipped is the one that makes it work: the retrieved passages have to go into the prompt, with the question, before the model answers. Say the full path in order 1. Ingest and clean documents, then split into chunks (a few hundred tokens with overlap is a fine start). 2. Embed chunks and index them. Add keyword search (BM25) for exact terms like product codes. 3. At query time: retrieve candidates (hybrid), rerank, keep the top few. 4. Assemble the prompt: instructions + retrieved passages + the question. Ask for citations and allow "not enough information". 5. Evaluate retrieval (was the right chunk retrieved?) separately from generation (did the answer use it faithfully?). The follow-up: "Your RAG app gives wrong answers. How do you debug it?" Split it. If the right chunk was not retrieved, fix chunking, embeddings, hybrid search or filters. If it was, fix the prompt, the context noise or the model. for q , gold_chunk_id , gold_answer in eval_set : hits = retrieve ( q , k = 5 ) retrieval_ok = gold_chunk_id in [ h . id for h in hits ] answer = generate ( q , hits ) record ( q , retrieval_ok , faithful ( answer , hits ) , correct ( answer , gold_answer ) ) 90-second drill: say steps 1-5 out loud without notes, then answer the debug follow-up. 12 must-know questions with model answers, free cheat sheet → https://valenx.org/go/free-aie?utm_source=devto&utm_medium=article&utm_campaign=dp1127&utm_content=D02 Valenx Press. Practice material, no interview promise.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/valenx/debugging-a-rag-app-in-an-interview-split-retrieval-from-generation-4plf

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
