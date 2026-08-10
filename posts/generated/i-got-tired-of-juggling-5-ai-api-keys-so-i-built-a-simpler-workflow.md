---
title: "I Got Tired of Juggling 5 AI API Keys, So I Built a Simpler Workflow"
slug: "i-got-tired-of-juggling-5-ai-api-keys-so-i-built-a-simpler-workflow"
author: "Lijing-Big"
source: "devto_ai"
published: "Mon, 10 Aug 2026 02:00:27 +0000"
description: "Last month I was shipping a small internal tool that needed text summarization, code review suggestions, and a bit of image captioning. Simple enough, right?..."
keywords: "model, self, different, env, one, diff, const, text"
generated: "2026-08-10T02:10:38.792226"
---

# I Got Tired of Juggling 5 AI API Keys, So I Built a Simpler Workflow

## Overview

Last month I was shipping a small internal tool that needed text summarization, code review suggestions, and a bit of image captioning. Simple enough, right? Except by the end of the week I had API keys from four different providers sitting in my .env file, three separate SDKs to keep updated, and a billing dashboard that looked like a stock portfolio. One provider changed their auth header without warning. Another had rate limits that silently dropped requests during our demo. I spent more time debugging integrations than writing actual features. That experience pushed me to rethink how I use AI tooling as a working dev. Here's what I learned and what I actually use now. Stop treating each model like a snowflake The biggest time sink was writing custom wrappers for every provider. OpenAI needs openai SDK. Anthropic needs anthropic . A local Ollama instance needs raw HTTP. Each has different error shapes, different retry logic, different token counting. I started standardizing on a thin internal client that normalizes requests: import os import requests class ModelClient : def __init__ ( self , base_url , api_key ): self . base_url = base_url self . headers = { " Authorization " : f " Bearer { api_key } " } def complete ( self , prompt , model = " default " ): payload = { " model " : model , " prompt " : prompt , " max_tokens " : 500 } resp = requests . post ( f " { self . base_url } /v1/complete " , json = payload , headers = self . headers , timeout = 30 ) resp . raise_for_status () return resp . json ()[ " text " ] # Same interface whether the backend is local or hosted client = ModelClient ( os . getenv ( " AI_BASE_URL " ), os . getenv ( " AI_KEY " )) print ( client . complete ( " Explain retry policies in 2 sentences " )) This isn't rocket science, but having one interface meant I could swap providers by changing two env vars. No code changes, no re-deploys. Aggregation actually saves sanity I used to think aggregator platforms were just for people who couldn't pick a model. Then I found https://xinghuo1300ai.com which aggregates 30+ models under one API key. For my internal tool, that meant I could test Claude for summarization, Gemini for captions, and a smaller open model for draft reviews without signing four contracts or managing four dashboards. The unified billing alone paid back the afternoon I spent migrating. If you're building something where the "best model" changes per task, this kind of setup removes a lot of friction. Know when NOT to use AI Honest take: half the AI features I prototyped got cut. A regex validator I wrapped in an LLM call was slower and less accurate than the 10-line function it replaced. A "smart" search box confused users who just wanted to filter by date. Practical rule I now follow: If the task is deterministic and small, don't call a model. If the task needs judgment on messy input (summaries, unclear bug reports), models help. If latency matters (<200ms), avoid round-trips to hosted models. A concrete example: PR description drafts We added a pre-push git hook that sends the diff to a model and suggests a PR description. It's not always right, but it's a good starting point: const { execSync } = require ( ' child_process ' ); const fetch = require ( ' node-fetch ' ); async function draftPr () { const diff = execSync ( ' git diff origin/main...HEAD ' ). toString (). slice ( 0 , 8000 ); const res = await fetch ( process . env . AI_BASE_URL + ' /v1/complete ' , { method : ' POST ' , headers : { ' Authorization ' : `Bearer ${ process . env . AI_KEY } ` }, body : JSON . stringify ({ model : ' summarizer ' , prompt : `Write a concise PR description for this diff:\n ${ diff } ` }) }); const data = await res . json (); console . log ( data . text ); } draftPr (); We run this locally, review the output, and paste what's useful. Nobody commits the AI text blindly. Pricing reality Most aggregators and providers charge per token. For a team of 6 doing ~200 summaries/day at ~1k tokens each, that's roughly 120k tokens/day. At $0.002/1k tokens that's under $8/month. Cheap — but watch the image and embedding models, those add up fast if you batch poorly. What stuck with me After the migration, my .env went from five keys to one. The demo that failed last month now fails over to a backup model automatically because the client just points at a different model string. I still write plain functions for the boring stuff, but for the messy human-language tasks, having one normalized layer and a platform like https://xinghuo1300ai.com behind it made the whole thing maintainable instead of a maintenance burden.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/lijingbig/i-got-tired-of-juggling-5-ai-api-keys-so-i-built-a-simpler-workflow-1gd

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
