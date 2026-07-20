---
title: "I gave my AI agent the ability to send email"
slug: "i-gave-my-ai-agent-the-ability-to-send-email"
author: "DevOps Daily"
source: "devto_ai"
published: "Mon, 20 Jul 2026 19:43:43 +0000"
description: "Last month I wired Claude up to my email infrastructure. Not "Claude writes an email draft and I paste it somewhere" but the agent checks my domain status, s..."
keywords: "mcp, api, server, agent, tool, email, claude, call"
generated: "2026-07-20T19:49:00.048654"
---

# I gave my AI agent the ability to send email

## Overview

Last month I wired Claude up to my email infrastructure. Not "Claude writes an email draft and I paste it somewhere" but the agent checks my domain status, sends the email, and reads back the delivery events, all from the chat. The glue that makes this possible is MCP (Model Context Protocol), and the whole setup takes about five minutes. Here is exactly how to do it, plus what surprised me once agents could actually touch production infrastructure. What MCP actually is MCP is a small JSON-RPC protocol that lets an AI client (Claude, Cursor, Windsurf, your own agent) call tools exposed by a server. The server describes its tools with JSON schemas, the model picks a tool and fills in the arguments, and the client executes the call. The important design decision is where the server runs. A lot of MCP servers are local stdio processes you install per machine. For anything talking to a hosted API, a hosted MCP server is the better shape: nothing to install, your API key is the auth, and every client that speaks HTTP can use it. I use SMTPfast for transactional email, which ships a hosted MCP endpoint at https://smtpfa.st/api/mcp . That is what I will use in the examples, but the pattern applies to any hosted MCP server. Step 1: Connect Claude Code One command: claude mcp add --transport http smtpfast https://smtpfa.st/api/mcp \ --header "Authorization: Bearer sf_your_api_key" For Cursor, it is a snippet in .cursor/mcp.json : { "mcpServers" : { "smtpfast" : { "url" : "https://smtpfa.st/api/mcp" , "headers" : { "Authorization" : "Bearer sf_your_api_key" } } } } That is the entire installation. No npm package, no local process, no version drift between machines. Step 2: See what the agent can do MCP servers self-describe. You can poke one with curl to see the tool list: curl -sS https://smtpfa.st/api/mcp \ -H "Content-Type: application/json" \ -H "Authorization: Bearer sf_your_api_key" \ -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}' The SMTPfast server exposes eight tools: send_email , list_emails , get_email , list_domains , verify_domain , list_suppressions , get_analytics , and list_contacts . The model reads those schemas and figures out the rest on its own. Step 3: Just ask With the server connected, I can type things like this into Claude: "Check if my domain is verified, then send a test email from hello@mydomain.com to my personal address and tell me when it is delivered." Behind the scenes the agent calls list_domains , sees the DKIM status, calls send_email , waits, then calls get_email to read the delivery events. I watch each tool call go by and approve it. No SDK, no glue code, no copy-pasting message IDs. The debugging workflow is where this gets genuinely useful: "Why did the email to jane@example.com bounce yesterday?" The agent pulls the email, reads the bounce event with the SMTP diagnostic code, checks whether the address landed on the suppression list, and explains it in plain language. That used to be five minutes of clicking through a dashboard. What surprised me 1. The approval step matters more than I expected. Most MCP clients show you each tool call before it runs. For read tools that feels like friction. For send_email it is exactly right. I would not connect a send-capable tool to an agent that runs unattended without scoping the key first. 2. Agents are great at chaining, bad at restraint. Ask a vague question and the agent will happily call four tools when one would do. Tight tool descriptions in the server matter as much as good prompts. 3. The server is the easy part. If your product already has a REST API, an MCP server is mostly a translation layer: tool schema in, API call out. The hard work (auth, rate limits, validation) already exists in the API. That is also why I prefer hosted MCP over stdio: it reuses everything the API already enforces, including that a compromised key can be revoked in one place. Try it If you want to reproduce this end to end: grab a free SMTPfast account (3,000 emails/month, no card), verify a domain, create an API key, and run the claude mcp add command above. The MCP docs cover the tool schemas and a few example prompts. And if you are building a dev tool yourself: ship the hosted MCP endpoint. It is a weekend of work and it makes your product usable by every AI agent your customers already run.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/devopsdaily/i-gave-my-ai-agent-the-ability-to-send-email-18nc

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
