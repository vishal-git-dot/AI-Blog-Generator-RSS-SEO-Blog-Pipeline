---
title: "I Built 10 MCP Servers in a Weekend — Here's the Template I Wish I Had Starting Out"
slug: "i-built-10-mcp-servers-in-a-weekend-heres-the-template-i-wish-i-had-starting-out"
author: "z z"
source: "devto_python"
published: "Thu, 11 Jun 2026 10:18:45 +0000"
description: "MCP (Model Context Protocol) is everywhere now. Every week there's a new server for GitHub, for databases, for APIs you've never heard of. But when I first s..."
keywords: "server, mcp, you, template, json, msg, tools, servers"
generated: "2026-06-11T10:47:52.346856"
---

# I Built 10 MCP Servers in a Weekend — Here's the Template I Wish I Had Starting Out

## Overview

MCP (Model Context Protocol) is everywhere now. Every week there's a new server for GitHub, for databases, for APIs you've never heard of. But when I first started, I spent more time reading docs than writing code. The protocol isn't hard — it's just that every tutorial either shows you a toy example or dumps you straight into the full TypeScript SDK without explaining the basics. So I built a template. Then I built 10 servers off it in one weekend. Here's what I learned, and the template I now use for every MCP server. The Core Insight An MCP server is just a stdio or HTTP server that speaks JSON-RPC. That's it. # Minimal MCP server in 20 lines import sys , json def handle_request ( msg ): if msg . get ( " method " ) == " tools/list " : return { " tools " : [{ " name " : " hello " , " description " : " Say hello " , " inputSchema " : { " type " : " object " , " properties " : {}}}]} elif msg . get ( " method " ) == " tools/call " and msg . get ( " params " , {}). get ( " name " ) == " hello " : return { " content " : [{ " type " : " text " , " text " : " Hello from MCP! " }]} return { " error " : " unknown method " } for line in sys . stdin : msg = json . loads ( line . strip ()) result = handle_request ( msg ) sys . stdout . write ( json . dumps ( result ) + " \n " ) sys . stdout . flush () That's a working MCP server. 20 lines. The Template I Actually Use After 10 iterations, this is the structure that scales: mcp-server/ ├── server.py # JSON-RPC handler + tool registry ├── tools/ # One file per tool │ ├── __init__.py │ ├── search.py │ └── transform.py ├── config.py # Env vars, defaults └── requirements.txt Key principles: One file per tool group — keeps things testable Tool registry pattern — register tools with a decorator, no routing boilerplate Stdio first, HTTP later — start with stdio for local dev, add HTTP transport when you need remote access What I Actually Built Over the weekend I made: A GitHub issues fetcher A SQL query builder (safe, no injection) A markdown-to-HTML converter A web scraper tool A JSON transformer A code formatter wrapper A weather data server A text summarizer A URL shortener A Docker log parser Tools that an AI assistant can actually use during development. The Hardest Part Wasn't the Code It was packaging and distribution. Getting the server from "works on my machine" to "anyone can install and run it" takes more effort than writing the server itself. That's why I put everything I learned into a starter kit — the template, the 10 servers, the packaging scripts, and a setup guide so you can go from zero to deployed in 30 minutes. The Fastest Way to Start If you want to build MCP servers without the packaging headache: 1. MCP Server Starter Kit — The template, 10 example servers, deployment scripts, and a step-by-step guide. $0 minimum (pay what you want). 2. AI Developer Toolkit — If you're building AI workflows, this has the prompts and patterns I use daily. $9.99. 3. Claude Code Skills Pack — 50 production-tested prompts for Claude Code. $9.99. I write about MCP, AI tooling, and developer workflows. Follow me for more practical guides — no fluff, just things that actually work.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/z_z_c01afd7cf4c3764a2c73d/i-built-10-mcp-servers-in-a-weekend-heres-the-template-i-wish-i-had-starting-out-1l70

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
