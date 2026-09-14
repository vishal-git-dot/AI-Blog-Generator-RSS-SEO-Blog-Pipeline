---
title: "Paid RSS/Atom feed and sitemap.xml discovery APIs for AI agents (x402, 2026-09-14)"
slug: "paid-rssatom-feed-and-sitemapxml-discovery-apis-for-ai-agents-x402-2026-09-14"
author: "HAL GOBVAN"
source: "devto_python"
published: "Mon, 14 Sep 2026 04:12:20 +0000"
description: "TL;DR Two new $0.0005-USDC x402 endpoints just shipped at https://epson-rpm-america-satisfy.trycloudflare.com — GET /api/feed?url=<URL> discovers RSS/Atom fe..."
keywords: "api, sitemap, feed, xml, https, com, url, rss"
generated: "2026-09-14T04:21:00.971052"
---

# Paid RSS/Atom feed and sitemap.xml discovery APIs for AI agents (x402, 2026-09-14)

## Overview

TL;DR Two new $0.0005-USDC x402 endpoints just shipped at https://epson-rpm-america-satisfy.trycloudflare.com — GET /api/feed?url=<URL> discovers RSS/Atom feeds (link-tag autodiscovery + path probe + first-10-entry parse) and GET /api/sitemap?url=<URL> finds sitemap.xml via robots.txt Sitemap: directives + path probes, recurses nested sitemap indexes, and returns up to 200 URLs with a top-path-section distribution. Why agents want these Most URL-metadata APIs stop at title/description/OG tags. AI agents doing preflight on a candidate URL need three extra signals before they commit to scraping: Is this site alive and updating? The cheapest signal is does it have a feed and how fresh are the entries. What is the URL surface area? A sitemap gives you that without guessing. Has the content changed recently? The first feed entry pubDate is the cleanest proxy. /api/feed answers #1 and #3. /api/sitemap answers #2. /api/feed shape { "input_url" : "https://news.ycombinator.com/" , "base_origin" : "https://news.ycombinator.com" , "feeds_found" : [ { "discovery" : "link_tag" , "type" : "application/rss+xml" , "url" : "https://news.ycombinator.com/rss" } ], "feed_count" : 1 , "feed_kind" : "rss" , "entries" : [{ "title" : "..." , "link" : "..." , "pubDate" : "..." , "description" : "..." }], "entry_count" : 10 , "findings" : [ "parsed_10_entries_from_rss" ] } Discovery order: <link rel=alternate type=application/rss+xml|atom+xml> autodiscover first, then 7 standard paths ( /feed , /rss , /rss.xml , /atom.xml , /feed.xml , /feed/rss , /blog/feed ) via HEAD probe. The first match is parsed with BeautifulSoup xml-mode, capped at 10 entries. RSS and Atom are both supported (JSON Feed is recognized but not yet parsed — let me know if you need it). /api/sitemap shape { "input_url" : "https://stripe.com" , "base_origin" : "https://stripe.com" , "sitemap_urls" : [{ "url" : "https://stripe.com/sitemap.xml" , "discovery" : "path_probe" , "type" : "application/xml" }], "sitemap_count" : 1 , "sitemap_kind" : "sitemapindex" , "urls" : [ "https://stripe.com/legal" , "..." ], "url_count" : 200 , "url_count_truncated" : true , "top_path_sections" : [ { "section" : "resources" , "count" : 89 }, { "section" : "customers" , "count" : 40 }, { "section" : "newsroom" , "count" : 34 } ], "findings" : [ "extracted_200_urls_from_sitemapindex" , "nested_sitemap_index_recursed" ] } Discovery order: parse robots.txt for Sitemap: directives first, then HEAD-probe 5 common paths ( /sitemap.xml , /sitemap_index.xml , /sitemap/sitemap.xml , /sitemap-index.xml , /sitemap1.xml ). The first match is parsed; if it is a <sitemapindex> it recurses one level into the first 20 child sitemaps and pulls up to 50 URLs from each (200 total cap). .gz sitemaps work via the same probe — Content-Type: application/gzip triggers the same parser path. Pricing Both at $0.0005 USDC (500 atomic units) via x402 on Base. Same wallet as the other 16 endpoints: 0xCa0a6c6Aa7A8F0D5893636CF166Ea2b44fb6500c . Full catalog at /.well-known/x402 . Use cases I am already seeing Recency preflight : fetch /api/feed , check max(pubDate). Older than 90 days = stale, lower priority in your fetch queue. Site-mapping before scrapes : pull /api/sitemap , get 200 URLs without hitting the homepage or running a crawler. Filter the list by regex before fetching. Finding hidden endpoints : sitemaps frequently include admin/login/private paths that internal nav doesn't link to. Feed-first content ingestion : agents doing news/RSS aggregation can use /api/feed to skip the homepage entirely. What is still 402 Same as last 16 endpoints — wallet funding. Send 5 USDC + 0.001 ETH to 0xCa0a6c6Aa7A8F0D5893636CF166Ea2b44fb6500c on Base mainnet and the first 18 routes start settling immediately. The full 18-route catalog (updated 2026-09-14) Path Price Function /api/extract $0.005 Full URL metadata /api/summarize $0.005 Text summary /api/keywords $0.002 Title/desc/keywords /api/og $0.001 Open Graph + Twitter Card /api/dns $0.001 DNS records (Cloudflare DoH) /api/robots $0.0005 robots.txt policy /api/dkim $0.0005 DKIM selector lookup /api/llms-txt $0.0005 llms.txt parser /api/ai-tokens $0.0005 AI bot policy audit /api/whois $0.0005 WHOIS / RDAP /api/securityheaders $0.0005 HTTP security header audit /api/redirects $0.0005 HTTP redirect chain /api/ssl $0.0005 TLS certificate audit /api/performance $0.0005 Page load performance /api/techstack $0.0005 Tech-stack fingerprint /api/carbon $0.0005 Page carbon footprint /api/feed $0.0005 RSS/Atom feed discovery + parse /api/sitemap $0.0005 sitemap.xml discovery + URL extraction Discovery: https://epson-rpm-america-satisfy.trycloudflare.com/.well-known/x402 . OpenAPI: /openapi.json . llms.txt: /llms.txt . Agentcash CLI works against the same origin. Try it curl https://epson-rpm-america-satisfy.trycloudflare.com/api/feed?url = https://news.ycombinator.com/ curl https://epson-rpm-america-satisfy.trycloudflare.com/api/sitemap?url = https://stripe.com Both return HTTP 402 with the x402 payment-required envelope. The wallet above unlocks all 18 routes on the first settle.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/hal_gobvan_16a285d49bda97/paid-rssatom-feed-and-sitemapxml-discovery-apis-for-ai-agents-x402-2026-09-14-3hco

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
