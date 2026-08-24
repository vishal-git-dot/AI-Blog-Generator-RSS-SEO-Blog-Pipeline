---
title: "OpenART Red-Teams Stateful Agents Across 10,000 Evolving Environment Scenarios"
slug: "openart-red-teams-stateful-agents-across-10000-evolving-environment-scenarios"
author: "aimodels-fyi"
source: "devto_ai"
published: "Mon, 24 Aug 2026 18:34:19 +0000"
description: "This is a Plain English Papers summary of a research paper called OpenART Red-Teams Stateful Agents Across 10,000 Evolving Environment Scenarios . If you lik..."
keywords: "openart, across, environment, safety, red, stateful, scenarios, can"
generated: "2026-08-24T18:48:28.655490"
---

# OpenART Red-Teams Stateful Agents Across 10,000 Evolving Environment Scenarios

## Overview

This is a Plain English Papers summary of a research paper called OpenART Red-Teams Stateful Agents Across 10,000 Evolving Environment Scenarios . If you like these kinds of analyses, you can find more AI and machine-learning research on AIModels.fyi or follow us on Twitter . OpenART turns persistent state into the red-team target OpenART evaluates agent safety across more than 10,000 validated stateful scenarios spanning 50 domains and requiring a median of 97 tool calls. Its central claim is that safety failures can emerge from trajectories in which workspace data, permissions, memory, and plans are repeatedly modified, rather than from isolated prompts alone. The arena keeps each benign task objective and hidden safety contract fixed while changing only the target-visible environment state. This design targets delayed failures that static benchmarks can miss: an early authorized mutation may influence later decisions, expose protected resources, or produce unsafe output many steps after the original change. OpenART extends the broader idea of agent safety evaluation by making persistent environment state the object that evolves during testing. OpenART reports a pooled strict Attack Success Rate of 85.0% across 75 agent-model configurations. Strict success requires both the deterministic evaluator and a GLM-5.2 judge to identify the attack condition, so disagreements count as failures rather than being treated as partial evidence.... Continue reading the full paper summary on AIModels.fyi →

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/aimodels-fyi/openart-red-teams-stateful-agents-across-10000-evolving-environment-scenarios-2063

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
