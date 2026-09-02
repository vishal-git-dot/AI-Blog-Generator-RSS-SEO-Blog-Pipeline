---
title: "Screen a crypto wallet without leaving Claude or ChatGPT (PublicAML MCP server)"
slug: "screen-a-crypto-wallet-without-leaving-claude-or-chatgpt-publicaml-mcp-server"
author: "PublicAML"
source: "devto_ai"
published: "Wed, 02 Sep 2026 16:16:07 +0000"
description: "AI assistants are great at reasoning about on-chain data — but they can't see whether a wallet is sanctioned, tied to a scam, or where its funds came from un..."
keywords: "mcp, publicaml, server, api, add, wallet, claude, chatgpt"
generated: "2026-09-02T16:20:36.993841"
---

# Screen a crypto wallet without leaving Claude or ChatGPT (PublicAML MCP server)

## Overview

AI assistants are great at reasoning about on-chain data — but they can't see whether a wallet is sanctioned, tied to a scam, or where its funds came from unless you give them a tool. PublicAML now ships an MCP server , so Claude and ChatGPT can run AML/KYT checks directly in the chat. What it does Once connected, the assistant can call three tools against PublicAML's keyless backend: screen_address — risk score, sanctions status, category and source of funds for a BTC/ETH/BNB Chain/TRON address trace_funds — follow where funds moved list_counterparties — who the address transacted with No API key, no account — it is a non-profit public good. Two ways to add it Remote (zero install) — add the hosted server as a custom connector: https://mcp.publicaml.org/mcp In Claude: Settings → Connectors → Add custom connector → paste the URL. In ChatGPT: add it as a custom MCP connector. Then ask "screen 0x28C6…d60 for AML risk" and it calls the tool. Local (stdio) — for developers who want it in their own MCP client: npx @publicaml/mcp-server Both are listed in the official MCP registry (search "publicaml" at registry.modelcontextprotocol.io). Why it matters Pre-transaction screening usually means a paid API or a separate dashboard. Putting it behind MCP means the check happens where you already are — mid-conversation, mid-investigation — for free. Try the API directly: https://publicaml.org/api · Free wallet check: https://publicaml.org/free-crypto-aml/

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/public_aml/screen-a-crypto-wallet-without-leaving-claude-or-chatgpt-publicaml-mcp-server-3ogo

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
