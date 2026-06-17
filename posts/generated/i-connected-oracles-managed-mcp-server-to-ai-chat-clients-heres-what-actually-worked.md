---
title: "I Connected Oracle's Managed MCP Server to AI Chat Clients — Here's What Actually Worked"
slug: "i-connected-oracles-managed-mcp-server-to-ai-chat-clients-heres-what-actually-worked"
author: "Ranjith Kumar Kondoju"
source: "devto_ai"
published: "Wed, 17 Jun 2026 04:40:44 +0000"
description: "AI assistants are getting good at doing things, not just talking — largely thanks to MCP (Model Context Protocol) , the open standard that lets an AI client ..."
keywords: "server, mcp, oauth, user, client, database, read, only"
generated: "2026-06-17T04:47:02.514212"
---

# I Connected Oracle's Managed MCP Server to AI Chat Clients — Here's What Actually Worked

## Overview

AI assistants are getting good at doing things, not just talking — largely thanks to MCP (Model Context Protocol) , the open standard that lets an AI client call external tools. Oracle recently shipped a managed MCP server in OCI (Database Tools MCP Server) that lets an AI client run queries against an Oracle database, with OAuth and role-based access built in. I wanted to use it for something practical: read-only health checks for an Oracle E‑Business Suite database on 19c, surfaced inside an AI chat — "Is the database up? Any blocking sessions? Which concurrent managers are down?" It worked in the end — an AI assistant pulling live, read-only database health data. But getting there taught me a lot about how managed MCP + OAuth actually behaves. Here's the honest journey. The setup, in plain terms A managed MCP server in OCI, pointed at the database through a read-only user . A few custom read-only SQL tools (instance overview, active sessions, blocking sessions, concurrent‑manager status…). An AI chat client connected over MCP + OAuth. Gotcha #1 — a private database needs a Private Endpoint The MCP service is managed — it runs in Oracle's tenancy, not your network. So it can't reach a private database by itself. You attach a Private Endpoint to give it a foothold inside your VCN. Keeping things private is exactly why you need the endpoint, not a reason to skip it. Gotcha #2 — read-only is your real guardrail I pointed the connection at a read-only database user . Even though the toolset can run general SQL, the account simply can't write . That one decision beats any amount of "please be careful" prompting. Gotcha #3 — the endpoint URL has a version date, and it matters Every OCI MCP server URL has an API-version segment like /20250830/ . I reused a URL from an earlier server with a different date. Result: HTTP 404 on every call , no matter how perfect my auth was. Lesson: copy the exact Server URL from the console , version date included. The 404 looked like an auth problem for ages — it wasn't. Gotcha #4 — OAuth: 404 vs 401 breaks self-hosted web chat UIs The big one. Many clients' MCP OAuth is discovery-driven : hit the server, expect a 401 with OAuth metadata, use it to launch the login. Oracle's server returns 404 to unauthenticated requests — so a self-hosted web chat UI (I tried LibreChat) never builds the login URL and can't start the flow, even when everything is configured correctly. Two things compound it for server-hosted web UIs: They run headless (no browser for the interactive login). The 404 defeats auto-discovery. So server-hosted chat UIs aren't a good fit for this server today. Gotcha #5 — the role rides on the user token, not the app token I tried a client-credentials token (app identity) to skip the browser. It authenticated (HTTP 200!) but every tool call returned Missing required permissions . The access role is a user role — and client-credentials tokens carry scopes, not roles . The fix was an authorization_code (user) token : the user has the role, so their token is authorized. What actually worked: desktop clients Desktop AI clients have a browser for the login and happily do the user OAuth flow. Using mcp-remote with static OAuth metadata (so it doesn't depend on the 404 discovery), I connected from Claude Desktop and VS Code + Cline : { "mcpServers" : { "db_diag" : { "command" : "npx.cmd" , "args" : [ "-y" , "mcp-remote" , "<exact Server URL with the correct /YYYYMMDD/>" , "3334" , "--static-oauth-client-info" , "{ \" client_id \" : \" <public client id> \" }" , "--static-oauth-server-metadata" , "{ \" issuer \" : \" ... \" , \" authorization_endpoint \" : \" .../authorize \" , \" token_endpoint \" : \" .../token \" }" ] } } } A browser opened, I logged in as a user with the right role, and the tools appeared. Asking "give me the instance overview" returned live data — instance name, version, open mode, uptime — all read-only. A few smaller traps On Windows, clients spawn npx and fail with ENOENT — use npx.cmd and restart the app so PATH refreshes. Don't run two clients on the same OAuth callback port ( EADDRINUSE ) — give each its own port and register both redirects. Avoid TO_CHAR(date,'HH24:MI:SS') in toolset SQL — the colons get parsed as bind variables. Return the raw date. Use gv$ views (not v$ ) to see all RAC instances. Takeaways Managed MCP + AI agents are real — a governed, read-only DB assistant is genuinely useful. Match the client to the deployment — desktop clients handle the OAuth user flow; headless web UIs struggle. A read-only DB user is your strongest control. Copy the exact server URL — a 404 is often a path problem, not auth. Roles live on user tokens — client-credentials gets you authenticated, not authorized. If you're wiring an AI client to Oracle's managed MCP server, I hope this saves you a few hours. Questions welcome in the comments. 👇

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/rkondoju/i-connected-oracles-managed-mcp-server-to-ai-chat-clients-heres-what-actually-worked-k6p

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
