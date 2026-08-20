---
title: "We're in Anthropic's Connectors Directory — here's what our MCP server actually exposes"
slug: "were-in-anthropics-connectors-directory-heres-what-our-mcp-server-actually-exposes"
author: "Michael Egberts"
source: "devto_webdev"
published: "Thu, 20 Aug 2026 12:51:49 +0000"
description: "WebsitePublisher.ai is now listed in Anthropic's Connectors Directory. Claude users on any plan can connect it in one click: claude.ai/directory/websitepubli..."
keywords: "directory, what, websitepublisher, claude, model, mcp, can, everything"
generated: "2026-08-20T12:58:10.476732"
---

# We're in Anthropic's Connectors Directory — here's what our MCP server actually exposes

## Overview

WebsitePublisher.ai is now listed in Anthropic's Connectors Directory. Claude users on any plan can connect it in one click: claude.ai/directory/websitepublisher-ai This post is about what sits behind that click, because "MCP server for websites" doesn't tell you much. The problem with code-generating website tools An LLM writing HTML is solved. What isn't solved is everything after: hosting, DNS, a form endpoint that survives a bot, structured content that isn't hardcoded in a <div> , and credentials that don't end up in a prompt. So the design goal was never "generate a page." It was: give the model a complete publishing surface, and keep everything dangerous out of its context. The tool surface 43 tools across layers: Layer Responsibility PAPI pages, fragments, assets, version history, rollback MAPI entities and records — schema + data SAPI forms, lead capture, visitor auth, analytics IAPI third-party integrations VAPI encrypted secret vault AAPI scheduled tasks TAPI task tracking An entity is a table. A record is a row. That's what turns a generated page into an actual application — a catalogue you can query, a booking table, a member list behind a magic-link login. Two design rules that made the review survivable 1. Scope everything by tenant, fail closed. Every endpoint that accepts an ID resolves the tenant first, then verifies ownership. Foreign tenant returns 404, not 403 — a 403 confirms the resource exists, which is an information leak. 2. Secrets never enter model context. Integration credentials live in the vault. The model can call execute_integration and reference a credential by name, but responses are sanitised before they're returned. The model orchestrates without ever seeing the key. Both were architectural decisions from the start, not hardening passes. Retrofitting either one is painful, so decide early. Connecting Any Claude plan: claude.ai/directory/websitepublisher-ai — connect, then ask it to build something and watch it publish. Full setup for ChatGPT, Cursor, Windsurf, Copilot, Gemini, Grok and Mistral: websitepublisher.ai/docs/mcp Questions about the architecture or the submission process — ask below.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/megberts/were-in-anthropics-connectors-directory-heres-what-our-mcp-server-actually-exposes-29f8

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
