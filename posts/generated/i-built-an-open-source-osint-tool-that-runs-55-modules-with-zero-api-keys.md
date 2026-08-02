---
title: "I built an open-source OSINT tool that runs 55 modules with zero API keys"
slug: "i-built-an-open-source-osint-tool-that-runs-55-modules-with-zero-api-keys"
author: "FlowThingy"
source: "devto_python"
published: "Sun, 02 Aug 2026 12:59:46 +0000"
description: "Been learning web security for a while and kept jumping between different tools for every recon task so I just built my own. It's a Python script with a term..."
keywords: "out, built, runs, api, keys, security, while, secret"
generated: "2026-08-02T13:39:46.250129"
---

# I built an open-source OSINT tool that runs 55 modules with zero API keys

## Overview

Been learning web security for a while and kept jumping between different tools for every recon task so I just built my own. It's a Python script with a terminal menu. Give it a URL and it runs subdomains, directory bruteforce, JS secret scanning, DNS, headers, SSL, CORS, Shodan, VirusTotal, email security, username search across 30 platforms, GitHub commit email mining. Spits out a report at the end automatically. No API keys needed for any of it. The JS secret detection took a while to get right. Pure regex gives too much noise so I added Shannon entropy scoring on top to filter out placeholders and test values automatically. Everything gets stored in DuckDB so you can query findings with SQL which is way cleaner than digging through JSON. If you want to check it out: github.com/FlowThingy/FlowOsint

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/flowthingy/i-built-an-open-source-osint-tool-that-runs-55-modules-with-zero-api-keys-1614

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
