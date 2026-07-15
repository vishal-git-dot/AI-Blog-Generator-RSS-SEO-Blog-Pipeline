---
title: "How to check Core Web Vitals for hundreds of URLs at once (API + code)"
slug: "how-to-check-core-web-vitals-for-hundreds-of-urls-at-once-api-code"
author: "quantoracledev"
source: "devto_webdev"
published: "Wed, 15 Jul 2026 02:37:16 +0000"
description: "Google's PageSpeed Insights is great for auditing one page. But the moment you want to track Core Web Vitals across a whole site — or every client site you m..."
keywords: "score, com, cls, https, web, page, you, core"
generated: "2026-07-15T02:52:14.906677"
---

# How to check Core Web Vitals for hundreds of URLs at once (API + code)

## Overview

Google's PageSpeed Insights is great for auditing one page. But the moment you want to track Core Web Vitals across a whole site — or every client site you manage, or every page after a deploy — clicking through a web UI (or fighting per-key rate limits) stops scaling. Here's how to measure LCP, CLS, FCP and TTFB in bulk , in real Chromium, with a plain API call and no rate-limit juggling. What we're measuring The metrics that actually affect Google ranking and user experience: LCP (Largest Contentful Paint) — when the main content appears. Target < 2.5s. CLS (Cumulative Layout Shift) — how much the layout jumps. Target < 0.1. FCP (First Contentful Paint) — first pixel of content. TTFB (Time To First Byte) — server responsiveness. Plus the why : total page weight, request count, third-party load, DOM size — the things you actually change to fix a bad score. The bulk approach Website Performance Audit loads each URL in a real browser, measures Core Web Vitals via the standard PerformanceObserver APIs (lab data, comparable to Lighthouse), and returns a 0–100 score plus a prioritized list of opportunities. curl -X POST "https://api.apify.com/v2/acts/runlayer~website-performance-audit/run-sync-get-dataset-items?token=YOUR_APIFY_TOKEN" \ -H "Content-Type: application/json" \ -d '{ "urls": ["https://example.com", "https://example.com/pricing", "https://example.com/blog"], "device": "mobile" }' Each URL comes back like this: { "url" : "https://example.com/pricing" , "score" : 72 , "lcpMs" : 2380 , "cls" : 0.04 , "fcpMs" : 1290 , "ttfbMs" : 410 , "totalKb" : 2648 , "requests" : 84 , "thirdPartyRequests" : 37 , "opportunities" : [ { "severity" : "warning" , "title" : "Render-blocking resources" , "detail" : "5 synchronous scripts/stylesheets in <head>…" }, { "severity" : "warning" , "title" : "Heavy JavaScript" , "detail" : "Scripts total 1180 KB…" } ] } Make it a performance budget in CI The useful part isn't a one-time number — it's catching regressions. Fail your build if a key page's score drops or LCP crosses a threshold: const urls = [ " https://example.com " , " https://example.com/pricing " ]; const results = await fetch ( " https://api.apify.com/v2/acts/runlayer~website-performance-audit/run-sync-get-dataset-items?token= " + process . env . APIFY_TOKEN , { method : " POST " , headers : { " Content-Type " : " application/json " }, body : JSON . stringify ({ urls , device : " mobile " }), } ). then (( r ) => r . json ()); const budget = { score : 70 , lcpMs : 2500 , cls : 0.1 }; const failures = results . filter ( ( r ) => r . score < budget . score || r . lcpMs > budget . lcpMs || r . cls > budget . cls ); if ( failures . length ) { console . error ( " Performance budget exceeded: " ); for ( const f of failures ) console . error ( ` ${ f . url } — score ${ f . score } , LCP ${ f . lcpMs } ms, CLS ${ f . cls } ` ); process . exit ( 1 ); } Drop that in a GitHub Action after deploy and you get a hard gate on performance regressions — across as many pages as you want, in one call. Auditing a whole site on a schedule Feed it your sitemap URLs (or pair it with a crawler) and run it on an Apify Schedule weekly. Sort the resulting dataset by score ascending and you've got a prioritized worklist: worst pages first, each with the specific opportunities to fix. SEO, not just speed? Core Web Vitals are one ranking input. If you also want on-page SEO — titles, meta descriptions, headings, canonical tags, structured data, broken links — the companion SEO Audit actor returns all of that plus Core Web Vitals in one record, each issue paired with a concrete fix. Cost Pay per page audited, no subscription, no per-key rate limits, failures free. Auditing a 100-page site is pocket change and runs in a couple of minutes — and Apify's free credits cover plenty of testing. Built this because bulk Core Web Vitals shouldn't require a spreadsheet of PageSpeed tabs. Feedback and feature requests (INP? filmstrips?) via the actor's issues tab. The full utility suite is at apify.com/runlayer .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/quantoracle/how-to-check-core-web-vitals-for-hundreds-of-urls-at-once-api-code-45ni

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
