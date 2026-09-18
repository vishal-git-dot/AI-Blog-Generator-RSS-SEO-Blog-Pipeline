---
title: "Give Your AI Agent WhatsApp Superpowers with MCP (Official Business API)"
slug: "give-your-ai-agent-whatsapp-superpowers-with-mcp-official-business-api"
author: "Dhotiiiii"
source: "devto_ai"
published: "Fri, 18 Sep 2026 16:05:26 +0000"
description: "What if Claude could check your store's WhatsApp inbox, look up an order, and send the customer a reply — by itself? That's what the Model Context Protocol (..."
keywords: "api, mcp, your, whatsapp, tokolaku, claude, business, https"
generated: "2026-09-18T16:10:33.642055"
---

# Give Your AI Agent WhatsApp Superpowers with MCP (Official Business API)

## Overview

What if Claude could check your store's WhatsApp inbox, look up an order, and send the customer a reply — by itself? That's what the Model Context Protocol (MCP) makes possible, and in this post I'll show you how to wire any MCP-capable AI client (claude.ai, Claude Code, ChatGPT, or your own agent) to a live WhatsApp Business platform in under two minutes. No SDKs, no servers to host — it's a remote MCP server. The server Tokolaku is a WhatsApp business platform for Indonesian SMBs built on Meta's official WhatsApp Business API (Cloud API — so no gray-market gateways, no ban roulette). It exposes a hosted MCP server: https://api.tokolaku.id/mcp Transport: Streamable HTTP, stateless Auth: OAuth 2.1 (interactive clients) or API key (programmatic) Tools: send messages, browse inbox conversations, products, orders, manage webhooks Option 1: claude.ai / ChatGPT — just paste the URL Modern MCP clients support OAuth discovery, so the whole setup is: Settings → Connectors → Add custom connector (claude.ai) or the MCP equivalent in your client Paste https://api.tokolaku.id/mcp You'll be redirected to sign in with your Tokolaku account and approve access Done. Claude now has 6 read-only tools scoped to your account: list_channels , list_conversations , get_conversation , list_products , list_orders , get_order . Behind the scenes this uses PKCE, dynamic client registration (RFC 7591), and standard discovery metadata (RFC 8414/9728) — tokens are minted per user, short-lived, and revocable from the dashboard. Try prompts like: "Any unpaid orders from this week? Summarize who I should follow up with." "Which products got asked about most in yesterday's chats?" Option 2: Claude Code / SDK agents — API key For write access (actually sending messages), use a secret API key from the developer dashboard: { "mcpServers" : { "tokolaku" : { "type" : "http" , "url" : "https://api.tokolaku.id/mcp" , "headers" : { "x-api-key" : "tk_live_sk_xxx" } } } } Tools follow your key's scopes ( tools/list reflects them), and write tools like send_message go through the exact same billing, quota, and rate-limit path as the REST API — your agent can't do anything your key can't. A fun one to try in Claude Code: "A customer at +62812xxxx asked about their order this morning. Check the conversation, find the order status, and send them a polite update." Why this pattern is interesting Most "AI + WhatsApp" setups either screen-scrape the desktop app (fragile, ToS-risky) or make you build a bot pipeline first. A remote MCP server flips it: the platform speaks MCP natively, and any agent — today's or next year's — gets structured, permissioned access to real business state: conversations, catalog, orders. The same endpoint also serves classic REST ( POST /api/v1/messages , webhooks with HMAC signatures) and official SDKs on npm , PyPI , and Packagist — so the MCP layer is a first-class citizen, not a demo. Links Server metadata: https://github.com/Rustam335/tokolaku-mcp API reference & MCP docs: https://tokolaku.id/api-docs The platform (WhatsApp Business API from Rp99k/mo, zero message markup): https://tokolaku.id/whatsapp-api Questions or weird edge cases? I'd love to hear what your agents do with a WhatsApp inbox. 👇

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/rustam335/give-your-ai-agent-whatsapp-superpowers-with-mcp-official-business-api-3f9l

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
