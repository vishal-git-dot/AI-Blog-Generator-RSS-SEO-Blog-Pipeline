---
title: "Capturing AI-Assistant Referrers in Application Logs Without Breaking Caching"
slug: "capturing-ai-assistant-referrers-in-application-logs-without-breaking-caching"
author: "Peter Panda"
source: "devto_python"
published: "Sat, 31 Oct 2026 21:03:38 +0000"
description: "When a user clicks from an AI answer into your site, the referrer field is one of the few signals you get. Many teams lose it to CDN defaults, aggressive cac..."
keywords: "first, referrer, you, not, cache, they, assistant, when"
generated: "2026-10-31T21:15:20.725237"
---

# Capturing AI-Assistant Referrers in Application Logs Without Breaking Caching

## Overview

When a user clicks from an AI answer into your site, the referrer field is one of the few signals you get. Many teams lose it to CDN defaults, aggressive cache keys or SPA navigations that never send the first landing referrer to analytics. Log the first HTML request In nginx (or your edge worker), dump $http_referer , $arg_utm_source and a request id on the first document request. Do not wait for a tag manager event; ad blockers and refused JS wipe that path. Keep HTML cache keys from ignoring the landing URL If you cache HTML, ensure the first landing still records referrer server-side before a cache hit serves a shell. Some stacks log only on miss; force a lightweight collect endpoint instead. Normalise known assistant hosts Maintain a small map: host contains chatgpt , perplexity , copilot , etc. Store both raw referrer and a normalised ai_source dimension so dashboards stay readable when domains change. Pass the signal into the CRM on form submit Stash the first referrer in a first-party cookie or server session with a short TTL. On lead submit, write it onto the contact. Otherwise sales never sees that the lead came from an assistant. Review weekly, not once a quarter AI traffic patterns shift. A weekly count of landings by ai_source is enough to see whether content experiments move anything. Practical checklist Before you ship the change, walk through a short checklist with someone who did not write the page. Ask them to explain the offer, the price or fee range, the timeline and the main risk in their own words. If they cannot, the draft is not ready for assistants or for humans either. Document the owner of the page, the next review date and the source of every number you quote. When a platform policy or a fee changes, you want a single place to update rather than a scavenger hunt across blog posts, help articles and sales decks. Common failure modes Teams usually fail in three ways. They publish once and never revisit dates. They keep conflicting facts on the About page, a directory and a PDF one-pager. They measure vanity traffic instead of whether the answers that matter improved. A lightweight monthly review catches all three earlier than a panicked quarterly audit. How this ties to pandawm.com work Overseas ads, multilingual sites, GEO and crypto checkout for overseas merchants share the same underlying need: clear facts, consistent entities and pages that can be quoted without guesswork. The implementation details differ by channel; the editorial discipline does not. A fuller attribution pattern for AI leads is in how to attribute AI search leads . Published by PandaWM , an overseas marketing team based in Hong Kong.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/pandawm/capturing-ai-assistant-referrers-in-application-logs-without-breaking-caching-172h

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
