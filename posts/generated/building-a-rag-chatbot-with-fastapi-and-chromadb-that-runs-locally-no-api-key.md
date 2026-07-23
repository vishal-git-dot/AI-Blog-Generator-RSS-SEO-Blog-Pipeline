---
title: "Building a RAG Chatbot with FastAPI and ChromaDB (that runs locally, no API key)"
slug: "building-a-rag-chatbot-with-fastapi-and-chromadb-that-runs-locally-no-api-key"
author: "deaw.ai"
source: "devto_python"
published: "Thu, 23 Jul 2026 13:57:14 +0000"
description: "Everyone wants a chatbot that can answer questions from their own documents — a company handbook, a contract, a research paper. The technique behind this is ..."
keywords: "chunks, rag, question, llm, you, chatbot, vector, key"
generated: "2026-07-23T14:15:19.711216"
---

# Building a RAG Chatbot with FastAPI and ChromaDB (that runs locally, no API key)

## Overview

Everyone wants a chatbot that can answer questions from their own documents — a company handbook, a contract, a research paper. The technique behind this is called RAG (Retrieval-Augmented Generation) . I build production RAG and LLM systems for a living, and I kept re-wiring the same foundation on every project. So I cleaned it up into a small, open-source starter. This post walks through how RAG actually works, the design decisions that matter, and how you can run the whole thing for free — no API key required. At the end there's a link to the full open-source repo you can clone and run in minutes. Why RAG? An LLM like GPT or Claude only knows what it was trained on. Ask it about a document sitting on your laptop and it will guess — or hallucinate. RAG fixes this with a simple idea: retrieve the relevant information first, then let the LLM answer using only that. The result is answers grounded in your actual documents, with citations you can trace back to a specific page. The pipeline, in two paths Path 1 — Indexing (when a document comes in): Extract text from the PDF Split it into overlapping chunks Convert each chunk into a vector (an embedding) that captures its meaning Store those vectors in a vector database Path 2 — Querying (when a user asks something): Embed the question with the same model Search the vector database for the most similar chunks Send those chunks + the question to the LLM The LLM answers using that context, and we return the source pages Picking the stack After building a few of these, here's a stack that's easy to start with and holds up in production: FastAPI — fast to write, clean async APIs ChromaDB — a lightweight vector database that runs embedded, no separate server to manage SentenceTransformers — free embeddings, with multilingual models available Any LLM — OpenAI, Claude, Gemini, or local Ollama One detail people miss: you can test the whole pipeline without any API key , either in a retrieval-only mode that returns the matched chunks, or fully local with Ollama so nothing leaves your machine. The core of the retrieval step Here's roughly what the query side looks like — embed the question, search, hand the chunks to the LLM: def answer_question ( question : str , top_k : int = 3 ): # 1. Embed the question with the same model used at indexing time query_embedding = embed ( question ) # 2. Retrieve the most similar chunks from the vector store chunks = vector_store . search ( query_embedding , top_k = top_k ) # 3. Build a prompt grounded in those chunks, then ask the LLM context = " \n\n " . join ( c [ " text " ] for c in chunks ) answer = llm . generate ( question = question , context = context ) return answer , chunks # chunks double as citations The key constraint: use the same embedding model for the question and the documents. Vectors from different models aren't comparable, and this is a surprisingly common bug. Details that make or break quality From experience, whether a RAG system answers well comes down to a few things people underestimate: Chunk size. Too big and unrelated content bleeds together; too small and each chunk loses context. Overlap between chunks helps avoid cutting sentences mid-thought. Scanned PDFs. If the file is an image, normal text extraction returns nothing. You need an OCR fallback, or those pages silently index as empty. Re-ranking. Pure vector search is fast but coarse. Adding a cross-encoder re-ranker that reads the question and each chunk together noticeably improves which chunks you actually feed the model. Try it (free, open source) I packaged all of this into a starter template, open-sourced under MIT. Clone it, run one Docker command, and you have a working document Q&A chatbot with source citations. It's multilingual, and runs free with no API key. 👉 GitHub: https://github.com/panutpl/rag-chatbot-template-starter git clone https://github.com/panutpl/rag-chatbot-template-starter cd rag-chatbot-template-starter cp .env.example .env docker compose up --build Then open http://localhost:8000/docs , upload a PDF, and start asking questions. If you're building RAG or just getting started, I'd love feedback — especially on chunking and retrieval strategies, which I'm still tuning myself. Drop a comment about what's working for you.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/deaw_ai/building-a-rag-chatbot-with-fastapi-and-chromadb-that-runs-locally-no-api-key-36aj

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
