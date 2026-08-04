---
title: "Understanding LLM Agents and Tool"
slug: "understanding-llm-agents-and-tool"
author: "Mohammad Jawad (Kasir) Barati"
source: "devto_ai"
published: "Tue, 04 Aug 2026 14:13:59 +0000"
description: "In this post, I'll explain how prompt chaining, tools/skills, and iteration actually make agnets to produce results which are not usually possible when we us..."
keywords: "llm, you, get, portfolio, prompt, your, what, turn"
generated: "2026-08-04T14:28:10.958865"
---

# Understanding LLM Agents and Tool

## Overview

In this post, I'll explain how prompt chaining, tools/skills, and iteration actually make agnets to produce results which are not usually possible when we use simple LLMs. LLM chaining You know how sometimes you write one massive prompt like: Create a detailed travel itinerary for a 5-day trip to Japan, including budget breakdown, must-see attractions, and restaurant recommendations, and then translate it all into Japanese. And sometimes it works great! The LLM has the freedom to structure everything however it wants. But other times, you want more control. Maybe you need the itinerary to follow a specific format for your app, or you want to test the budget calculation separately from the translation. The solution? Chain your LLM calls. Graphically, it looks like one LLM calling another. But in reality, it's just: call LLM → take output → use it in next prompt. Tools/Skills User asks: "What's the weather like in Berlin tomorrow?" LLM somehow knows to check a weather API and return the answer. But here's what's really happening: The Agent Loop Now things get interesting. What if your task requires multiple tool calls? Imagine you're building a portfolio tracker bot. A user asks: "What's my current portfolio value?" Here's the agent loop in action: Turn 1 - Get the Portfolio Prompt: "Your task is to find the current value of my portfolio. You can: 1. retrieve_portfolio() - gets list of holdings 2. lookup_price(symbol) - gets current stock price User: What's my portfolio value?" LLM responds: "USE_TOOL: retrieve_portfolio()" You run it, get: "3 shares of AAPL, 5 shares of GOOGL" Turn 2 - Get the prices: [ Same prompt ] Tool result: Portfolio contains 3 shares of AAPL, 5 shares of GOOGL LLM responds: "USE_TOOL: lookup_price(AAPL)" You run it, get: "AAPL: $175" Turn 3 - Get the next price: [Same prompt, now with AAPL price] LLM responds: "USE_TOOL: lookup_price(GOOGL)" You run it, get: "GOOGL: $140" Turn 4 - Calculate and respond: [ Full conversation history with all prices ] LLM responds: "Your portfolio value is $1,225 (3 × $175 + 5 × $140)" This is the agent loop. Each turn, you: Add the LLM's response to the conversation. If it called a tool, run it and add the result. Call the LLM again with the updated conversation. Repeat until it provides a final answer.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/kasir-barati/understanding-llm-agents-and-tool-2g7

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
