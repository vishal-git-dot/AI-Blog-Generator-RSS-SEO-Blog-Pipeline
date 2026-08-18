---
title: "I built TookEffect to verify what AI agents actually did"
slug: "i-built-tookeffect-to-verify-what-ai-agents-actually-did"
author: "Gabriel Salera"
source: "devto_ai"
published: "Tue, 18 Aug 2026 18:35:00 +0000"
description: "AI coding agents are getting very good at taking real actions: merging pull requests, deploying applications, and changing production systems. But there is a..."
keywords: "tookeffect, agent, real, agents, expected, built, what, actually"
generated: "2026-08-18T18:44:45.288328"
---

# I built TookEffect to verify what AI agents actually did

## Overview

AI coding agents are getting very good at taking real actions: merging pull requests, deploying applications, and changing production systems. But there is a problem I kept running into: An agent saying "done" is not proof that the intended change actually happened. So I built TookEffect . TookEffect independently checks the real external system after an AI agent performs an action, verifies the expected outcome, and keeps evidence of what actually happened. A simple example An AI agent says: "The pull request was merged." TookEffect doesn't trust that response. It reads GitHub independently, checks the expected repository, PR, branch and resulting state, and produces a verdict: APPLIED — the expected effect is proven NOT_APPLIED — the expected effect did not happen AMBIGUOUS — there isn't enough evidence to prove either outcome The same idea applies to deployments. An agent says: "Production was deployed." TookEffect checks the real deployment platform instead of trusting the agent's own tool response. What works today Right now TookEffect supports verified actions across: GitHub Vercel Cloudflare It can be used through an API or MCP, so the verification layer is independent of the AI model or coding agent you're using. The principle behind the project is: AI says done. TookEffect proves it. I built this because I think AI agents will increasingly be allowed to perform consequential actions on real systems, and we need something outside the agent itself to verify the resulting state. It's still early, and I'm especially interested in feedback from developers already using AI agents in real repositories or deployment workflows. Would independent verification like this be useful in your workflow? https://tookeffect.com

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/gabriel_salera_8f21f3260a/i-built-tookeffect-to-verify-what-ai-agents-actually-did-38dn

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
