---
title: "I was burning context feeding HTML to LLMs, so I built a Markdown converter for agents"
slug: "i-was-burning-context-feeding-html-to-llms-so-i-built-a-markdown-converter-for-agents"
author: "Konstantin Konstantinov"
source: "devto_python"
published: "Thu, 25 Jun 2026 19:13:15 +0000"
description: "If you build AI agents, scrapers, or RAG pipelines, you have run into this: feeding raw HTML to a model is mostly waste. The <div> , the class="..." , the na..."
keywords: "markdown, html, agents, you, not, cloudflare, your, browser"
generated: "2026-06-25T20:09:21.019741"
---

# I was burning context feeding HTML to LLMs, so I built a Markdown converter for agents

## Overview

If you build AI agents, scrapers, or RAG pipelines, you have run into this: feeding raw HTML to a model is mostly waste. The <div> , the class="..." , the nav, the cookie banner. None of it is the content you wanted, and all of it costs tokens. I knew this was inefficient. I did not appreciate how inefficient until I measured it. Here is a single page of GitHub's documentation, run through an audit: HTML Markdown Savings ─────────────────────────────────────────────────── Tokens 138,550 9,364 -93.2% Chars 554,200 37,456 -93.2% Words 27,123 4,044 Size 541.3 KB 36.6 KB -93.2% Ninety-three per cent of the tokens, gone, with no loss of meaning. The intuition is simple: <h2>About Us</h2> carries the same information as ## About Us and costs several times more to read. Multiply that across a real page and the boilerplate is most of your payload. Across a scraping or RAG workload, that is the difference between a cost model that works and one that does not. What was already out there Before writing anything, I looked at the options. Heavy scrapers. Spinning up Puppeteer or Cheerio to strip HTML works, but it drags a headless browser and a pile of dependencies into a project that may not want either. Cloudflare's Markdown for Agents. Cloudflare ships exactly this conversion at the edge, and it is genuinely good. It is also free on their paid plans, so if your site already sits behind Cloudflare, you may not need anything else. The catch is in the requirement itself: it only helps if your traffic runs through Cloudflare. I wanted something that lived in my own code, ran anywhere, and did not assume a particular network sat in front of it. The library credits Cloudflare's work as the inspiration, because that is where the idea came from. What I actually wanted was a small, framework-agnostic way to serve Markdown whenever an agent asked for it, with nothing else attached. markdown-for-agents The mechanism is content negotiation, the boring HTTP feature that turns out to be exactly right for this. A normal browser visits your site and gets HTML. An agent visits with Accept: text/markdown , and the middleware intercepts the request, strips the boilerplate, and returns clean Markdown from the same URL. No second endpoint, no separate build, no fork in your routing. import { convert } from ' markdown-for-agents ' ; const { markdown , tokenEstimate } = convert ( html , { extract : true }); The design goals, in order: One dependency. The core relies on a single HTML parser and nothing else. No headless browser, no DOM. Runs anywhere. Node, Bun, Deno, Cloudflare Workers, Vercel Edge, the browser. If it speaks Web Standards, it works. The same idea in Python. There is a zero-dependency Python package alongside the TypeScript one, with middleware for FastAPI, Flask, and Django. Half the RAG and scraping world lives in Python, and I did not want to leave it out. Drop-in middleware. Express, Fastify, Hono, Next.js, and any Web Standard server. The middleware reads the Accept header, passes normal browser traffic through untouched, and converts only when an agent asks. Try it without installing anything Point the audit tool at any URL and see what you would save: npx @markdown-for-agents/audit https://docs.github.com/en/copilot/get-started/quickstart Or paste a URL or raw HTML into the playground and watch the conversion happen live: https://markdown-for-agents.vercel.app/playground Why I open-sourced it I built it because I wanted my own websites to be prepared and agent-friendly, and I was seeing my own usage limits get burned by HTML-only websites. If you are dealing with context limits or token costs from web content, it might save you the same. The code is here: https://github.com/KKonstantinov/markdown-for-agents``

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/kkonstantinov/i-was-burning-context-feeding-html-to-llms-so-i-built-a-markdown-converter-for-agents-2c2m

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
