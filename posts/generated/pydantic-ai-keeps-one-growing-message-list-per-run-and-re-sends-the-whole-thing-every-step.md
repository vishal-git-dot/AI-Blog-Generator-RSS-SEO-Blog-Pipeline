---
title: "Pydantic AI keeps one growing message list per run — and re-sends the whole thing every step"
slug: "pydantic-ai-keeps-one-growing-message-list-per-run-and-re-sends-the-whole-thing-every-step"
author: "wartzar-bee"
source: "devto_python"
published: "Sat, 22 Aug 2026 12:37:48 +0000"
description: "Pydantic AI gives you a clean, typed agent: define an Agent , hand it tools, call agent.run(...) , and it loops — model call, tool call, model call — until i..."
keywords: "step, run, you, every, tool, list, model, agent"
generated: "2026-08-22T12:48:49.580336"
---

# Pydantic AI keeps one growing message list per run — and re-sends the whole thing every step

## Overview

Pydantic AI gives you a clean, typed agent: define an Agent , hand it tools, call agent.run(...) , and it loops — model call, tool call, model call — until it produces a validated result. The typed ergonomics are great. What the quickstart doesn't spell out is what the model receives on each pass of that loop. I read the run graph ( pydantic_ai_slim/pydantic_ai/_agent_graph.py on main ) to find out. The mechanism is structural, and it's the same shape I found in the OpenAI Agents SDK and smolagents. One list, appended twice per turn Each run holds a single mutable conversation list on its state: message_history : list [ _messages . ModelMessage ] = dataclasses . field ( default_factory = list [ _messages . ModelMessage ]) On every model step the graph appends to it — first the outgoing request, then the model's response: ctx . state . message_history . append ( self . request ) ... ctx . state . message_history . append ( response ) Nothing is removed. The list only grows: request, response, request, response — with tool calls and, crucially, tool outputs riding inside those messages. The full list is re-sent every step When the graph builds the input for the next model call, it takes the entire accumulated history — a full copy: messages = ctx . state . message_history [:] ... messages [:] = _clean_message_history ( ctx . state . message_history ) That [:] is the whole conversation to date. So on step 1 the model sees your prompt; on step 2 it sees your prompt + step 1's request + step 1's response (including the tool output); on step 5 it sees all of that plus steps 2–4. The payload you pay for grows every single step, and the heaviest passengers are usually the tool outputs — the search results, file contents, and API responses you least want re-uploaded five times. Why it's quadratic, and why nothing warns you A run of n steps sends roughly 1 + 2 + 3 + … + n copies of history — O(n²) cumulative tokens in the step count. A 3-step agent is fine. A 12-step agent that reads a couple of files is not: each file's contents rides along on every later step. The run still succeeds , your tests still pass — the only artifact is a bigger number on the usage line, and you don't see it until the invoice. The knob you actually have Pydantic AI hands you the full transcript back ( result.all_messages() ) and every run method takes a message_history parameter: message_history : Sequence [ _messages . ModelMessage ] | None = None — "History of the conversation so far." That's the lever: across a multi-turn conversation you decide what prior history to replay, so you can pass a trimmed or summarized history into the next run instead of the raw accumulation. Inside a single deep tool-loop the re-send is inherent to how tool-calling works (it's true of every framework) — which is exactly why the move is to measure it, not assume it's free. Measure it before you argue about it Before refactoring anything, put a number on it — the token cost of your run, priced in dollars, not tokens. That's what @wartzar-bee/tokenscope does ( npm i @wartzar-bee/tokenscope ): it takes real usage and prices each bucket — input, output, cache-write (~1.25×), cache-read (~0.1×) — into an actual per-run dollar figure, so "the 12-step version costs 4× the 4-step version" stops being a hunch. And if this runs in CI, gate it: wartzar-bee/ci-guardrail is an Apache-2.0 GitHub Action (built on tokenscope) that fails the check when a run crosses an absolute max-usd ceiling — so the quadratic step doesn't reach production as a silent 4× before anyone notices. - uses : wartzar-bee/ci-guardrail@v1 with : max-usd : " 0.50" If you run Pydantic AI: how many steps does your deepest agent take, and how big are the tool outputs it re-sends on every one? Worth pricing one real run before the next invoice does it for you.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/wartzarbee/pydantic-ai-keeps-one-growing-message-list-per-run-and-re-sends-the-whole-thing-every-step-4o7b

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
