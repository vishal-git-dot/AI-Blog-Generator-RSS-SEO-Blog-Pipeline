---
title: "I Built an MCP Server So AI Assistants Can Process PDFs Directly"
slug: "i-built-an-mcp-server-so-ai-assistants-can-process-pdfs-directly"
author: "Peter Ndumia"
source: "devto_ai"
published: "Mon, 03 Aug 2026 19:35:24 +0000"
description: "I run PDFHaul, a free browser and mobile PDF toolkit, as a solo founder. A few months ago I kept running into the same friction point: every time I wanted an..."
keywords: "server, pdf, mcp, than, pdfhaul, assistant, tool, run"
generated: "2026-08-03T19:44:41.768699"
---

# I Built an MCP Server So AI Assistants Can Process PDFs Directly

## Overview

I run PDFHaul, a free browser and mobile PDF toolkit, as a solo founder. A few months ago I kept running into the same friction point: every time I wanted an AI assistant to help with a PDF task, I had to manually download the file, upload it somewhere, run the tool, then feed the result back into the conversation. For anything involving more than one file, that loop got old fast. So I built an MCP server for PDFHaul. This post covers what it does, how it's built, and a few of the harder decisions along the way. What MCP Actually Solves Here Model Context Protocol gives an AI assistant a standard way to call external tools directly, instead of a person acting as the manual bridge between the assistant and every service it needs. For PDF work specifically, that means an assistant like Claude or Cursor can merge, split, compress, or convert a file as part of a conversation, without a human stepping out to run the tool separately. The PDFHaul MCP server exposes 12 tools across four categories: file management, editing, conversion, and compression. It's live at pdfhaul.com/mcp-server , where you can find setup instructions and generate an API key. Architecture The server runs on the same Node.js/TypeScript and GCP Cloud Run infrastructure as the rest of PDFHaul, which kept the initial build simpler than starting a separate service from scratch. The tools themselves wrap the existing PDF processing logic, so I wasn't rebuilding PDF handling, just exposing it through a new interface. A few decisions that took more thought than I expected: Auth. API keys are hashed with bcrypt before storage, and requests are authenticated with a combination of the API key and a JWT. I didn't want to store anything resembling a plaintext credential, even for a free product, since API keys tend to get pasted into config files and committed by accident more often than anyone would like to admit. Rate limiting. In-memory rate limiting per key, tuned conservatively at first. Cloud Run's stateless nature means in-memory limits reset on cold starts, which is a real tradeoff worth knowing about if you're building something similar. I accepted it for now rather than standing up Redis for a v1. SSRF prevention. Several of the tools accept a URL as input (for example, fetching a PDF to process rather than uploading bytes directly). Any tool that accepts a URL from the caller is a potential server-side request forgery vector, so requests are validated against a blocklist of internal IP ranges and non-HTTP(S) schemes before the server ever fetches anything. Idempotency keys. AI assistants sometimes retry tool calls, whether from a timeout, a dropped connection, or the assistant itself deciding to try again. Without idempotency handling, a retried "merge these files" call could produce duplicate output or double-charge a rate limit. Each mutating tool call accepts an idempotency key so a retry returns the original result instead of redoing the work. Audit logging. Every tool call is logged with enough detail to reconstruct what happened, without logging the file contents themselves. This matters more for a PDF tool than it might for other APIs, since the whole product's trust model is built around not retaining user files longer than necessary. Getting Listed The server is listed on the official MCP registry , which so far has been the main discovery channel. Compared to building a plugin or waiting on marketplace approval in other ecosystems, the registry listing process was refreshingly lightweight. Where This Leaves Things Foxit and Nitro are the other PDF vendors I've seen building MCP servers, both larger companies with existing enterprise PDF products. Being early here as a solo founder is less about outcompeting them head-on and more about being genuinely useful to the AI-assistant-tooling crowd before the space gets crowded. If you're working with PDFs inside an AI assistant workflow and want to try it, the server is free to use: pdfhaul.com/mcp-server . I'm happy to answer questions about the implementation in the comments, especially on the auth or SSRF handling if anyone's building something similar. Peter, founder of PDFHaul

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/peter_ndumia_pdfhaul/i-built-an-mcp-server-so-ai-assistants-can-process-pdfs-directly-80k

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
