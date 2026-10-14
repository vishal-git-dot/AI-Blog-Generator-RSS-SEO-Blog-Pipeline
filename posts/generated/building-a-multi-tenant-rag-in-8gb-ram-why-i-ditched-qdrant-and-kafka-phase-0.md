---
title: "Building a Multi-Tenant RAG in 8GB RAM: Why I Ditched Qdrant and Kafka (Phase 0)"
slug: "building-a-multi-tenant-rag-in-8gb-ram-why-i-ditched-qdrant-and-kafka-phase-0"
author: "Alejandro Tacoronte González"
source: "devto_python"
published: "Wed, 14 Oct 2026 21:11:58 +0000"
description: "I have 8 GB of RAM and 6 vCPUs . With those specs, I'm building and running a full production-ready RAG system. I’m not self-hosting the LLM. I’m not spinnin..."
keywords: "ram, not, every, vector, multi, tenant, rag, qdrant"
generated: "2026-10-14T21:28:09.485989"
---

# Building a Multi-Tenant RAG in 8GB RAM: Why I Ditched Qdrant and Kafka (Phase 0)

## Overview

I have 8 GB of RAM and 6 vCPUs . With those specs, I'm building and running a full production-ready RAG system. I’m not self-hosting the LLM. I’m not spinning up Qdrant. I’m not adding Kafka. Those aren't my personal preferences—they are constraints strictly dictated by the hardware. When you run a JVM alongside a Python AI worker on an 8 GB machine, every megabyte counts. Today, I’m starting to build Corpus in public: a document chat platform where every answer strictly cites its sources, and each organization's data remains completely isolated from the rest (strict multi-tenancy). The Stack (100% Dockerized) Backend API: Java 21 + Spring Boot 4 AI & Embeddings Service: Python + FastAPI Storage & Vector DB: PostgreSQL ( pgvector ) + Redis Frontend: React Why this architecture? PostgreSQL + pgvector over Qdrant/Milvus: Maintaining a dedicated vector database alongside a relational DB in 8 GB of RAM is overkill. Keeping relational metadata and vector embeddings in the same engine simplifies transactions and saves precious memory. Redis over Kafka: I need asynchronous processing for document ingestion, not a massive distributed event-streaming cluster eating up heap memory. Current Status: Phase 0 All 5 services spin up cleanly with a single docker compose up , and the core system design is locked in the repository. There is no live demo yet. Next step: The ingestion pipeline—turning raw PDFs into queryable vector chunks without triggering the Linux OOM killer. I’ll be documenting every architectural trade-off and every failure along the way. 🔗 GitHub Repository: aletgdev/corpus-rag Looking for advice from the community 👇 For those of you who have built something similar under tight resource constraints: How would you handle local embedding generation within an 8 GB RAM budget while guaranteeing strict multi-tenant isolation in pgvector ? (e.g., Row-Level Security vs. schema-per-tenant vs. metadata filtering). Any war stories or tips are more than welcome in the comments!

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/alejandrotg-code/building-a-multi-tenant-rag-in-8gb-ram-why-i-ditched-qdrant-and-kafka-phase-0-8b

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
