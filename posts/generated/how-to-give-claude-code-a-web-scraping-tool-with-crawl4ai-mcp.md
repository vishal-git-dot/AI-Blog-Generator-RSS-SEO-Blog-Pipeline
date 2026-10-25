---
title: "How to give Claude Code a web scraping tool with Crawl4AI (MCP)"
slug: "how-to-give-claude-code-a-web-scraping-tool-with-crawl4ai-mcp"
author: "Deduped"
source: "devto_python"
published: "Sun, 25 Oct 2026 03:33:22 +0000"
description: "Coding agents are great at research until they need to read a real web page. Crawl4AI is an open-source crawler and scraper that turns websites into clean, L..."
keywords: "mcp, com, your, page, markdown, hosted, claude, use"
generated: "2026-10-25T04:06:12.672702"
---

# How to give Claude Code a web scraping tool with Crawl4AI (MCP)

## Overview

Coding agents are great at research until they need to read a real web page. Crawl4AI is an open-source crawler and scraper that turns websites into clean, LLM-ready Markdown, and it ships an MCP server so Claude Code can scrape, extract and search on its own. This guide covers both ways to use it: the hosted MCP server (one command in Claude Code) and the free open-source library you run yourself. Option 1: hosted MCP in Claude Code Get a key Sign up at crawl4ai.com and verify your email. Per the README, the free tier is 1,000 credits every month, 10 requests a minute and 2 at a time, with no card. Paid plans start at $10 a month (120 a minute, 10 at a time). Hosted requests are billed against your key, so keep CRAWL4AI_KEY out of shared scripts. export CRAWL4AI_KEY = "your-key-here" Add the MCP server claude mcp add --transport http crawl4ai https://api.crawl4ai.com/mcp \ --header "Authorization: Bearer $CRAWL4AI_KEY " The README links setup for Codex, Cursor and OpenCode too. Use it Start Claude Code and ask for a page in plain language: Use crawl4ai to scrape https://docs.crawl4ai.com and summarize the installation options as a table. The same key gives you /scrape (page to Markdown), /extract (page to JSON, no LLM key of your own needed), /search (web search), /serp (Google's results page as data, in beta) and /answer (a direct answer with sources, experimental). JS-heavy pages and bot walls are handled for you on the hosted side. Quick test without an agent curl -s https://api.crawl4ai.com/scrape \ -H "Authorization: Bearer $CRAWL4AI_KEY " \ -H "Content-Type: application/json" \ -d '{"url": "https://news.ycombinator.com"}' | jq -r .markdown Option 2: run it yourself for free The hosted API is optional. The open-source crawler runs free on your machine. pip install -U crawl4ai crawl4ai-setup # installs and sets up the browser crawl4ai-doctor # checks the installation If the browser setup fails, install Chromium by hand with python -m playwright install --with-deps chromium . import asyncio from crawl4ai import AsyncWebCrawler async def main (): async with AsyncWebCrawler () as crawler : result = await crawler . arun ( url = " https://news.ycombinator.com " ) print ( result . markdown ) asyncio . run ( main ()) Save result.markdown per page and you have clean input for a RAG index. For tighter output, the "fit Markdown" filters ( PruningContentFilterLXML , BM25ContentFilter , LLMContentFilter ) strip menus, footers and boilerplate. Or from the command line crwl https://news.ycombinator.com -o markdown crwl https://docs.crawl4ai.com --deep-crawl bfs --max-pages 10 Self-hosted MCP with Docker If you want MCP without the hosted API, run your own server. It needs a token; without one it only answers inside its container. export CRAWL4AI_API_TOKEN = " $( openssl rand -hex 32 ) " docker run -d -p 11235:11235 --name crawl4ai --shm-size = 1g \ -e CRAWL4AI_API_TOKEN = " $CRAWL4AI_API_TOKEN " \ unclecode/crawl4ai:latest Allow about 10 seconds for it to start, then test: curl -s http://localhost:11235/md \ -H "Authorization: Bearer $CRAWL4AI_API_TOKEN " \ -H "Content-Type: application/json" \ -d '{"url": "https://news.ycombinator.com"}' | jq -r .markdown The server exposes /md , /html , /crawl , /screenshot , /pdf and /execute_js , plus a dashboard at http://localhost:11235/dashboard and a playground at /playground . The README says the self-hosted server also supports MCP for Claude Code and other agents; the exact connection steps are in the self-hosting guide . Which one should you pick? Library : free, runs in your Python process, your proxies and settings. Your own Docker server : free apart from hosting, shared by several tools. Hosted : no browsers to run, bot walls handled, and the only option with /search , /serp and /answer . Whichever you choose, respect each site's terms and robots rules when crawling. Use cases with copy-paste prompts Each page has who it is for, the steps, and a prompt you can paste into your coding agent. Use case: Give Claude Code a web scraping tool over MCP Use case: Turn any web page into clean Markdown for RAG Use case: Scrape a page with one curl call Get one email every Monday with the week's hottest AI repos and exactly how to use them: subscribe free at dedupedai.com

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dedupedai/how-to-give-claude-code-a-web-scraping-tool-with-crawl4ai-mcp-ege

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
