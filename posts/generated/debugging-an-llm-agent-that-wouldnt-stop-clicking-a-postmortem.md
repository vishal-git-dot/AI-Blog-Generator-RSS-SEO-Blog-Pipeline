---
title: "Debugging an LLM Agent That Wouldn't Stop Clicking: A Postmortem"
slug: "debugging-an-llm-agent-that-wouldnt-stop-clicking-a-postmortem"
author: "Amarjit Jim"
source: "devto_python"
published: "Thu, 23 Jul 2026 18:16:16 +0000"
description: "I built BrowserPilot — a browser automation agent that pairs Playwright with an LLM to navigate real websites: FastAPI backend, a WebSocket UI for watching i..."
keywords: "same, model, agent, state, what, click, just, had"
generated: "2026-07-23T19:26:23.865332"
---

# Debugging an LLM Agent That Wouldn't Stop Clicking: A Postmortem

## Overview

I built BrowserPilot — a browser automation agent that pairs Playwright with an LLM to navigate real websites: FastAPI backend, a WebSocket UI for watching it work in real time, Gemini 2.0 Flash making the decisions. Point it at a task, it plans, clicks, types, and reports back. Then it got stuck in a loop. Same button, over and over, for 40+ tool calls, never progressing. This is the writeup of how I found out why, and what I built to make sure it wouldn't happen silently again. The symptom The agent would reach a certain page state, issue a "click" action, and instead of moving forward, issue the exact same "click" action again next turn. And again. It wasn't crashing — it was confidently, repeatedly doing the same wrong thing, burning API calls the whole time. Watching it live in the WebSocket UI didn't tell me much beyond "it's stuck." Screenshots looked identical between iterations. No exceptions. No obviously broken state. Just a model that kept making the same call and never noticing it wasn't working. Why "just look at the screenshot" wasn't enough My first instinct was to eyeball the screenshots being passed to the model at each step. They looked fine — same page, same button. What I couldn't see just by looking was what the model actually received as context on each turn: was it getting the result of its previous action? Was the DOM snapshot accurately reflecting that the click had registered? Was the prompt telling it anything about prior attempts at all? Screenshots show you the world. They don't show you the model's reasoning, or what it was actually given to reason with. I needed the second thing, not the first. Building the trace I added structured logging of every LLM call — request and response — to a llm_calls.jsonl file. Each line: the full prompt sent, the tool calls requested, the DOM state at that point, timestamps. Nothing clever, just append-only structured logs I could grep and diff. Once I had that, the bug stopped being invisible. Diffing consecutive entries showed the actual problem: the DOM pruning step — which trims the page structure before sending it to the model, to keep token usage sane — was stripping out a state attribute that changed after the click fired. To the model, turn 12 and turn 13 looked identical , because the one thing that had changed was exactly the thing getting pruned away. The click wasn't failing. The agent's view of whether the click had worked was failing. It had no signal that anything had changed, so from its perspective, repeating the action was the reasonable move. The actual fixes Three changes came out of this, in order of how much they mattered: 1. Fixed the pruning logic to preserve state-relevant attributes. The DOM pruner was built for token efficiency first and correctness second. I rebalanced it to always retain attributes that commonly signal state changes (aria-expanded, checked, disabled, class diffs on the target element) even when trimming everything else around them. 2. Added an explicit "did anything change since last action" signal. Rather than relying on the model to infer state change from a raw DOM diff, I now compute a lightweight diff server-side and inject a blunt one-line summary into the prompt: changed / unchanged, and what changed if anything. Cheap to compute, and it means the model doesn't have to do the noticing — it just has to react. 3. A repetition guard as a backstop. If the same tool call with the same arguments fires 3 times in a row with no state change, the agent now breaks out and either tries an alternate strategy or surfaces the stall instead of continuing silently. This isn't a fix for the root cause — it's insurance against the next root cause I haven't found yet. The part that generalizes The specific bug was mine — a pruning function trimming the wrong thing. But the shape of it isn't specific to browser agents: an LLM agent can only reason about what it's told, and "looks right in a screenshot" is not the same as "is actually in the model's context." Any time an agent loops, stalls, or repeats — the first move isn't to stare at the output, it's to log the input, verbatim, at every step, and diff it across turns. If two turns look the same to the model, of course it behaves the same. The question is always why do they look the same , not why is the model being dumb . I also added a provider fallback chain (Gemini → Groq) while I was in there, mostly for uptime — but it turned out useful for a second reason: running the same trace through a different model was a fast way to sanity-check whether a stall was a prompt/context problem (both models loop) or a Gemini-specific quirk (only one loops). Cross-provider comparison as a debugging tool, not just a failover. *I build backend and browser automation systems in Python — FastAPI, Playwright, LLM integrations. If you're dealing with a similar agent-reliability problem or want to talk through one, I'm at https://www.linkedin.com/in/amarjit-jim-978322371

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/bob1982/debugging-an-llm-agent-that-wouldnt-stop-clicking-a-postmortem-57em

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
