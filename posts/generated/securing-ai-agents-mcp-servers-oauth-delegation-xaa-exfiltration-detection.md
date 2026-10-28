---
title: "Securing AI Agents & MCP Servers: OAuth Delegation (XAA) & Exfiltration Detection"
slug: "securing-ai-agents-mcp-servers-oauth-delegation-xaa-exfiltration-detection"
author: "erz"
source: "devto_ai"
published: "Wed, 28 Oct 2026 22:16:20 +0000"
description: "Most MCP (Model Context Protocol) servers deployed today rely on static Service Accounts [00:04:14]. This creates two major flaws: over-privileged agents and..."
keywords: "mcp, tool, xaa, agents, delegation, exfiltration, service, lab"
generated: "2026-10-28T22:24:29.417140"
---

# Securing AI Agents & MCP Servers: OAuth Delegation (XAA) & Exfiltration Detection

## Overview

Most MCP (Model Context Protocol) servers deployed today rely on static Service Accounts [00:04:14]. This creates two major flaws: over-privileged agents and zero human accountability in the logs (every action just shows up as svc-ai-agent ). Following recent incidents (Asana MCP, Cline, Salesforce) [00:05:15], we built a lab (Azure APIM, MCP Server, Okta, CrowdStrike) to test two things: 1. Replacing Service Accounts with Delegated Tokens (XAA) To enforce least privilege down to the MCP server and keep human attribution in the SIEM, we implemented a 3-step token exchange using Cross-App Access (XAA) [00:12:05]: 2. Why IAM isn't enough (Tool-based Exfiltration) ​Even with strict token delegation, an agent can still abuse a legitimate tool (like http_request) to base64-encode and exfiltrate secrets the user is allowed to read [00:19:18]. Catching this requires correlating API Gateway prompt inspection (Azure APIM) with SIEM identity & network logs [00:20:34], alongside strict tool sandboxing/whitelisting [00:24:17]. ​ Lab Walkthrough (Video) ​(Note: Audio is in French — YouTube English auto-captions work well, and the console/terminal demos are visual). ​ ​Direct timestamps to skip the intro: ​[00:08:54] — Lab architecture & Service Account vulnerability demo ​[00:12:05] — Implementing XAA 3-step token delegation ​[00:15:27] — Auth Server scopes & group policies configuration ​[00:18:58] — Bypassing IAM: Data exfiltration via http_request tool ​[00:20:34] — Catching the leak: Azure APIM prompt inspection & SIEM correlation ​[00:23:57] — Limitations: Tool sandboxing & fully autonomous agents

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/erz/securing-ai-agents-mcp-servers-oauth-delegation-xaa-exfiltration-detection-3mi2

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
