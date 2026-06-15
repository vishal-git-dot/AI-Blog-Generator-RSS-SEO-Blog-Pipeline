---
title: "How to Check Core Web Vitals in 10 Minutes"
slug: "how-to-check-core-web-vitals-in-10-minutes"
author: "Kui Luo"
source: "devto_webdev"
published: "Mon, 15 Jun 2026 12:12:50 +0000"
description: "You don't need expensive tools to check your Core Web Vitals. Here's a practical approach to auditing LCP, INP, and CLS using entirely free tools. Why Core W..."
keywords: "inp, web, vitals, lcp, cls, check, step, layout"
generated: "2026-06-15T12:29:05.505711"
---

# How to Check Core Web Vitals in 10 Minutes

## Overview

You don't need expensive tools to check your Core Web Vitals. Here's a practical approach to auditing LCP, INP, and CLS using entirely free tools. Why Core Web Vitals Matter Google uses Core Web Vitals as a ranking signal. Sites that pass the CWV assessment see an average 11% increase in organic traffic within 60 days, based on Chrome UX Report data. The three metrics you need to monitor: Metric Good Threshold What It Measures LCP ≤ 2.5 seconds Largest contentful paint INP ≤ 200 ms Interaction to Next Paint CLS ≤ 0.1 Cumulative Layout Shift Step 1: Run Lighthouse from DevTools Open your site in Chrome Press F12 to open DevTools Go to the Lighthouse tab Select Performance mode Click Analyze page load Lighthouse gives you a real-time audit. Focus on the LCP, INP, and CLS scores. Step 2: Check Real User Data Lab data from Lighthouse only shows one test run. Real user data matters more. Go to pagespeed.web.dev and enter your URL. The report shows field data from actual Chrome users at the 90th percentile, plus diagnostic suggestions prioritized by impact. A passing score requires all three metrics in "Good" range for at least 75% of sessions. Step 3: Fix the Most Common Issues LCP over 2.5s (Slow Loading) Optimize hero image: serve WebP at correct dimensions Preload critical resources with <link rel="preload"> Eliminate render-blocking CSS below the fold INP over 200ms (Sluggish Interactions) Reduce JavaScript execution on the main thread Break up long tasks using requestIdleCallback Minimize third-party scripts — each adds 50-150ms to INP CLS over 0.1 (Layout Shifts) Set explicit width and height on images and videos Reserve space for ads and dynamic content with min-height Never inject content above existing content without user interaction Step 4: Monitor Continuously Set up a free monitoring workflow: Search Console → Core Web Vitals report (CWV status per URL) web-vitals JS library → send real-user data to analytics Lighthouse CI → run on every deploy via GitHub Actions The web-vitals library is a 1.5KB script: <script type= "module" > import { onLCP , onINP , onCLS } from ' https://unpkg.com/web-vitals ' ; onLCP ( console . log ); onINP ( console . log ); onCLS ( console . log ); </script> Quick Impact Summary Action Expected Improvement Optimize hero image LCP -30% to -50% Defer non-critical JS INP -20% to -40% Set explicit dimensions CLS → 0.0 The audit takes about 7-10 minutes per page. Start with your top 10 landing pages by traffic — fixing those typically improves domain-wide CWV pass rate by 40-60%. Most improvements need only HTML and CSS changes. No server reconfiguration, no build tools, no budget needed.webdevseobeginnersMost developers check Core Web Vitals once, see green scores, and never look again. That's a mistake — Core Web Vitals fluctuate with every deployment. Here's a quick, practical guide to auditing LCP, INP, and CLS without leaving Chrome DevTools. What to Measure Metric What It Measures Good Score Tool to Use LCP Largest content paint Under 2.5s Performance tab INP Interaction to next paint Under 200ms Event trace CLS Cumulative layout shift Under 0.1 Layout shift panel Step 1 — Open the Performance Panel Press F12 , go to the Performance tab. Check the "Web Vitals" checkbox at the top. Reload the page with Ctrl+Shift+R (hard reload) to bypass cache. Step 2 — Read the LCP Value After reload, look at the LCP marker in the timeline. It appears as a colored bar showing which element is the largest contentful paint — usually a hero image or heading block. Common LCP problems I see in audits: Unoptimized hero images : Serving 2MB JPEGs when 80KB WebP looks identical Render-blocking CSS : 400KB stylesheet delaying first paint by 1.5s Client-side rendering : Empty HTML shell waiting for JS bundle to hydrate Step 3 — Check INP (Replaces FID) Google replaced FID with INP in March 2024. INP measures the worst interaction latency throughout the entire page lifecycle, not just the first click. To test it: Open the Performance tab and check "Web Vitals" Interact with the page naturally — click buttons, type in forms, open menus Watch the INP counter update in real-time Note the highest value recorded INP above 200ms typically means: Event handlers doing too much synchronous work Main thread blocked by long tasks during user interaction Heavy layout recalculations triggered by DOM changes Step 4 — Measure CLS In the Performance tab, enable the Layout Shift Regions checkbox. Reload the page and watch for red highlighted areas — those are layout shifts. The top 3 CLS causes I find regularly: Images without explicit dimensions : Always set width and height attributes Dynamically injected content : Ads, modals, and late-loading widgets pushing existing content Web fonts with FOIT : Font swaps causing visible text reflow after load Step 5 — Automate with PageSpeed Insights API For continuous monitoring, use the free PageSpeed Insights API: curl "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://example.com&strategy=mobile" This returns lab data for all three metrics. Extract the LCP, INP, and CLS values from the lighthouseResult.audits object. Quick Reference Check LCP after every image optimization Test INP by clicking every interactive element on the page Monitor CLS by enabling layout shift regions in DevTools Automate checks with the PSI API in your CI/CD pipeline Set up a 5-minute check after each deploy. It catches regressions before your users do.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/kui_luo/how-to-check-core-web-vitals-in-10-minutes-5d00

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
