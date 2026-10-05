---
title: "Eight broken tool calls: how six agent frameworks recover"
slug: "eight-broken-tool-calls-how-six-agent-frameworks-recover"
author: "Rashid Mahmood"
source: "devto_python"
published: "Mon, 05 Oct 2026 04:16:23 +0000"
description: "Models send bad tool calls: malformed JSON, a tool name that does not exist, a missing argument. What happens next is decided by the agent framework, not the..."
keywords: "res, tool, framework, not, model, calls, arena, argument"
generated: "2026-10-05T05:01:22.635281"
---

# Eight broken tool calls: how six agent frameworks recover

## Overview

Models send bad tool calls: malformed JSON, a tool name that does not exist, a missing argument. What happens next is decided by the agent framework, not the model. In agentic-arena I measure that directly. What was measured The resilience arena feeds eight scripted faults to every framework. The scripted model turns are byte-identical for all of them, so any difference in outcome is the framework's own error handling: res-01 calculator called with malformed JSON arguments res-02 a tool that does not exist res-03 an unevaluable expression (the tool returns ERROR) res-04 a required argument missing entirely res-05 an extra argument the tool does not accept res-06 search with an empty query res-07 an expression the safe evaluator must refuse res-08 arguments serialised as JSON null instead of an object Results framework recovered notes hand-rolled baseline 8/8 2 LLM calls each pydantic_ai 8/8 microsoft_af 8/8 langgraph 7/8 fails res-01 , malformed tool arguments openai_agents 7/8 raises on res-02 , unknown tool name google_adk 6/8 fails res-01 and res-02 , both uncaught exceptions smolagents 8/8 but 6 LLM calls on four faults, against 2 elsewhere The smolagents split is exact. On the four faults where the tool ran and returned something, it recovers in two calls like everyone else. On the four its validation layer rejects first (unknown name, missing argument, unexpected argument, null arguments), the error never reaches the transcript. The model cannot see it, re-emits the identical call, and the run spends the whole six-call budget, about 2.7x the prompt tokens, with zero tool calls recorded. It still reaches the right final answer, so the item passes. A retry wrapper would not help: the prompt is byte-identical every time. Google ADK is the only framework that loses both res-01 and res-02 . Both are uncaught exceptions rather than the model giving up, which is at least loud, and the kind of failure a retry wrapper can handle. A correction The smolagents row read 4/8 for several iterations. That was measured when an exhausted run returned an empty string; it now surfaces a final answer from its last memory step, so the check passes. The mechanism is unchanged, but the consequence is roughly 3x the cost, not a lost item. check_resilience.py now gates every count in this table, so the next drift fails CI instead of ageing silently. Caveats These are scripted-model (mock) behaviour measurements, not answer-quality rankings. Mock mode compares two things honestly: what a framework sends on the wire, and how it behaves when the model misbehaves. This arena is the second. It says nothing about how well any framework does with a real model on real tasks. Reproduce python -m arena run --arena resilience --framework all --mode mock --no-scorecard && python .github/scripts/check_resilience.py Full findings, with the command behind every number: https://code-with-rashid.github.io/agentic-arena/findings/

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/code-with-rashid/eight-broken-tool-calls-how-six-agent-frameworks-recover-9k1

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
