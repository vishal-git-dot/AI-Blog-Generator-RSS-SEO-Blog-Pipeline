---
title: "Instrument First, Then Prompt: Finding Real Agentic Pipeline Bugs"
slug: "instrument-first-then-prompt-finding-real-agentic-pipeline-bugs"
author: "Tae Kim"
source: "devto_python"
published: "Sat, 18 Jul 2026 02:42:57 +0000"
description: "The default reaction when an agentic pipeline misbehaves is to open the system prompt and start rewriting it. The instinct makes sense — the prompt is visibl..."
keywords: "prompt, tool, you, time, first, chunk, result, agent"
generated: "2026-07-18T02:53:43.788608"
---

# Instrument First, Then Prompt: Finding Real Agentic Pipeline Bugs

## Overview

The default reaction when an agentic pipeline misbehaves is to open the system prompt and start rewriting it. The instinct makes sense — the prompt is visible, editable, and feels like the thing you control. The problem is that the prompt is almost never where the bug is. What Actually Breaks Three failure modes come up repeatedly in production agentic systems, and none of them are prompt problems. Chunk boundary truncation. The agent retrieved the right document and extracted the right section. But the chunk ended mid-sentence, cutting off the date field the downstream validation step required. The prompt correctly asked for the date. The agent correctly tried to provide it. The data was not there. Tool output drift. The agent correctly identified which tool to call. The tool returned a response, but the field name had changed — employee_count had become headcount in a dependency update three weeks earlier. The prompt expected employee_count . The model interpreted the unexpected field and got it wrong roughly half the time. Eval dataset blindspot. The agent handled the first four inputs in the eval set correctly. On the fifth, it received a malformed date string the eval set had never included. The agent guessed wrong. The eval passed. Production failed the first time a real user sent that format. None of these are visible in prompt outputs. You cannot find them by reading model responses. Adding Instrumentation When I wire a new agentic pipeline, the first thing I add is not a system prompt improvement — it is instrumentation. Three pieces. A decorator around every tool call: import time import json from functools import wraps def traced_tool ( tool_fn ): @wraps ( tool_fn ) def wrapper ( * args , ** kwargs ): start = time . time () result = tool_fn ( * args , ** kwargs ) elapsed = time . time () - start print ( json . dumps ({ " event " : " tool_call " , " tool " : tool_fn . __name__ , " elapsed_ms " : round ( elapsed * 1000 ), " result_keys " : list ( result . keys ()) if isinstance ( result , dict ) else type ( result ). __name__ })) return result return wrapper The result_keys line catches tool output drift. If a field name changes upstream, the log shows the changed shape the next time the tool fires. A log call around every context injection: def log_context_injection ( context_items : list , step_name : str ): print ( json . dumps ({ " event " : " context_inject " , " step " : step_name , " item_count " : len ( context_items ), " item_lengths " : [ len ( str ( item )) for item in context_items ], " total_chars " : sum ( len ( str ( item )) for item in context_items ) })) The item_lengths list shows when a chunk is unusually short — which is often the symptom of a boundary cut. A 12-character chunk where you expected 800 characters tells you something different from an empty result. A counter around every router branch: route_counter : dict [ str , int ] = {} def log_route ( branch_name : str ): route_counter [ branch_name ] = route_counter . get ( branch_name , 0 ) + 1 print ( json . dumps ({ " event " : " route " , " branch " : branch_name , " count " : route_counter [ branch_name ] })) None of this requires a tracing backend. Timestamped JSON lines that survive a production deploy are enough to start. grep event=tool_call | jq . is sufficient for most initial debugging. The Debugging Loop That Works Once instrumentation is in place, the loop is: Run the pipeline on the failing input Find the first log entry where something diverged from expectation — a missing key, an unusually short chunk, an unexpected branch Fix the thing that caused the divergence That thing is almost always one of: a data shape mismatch at a tool boundary, a chunk size configuration that cuts content too early, or an eval dataset that does not cover the input format real users actually send. Rewriting the prompt to compensate for a broken interface teaches the model to paper over a structural defect. The next upstream change breaks the workaround and you debug it again. Fixing the interface eliminates the failure mode. If You Want a Proper Backend For LangGraph pipelines, LangSmith integrates at the graph level and gives you span-level trace visualization without additional instrumentation code. Weave (Weights and Biases) is the alternative if you are already on the W&B stack. Both capture tool calls, model inputs and outputs, and latency across a full run. For custom pipelines outside any framework, a thin OpenTelemetry layer is roughly an hour of setup and pays for itself the first time you trace a production failure back to a specific tool call. Curious what others are using — LangSmith, Weave, custom spans — and whether prompt-first debugging is actually your default when something breaks.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/hannune/instrument-first-then-prompt-finding-real-agentic-pipeline-bugs-if9

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
