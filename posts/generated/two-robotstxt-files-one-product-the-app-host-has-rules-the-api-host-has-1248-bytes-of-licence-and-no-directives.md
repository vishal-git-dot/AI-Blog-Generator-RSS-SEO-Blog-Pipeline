---
title: "Two robots.txt Files, One Product: The App Host Has Rules, the API Host Has 1,248 Bytes of Licence and No Directives"
slug: "two-robotstxt-files-one-product-the-app-host-has-rules-the-api-host-has-1248-bytes-of-licence-and-no-directives"
author: "OnePassApps"
source: "devto_webdev"
published: "Sun, 08 Nov 2026 05:23:54 +0000"
description: "I work on OnePassApps, so this is our own infrastructure and every number below was measured on it today with plain HTTPS - no browser, no session, no cookie..."
keywords: "one, host, api, file, app, sitemap, onepassapps, bytes"
generated: "2026-11-08T05:28:47.823351"
---

# Two robots.txt Files, One Product: The App Host Has Rules, the API Host Has 1,248 Bytes of Licence and No Directives

## Overview

I work on OnePassApps, so this is our own infrastructure and every number below was measured on it today with plain HTTPS - no browser, no session, no cookies and no JavaScript. One product, two hostnames, two robots.txt files. The one on the app host is 160 bytes of crawler rules. The one on the API host is 1,248 bytes of commentary that contains not one directive. That difference is the whole story, and neither file is wrong. The app host's file: eight lines, every one of them a directive https://app.onepassapps.com/robots.txt answers 200 with 160 bytes and 8 non-empty lines. All 8 are directives, none is a comment: User-agent: * Allow: / Disallow: /api Disallow: /api/ Disallow: /account Disallow: /sign-in Disallow: /sign-up Sitemap: https://app.onepassapps.com/sitemap.xml One User-agent group for everybody, one Allow: / , 5 Disallow paths and one Sitemap line. That last line is the useful one: it points at https://app.onepassapps.com/sitemap.xml , which answers 200 and carries 56 URLs. The API host's file: 20 lines, and every one of them is a comment https://api.onepassapps.com/robots.txt also answers 200, with 1,248 bytes. This one is the opposite shape. It has 20 non-empty lines and 0 of them are directives . There is no User-agent line, no Allow , no Disallow , no Sitemap and no Content-Signal: line either - nothing a crawler could act on. What the file does have is three named signals, defined in its own comment text: # search: building a search index and providing search results (e.g., returning # ai-input: inputting content into one or more AI models (e.g., retrieval # ai-train: training or fine-tuning AI models. And it closes with a legal footnote, in three comment lines: # ANY RESTRICTIONS EXPRESSED VIA CONTENT SIGNALS ARE EXPRESS RESERVATIONS OF # RIGHTS UNDER ARTICLE 4 OF THE EUROPEAN UNION DIRECTIVE 2019/790 ON COPYRIGHT # AND RELATED RIGHTS IN THE DIGITAL SINGLE MARKET. The notice does not name us either: the string onepassapps appears nowhere in those 1,248 bytes. It is a statement about the three uses, not about this site. So the API host tells a crawler what the three uses mean, in prose, and then tells it nothing at all about this site. The file names no path, so nothing on that host is disallowed by robots.txt - the file grants no permission and withholds none. Neither file advertises an API, and only one of them points at a sitemap The app host's file names its sitemap. The API host serves no sitemap at all: https://api.onepassapps.com/sitemap.xml answers 404 with 124 bytes - the same NOT_FOUND envelope that host returns for any path it does not have. There is no Sitemap: line to find on that host either, because the file has no directive lines at all. Which means the two hosts behave the same way from a crawler's point of view and differently from a reader's: the app host hands you a rulebook and a map, and the API host hands you a notice. The two files are even served under different caching rules app.onepassapps.com api.onepassapps.com Bytes 160 1,248 Non-empty lines 8 20 Directive lines 8 0 Cache-Control public, max-age=14400, must-revalidate private, no-store, max-age=0 ETag yes none The app host's file is cacheable for four hours and carries an ETag. The API host's file is private, no-store, max-age=0 and carries no ETag, so every fetch of it is a fresh request rather than a cached copy. Limits One build, one fetch per URL, 8 November 2026, plain HTTPS from one network, no browser and no JavaScript. Both files are a snapshot of one build. This post describes what the two files contain and what a crawler could read out of them; it makes no claim about how any particular crawler or AI agent behaves, and none about the legal meaning of the text it quotes - that is not my call. If you want to see the apps themselves rather than the files that describe them, the guides page lists all of them, and the home page is where the nine apps live.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/onepassapps/two-robotstxt-files-one-product-the-app-host-has-rules-the-api-host-has-1248-bytes-of-licence-4o08

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
