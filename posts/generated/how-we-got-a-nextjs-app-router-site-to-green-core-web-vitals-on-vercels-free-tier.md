---
title: "How we got a Next.js App Router site to green Core Web Vitals on Vercel’s free tier"
slug: "how-we-got-a-nextjs-app-router-site-to-green-core-web-vitals-on-vercels-free-tier"
author: "ENZORA"
source: "devto_webdev"
published: "Thu, 29 Oct 2026 22:13:54 +0000"
description: "Shipping a marketing site that looks premium is easy. Shipping one that stays fast on mid-range phones, on cold cache, without a performance budget spreadshe..."
keywords: "next, not, vercel, image, after, app, site, vitals"
generated: "2026-10-29T22:37:17.909646"
---

# How we got a Next.js App Router site to green Core Web Vitals on Vercel’s free tier

## Overview

Shipping a marketing site that looks premium is easy. Shipping one that stays fast on mid-range phones, on cold cache, without a performance budget spreadsheet—that takes discipline. We recently tightened ENZORA’s public site on Next.js 15 App Router, hosted on Vercel’s Hobby tier. This article walks through what actually moved Core Web Vitals into the green zone for us, and what we deliberately did not do. Start with measurement, not guesses Before changing code, we ran Lighthouse against a production build ( next build + next start ), not next dev . Dev mode inflates JavaScript cost and hides image optimisation. Mobile emulation matters: most agency traffic lands on phones. We tracked three field-aligned lab signals: Largest Contentful Paint (LCP) — usually the hero headline block or a large visual above the fold. Cumulative Layout Shift (CLS) — often from web fonts, late-loading widgets, or images without reserved space. Interaction to Next Paint (INP) — main-thread work from hydration, analytics, or heavy client components. If a metric is red, write down the LCP element name from Lighthouse. That single line saves hours of random bundle trimming. Keep the critical path boring Static generation where possible App Router pages that do not need per-request data should be static. Our home, services, legal, and blog index routes prerender at build time. That gives CDN-friendly HTML and predictable TTFB on Vercel. Dynamic routes ( /blog/[slug] , /services/[slug] ) use generateStaticParams so builds emit HTML for known URLs. Avoid force-dynamic unless you truly need it. Fonts without layout drama We load Inter for body copy with display: "swap" and preload it. A secondary display font loads with preload: false so it does not compete with LCP. Pair swap with consistent fallback metrics in CSS ( size-adjust or a close system stack) if CLS spikes when the webfont arrives. Images: one pipeline The React tree should use next/image for raster assets so AVIF/WebP negotiation and sizing stay automatic. Enable modern formats in config: images : { formats : [ " image/avif " , " image/webp " ] }, For decorative portfolio tiles rendered as CSS/SVG mockups, we use explicit aspect-ratio boxes so nothing reflows when lazy sections mount. Defer non-critical client JavaScript Marketing sites accumulate “nice to haves”: custom cursors, chat widgets, animation libraries. We moved non-essential UI into a client shell loaded after hydration with next/dynamic and ssr: false . The hero and primary call-to-action render as server components; the floating chat and cursor do not block first paint. Analytics follows the same rule: Google Analytics 4 loads only after explicit cookie consent. Vercel Analytics and Speed Insights are lightweight first-party scripts and stayed enabled—they report vitals without blocking interaction in our tests. Third-party scripts are a tax Every tag manager, chat vendor, or A/B snippet competes with INP. On the free tier you feel this immediately. Our defaults: No tag manager on launch. Chat is optional; a lightweight in-house panel replaces a heavy embed until a vendor is required. Consent-gated GA4 with send_page_view controlled manually on route changes (App Router needs a small client listener). If marketing insists on a pixel, load it after consent and measure INP again. CSS and motion without jank Tailwind v4 kept our stylesheet lean, but motion still caused jank when tied to scroll on the main thread. We gate expensive scroll-driven effects behind a class added on first user interaction (scroll, pointer, keydown). That avoids animating large layers before the user engages—helpful for INP on low-end devices. Reserve space for fixed cookie banners ( position: fixed with a modest height) so accepting cookies does not shove the layout. A small banner beat a full-screen modal for CLS. Caching and headers Vercel already sends HSTS and compresses assets. We add long-cache headers for hashed static files in vercel.json and keep HTML on short cache with revalidation. Do not cache HTML aggressively if you ship content fixes often; do cache /logo/* , fonts, and media under /public . What our numbers looked like On a production build served locally and spot-checked on the deployed preview, mobile Lighthouse reported LCP around 1.1 s , CLS 0 , and INP in the tens of milliseconds after the above passes. Scores move with network noise—treat Lighthouse as a regression guard, not a vanity badge. Re-run tests after every new script marketing asks for. One embed can undo a week of image optimisation. Checklist you can copy Production build + mobile Lighthouse baseline. Identify the LCP element; optimise that first. Static-generate marketing routes; static params for slugs. next/image + AVIF/WebP; fixed aspect ratios for media. Split client bundles; defer chat, cursor, GA4 until needed/consented. Gate scroll/motion effects until interaction. Re-measure after each third-party add. Green Core Web Vitals on a free tier is not magic—it is scope control. The site still has rich typography and motion; we just refuse to let optional scripts sit on the critical path. If you are tuning a similar agency site, start with consent-gated analytics and dynamic-imported widgets; the vitals usually follow. Originally published on the ENZORA blog . ENZORA builds fast Next.js and Shopify sites, SEO and ads for growing businesses: enzora.vercel.app .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/enzora_official/how-we-got-a-nextjs-app-router-site-to-green-core-web-vitals-on-vercels-free-tier-2o98

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
