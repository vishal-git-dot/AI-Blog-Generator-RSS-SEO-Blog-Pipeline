---
title: "TOBER FEST"
slug: "tober-fest"
author: "Rathnam.S"
source: "devto_ai"
published: "Mon, 05 Oct 2026 04:56:53 +0000"
description: "What I Built I built SecondMind — a local-first second brain that runs on your own laptop. The idea came from building something useful for a friend who ofte..."
keywords: "memory, memories, can, secondmind, open, project, model, ollama"
generated: "2026-10-05T05:01:22.636616"
---

# TOBER FEST

## Overview

What I Built I built SecondMind — a local-first second brain that runs on your own laptop. The idea came from building something useful for a friend who often has to repeatedly remember and search through personal notes, study plans, preferences, and project context. Instead of relying on a cloud AI service that sends everything to a remote server, SecondMind stores memories locally and uses a local open-weight model to understand conversations and retrieve relevant information when needed. You can talk to it normally, and it can remember useful information, recall relevant memories later, and forget information when asked. For example: "I'm studying DSA and I'm currently focusing on dynamic programming." Later: "What am I studying right now?" SecondMind can retrieve the relevant memory and use it to answer. The goal isn't to build another generic chatbot. It's to build a small personal memory layer that belongs to the person using it. Demo The project runs locally with Django and Ollama. Code https://github.com/RathnamS089/secondmind The project is built around a simple architecture: Browser ↓ Django ↓ SecondMind Agent ├── Memory Tools │ ├── Remember │ ├── Recall │ └── Forget │ ├── Retrieval │ └── Cosine Similarity │ └── Ollama ├── Qwen 2.5 1.5B └── nomic-embed-text How I Built It SecondMind is built with Django, SQLite, NumPy and Ollama . For the language model, I used the open-weight Qwen 2.5 1.5B model through Ollama. For memory retrieval, I use nomic-embed-text to convert both the user's query and stored memories into embedding vectors. When a user asks something that might require memory: User query ↓ Embedding ↓ Compare with stored memory embeddings ↓ Cosine similarity ↓ Rank memories ↓ Relevant memories ↓ Qwen ↓ Response The memory system also has three tools: Remember — stores a memory and its embedding locally. Recall — searches stored memories using semantic similarity. Forget — removes a stored memory. The agent can decide when to use these tools, while the UI also provides direct access to them through a Tools menu. Everything is orchestrated through Django, while OllamaClient is kept as the single layer responsible for communicating with Ollama. Why Does Open Innovation Matter? This project wouldn't have the same meaning if the AI depended on a closed API. The most important part of SecondMind is that the memories belong to the user and the model can run locally. The entire system can run on a laptop without sending personal memories to a third-party AI provider. Using open-weight models also means I can experiment. I can change: Qwen 2.5 1.5B to another compatible open-weight model without redesigning the entire application. I can also inspect how the memory system works, change the retrieval strategy, change the agent's behavior, fine-tune models in the future, and experiment with different embedding models. For a personal memory assistant, that control matters more to me than simply calling the most powerful closed model available. The project is also intentionally small enough to understand: Django + SQLite + Ollama + Open-weight models + Local embeddings There is no cloud database and no mandatory paid AI API sitting between the user and their memories. That is where open innovation worked better for this project: I wasn't just consuming an AI service — I could actually build the AI system around the way I wanted it to work.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/rathnams089/tober-fest-3dg2

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
