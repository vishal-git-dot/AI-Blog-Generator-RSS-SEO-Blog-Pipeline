---
title: "I built a Casablanca Stock Exchange terminal as a highschool senior"
slug: "i-built-a-casablanca-stock-exchange-terminal-as-a-highschool-senior"
author: "Adam Elfaqir"
source: "devto_python"
published: "Sat, 14 Nov 2026 21:58:29 +0000"
description: "I'm a 2ème bac student in Fès, Morocco, and I want a career in finance. Following the Casablanca Stock Exchange meant jumping between slow, scattered sites, ..."
keywords: "exchange, terminal, data, free, live, charts, company, market"
generated: "2026-11-14T22:10:54.920991"
---

# I built a Casablanca Stock Exchange terminal as a highschool senior

## Overview

I'm a 2ème bac student in Fès, Morocco, and I want a career in finance. Following the Casablanca Stock Exchange meant jumping between slow, scattered sites, so I built the screen I wanted: SAHM Terminal, a free terminal with live charts, a sector heat map, company pages, market news and a DCF valuation tool, in French and English. Live: https://sahm-terminal.vercel.app The stack Backend: Python and FastAPI serving JSON under /api/v1, plus the static front end. Front end: vanilla JavaScript, no framework, a hash router and function keys (F1 to F10) like a real terminal. Charts: TradingView Lightweight Charts for historical data, plus embedded market-data widgets for live quotes and the heat map. Tests: 113 pytest tests. Hosting: Vercel's free plan. The hard part: price history Historical prices come as exchange exports, one file per instrument. Raw prices are misleading when a company splits its shares: the price suddenly falls by half and a chart shows a crash that never happened. The pipeline detects splits, adjusts earlier prices, and keeps the original files untouched so any adjustment can be checked. A refresh script merges new exports into the existing history. The valuation tool The DCF screen estimates what a company could be worth from the cash it may generate in the future. The result depends entirely on the assumptions you enter, so the app labels it as an educational estimate and never as a recommendation. What went wrong I got the licence question wrong at first: historical exchange data can have redistribution conditions. I wrote to the exchange and am still waiting for an answer, and I will change anything they ask. Free hosting that runs Python without a credit card is hard to find. Vercel's FastAPI support worked after I told it where my app lived. Getting people to try it is a different job from building it. Feedback If you follow the Moroccan market, or you build data products, tell me what's missing. Contact: sahmterminal1@gmail.com

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/adam_elfaqir_da9c8c379d9c/i-built-a-casablanca-stock-exchange-terminal-as-a-highschool-senior-391e

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
