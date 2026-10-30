---
title: "We put a free, unlimited LLM inside a static web page — Transformers.js + a 135M model, zero servers"
slug: "we-put-a-free-unlimited-llm-inside-a-static-web-page-transformersjs-a-135m-model-zero-servers"
author: "Astro"
source: "devto_ai"
published: "Fri, 30 Oct 2026 05:09:54 +0000"
description: "Every LLM demo I have ever seen has the same fine print: bring your own API key , or the demo is rate-limited , or your prompts go to our server . So I built..."
keywords: "your, model, llm, api, devkit, playground, tokens, page"
generated: "2026-10-30T05:13:18.346586"
---

# We put a free, unlimited LLM inside a static web page — Transformers.js + a 135M model, zero servers

## Overview

Every LLM demo I have ever seen has the same fine print: bring your own API key , or the demo is rate-limited , or your prompts go to our server . So I built the opposite demo. DevKit's AI Playground is a chat with a real language model that runs 100% in your browser . No backend, no API key, no cost per token, and — because there is no server at all — nothing you type can leave the page. It's a static HTML file on GitHub Pages, like the rest of DevKit. How it works Transformers.js v3 does the inference, inside a Web Worker so generation never freezes the UI. The model is SmolLM-135M-Instruct , 4-bit quantized ( q4f16 ). The weights file is ~117 MB; with the tokenizer the one-time download is ~121 MB, and your browser caches it for future visits. It tries WebGPU first (your graphics chip) and falls back to WASM on the CPU. Tokens stream in as they're generated, with a live tokens/sec readout — which is either a fun toy or a benchmark, depending on how serious your hardware is. Click "Load the model", wait for the one-time download, and chat. That's the whole signup flow. Honest limits It's a 135M-parameter model that lives in your RAM . It writes plausible text, answers simple questions, does little creative tasks — and cheerfully makes things up. It is not GPT-class, and the page says so up front. The point isn't to replace an API; it's to show how far "the browser is the runtime" has come, and to give the LLM-curious a playground with literally zero setup and zero bill. DevKit's other LLM tools are the grown-up counterparts: a cost calculator that prices 14 real API models with cached-read/cache-write splits, and a tokens/sec simulator. The playground is what those calculators look like when the model is small enough to be free . Also new in this release Four more client-side tools joined the kit: a JWT decoder (decode-only, and it says so — the signature is not verified), a cron expression explainer (plain English + next 5 run times), a color palette generator , and a Pomodoro timer whose countdown runs in the tab title. Same rules as everything on DevKit: no uploads, no accounts, no tracking, and every calculator's math is checked by automated tests (310 checks and counting). Try it and tell me the tokens/sec number your machine gets — and which model you'd want to see in the playground next. SmolLM2-360M? Qwen? The download budget is the boss fight.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/astrodevkit/we-put-a-free-unlimited-llm-inside-a-static-web-page-transformersjs-a-135m-model-zero-servers-jjo

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
