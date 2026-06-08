---
title: "We tried to independently verify all 22,561 MCP servers. Only 18 could be checked."
slug: "we-tried-to-independently-verify-all-22561-mcp-servers-only-18-could-be-checked"
author: "Dinesh Kumar"
source: "devto_ai"
published: "Mon, 08 Jun 2026 04:34:41 +0000"
description: "I maintain a deduplicated index of 22,561 MCP servers. I tried to independently verify all of them at runtime. Not by scanning the source in the repo, but by..."
keywords: "server, mcp, can, servers, not, code, how, production"
generated: "2026-06-08T04:42:39.223262"
---

# We tried to independently verify all 22,561 MCP servers. Only 18 could be checked.

## Overview

I maintain a deduplicated index of 22,561 MCP servers. I tried to independently verify all of them at runtime. Not by scanning the source in the repo, but by actually reaching the running server to check it responds and behaves. Only 18 could be checked. Here is what that says about how we trust the tools our agents call. The numbers 22,561 MCP servers indexed, deduplicated across registries. 117 have any independent behavioral or reliability record. That is 0.52%. 18 expose a live MCP endpoint I can independently reach and test. That is 0.08%. 8,655 list an http endpoint. Only about 150 resolve to a real hosted service. Only 18 of those actually respond as a working MCP server. The rest are GitHub repos, npm packages, or local stdio servers. Code you can read, but not a running service anyone can verify in production. Static scans read the code. They never see the running server. The popular way to vet an MCP server today is a static scan: read the source in the repo, look for known issues, give it a grade. That is useful, but it grades the code in a repository. It is not the server your agent connects to at call time, and the two can differ. A server can pass a code review and then, in production, be slow, dead, swapped, or behave nothing like its description. The attacks the security community worries about most for agents, tool poisoning and rug pulls, happen at runtime, after a human approved the server. That is exactly where a static scan cannot see. The gap So we have an ecosystem where 99.9% of servers cannot be independently reached or tested in production, and the dominant trust signal is a one time read of code that is not even the running artifact. That is not a reliability record. It is a black box with a nice README. If you run agents in production, the question is not did this code pass a scan. It is can I prove what this server did the last thousand times an agent called it. Today, for almost every MCP server, nobody can. What I am doing about it I measure MCP servers by behavior, not by reading their code. Every server I can reach gets tested for whether it responds, how often, how fast, and whether it does what it claims, over time, with a signed and tamper evident record so the history cannot be quietly rewritten. It is a small slice of the ecosystem today because the ecosystem is structurally hard to verify. That is the point. The gap is the story. Check any server: https://dominionobservatory.com/atlas/score The full data: https://dominionobservatory.com/atlas/report How runtime verification works: https://dominionobservatory.com/atlas/liveness How are you verifying the MCP servers your agents use in production, if at all?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/vdineshk/we-tried-to-independently-verify-all-22561-mcp-servers-only-18-could-be-checked-1398

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
