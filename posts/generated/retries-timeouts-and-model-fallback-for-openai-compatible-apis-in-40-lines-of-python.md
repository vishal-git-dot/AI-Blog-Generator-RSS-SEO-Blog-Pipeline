---
title: "Retries, timeouts and model fallback for OpenAI-compatible APIs in ~40 lines of Python"
slug: "retries-timeouts-and-model-fallback-for-openai-compatible-apis-in-40-lines-of-python"
author: "lucky wang"
source: "devto_python"
published: "Sat, 17 Oct 2026 15:09:06 +0000"
description: "Disclosure: I work on the APIGOTO team. APIGOTO is an independent OpenAI-compatible API gateway and is not affiliated with OpenAI, Anthropic or Google. The p..."
keywords: "model, openai, your, models, you, api, not, compatible"
generated: "2026-10-17T15:18:37.846189"
---

# Retries, timeouts and model fallback for OpenAI-compatible APIs in ~40 lines of Python

## Overview

Disclosure: I work on the APIGOTO team. APIGOTO is an independent OpenAI-compatible API gateway and is not affiliated with OpenAI, Anthropic or Google. The pattern below works with any OpenAI-compatible endpoint, ours or not. When a prototype calls an LLM API, the first production problem is rarely the prompt. It's a 429, a slow response that hangs your worker, or one model being temporarily unavailable. Here is the small wrapper I use to handle all three. The idea Set a hard timeout on every request. Retry rate-limit and server errors with exponential backoff. If a model keeps failing, move on to the next model in a list. Code import os , time from openai import OpenAI , APIStatusError , APITimeoutError , APIConnectionError client = OpenAI ( base_url = os . getenv ( " LLM_BASE_URL " , " https://api.china-aiapi.com/v1 " ), api_key = os . environ [ " LLM_API_KEY " ], timeout = 30 , # never wait forever max_retries = 0 , # we handle retries ourselves ) RETRYABLE = { 429 , 500 , 502 , 503 , 504 } def chat ( messages , models , attempts = 3 ): last_err = None for model in models : for i in range ( attempts ): try : r = client . chat . completions . create ( model = model , messages = messages ) return model , r . choices [ 0 ]. message . content except APIStatusError as e : last_err = e if e . status_code not in RETRYABLE : break # 400/401/404: retrying won't help, try next model except ( APITimeoutError , APIConnectionError ) as e : last_err = e time . sleep ( min ( 2 ** i , 8 )) raise RuntimeError ( f " all models failed: { last_err } " ) model , text = chat ( [{ " role " : " user " , " content " : " Summarize HTTP 429 in one sentence. " }], models = [ " your-primary-model " , " your-backup-model " ], ) print ( model , text ) Notes Use the model IDs your provider actually lists ( client.models.list() ), not names you assume exist. A 401 or 404 means fix your key or model name; don't retry it. Log which model answered. When the fallback fires often, you want to know. Because only base_url and the key change, you can point this at OpenAI directly, a self-hosted server, or a gateway. If you want to try it against our gateway, the base URL is https://api.china-aiapi.com/v1 , and pricing is pay-as-you-go: www.china-aiapi.com . Feedback on the pattern is welcome in the comments.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/lucky_wang_52b64623a6001a/retries-timeouts-and-model-fallback-for-openai-compatible-apis-in-40-lines-of-python-3d9j

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
