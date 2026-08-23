---
title: "A simple typo swallowed our telemetry: Why our AI agent spans vanished into the void"
slug: "a-simple-typo-swallowed-our-telemetry-why-our-ai-agent-spans-vanished-into-the-void"
author: "S M Tahosin"
source: "devto_python"
published: "Sun, 23 Aug 2026 18:20:08 +0000"
description: "This is a submission for DEV's Summer Bug Smash: Clear the Lineup . The setting In the modern era of autonomous AI agents, observability is everything. If an..."
keywords: "agents, model, sdk, agent, spans, telemetry, sentry, code"
generated: "2026-08-23T18:35:57.068965"
---

# A simple typo swallowed our telemetry: Why our AI agent spans vanished into the void

## Overview

This is a submission for DEV's Summer Bug Smash: Clear the Lineup . The setting In the modern era of autonomous AI agents, observability is everything. If an agent hallucinates or takes an unexpected path, you need to know exactly which model was invoked, what the system prompt was, and how long it took. The Sentry Python SDK provides a fantastic integration ( OpenAIAgentsIntegration ) specifically designed to trace the internal execution of the openai Swarm/Agents framework. It hooks into the framework's core loops to automatically generate beautiful, hierarchical tracing spans for every tool execution and model invocation. The silence While reviewing the integration for version 0.8.0 of the openai-agents SDK, something felt off. The tool execution spans were working perfectly, but the model invocation spans—the most critical pieces of the telemetry—were completely missing. The Sentry dashboard was virtually blind to when the agent actually reached out to the LLM. The investigation I started digging into the SDK's source code at sentry_sdk/integrations/openai_agents/__init__.py . In the 0.8.0 release of the openai-agents framework, the internal architecture had changed. The method responsible for resolving models was refactored and moved from AgentRunner._get_model() to a new location: agents.run_internal.turn_preparation.get_model() . The Sentry maintainers were aware of this change. They wrote the exact code needed to wrap the new turn_preparation.get_model function: @wraps ( turn_preparation . get_model ) def new_wrapped_get_model ( agent : " agents.Agent " , run_config : " agents.RunConfig " ) -> " agents.Model " : return _get_model ( turn_preparation . get_model , agent , run_config ) The wrap was perfectly executed. The telemetry injection was flawless. So why wasn't it working? I looked at the very next line of code, where the wrapped function is injected back into the SDK: agents . run_internal . run_loop . get_model = new_wrapped_get_model There it was. A simple, silent typo. They correctly wrapped turn_preparation.get_model , but they assigned the result to run_loop.get_model . Because the SDK internally uses turn_preparation to resolve the model, the patched function sitting inside run_loop was completely ignored. The patch never installed. The model invocation spans vanished into the void. The fix The fix was as simple as correcting the assignment target. I submitted a patch to ensure the wrapped function overwrites the actual method the SDK uses: - agents . run_internal . run_loop . get_model = new_wrapped_get_model + agents . run_internal . turn_preparation . get_model = new_wrapped_get_model By changing run_loop to turn_preparation , the SDK now correctly intercepts the model resolution step. Accurate telemetry restored! In software engineering, some of the most critical bugs—the ones that entirely disable core features—often come down to a single line of misdirected code. GitHub PR: getsentry/sentry-python#7227

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/tahosin/a-simple-typo-swallowed-our-telemetry-why-our-ai-agent-spans-vanished-into-the-void-526l

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
