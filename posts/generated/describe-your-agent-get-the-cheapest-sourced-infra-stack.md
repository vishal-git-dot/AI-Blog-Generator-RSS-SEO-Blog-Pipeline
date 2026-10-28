---
title: "Describe your agent, get the cheapest sourced infra stack"
slug: "describe-your-agent-get-the-cheapest-sourced-infra-stack"
author: "Lantern Works"
source: "devto_python"
published: "Wed, 28 Oct 2026 22:13:41 +0000"
description: "If you're building an agent, at some point you have to answer a boring question: what will the infrastructure cost each month? Scraping, proxies, a search AP..."
keywords: "checked, https, gpu, com, stack, pricing, priced, referral"
generated: "2026-10-28T22:24:29.413931"
---

# Describe your agent, get the cheapest sourced infra stack

## Overview

If you're building an agent, at some point you have to answer a boring question: what will the infrastructure cost each month? Scraping, proxies, a search API, an LLM, maybe some GPU hours. I added a tool to the Lantern Works MCP server that answers it from a plain-text description of the agent. optimize_agent_stack (new in lantern-works-deals-mcp 0.3.6, MIT) parses the description with keywords and regex (no LLM), then picks the cheapest option with a cited price for each component among tracked providers. Every line has the math, the vendor's pricing URL and when the price was checked. If no price is cited for a component, it says so and doesn't guess. Try it uvx lantern-works-deals-mcp # stdio MCP server, 6 read-only tools, no API key Or use the browser version: https://thelanternworks.com/stack/?utm_source=devto&utm_medium=post&utm_campaign=stack-optimizer There's also an OpenAI Agents SDK example: https://github.com/connormatthewdouglas/agent-work-stack-deals/tree/main/examples/stack-optimizer Real output (PyPI 0.3.6, run Oct 28, 2026) tools: compare_deals, compare_gpu_prices, get_deal, optimize_agent_stack, optimize_stack, search_deals job: scrapes 20k JS pages/month via 5 GB residential proxies, 3k search queries, summarizes with an LLM, budget $300/mo parsed components: scraping, proxy, llm_api, search scraping: ZenRows Launch, $69.0/mo [priced], 20,000 x 5 = 100,000 credits; within 250,000 included at $69/mo, checked 2026-10-27T02:54:00-04:00, https://www.zenrows.com/pricing proxy: 9Proxy Residential (per GB), $3.4/mo [priced], $0/mo incl. 0 + 5 x $0.68 per 1 extra, checked 2026-10-27T02:54:00-04:00, https://9proxy.com/pricing (referral link) llm_api: Groq Free plan with documented model rate limits (RPM/RPD/TPM) in Groq console docs, $0.0/mo [entry_price], free tier ($0), checked 2026-10-27T01:45:00-04:00, https://console.groq.com/docs/rate-limits search: Exa Starter credits + pay as you go, $4/mo [priced], $0/mo incl. 2,500 + 1 x $4 per 1,000 extra, checked 2026-10-27T02:54:00-04:00, https://exa.ai/pricing (referral link) $69.00 (scraping) + $3.40 (proxy) + $0.00 (llm_api) + $4.00 (search) = $76.40/mo (complete) within budget: True job: serve a 13B model for 40 GPU hours, send 5k emails, budget $150/mo parsed components: gpu, email gpu: RunPod RTX A6000 (Community Cloud), $13.2/mo [priced], $0.33/hr x 40 h, checked 2026-10-28T16:43:09+00:00, https://www.runpod.io/pricing (referral link; manual signup only) email: SendPulse Basic (free), $0.0/mo [priced], within 12,000 included at $0/mo, checked 2026-10-27T02:54:00-04:00, https://sendpulse.com/prices/smtp (referral link) $13.20 (gpu) + $0.00 (email) = $13.20/mo (complete) within budget: True A few things to notice: The numbers show their work: "20,000 x 5 = 100,000 credits; within 250,000 included at $69/mo". The LLM line is entry_price . That's the cheapest cited entry plan (a free tier), and real usage may need a bigger plan. "Cheapest" means cheapest among tracked providers. A vendor we don't track may cost less, and the full JSON lists providers that aren't priced. The 13B line filters GPUs by a stated rule: 13 x 2 bytes (FP16) x 1.2 = 31.2 GB VRAM on one GPU for inference. Quantized models need less; full fine-tuning needs several times more, so this estimate is for serving, not training. RunPod is flagged manual_signup_only : a human has to create the account (the vendor's terms ban automated signups). GPU rates are re-checked daily, so the RunPod line may differ when you run it (this one was checked 2026-10-28, 12:43 PM ET). The other prices were checked 2026-10-27. Prices are monthly list prices before tax. Check the vendor page before you pay for anything. Disclosure Disclosure: some result links returned by the server are referral links. They're marked affiliate: true with a referral_disclosure (lines tagged "(referral link)" above), and affiliate status isn't a ranking factor. The source_url is always the vendor's own pricing page. Repo: https://github.com/connormatthewdouglas/agent-work-stack-deals

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/lanternworks/describe-your-agent-get-the-cheapest-sourced-infra-stack-bci

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
