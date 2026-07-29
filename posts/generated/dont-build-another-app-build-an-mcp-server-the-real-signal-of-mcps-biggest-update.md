---
title: "Don't build another app — build an MCP server: the real signal of MCP's biggest update"
slug: "dont-build-another-app-build-an-mcp-server-the-real-signal-of-mcps-biggest-update"
author: "Hunter G"
source: "devto_ai"
published: "Wed, 29 Jul 2026 19:17:37 +0000"
description: "Anthropic just shipped the biggest MCP update since launch (MCP 2026-07-28). Most write-ups read like a changelog: stateless core, extensions, auth hardening..."
keywords: "mcp, server, build, your, claude, anthropic, you, signal"
generated: "2026-07-29T19:24:36.671214"
---

# Don't build another app — build an MCP server: the real signal of MCP's biggest update

## Overview

Anthropic just shipped the biggest MCP update since launch (MCP 2026-07-28). Most write-ups read like a changelog: stateless core, extensions, auth hardening. But if you actually build things, the update has one real signal: your distribution channel just got upgraded. MCP is now the HTTP of the AI era — and the pipe is enterprise-grade, runs on serverless, and can render your UI inside Claude itself . Which points at a very concrete move: stop building another app to fight for attention. Build an MCP server, and let the agent ecosystem be your distribution. (Based on a 新智元 / 36kr write-up and Anthropic's official MCP blog; specs per Anthropic.) The standard war is over 400M+ monthly SDK downloads (4x this year). TypeScript and Python each past 1 billion cumulative downloads. 950+ MCP servers in the Claude store, used by millions daily. As Anthropic frames it: HTTP wired the world's computers into the internet; MCP is wiring the world's software, data, and APIs into a network an AI orchestrates. For builders, "should I use MCP" is settled. The question is whether you're on the rail. Signal 1: the core went stateless — so your server can run serverless The change developers wanted most: MCP moved from stateful (session state, connection handshakes, hard to scale in cloud-native setups) to a pure request/response model. Every request is self-describing (identity and capabilities live in _meta ). The payoff: Serverless / edge : deploy the server to AWS Lambda, Vercel, Cloudflare Workers — no renting a persistent box for a few KB of session state. Unlimited horizontal scaling : put it behind a plain round-robin load balancer; any machine can handle any request. Need state? Generate an explicit Handle the model passes back as a parameter — not hidden in the transport layer. Cleaner, and it fits how the model thinks. Translation: building an MCP server now costs about as much as writing one serverless function. The channel got bigger and the bar to get on it dropped — those two happening together is the actual opportunity window. Signal 2: extensions are first-class — you may not need a front-end Anthropic promoted Extensions to first-class citizens with an official framework. Three launch features, and the first is the one that should reframe how you think about products: MCP Apps : your server renders an interactive UI right inside the Claude chat (a sandboxed iframe). Ask Claude for revenue data → it renders a live interactive dashboard in the thread. Ask it to run a cloud server → a control panel pops up. No more tab-switching between Claude and every SaaS app. Tasks : long-running async work (analyze 100GB of logs, render a 3D video) via polling + a subscription stream. Enterprise Managed Auth (EMA) : central access control through Microsoft Entra, Okta; zero-touch SSO. MCP Apps is the punchline: your interface can live inside Claude. You don't build a front-end, pull a user base, and educate a market. You make the capability; the channel carries the interface and the users. Signal 3: the pipe now reaches inside the firewall The protocol got an 18-month production-hardening pass: MRTR (multi round-trip requests) replacing long-lived connections, header-based routing ( Mcp-Method / Mcp-Name so gateways/rate-limiters route without parsing JSON), cacheable list responses ( ttlMs + cacheScope — prompt cache is money), and military-grade auth (production OAuth 2.0/OIDC, RFC 9207, deprecating DCR for CIMD — finally killing the localhost redirect_uri pain for CLI clients). The headline for enterprises is MCP Tunnels (research preview): connect Claude to an internal MCP server with no public IP, no inbound firewall rules, no IP allowlist — an encrypted tunnel under the corporate firewall, so finance/health/gov data can reach AI safely. Figma, Intuit, Netlify, and Zoom are backing it — their hardest requirements (design assets, finance-grade auth, serverless-native statelessness, low latency) all satisfied at once. That's MCP crossing from "geek toy" into the enterprise deep end. The takeaway: build a capability, not another app The real signal of this update isn't "the protocol got better." It's that distribution got upgraded and the bar to get on it dropped, at the same time — standard established, enterprise-grade, serverless-runnable, UI-lives-in-Claude. So the concrete move for builders: don't build another website or app to fight the whole world for attention. Build an MCP server, and let the agent ecosystem be your distribution. API first, UI later — because the interface (MCP Apps), the users (millions), the enterprise access (Tunnels), and the billing/caching are already laid down for you. Agents are the new distribution channel. This update paved the road into a highway. All four Tier-1 SDKs (TS/Python/Go/C#) are updated, with a 12-month deprecation window for the old way. The cheapest ticket into the age of agents is to go refactor one MCP server of your own — the next hit might be sitting in that list of 950+. Based on 新智元 (author ASI启示录), republished by 36kr, and Anthropic's MCP blog / @ClaudeDevs. Data and specs per Anthropic; this is a structured secondary read.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/hunter_g_50e2ec233acd07b5/dont-build-another-app-build-an-mcp-server-the-real-signal-of-mcps-biggest-update-1iio

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
