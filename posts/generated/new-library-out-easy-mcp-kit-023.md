---
title: "New Library Out easy-mcp-kit 0.2.3"
slug: "new-library-out-easy-mcp-kit-023"
author: "Batman"
source: "devto_python"
published: "Fri, 18 Sep 2026 20:26:26 +0000"
description: "easy-mcp-kit 0.2.3 is out, and it now ships two ready-made MCP servers you can run with a single command: one for GitHub, one for Postgres. The video is one ..."
keywords: "mcp, easy, kit, github, one, you, postgres, your"
generated: "2026-09-18T20:42:06.199549"
---

# New Library Out easy-mcp-kit 0.2.3

## Overview

easy-mcp-kit 0.2.3 is out, and it now ships two ready-made MCP servers you can run with a single command: one for GitHub, one for Postgres. The video is one real terminal session, no cuts: pip install "easy-mcp-kit[postgres]" point it at your data with DATABASE_URL (a GitHub token is optional for public repos) register both with your MCP client, one line each ask in plain language: which product earned the most revenue, who spent the most, what were the last two merged PRs The assistant discovers the schema, writes the SQL, calls the GitHub API, and answers with real numbers. Every Postgres statement runs in a READ ONLY transaction with a timeout and a row cap, so it can explore but never modify. GitHub is read-only unless you opt in, and the write tools are hidden from any client without the right scope. Both connectors are built with the same @server .tool decorator the library gives you for your own functions, so validation, rate limits, timeouts, sanitized errors, and the audit log apply unchanged. pip install easy-mcp-kit https://pypi.org/project/easy-mcp-kit/ https://github.com/Mark007-R/Easy-MCP Demo at - https://drive.google.com/file/d/1q-PjqnYU3hNDJSxk66uAsg_MJagTIVVE/view

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/iambatttmannnn07/new-library-out-easy-mcp-kit-023-2a2

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
