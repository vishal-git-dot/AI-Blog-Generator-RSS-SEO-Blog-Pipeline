---
title: "Use GPT, Claude, and Gemini with the OpenAI SDK - one base_url, any language"
slug: "use-gpt-claude-and-gemini-with-the-openai-sdk-one-baseurl-any-language"
author: "chenxiao5580-cmd"
source: "devto_python"
published: "Fri, 19 Jun 2026 15:24:17 +0000"
description: "If you're juggling separate SDKs and API keys for OpenAI, Anthropic, and Google, here's a simpler setup: point the OpenAI SDK at an OpenAI-compatible gateway..."
keywords: "openai, model, gpt, content, claude, gemini, client, resp"
generated: "2026-06-19T15:31:48.964432"
---

# Use GPT, Claude, and Gemini with the OpenAI SDK - one base_url, any language

## Overview

If you're juggling separate SDKs and API keys for OpenAI, Anthropic, and Google, here's a simpler setup: point the OpenAI SDK at an OpenAI-compatible gateway and call GPT, Claude, and Gemini through one base_url and one key — at a flat, predictable per-call price instead of three separate per-token bills. Here's the exact change in five common stacks. Python (OpenAI SDK) from openai import OpenAI client = OpenAI ( base_url = " https://modelishub.com/v1 " , api_key = " YOUR_MODELIS_KEY " , ) resp = client . chat . completions . create ( model = " gpt-4o-mini " , messages = [{ " role " : " user " , " content " : " Hello " }], ) print ( resp . choices [ 0 ]. message . content ) The rest of your code stays the same — only base_url and api_key change. Node.js (openai v4) import OpenAI from ' openai ' ; const client = new OpenAI ({ baseURL : ' https://modelishub.com/v1 ' , apiKey : process . env . MODELIS_API_KEY , }); const resp = await client . chat . completions . create ({ model : ' gpt-4o-mini ' , messages : [{ role : ' user ' , content : ' Hello ' }], }); console . log ( resp . choices [ 0 ]. message . content ); curl (works in any language) curl https://modelishub.com/v1/chat/completions \ -H "Authorization: Bearer YOUR_MODELIS_KEY" \ -H "Content-Type: application/json" \ -d '{"model":"gpt-4o-mini","messages":[{"role":"user","content":"Hello"}]}' The same pattern works in Go, Java, PHP, Rust — anywhere you can make an HTTP request. LangChain from langchain_openai import ChatOpenAI llm = ChatOpenAI ( base_url = " https://modelishub.com/v1 " , api_key = " YOUR_MODELIS_KEY " , model = " gpt-4o-mini " , ) print ( llm . invoke ( " Hello " ). content ) Switching between GPT, Claude, and Gemini To use a different model, just change the model id — claude-sonnet-4-6 , gemini-2.5-flash , and so on. Same endpoint, same key. Fetch the full list any time with GET /v1/models . resp = client . chat . completions . create ( model = " claude-sonnet-4-6 " , # or gemini-2.5-flash, gpt-4o, ... messages = [{ " role " : " user " , " content " : " Hello " }], ) This runs on Modelis , an OpenAI-compatible LLM gateway that auto-routes each request to a model fitted to the task and bills a flat per-call price (not per-token), so your bill stays predictable regardless of which model answered. Free tier to try it — details + free key .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/chenxiao5580cmd/use-gpt-claude-and-gemini-with-the-openai-sdk-one-baseurl-any-language-475n

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
