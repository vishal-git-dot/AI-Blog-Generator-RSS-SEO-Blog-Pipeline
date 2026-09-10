---
title: "Multi-Provider LLM Router, or How I Got Tired of Forgetting Which API Format I Had To Use"
slug: "multi-provider-llm-router-or-how-i-got-tired-of-forgetting-which-api-format-i-had-to-use"
author: "Sergio Wolf Knapik"
source: "devto_python"
published: "Thu, 10 Sep 2026 03:53:49 +0000"
description: "If you've ever built an application that integrates with multiple LLM providers (Anthropic, Google, OpenAI, DeepSeek), you already know the pain: Each provid..."
keywords: "you, models, provider, thinking, multi, llm, fastapi, stream"
generated: "2026-09-10T04:04:27.712360"
---

# Multi-Provider LLM Router, or How I Got Tired of Forgetting Which API Format I Had To Use

## Overview

If you've ever built an application that integrates with multiple LLM providers (Anthropic, Google, OpenAI, DeepSeek), you already know the pain: Each provider has its own distinct Python SDK. Streaming responses using Server-Sent Events (SSE) requires divergent parser logic. Thinking / Reasoning blocks are formatted completely differently. I recently extracted the core streaming router from my platform into an open-source FastAPI template. Here is how it works. Objective A single asynchronous endpoint: POST /v1/chat/stream It accepts a unified request payload and returns a standardized SSE stream emitting four clean events: event: thinking — Internal model reasoning tokens (streamed in real-time). event: content — User-facing response text. event: tool_call — Function calling requests. event: done — Stream completion ( [DONE] ). Architecture Instead of pulling heavy wrapper frameworks, use direct asynchronous HTTP via httpx.AsyncClient and the official Google GenAI SDK: fastapi-multi-llm-starter/ ├── app/ │ ├── config.py # Pydantic Settings loading environment variables │ ├── main.py # FastAPI app with CORS, health check & test playground │ ├── models.json # Dynamic model catalog (Claude, Gemini, GPT) │ ├── router.py # Unified multi-provider async stream dispatcher │ └── schemas.py # Strict Pydantic v2 validation models ├── tests/ # Automated unit tests (pytest) ├── requirements.txt └── README.md Dynamic Model Catalog I disliked the idea of hardcoded models, so I decoupled them into a models.json file: { "models" : [ { "id" : "claude-sonnet-5" , "name" : "Claude Sonnet 5" , "provider" : "Anthropic" , "thinking" : true }, { "id" : "gemini-3.8-flash" , "name" : "Gemini 3.8 Flash" , "provider" : "Google" , "thinking" : true }, { "id" : "gpt-5.6-terra" , "name" : "GPT 5.6 Terra" , "provider" : "OpenAI" , "thinking" : true } ] } Now, if you want to add another model, you just edit the JSON. The backend and the embedded UI dynamically populate available models via GET /v1/models . Testing Playground The repository includes a testing playground running directly at http://localhost:8000/ . You can immediately test prompts, check streaming latency, and verify reasoning blocks without setting up a frontend framework. Of course, you'll need your own API keys. Open Source Code The full core code is open-source under the MIT License on GitHub: 👉 github.com/wolfnomknight/fastapi-multi-llm-starter Includes full pytest test coverage, .env.example , and clean Pydantic v2 schemas. Feel free to fork it, use it in your side projects or micro-SaaS, and let me know if you run into any issues or have ideas for additional providers!

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/wolfnom/multi-provider-llm-router-or-how-i-got-tired-of-forgetting-which-api-format-i-had-to-use-lk3

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
