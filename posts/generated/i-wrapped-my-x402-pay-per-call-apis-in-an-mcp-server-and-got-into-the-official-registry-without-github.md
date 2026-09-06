---
title: "I Wrapped My x402 Pay-Per-Call APIs in an MCP Server — and Got Into the Official Registry Without GitHub"
slug: "i-wrapped-my-x402-pay-per-call-apis-in-an-mcp-server-and-got-into-the-official-registry-without-github"
author: "Marcus Chenmember_832ef635"
source: "devto_webdev"
published: "Sun, 06 Sep 2026 19:50:00 +0000"
description: "Three weeks ago I put a QR code generator behind HTTP 402 and called it a business. It made $0.00. Then I added an image toolkit. Same result. The endpoints ..."
keywords: "mcp, tools, registry, http, domain, free, you, call"
generated: "2026-09-06T20:14:44.039973"
---

# I Wrapped My x402 Pay-Per-Call APIs in an MCP Server — and Got Into the Official Registry Without GitHub

## Overview

Three weeks ago I put a QR code generator behind HTTP 402 and called it a business. It made $0.00. Then I added an image toolkit. Same result. The endpoints were listed on every x402 directory I could find, the 402 challenges were textbook-compliant, and still — nothing. The problem wasn't pricing or discoverability. It was shape : the agents I wanted as customers don't shop for REST endpoints. They shop for tools . MCP tools. So last night I wrapped all three pay-per-call APIs in a single MCP server (streamable-http), kept the x402 payment gate exactly where the money moves, and published the result to the official MCP Registry — without a GitHub account, without a paid domain, without KYC. Here's the whole trick. The gate: 402 on tools/call , everything else free The MCP handshake has to be free, or directory probes and clients can't even list your tools. My server answers initialize , tools/list , ping and notifications for free, and only charges when an agent actually calls a tool: FREE_METHODS = ( " initialize " , " notifications/initialized " , " notifications/cancelled " , " tools/list " , " ping " ) if method != " tools/call " : ... # free # tools/call without a PAYMENT-SIGNATURE header -> HTTP 402 # + a base64 PAYMENT-REQUIRED header describing price in USDC on Base One subtlety that cost me an hour: directory validators send empty or unknown-method POSTs to probe your endpoint. If you answer those with a JSON-RPC error (HTTP 200), the validator reports "endpoint returns 200 instead of 402" and rejects you. Any non-free method, identified or not, must get the 402 challenge. Three tools, settled through the PayAI facilitator (permissionless, no API key, the facilitator pays the gas): generate_qr_code — $0.01 process_image (resize/convert/compress/thumbnail) — $0.01 analyze_text (summary/sentiment/keywords/translate, LLM-backed) — $0.02 The registry: HTTP auth with a key you host yourself The official MCP Registry ( registry.modelcontextprotocol.io ) is what PulseMCP and friends crawl. The docs push the GitHub login flow — my GitHub account was long dead, so I used the other option almost nobody writes about: HTTP authentication . You generate an Ed25519 key, serve one line of text at /.well-known/mcp-registry-auth on a domain you control, and the registry accepts your reverse-DNS namespace: openssl genpkey -algorithm Ed25519 -out key.pem PUBLIC_KEY = " $( openssl pkey -in key.pem -pubout -outform DER | tail -c 32 | base64 ) " echo "v=MCPv1; k=ed25519; p= ${ PUBLIC_KEY } " > mcp-registry-auth # serve it at https://your-domain/.well-known/mcp-registry-auth mcp-publisher login http --domain your-domain --private-key <hex> mcp-publisher publish My "domain" is a free sslip.io hostname on a $4 VPS. It worked. One gotcha: the registry caps description at 100 characters (422 otherwise) — the schema error tells you the limit, at least. The server.json for a remote-only server is refreshingly small: { "name" : "io.sslip.249.111.77.187/x402-mcp-tools" , "description" : "Pay-per-call MCP tools via x402 (USDC on Base): QR codes, image processing, LLM text analysis." , "version" : "1.0.0" , "remotes" : [{ "type" : "streamable-http" , "url" : "https://mcp.187.77.111.249.sslip.io/mcp" }] } Ugly namespace, granted. It's mine, it verifies, and it cost exactly $0. What I learned Distribution beats features. The same three APIs sat unbought as REST endpoints. As MCP tools they're one tools/list away from any agent with a wallet. Free handshake, paid execution is the only viable MCP monetization pattern today — and it maps cleanly onto x402's 402 challenge. You don't need GitHub for the official registry. The HTTP auth flow is documented but nobody seems to use it. A throwaway domain and one OpenSSL command are enough. Revenue so far: still $0.00. But the server is now in the registry every major MCP directory crawls, the 402 gate is standard-compliant, and settlement costs me nothing. The infrastructure bet is placed — now we see if agents actually pay for QR codes.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/marcuschen-dev/i-wrapped-my-x402-pay-per-call-apis-in-an-mcp-server-and-got-into-the-official-registry-without-3gm2

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
