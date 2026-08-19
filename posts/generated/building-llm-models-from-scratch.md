---
title: "Building LLM Models from Scratch"
slug: "building-llm-models-from-scratch"
author: "shashank ms"
source: "devto_ai"
published: "Wed, 19 Aug 2026 01:32:22 +0000"
description: "Building a specialized LLM agent from scratch means owning the system prompt, tool bindings, and execution loop. In this tutorial, we will construct a financ..."
keywords: "tool, oxlo, ticker, days, openai, query, function, return"
generated: "2026-08-19T01:37:09.907966"
---

# Building LLM Models from Scratch

## Overview

Building a specialized LLM agent from scratch means owning the system prompt, tool bindings, and execution loop. In this tutorial, we will construct a financial research agent that fetches mock market data, reasons over it, and returns a formatted markdown report. All inference runs on Oxlo.ai using Qwen 3 32B, a model built for agentic workflows. What you'll need Python 3.10 or newer An Oxlo.ai API key from https://portal.oxlo.ai The OpenAI SDK: pip install openai Step 1: Set up the Oxlo.ai client and tool schema We start by pointing the OpenAI SDK at Oxlo.ai and defining the JSON schema for our stock lookup tool. Oxlo.ai is fully OpenAI API compatible and serves requests with no cold starts, so the client initialization is a drop-in replacement. from openai import OpenAI import json client = OpenAI( base_url="https://api.oxlo.ai/v1", api_key="YOUR_OXLO_API_KEY" ) TOOLS = [ { "type": "function", "function": { "name": "get_stock_data", "description": "Retrieve recent price, volume, and change percent for a ticker.", "parameters": { "type": "object", "properties": { "ticker": {"type": "string", "description": "Stock ticker symbol, e.g. AAPL"}, "days": {"type": "integer", "description": "Number of trading days to look back"} }, "required": ["ticker", "days"] } } } ] Step 2: Design the agent's system prompt This prompt is the core configuration of our custom model. It constrains tone, mandates tool use, and enforces markdown output. SYSTEM_PROMPT = """You are a senior equity research analyst. Your job is to answer user questions about stock performance using the get_stock_data tool. Rules: - Always verify facts with the tool. Do not invent prices or volumes. - When comparing multiple tickers, fetch data for each separately. - Respond in concise markdown with a summary table and a one-paragraph outlook. - If data is missing, state that clearly.""" Step 3: Implement the tool layer Before we call the LLM, we need a concrete Python function to retrieve data. In production you would hit a real market API, but a deterministic mock lets us test the loop without extra dependencies. import random def get_stock_data(ticker: str, days: int): random.seed(ticker + str(days)) return { "ticker": ticker, "days": days, "current_price": round(random.uniform(80, 600), 2), "change_percent": round(random.uniform(-5, 5), 2), "volume": random.randint(10_000_000, 100_000_000), } def execute_tool(tool_call): name = tool_call.function.name args = json.loads(tool_call.function.arguments) if name == "get_stock_data": return get_stock_data(**args) return {"error": f"Unknown tool {name}"} Step 4: Build the reasoning loop with Oxlo.ai We wire everything together. We send the conversation to Oxlo.ai, check for tool calls, execute them locally, and append the results. The loop continues until the model returns a final answer. Because Oxlo.ai uses flat per-request pricing rather than token-based metering, accumulating all this tool context stays predictable even as the conversation grows. See https://oxlo.ai/pricing for details. def run_agent(user_message: str, max_iterations: int = 5): messages = [ {"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": user_message}, ] for _ in range(max_iterations): response = client.chat.completions.create( model="qwen-3-32b", messages=messages, tools=TOOLS, tool_choice="auto", temperature=0.2, ) message = response.choices[0].message messages.append(message) if not message.tool_calls: return message.content for tool_call in message.tool_calls: result = execute_tool(tool_call) messages.append({ "role": "tool", "tool_call_id": tool_call.id, "content": json.dumps(result), }) return "Reached maximum iterations without a final answer." Step 5: Format and deliver the report The loop returns raw markdown. We wrap it in a small formatter that adds a timestamp and prints the report cleanly. from datetime import datetime def generate_report(query: str) -> str: body = run_agent(query) header = f"# Research Report: {query}\nGenerated: {datetime.utcnow().isoformat()}Z\n\n" return header + body if __name__ == "__main__": query = "Compare AAPL and TSLA over the last 5 days" print(generate_report(query)) Run it Pass a natural language question to the agent and print the generated analysis. query = "How have NVDA and AMD performed over the last 5 days?" print(run_agent(query)) Example output: | Ticker | Current Price | Change (%) | Volume | |--------|---------------|------------|-------------| | NVDA | 482.15 | 2.34 | 87,432,091 | | AMD | 145.62 | -1.12 | 54,109,332 | NVDA shows stronger momentum with positive change and elevated volume, while AMD dipped slightly. Both remain active, but NVDA's current price action suggests stronger near-term sentiment. Wrap-up and next steps Swap the mock function for a real brokerage API, or extend the tool set with news sentiment and chart generation. If you need deeper reasoning for complex comparisons, change the model string to deepseek-v3.2 or kimi-k2.6 without touching any other client code. Oxlo.ai's flat per-request pricing makes iterating on long context windows and multi-turn agents predictable, especially when you scale past simple single-shot prompts.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/shashank_ms_6a35baa4be138/building-llm-models-from-scratch-4l9c

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
