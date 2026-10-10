---
title: "Building a revenue path for registered agents — looking for collaborators"
slug: "building-a-revenue-path-for-registered-agents-looking-for-collaborators"
author: "Bryant rudolph"
source: "devto_ai"
published: "Sat, 10 Oct 2026 12:09:44 +0000"
description: "I've been building infrastructure for agent-to-agent commerce and I'm at the point where the technical foundation works but the demand side is empty. I'm loo..."
keywords: "agent, what, agents, saax, where, building, commitment, mcp"
generated: "2026-10-10T12:13:29.606236"
---

# Building a revenue path for registered agents — looking for collaborators

## Overview

I've been building infrastructure for agent-to-agent commerce and I'm at the point where the technical foundation works but the demand side is empty. I'm looking for people who want to build revenue on top of it. What SAAX does, in one line: it's a commitment layer that records what an agent agreed to, verifies fulfillment, and handles recovery if it fails. It sits between authorization (AP2, ACP) and settlement (x402, MPP, card networks). What's live right now: MCP endpoint at https://www.saax-protocol.com/mcp with 10 tools Commitment lifecycle with persistent storage Public spec, conformance suite, integration docs Registry listing on the MCP Registry and Glama Where I want to go with it: Two directions I think are viable right now, and I don't have the bandwidth to pursue both: Direction 1 — Registered agents selling services. An agent registers its capability (data retrieval, code review, translations, security scans, etc.), and SAAX routes demand to it. The agent gets paid per job. The routing and settlement already work. What's missing is agents that actually have services to sell. Direction 2 — Businesses sending agents to purchase. A business has an agent that needs to buy something from a supplier. SAAX records the commitment, verifies the delivery, handles the payment, and writes the audit trail. The infrastructure exists. What's missing is businesses that have agents transacting at a volume where the commitment layer is worth using. What I'm asking: Is this useful to anyone here? If you're running an agent that has a service to sell, or you're building a system where agents transact with external suppliers, I'd like to hear where it breaks for you and what would need to exist to make it work. If you're interested in building revenue on top of this — as an agent operator, a supplier, or a partner — I'm open to conversations. No token, no pitch deck. Just a working protocol looking for its first users. Spec is at saax-protocol.com/spec. MCP endpoint is live and free to test. Reply here or reach out at support@saax-protocol.com .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/brudy_dev24/building-a-revenue-path-for-registered-agents-looking-for-collaborators-4dbk

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
