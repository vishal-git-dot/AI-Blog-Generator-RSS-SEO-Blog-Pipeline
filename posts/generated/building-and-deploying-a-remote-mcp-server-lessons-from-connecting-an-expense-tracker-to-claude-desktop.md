---
title: "Building and Deploying a Remote MCP Server: Lessons from Connecting an Expense Tracker to Claude Desktop"
slug: "building-and-deploying-a-remote-mcp-server-lessons-from-connecting-an-expense-tracker-to-claude-desktop"
author: "Ali Raza"
source: "devto_python"
published: "Thu, 16 Jul 2026 07:21:50 +0000"
description: "The Problem Personal finance tracking usually means switching between an app, a spreadsheet, or a browser tab just to log a single transaction. I wanted a lo..."
keywords: "mcp, server, claude, desktop, remote, app, tools, database"
generated: "2026-07-16T08:22:50.505581"
---

# Building and Deploying a Remote MCP Server: Lessons from Connecting an Expense Tracker to Claude Desktop

## Overview

The Problem Personal finance tracking usually means switching between an app, a spreadsheet, or a browser tab just to log a single transaction. I wanted a lower-friction way to capture and query expenses — ideally through natural conversation with an AI assistant, without giving up structured storage or control over my own data. The Model Context Protocol (MCP) made this possible: it lets an AI client like Claude Desktop call tools exposed by a server I own and control, over a standard interface. The Solution I built and deployed a remote MCP server that exposes an expense tracker as a set of callable tools, then connected it directly to Claude Desktop as a live data source. Stack and architecture: FastMCP to define and expose tools (add_expense, get_summary, list_transactions, category management) over the MCP protocol aiosqlite for async-safe database access, migrated from a synchronous sqlite3 connection to avoid blocking calls in an async server A temporary, writable directory (via Python's tempfile) for database storage, since the deployment target does not guarantee a writable path at a fixed location Deployed remotely on Horizon, then registered as a connector in Claude Desktop's configuration The repository is public here: github.com/AliRaza3485/test-remote-mcp-server Problems Along the Way Two issues took real debugging time and aren't well covered in introductory MCP material: 1. Locating the client configuration on Windows. Claude Desktop on Windows is distributed as an MSIX package — Microsoft's sandboxed app packaging format, similar in spirit to how Android isolates APKs. MSIX apps don't write to the file paths a normal Windows install would use; the OS virtualizes the path so the app sees what looks like a standard location, while the actual file lives in an isolated, package-specific directory. This meant the config file wasn't where standard documentation implied — finding the correct sandboxed path required checking the MSIX virtualization behavior directly rather than trusting the "expected" path. 2. OAuth handling beyond the basics. Most MCP quick-start guides demonstrate local, tool-only servers with no external authentication. As soon as a server needs to authorize against an external service, the flow requires handling the redirect, exchanging the returned code for a token, storing it safely, and refreshing it when it expires — none of which the beginner-level guides walk through. Getting this right meant working from the OAuth spec directly rather than a tutorial. The Outcome The result is a working setup where a plain-language instruction in Claude Desktop — for example, logging an expense with an amount and category — is routed through MCP to the deployed server and persisted in the database, with no separate app or manual form involved. More importantly, building this end-to-end (real deployment, real client integration, real platform-specific failure modes) surfaced problems that toy examples don't: packaging quirks, async database access, and authentication lifecycle management. What's Next I'm currently extending this into more general agentic workflows using LangGraph — state graphs, checkpointing, and human-in-the-loop interrupts — with the goal of combining stateful agent logic with MCP-exposed tools. If you're building with MCP or LangGraph and want to compare notes, I'd welcome the conversation. GitHub: github.com/AliRaza3485 Repo: github.com/AliRaza3485/test-remote-mcp-server

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ali_raza_1ce2540f37e01a91/building-and-deploying-a-remote-mcp-server-lessons-from-connecting-an-expense-tracker-to-claude-2f4o

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
