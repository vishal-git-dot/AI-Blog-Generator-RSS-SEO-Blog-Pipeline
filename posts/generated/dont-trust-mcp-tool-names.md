---
title: "DON’T trust MCP tool names"
slug: "dont-trust-mcp-tool-names"
author: "Anatolii Maltsev"
source: "devto_ai"
published: "Fri, 16 Oct 2026 16:20:26 +0000"
description: "Two servers expose delete_user . Your trust list approves one. The runtime resolves by name and may execute the other. Nothing errors and the transcript lies..."
keywords: "name, trust, mcp, tool, list, nothing, field, money"
generated: "2026-10-16T16:24:14.490250"
---

# DON’T trust MCP tool names

## Overview

Two servers expose delete_user . Your trust list approves one. The runtime resolves by name and may execute the other. Nothing errors and the transcript lies. Quieter failure: MCP ships a version where transfer grows an optional destination_account field. Yesterday it moved money, today it moves money to a chosen account. Name unchanged, signature still valid, trust list still stale. def tool_identity ( server_id , name , schema ): canonical = json . dumps ( schema , sort_keys = True , separators = ( " , " , " : " )) return f " { server_id } :: { name } @ { sha256 ( canonical )[ : 16 ] } " Unreviewed drift suspends the tool. A flag that stops nothing is a log line. Full writeup with the field-classification problem: here

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/maltsev-dev/dont-trust-mcp-tool-names-1dh3

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
