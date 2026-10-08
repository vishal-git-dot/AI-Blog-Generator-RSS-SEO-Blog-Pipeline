---
title: "MCP connection errors explained: 404 on /sse, 406 Not Acceptable, session 400s, 402"
slug: "mcp-connection-errors-explained-404-on-sse-406-not-acceptable-session-400s-402"
author: "Tanod Labs"
source: "devto_ai"
published: "Thu, 08 Oct 2026 23:01:40 +0000"
description: "MCP Streamable HTTP is one URL. The client POSTs JSON-RPC to it and may open a GET stream on the same URL; nothing else is part of the address. Most connecti..."
keywords: "mcp, server, client, json, tanod, sse, not, stream"
generated: "2026-10-08T23:09:13.585481"
---

# MCP connection errors explained: 404 on /sse, 406 Not Acceptable, session 400s, 402

## Overview

MCP Streamable HTTP is one URL. The client POSTs JSON-RPC to it and may open a GET stream on the same URL; nothing else is part of the address. Most connection failures we see in our own server log are a client talking to a different address than the one it was given, or sending the wrong headers. Here is what each status means and the fix, with the exact messages the official TypeScript and Python SDKs send. 404 Not Found on /sse , or with /mcp appended The earlier HTTP+SSE transport (protocol revision 2024-11-05) opened a GET to an SSE URL and read an endpoint event that named a second URL for POSTs. Streamable HTTP (2025-03-26 and later) replaced both with a single URL. A client that still speaks SSE-only, or a bridge that guesses, appends /sse and gets a 404 from any Streamable HTTP server. Some clients also append /mcp to a URL that already ends in the server path. Fix: use the URL exactly as published. For a client that only speaks stdio, run a bridge such as npx mcp-remote https://tanod.dev/mcp --transport http-only so it does not fall back to SSE. For Tanod, every server is Streamable HTTP: https://tanod.dev/mcp and the focused servers such as https://tanod.dev/mcp/docs ; /mcp/docs/sse , /mcp/docs/mcp and /api/mcp are all 404. 406 Not Acceptable: Client must accept both application/json and text/event-stream A POST must carry Accept: application/json, text/event-stream , because the server may answer a request either with one JSON body or with an SSE stream. Both SDKs reject anything else with this message. A GET (the optional server-to-client stream) must accept text/event-stream . Curl and most HTTP libraries send Accept: */* , which some servers take and others do not; set the header explicitly. 415 Unsupported Media Type: Content-Type must be application/json The request body is JSON-RPC and must be sent as Content-Type: application/json . Form encoding, a missing header, or text/plain from a quick script all produce this. 400 Bad Request: Server not initialized, or Missing session ID A stateful server expects an initialize request first. Its response carries an Mcp-Session-Id header, and the client must send that header on every later request. Calling tools/list before initialize , or dropping the header, gives one of these two 400s. After the server restarts, the old session is gone and the server answers 404 Session not found : the client has to start a new session with a fresh initialize , which well-behaved clients do on their own. Tanod's servers are stateless: no session header is needed, and tools/list works as the first request, so a shell check is one command: curl -s -X POST https://tanod.dev/mcp/docs \ -H "Content-Type: application/json" \ -H "Accept: application/json, text/event-stream" \ -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}' 405 Method Not Allowed on GET The specification lets a server decline the standalone GET stream. A client that opens it and gets 405 should carry on with POSTs; this is not a failure of the connection, and tool calls still work. A browser shows a web page or a redirect A GET with Accept: text/html is a person, not an MCP client. Many servers, Tanod included, send that request to a human page (here, the server overview ). The MCP client, which POSTs, is unaffected. 402 Payment Required, or a tool result with isError and a PaymentRequired object On a pay-per-call server the price quote travels inside MCP: the tool result has isError: true and its structuredContent is an x402 PaymentRequired object (scheme, network, amount, pay-to address). An x402-aware client signs the payment and repeats the call with the payload in params._meta["x402/payment"] ; the receipt comes back in _meta["x402/payment-response"] . A client without x402 support sees a tool error with the price in it, which is the intended reading. On Tanod the free daily allowance is spent before any quote is issued, and the plain HTTP routes return a classic 402 with the same object as JSON. The call hangs, then the client reports a timeout Long tools (OCR of a large PDF, a full contract scan) can take tens of seconds, and clients ship with their own timeouts; Claude Code, for example, has an MCP_TIMEOUT setting in milliseconds. Tanod answers every call inside 90 seconds and returns a structured error rather than hanging, so a client timeout shorter than that is the thing to raise. If the server sends SSE progress notifications, the stream also keeps the connection alive through proxies. Checklist Use the published URL. Nothing appended, nothing guessed. POST with Content-Type: application/json and Accept: application/json, text/event-stream . Stateful servers: initialize first, then echo Mcp-Session-Id ; on 404 start over. Read 402 and PaymentRequired tool errors as price quotes. Raise the client timeout before blaming the server. Tanod's hosted MCP servers ( https://tanod.dev/mcp-servers/ ) are the worked example; the checks apply to any Streamable HTTP server. The guide version, kept current: https://tanod.dev/learn/mcp-server-connection-errors.html

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/tanod/mcp-connection-errors-explained-404-on-sse-406-not-acceptable-session-400s-402-dik

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
