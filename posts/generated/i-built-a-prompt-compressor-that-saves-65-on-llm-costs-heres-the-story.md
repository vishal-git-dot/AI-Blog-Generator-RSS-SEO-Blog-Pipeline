---
title: "I Built a Prompt Compressor That Saves 65% on LLM Costs — Here's the Story"
slug: "i-built-a-prompt-compressor-that-saves-65-on-llm-costs-heres-the-story"
author: "Arjun Shah"
source: "devto_python"
published: "Fri, 26 Jun 2026 19:45:49 +0000"
description: "I've been working on a side project called SuperCompress — an intelligent prompt compression system for LLMs. The idea is simple: most tokens you send to an ..."
keywords: "supercompress, tokens, context, gpu, what, policy, prompt, llm"
generated: "2026-06-26T19:58:27.779841"
---

# I Built a Prompt Compressor That Saves 65% on LLM Costs — Here's the Story

## Overview

I've been working on a side project called SuperCompress — an intelligent prompt compression system for LLMs. The idea is simple: most tokens you send to an LLM never need to be processed. They're padding, boilerplate, irrelevant context. But they still burn GPU cycles. I wanted to fix that. The Problem Working with LLM agents, I noticed something: every agent loop was sending massive context through the GPU. 10K tokens. 50K tokens. Sometimes more. Most of it was irrelevant to the specific task. Truncation (keeping head + tail) was the standard approach, but it regularly dropped critical information from the middle of the context. I thought: what if we could score each line of context for relevance BEFORE sending it to the GPU? A tiny CPU model that decides what matters. The Build The technical challenge was: Train a lightweight policy (~5K params) that runs on CPU in under 60ms Score each line of context relative to the user's question Evict low-relevance lines while keeping answer-critical ones Ensure the compressed output preserves correct answers After a lot of iteration, the results surprised even me: Policy KV Saved Oracle Recall Truncation 65% 25% H2O 65% 98% SuperCompress 65% 100% 100% oracle recall at the same token savings. The policy never dropped a line the answer depended on. The Environmental Angle Here's what hit me hardest: at 50M agent turns per day (a conservative estimate for the industry), we're wasting 100B tokens daily. That's 24K GPU hours, 1,526 tons of CO₂, 6.5M liters of cooling water. Every day. Per 1 million compressions, SuperCompress saves: 800M tokens avoided 29 kWh energy 12 kg CO₂ 52 L cooling water It's tiny per call. It's enormous at scale. Current Status ✅ Working policy with 100% oracle recall ✅ Benchmarks and tests (65 passing) ✅ Hosted API with free tier ✅ Browser demo (compresses in-browser) ✅ Python client library ✅ Integration guides (OpenAI, LangChain, LlamaIndex) ✅ Open source (MIT) Currently looking for: First real users and feedback Integration partners Contributors to the open-source codebase Try It Live demo: https://supercompress.vercel.app GitHub: https://github.com/arjunkshah/supercompress Docs: https://arjunkshah-supercompress-55.mintlify.app The ask: If you're building with LLMs, try compressing your next prompt. See if the answers stay the same. I'd love to hear what you think. Now available on PyPI! pip install supercompress Links: GitHub | PyPI | Live Demo

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/arjunkshah/i-built-a-prompt-compressor-that-saves-65-on-llm-costs-heres-the-story-2bdp

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
