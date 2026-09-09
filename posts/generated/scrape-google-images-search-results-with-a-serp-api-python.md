---
title: "Scrape Google Images Search Results with a SERP API (Python)"
slug: "scrape-google-images-search-results-with-a-serp-api-python"
author: "dodou"
source: "devto_python"
published: "Wed, 09 Sep 2026 04:00:40 +0000"
description: "Back when I needed product images for a comparison site, my first instinct was to parse Google Images' DOM. Two days later I had a pile of brittle selectors ..."
keywords: "images, google, image, json, page, img, you, api"
generated: "2026-09-09T04:06:24.344829"
---

# Scrape Google Images Search Results with a SERP API (Python)

## Overview

Back when I needed product images for a comparison site, my first instinct was to parse Google Images' DOM. Two days later I had a pile of brittle selectors and a CAPTCHA habit. The fix was boring: an API that returns the image grid as JSON. Here's the shortest Python version I use. The request SerpBase's images endpoint is a POST with a JSON body — same shape as their web search, but it costs 2 credits instead of 1 because image parsing is heavier on their side. import os import requests API_KEY = os . environ [ " SERPBASE_API_KEY " ] resp = requests . post ( " https://api.serpbase.dev/google/images " , headers = { " X-API-Key " : API_KEY , " Content-Type " : " application/json " }, json = { " q " : " mechanical keyboard " , " hl " : " en " , " gl " : " us " , " page " : 1 }, timeout = 30 , ) resp . raise_for_status () for img in resp . json ()[ " images " ][: 10 ]: print ( img [ " rank " ], img [ " title " ], img [ " image_url " ]) print ( " source page: " , img [ " link " ]) What comes back The images array is the grid you see on Google Images, as rows. Per the docs (I re-checked today), three fields are always there and a few more show up when available: Field Always? Use rank ✅ Grid position — correlates with relevance image_url ✅ The actual image file URL link ✅ The page the image lives on title optional Caption text source / domain optional Publisher, for filtering by site quality One honest caveat from the docs: some payloads only carry rank / link and skip normalized aliases like thumbnail — so code defensively with .get() . The workflow I settled on Metadata first, download second. The script above pulls image URLs and source pages into a CSV; a separate step downloads only the ones that pass filters (min resolution via a HEAD check, domain allowlist, dedupe by URL hash). This keeps the credit bill low — you only pay for the search, not for hosting junk you'll throw away. Pagination matters here: there's no num parameter, just page (1-based). Twenty pages of one keyword beats one page of twenty keywords when you're hunting a specific product shot. Next step Set your key (new accounts get 100 free searches, no card) and run it on a niche term. The full parameter list lives in the SerpBase /google/images endpoint docs . Your first useful filter will probably be domain — half the junk disappears once you blacklist aggregator sites.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dodou88/scrape-google-images-search-results-with-a-serp-api-python-l0m

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
