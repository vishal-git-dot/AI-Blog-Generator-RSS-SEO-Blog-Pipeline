---
title: "Give your AI agent a web scraper: PyScrappy now ships an MCP server"
slug: "give-your-ai-agent-a-web-scraper-pyscrappy-now-ships-an-mcp-server"
author: "Vedaant Singh"
source: "devto_python"
published: "Sat, 25 Jul 2026 18:58:03 +0000"
description: "Plenty of agents can already browse the web, so why bolt a scraper onto one? Two reasons: Structured data, not raw pages. Native web fetch hands the model a ..."
keywords: "mcp, pyscrappy, structured, server, can, web, you, agent"
generated: "2026-07-25T19:16:03.115246"
---

# Give your AI agent a web scraper: PyScrappy now ships an MCP server

## Overview

Plenty of agents can already browse the web, so why bolt a scraper onto one? Two reasons: Structured data, not raw pages. Native web fetch hands the model a rendered page and makes it re-extract the fields it wants. A scraper returns typed, structured JSON directly ( {title, rating, genre, ...} ), which is cheaper and more reliable for anything downstream. Not every setup can browse. A local model behind an MCP host has no internet at all unless you give it a tool. So I added an MCP server to PyScrappy , a Python web-scraping toolkit I maintain, to expose its scrapers as tools any Model Context Protocol client can call and get structured data back. This post shows how to wire it up. The idea PyScrappy returns clean, structured results from a wide range of sources: the open web, reference and research, finance, news, media, e-commerce, jobs, and local listings. Each scraper returns a ScrapeResult you can turn straight into JSON or a DataFrame. MCP is a natural fit: an agent asks for data, the server runs the right scraper, and hands back structured JSON. No glue code in between. Install pip install "pyscrappy[mcp]" That gives you a pyscrappy-mcp command, a stdio MCP server. Note: the MCP server needs Python 3.10+ (the MCP SDK requires it). PyScrappy's core library still supports 3.9, but the MCP server does not, so use 3.10 or newer here. Wire it into your agent MCP is an open standard , so this works with any MCP-compatible client, not just one vendor. That includes Claude (Desktop and Code), editors like Cursor , Windsurf , and VS Code , and open-source hosts such as LibreChat , Cline , and Goose that connect MCP servers to local or open models (Llama, Qwen, and friends). Any client that speaks MCP can use these tools; the examples below use Claude because it's a quick way to try it. Claude Code: claude mcp add pyscrappy pyscrappy-mcp Claude Desktop: add to claude_desktop_config.json and restart: { "mcpServers" : { "pyscrappy" : { "command" : "pyscrappy-mcp" } } } Cursor / Windsurf / VS Code (Cline): these use the same mcpServers block, just in their own MCP settings file (for example .cursor/mcp.json in Cursor): { "mcpServers" : { "pyscrappy" : { "command" : "pyscrappy-mcp" } } } Local / open models (Ollama, etc.): Ollama itself doesn't speak MCP, so you run a host that connects your local model to MCP servers. Tools like Goose , Cline , and LibreChat do this. In Goose, for instance, you add the same command as an extension: extensions : pyscrappy : type : stdio cmd : pyscrappy-mcp Point that host at an Ollama model that supports tool calling (Llama 3.1, Qwen 2.5, and similar), and it can now pull live web data. Whichever client you use, just ask in plain language: "Use pyscrappy to get the latest headlines from bbc.co.uk and the current AAPL quote." The agent picks scrape_news and scrape_stock , runs them, and reasons over the structured results. This is especially useful for local and open models , which usually have no web access at all: point one at this server through an MCP host and it can suddenly pull live, structured data. The only requirement is that the model supports tool calling ; how well it chooses the right tool depends on the model. What you can do with it The server gives the agent a set of tools spanning the topics and sectors PyScrappy covers: The open web: scrape any URL into structured text, links, images, and tables. Reference and research: encyclopedic articles and knowledge lookups. Finance and markets: stock quotes, price history, and company profiles. News and media: RSS feeds, news sites, movies and TV, and music. E-commerce: product search across general and category-specific retailers. Jobs and professional data: public job listings and hiring info. Local and lifestyle: restaurants and places by city. A quick example of the range, in one prompt : "Use pyscrappy to get today's tech headlines, the current NVDA quote, and a few laptops under $800." Everything comes back as structured JSON , so the agent can filter, compare, and reason over it rather than eyeballing raw HTML. More tools and sources are on the way, so expect this to grow. Two tools need a little setup: SoundCloud uses a browser backend (installed with pip install "pyscrappy[browser]" ), and the movie tool needs a free OMDb API key passed through the client config: { "mcpServers" : { "pyscrappy" : { "command" : "pyscrappy-mcp" , "env" : { "OMDB_API_KEY" : "your-key" } } } } How it works under the hood The server is built on the official MCP Python SDK ( FastMCP ). Each tool is a thin async wrapper around a scraper. PyScrappy's scrapers are synchronous, so each call runs in a worker thread via anyio.to_thread.run_sync to avoid blocking the event loop. Tools return a typed ScrapeToolResult , so the SDK gives clients a declared output schema and validated structured data rather than an opaque string. Responses are cached briefly (a few minutes), so when an agent asks for the same thing twice, the second call is instant and doesn't hit the site again. Try it Repo: https://github.com/mldsveda/PyScrappy pip install "pyscrappy[mcp]" Issues and PRs welcome. If you build something with it, I'd like to hear about it.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/vedaant00/give-your-ai-agent-a-web-scraper-pyscrappy-now-ships-an-mcp-server-3e8g

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
