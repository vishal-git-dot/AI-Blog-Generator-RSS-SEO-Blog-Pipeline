---
title: "LiteLLM Router — Stop Hardcoding One Provider Into Your App"
slug: "litellm-router-stop-hardcoding-one-provider-into-your-app"
author: "M.T.Ramkrushna"
source: "devto_python"
published: "Thu, 15 Oct 2026 03:43:28 +0000"
description: "Your support bot is fine until OpenAI returns 429s for twenty minutes. If the app called openai.OpenAI() with a single model string, those twenty minutes are..."
keywords: "openai, litellm, router, one, model, provider, fallbacks, client"
generated: "2026-10-15T04:04:26.695537"
---

# LiteLLM Router — Stop Hardcoding One Provider Into Your App

## Overview

Your support bot is fine until OpenAI returns 429s for twenty minutes. If the app called openai.OpenAI() with a single model string, those twenty minutes are an outage. Not because the product broke — because you married one vendor in the client code. LiteLLM gives you one OpenAI-compatible interface over 100+ providers, plus a Router that retries inside a model group and falls back to another group when the primary keeps failing. Your feature code keeps talking "chat completions." Reliability lives in the router config. What you're solving Most teams start with: from openai import OpenAI client = OpenAI () client . chat . completions . create ( model = " gpt-4o-mini " , messages = ...) That is fine for a prototype. In production you eventually want: A second provider when the first is rate-limited or down The same message shape no matter which model answers Retries that do not require rewriting every call site A place to log cost and failures without sprinkling try/except everywhere LiteLLM's answer is: keep the OpenAI client shape, move provider choice into a model_list + Router . Install and make one call pip install litellm # or: uv add litellm SDK style (no proxy yet): from litellm import completion import os os . environ [ " OPENAI_API_KEY " ] = " ... " os . environ [ " ANTHROPIC_API_KEY " ] = " ... " # Same completion() shape for every provider r = completion ( model = " openai/gpt-4o-mini " , messages = [{ " role " : " user " , " content " : " Summarize this ticket in one line. " }], ) print ( r . choices [ 0 ]. message . content ) r2 = completion ( model = " anthropic/claude-sonnet-4-5 " , messages = [{ " role " : " user " , " content " : " Summarize this ticket in one line. " }], ) Every response is OpenAI-shaped. Exceptions map to OpenAI-style errors ( RateLimitError , AuthenticationError , …), so existing handlers keep working. Docs: Getting Started . The workflow that matters: Router + fallbacks This is the part you actually ship. 1. Define deployments under shared aliases import os from litellm import Router model_list = [ { " model_name " : " support-summarizer " , # app-facing alias " litellm_params " : { " model " : " openai/gpt-4o-mini " , " api_key " : os . environ [ " OPENAI_API_KEY " ], }, }, { " model_name " : " support-summarizer-backup " , " litellm_params " : { " model " : " anthropic/claude-haiku-4-5 " , " api_key " : os . environ [ " ANTHROPIC_API_KEY " ], }, }, ] 2. Wire fallbacks and retries router = Router ( model_list = model_list , num_retries = 2 , fallbacks = [{ " support-summarizer " : [ " support-summarizer-backup " ]}], ) Retries stay inside the same model_name group. Fallbacks leave that group for the next one in the list. That split is deliberate: don't burn your backup provider on a flaky single request if another deployment of the primary can still answer. See Fallbacks and Router load balancing . 3. Call it like OpenAI response = router . completion ( model = " support-summarizer " , messages = [ { " role " : " system " , " content " : " One-line summary. No preamble. " }, { " role " : " user " , " content " : ticket_body }, ], ) summary = response . choices [ 0 ]. message . content Your ticket pipeline never imports Anthropic. If OpenAI rate-limits after retries, LiteLLM moves to the backup alias. 4. Log what still fails Catch litellm.RateLimitError / APIError after fallbacks exhaust. Those inputs become tomorrow's eval set and a signal to raise budgets or add another region. Optional: run the proxy instead of embedding the Router If more than one service needs the same failover rules, run the LiteLLM AI Gateway and point every OpenAI client at it: from openai import OpenAI client = OpenAI ( api_key = " sk-your-virtual-key " , base_url = " http://localhost:4000 " , ) client . chat . completions . create ( model = " support-summarizer " , messages = [{ " role " : " user " , " content " : " hello " }], ) Config YAML holds model_list , fallbacks , budgets, and virtual keys. Apps stay dumb; the gateway owns reliability. When not to bother One hobby script, one key, one model — a plain SDK is enough. You already have a mature internal gateway with the same features. Latency budgets are so tight that an extra hop or cross-provider fallback is worse than a brief 429. Everyone else who has been burned by a single-vendor outage: put the fallback config next to the model list, not inside twelve call sites. Checklist Replace scattered provider SDKs with LiteLLM completion or an OpenAI client pointed at the proxy. Give production jobs an app-facing model_name , not a raw vendor id. Set num_retries for transient failures inside the group. Set fallbacks to a different provider (or region) for sustained failures. Log exhausted fallbacks; treat them as product incidents, not "weird LLM noise." References LiteLLM Getting Started LiteLLM AI Gateway (proxy) Fallbacks / provider failover Router — load balancing, retries, cooldowns GitHub: BerriAI/litellm What do you use today when your primary LLM provider rate-limits — hope, a second hardcoded client, or a real router?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/m_t_ramkrushna/litellm-router-stop-hardcoding-one-provider-into-your-app-2chi

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
