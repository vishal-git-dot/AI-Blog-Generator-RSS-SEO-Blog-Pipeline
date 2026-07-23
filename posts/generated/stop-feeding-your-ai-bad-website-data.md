---
title: "Stop Feeding Your AI Bad Website Data"
slug: "stop-feeding-your-ai-bad-website-data"
author: "lukas schmeck"
source: "devto_python"
published: "Thu, 23 Jul 2026 18:38:48 +0000"
description: "If you've ever built a RAG application, AI agent, or documentation chatbot, you've probably experienced this: Your LLM gives a confident answer... but it's c..."
keywords: "you, documentation, your, data, more, context, website, rag"
generated: "2026-07-23T19:26:23.864095"
---

# Stop Feeding Your AI Bad Website Data

## Overview

If you've ever built a RAG application, AI agent, or documentation chatbot, you've probably experienced this: Your LLM gives a confident answer... but it's completely wrong. Most of the time, the model isn't the problem. The data is. The Hidden Problem A lot of developers scrape websites and immediately convert the HTML into Markdown or plain text. Unfortunately, real websites contain much more than the actual content: Navigation menus Cookie banners Sidebars Footer links Tracking scripts Related articles Advertisement blocks All of this ends up inside your embeddings. Instead of embedding actual documentation, you're embedding a mixture of useful information and website noise. The result? Worse retrieval quality Higher token usage Lower embedding quality More hallucinations What Good AI Data Looks Like For RAG, your documents should preserve the structure of the original content while removing everything that isn't relevant. A good document should: Keep headings and hierarchy Preserve code blocks Preserve tables Remove navigation and boilerplate Keep the surrounding context of each section For example, instead of storing this: Home Pricing Documentation Login Installation Guide pip install my-package Related Articles Privacy Policy you want something closer to this: Context: Documentation > Getting Started > Installation # Installation Guide Install the package: ``` bash pip install my-package Configure your environment variables before initialization. That difference has a surprisingly large impact on retrieval quality. ## Context Matters One thing I found especially important is preserving document hierarchy. Imagine two pages both containing a section called **Authentication**. Without context, they're nearly identical. With context, they become: Documentation > REST API > Authentication and Documentation > Admin Panel > Authentication That additional information makes retrieval much more accurate. ## Building a Better Pipeline While experimenting with different extraction approaches, I ended up building a crawler focused specifically on AI ingestion rather than traditional web scraping. The goal wasn't simply to download HTML. The goal was to produce clean, structured Markdown that can go directly into embedding pipelines and vector databases. The pipeline focuses on: - Removing website boilerplate - Preserving document structure - Keeping code blocks and tables intact - Adding contextual breadcrumbs - Generating useful metadata - Producing AI-ready Markdown ## Final Thoughts As LLMs become more capable, data quality becomes even more important. Many teams spend weeks experimenting with prompts or models while feeding their AI noisy website data. Improving your ingestion pipeline often delivers bigger improvements than changing the model itself. Garbage in still means garbage out. --- I'm currently building an Apify Actor that automates this workflow by converting websites and documentation portals into clean, RAG-ready Markdown. If you're working on AI agents or RAG systems, I'd love to hear how you're handling web content ingestion and what challenges you've run into.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/lukas_schmeck/stop-feeding-your-ai-bad-website-data-2gp8

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
