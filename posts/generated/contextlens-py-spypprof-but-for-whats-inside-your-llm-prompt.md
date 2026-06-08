---
title: "ContextLens — py-spy/pprof but for what's inside your LLM prompt"
slug: "contextlens-py-spypprof-but-for-whats-inside-your-llm-prompt"
author: "Harshal Sant"
source: "devto_python"
published: "Mon, 08 Jun 2026 15:32:34 +0000"
description: "In multi-turn agent loops, the full context re-sends on every API call. A tool result added at turn 3 gets billed again at turns 4, 5, 6, 7... forever. Most ..."
keywords: "contextlens, turn, report, tool, what, waste, model, client"
generated: "2026-06-08T16:07:42.605559"
---

# ContextLens — py-spy/pprof but for what's inside your LLM prompt

## Overview

In multi-turn agent loops, the full context re-sends on every API call. A tool result added at turn 3 gets billed again at turns 4, 5, 6, 7... forever. Most of it is never read again. Standard observability tools tell you the total token count. They never tell you what's in there or how much of it is waste . That's what ContextLens fixes. What it does ContextLens is a diagnostic profiler for LLM agent context windows. It: Decomposes the context window into regions: system prompt, tool schemas, tool results, retrieved chunks, user messages, assistant messages Tracks which blocks get re-billed across turns using SHA-256 content hashing Runs 5 waste detectors and ranks findings by dollar cost Prints a concrete one-line fix for each finding Renders an interactive D3 treemap report as a self-contained HTML file No API key required. Works offline on saved traces. The five detectors Detector What it finds Duplicate Same block re-sent verbatim across multiple turns Near-Duplicate >85% Jaccard similarity between distinct blocks Stale Tool Result Tool output never referenced by a later assistant message Unused Tool Schema Tool defined every turn but never called Redundant Retrieval Retrieved chunk with <15% overlap with model output ---Run the built-in demo (simulates a 30-turn agent loop, no API key needed): python -c "import contextlens; contextlens.demo()" python examples/demo.py Live capture — Anthropic import anthropic import contextlens as cl client = anthropic.Anthropic() with cl.capture_anthropic(client, model="claude-3-5-sonnet-20241022") as collector: for turn in range(20): client.messages.create( model="claude-3-5-sonnet-20241022", max_tokens=1024, system="You are a helpful assistant.", messages=build_messages(turn), ) report = cl.analyze_trace(collector.build_trace()) print(f"Recoverable waste: {report.recoverable_tokens:,} tokens (${report.recoverable_cost_usd:.4f})") Live capture — OpenAI import openai import contextlens as cl client = openai.OpenAI() with cl.capture_openai(client, model="gpt-4o") as collector: for turn in range(20): client.chat.completions.create(model="gpt-4o", messages=build_messages(turn)) report = cl.analyze_trace(collector.build_trace()) Analyze a saved trace report = cl.analyze_file("trace.json") html = cl.render_html_report(report) open("report.html", "w").write(html) Example terminal output +---------------------------------------------------------------------+ | ContextLens | Run demo-001 | | Model: claude-3-5-sonnet-20241022 | Provider: anthropic | Turns: 30 | +---------------------------------------------------------------------+ Context Composition by Region Region Tokens Cost (USD) Share assistant_message 11,490 $0.0345 ###....... 25.5% tool_result 10,333 $0.0310 ##........ 22.9% tool_schema 9,450 $0.0284 ##........ 21.0% retrieved_content 5,805 $0.0174 #......... 12.9% user_message 4,740 $0.0142 #......... 10.5% system 3,240 $0.0097 #......... 7.2% TOTAL 45,058 $0.1352 Re-billing: 43,185 tokens (95.8%) re-billing waste -> $0.1296 recoverable Top Waste Findings # Type Sev. Wasted Tokens Cost Fix 1 duplicate medium 7,084 $0.0213 Cache or externalize... 2 redundant_ret medium 5,805 $0.0174 Use a re-ranker... 3 unused_schema low 3,150 $0.0095 Remove send_email... Try the live demo No install, no API key: https://huggingface.co/spaces/Harshal0610/contextlens Links GitHub: https://github.com/HarshalSant/contextlens Install: pip install contextlens-profiler License: MIT Feedback welcome — especially from anyone running multi-turn agent loops at scale. What waste patterns do you run into most? Quickstart bash pip install contextlens-profiler

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/harshal_sant_be921c5039f2/contextlens-py-spypprof-but-for-whats-inside-your-llm-prompt-59l7

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
