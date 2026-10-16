---
title: "We re-priced six weeks of our own AI coding-agent usage. The "obvious" saving was 5.5x too big."
slug: "we-re-priced-six-weeks-of-our-own-ai-coding-agent-usage-the-obvious-saving-was-55x-too-big"
author: "Derrick Zhou"
source: "devto_ai"
published: "Fri, 16 Oct 2026 16:17:37 +0000"
description: "Over 46 days (35 of them active), one person's coding agent made 61,955 requests . There was no invoice for this exercise - a real client audit starts by rec..."
keywords: "cache, your, you, not, saving, one, every, minute"
generated: "2026-10-16T16:24:14.490522"
---

# We re-priced six weeks of our own AI coding-agent usage. The "obvious" saving was 5.5x too big.

## Overview

Over 46 days (35 of them active), one person's coding agent made 61,955 requests . There was no invoice for this exercise - a real client audit starts by reconciling to one - so we did what you do without one: we re-priced every request at the vendor's public, dated price sheet (retrieved 2026-10-16) and asked where the money would go. Every dollar figure below is API-equivalent , not what anyone was billed. The total came to $7,882 . Three things in it surprised us. 1. Almost all of it is re-reading 66% of the cost was cache reads , and 99% of input-side tokens were cache hits. Output - the thing people optimise prompts for - was 12%. Spend is driven by how long the context is x how many turns run on it , and one project accounted for 63% of it. The lever is context length and session hygiene, not a cleverer prompt. Cost category Share Cache reads (re-reading the existing context every turn) 66% 1-hour cache writes 20% Output (incl. thinking) 12% 5-minute cache writes 2% Fresh input ~0% 2. The headline saving was 5.5x too big Newer model versions are cheaper per token. If you re-price every request that ran on an older version at the newer version's rates, you "save" $1,625 (20.6%) . But most of those requests were made before the newer version existed. Counting only requests made after it was available: $293 (3.7%) . A saving you couldn't have taken at the time isn't a saving. 3. The expensive-looking setting was the right one 85% of cache-write tokens used the 1-hour prompt cache, which costs more to write than the 5-minute cache. We tested the opposite: if every cache write had used the 5-minute cache, anything idle for more than five minutes would have to be re-written at write prices. Only 2.5% of cache-read tokens came after such a gap, but those requests carried very large contexts. Net result: the 5-minute cache would have cost $1,781 more (+22.6%) . Keep the 1-hour cache. (And moving subagent work to a cheaper model saved $62 - not worth the quality risk.) What this is, and isn't It is a re-pricing from token counters, not realised savings. We did not evaluate output quality. Subagent streams were merged when measuring idle gaps, so those gaps look shorter than they were. The aggregated CSVs in the repo let you check the totals, and the scripts reproduce them from your own usage logs. Run it on your own logs The scripts are open source (MIT), deterministic, and make no LLM or network calls: https://github.com/zbl1998-sdjn/llm-spend-audit-toolkit extract per-request usage (token counters only) from your coding-agent logs price it by category from a dated public price sheet test "move to the newer model" with an available-at-the-time check test the 5-minute vs 1-hour cache counterfactual How we'd do this for your bill Export-only. Billing/usage exports - no API keys, no prompts, no production access. Deterministic analysis - scripts on your numbers, not a model reading your data. Reconcile first : recomputed spend must match your invoice within +/-3% before any saving is counted. Only conservative, de-duplicated, available-at-the-time findings - a lower bound, with the formula next to each number. If you spend $3,000+/month on LLM APIs and want a second pair of eyes: hello@currawongweb.com . Disclosure: the analysis scripts and this write-up were produced with AI assistance (Claude Code).

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/derrick_d15159abe0a5e6608/we-re-priced-six-weeks-of-our-own-ai-coding-agent-usage-the-obvious-saving-was-55x-too-big-3852

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
