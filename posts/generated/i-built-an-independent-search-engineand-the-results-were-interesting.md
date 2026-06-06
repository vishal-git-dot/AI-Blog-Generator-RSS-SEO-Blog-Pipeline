---
title: "I built an independent search engine—and the results were interesting"
slug: "i-built-an-independent-search-engineand-the-results-were-interesting"
author: "Splot Dev"
source: "devto_python"
published: "Sat, 06 Jun 2026 13:11:59 +0000"
description: "A few months ago, I came across FrogFind , a retro search engine, and I decided that I wanted to try my hand at making one, too. I first started with the cra..."
keywords: "search, engine, quokko, engines, crawler, wanted, simple, experience"
generated: "2026-06-06T13:56:22.889684"
---

# I built an independent search engine—and the results were interesting

## Overview

A few months ago, I came across FrogFind , a retro search engine, and I decided that I wanted to try my hand at making one, too. I first started with the crawler, carefully planning out a simple single threaded Python requests bot using SQLite3 that accommodated robots.txt. This was particularly difficult—I had barely any experience in the field of search engine creation, and its subcategories. After the crawler was the webapp, which was relatively easy, because of my experience with Flask. I used Redis for rate limit storage, and various algorithms to do the searching for me. I shoved my crawler and webapp into a pip package, quokko , with a CLI to control it. I wanted my project to be accessible, and for people to create their own search engines without trouble. Hosting it, as of Jun 6, 2026, there are around 13 million entries, which is very little for a search engine. The engine's quality may not be ideal, but it seems to provide me all these curious corners of the Internet, and also seems to be a tad more unfavourable to companies in the Big Tech category. It's now hosted here: quokko.splot.dev And you'll find the code and documentation here: https://codeberg.org/splot-dev/quokko This is a hobby project; errors are inevitable. Its simple customizability allows for people to make their own micro search engines, and the goal is for these micro search engines to form a net of niche, curious alternative human knowledge collections. The goal of Quokko is not to become a competitor search engine, but for it to be the open door for more other search engines.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/splotdev/i-built-an-independent-search-engine-and-the-results-were-interesting-1a9g

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
