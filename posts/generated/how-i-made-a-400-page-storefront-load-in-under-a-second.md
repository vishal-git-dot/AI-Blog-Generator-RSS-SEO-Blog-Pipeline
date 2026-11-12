---
title: "How I Made a 400-Page Storefront Load in Under a Second"
slug: "how-i-made-a-400-page-storefront-load-in-under-a-second"
author: "Shipon Talukdar All Project"
source: "devto_webdev"
published: "Thu, 12 Nov 2026 23:18:30 +0000"
description: "I run a small e-commerce storefront — an online vape shop in Dubai with about 170 products, 37 categories, and 420 URLs in the sitemap. It is built with Next..."
keywords: "product, page, what, every, not, build, reviews, admin"
generated: "2026-11-12T23:24:23.224567"
---

# How I Made a 400-Page Storefront Load in Under a Second

## Overview

I run a small e-commerce storefront — an online vape shop in Dubai with about 170 products, 37 categories, and 420 URLs in the sitemap. It is built with Next.js 16, Supabase, and Cloudinary, and it runs on the Vercel free plan, which means every deployment and every CPU second counts. Here is what actually moved the needle on speed, and what did not. The problem: product pages took 4–5 seconds Before the change, a product page took 1.3–1.6 seconds just to show the product name, 2.1–2.3 seconds for the buy box, and 4–5.3 seconds total on a slow connection, at 364KB. The page was server-rendered on every visit: product data, reviews, and related products all fetched per request. On a free plan, that is both slow and expensive. What worked: pre-render everything at build time The single biggest win was generateStaticParams on the product and category pages. All 405 static pages now build in about 32 seconds, and a visit serves a pre-rendered page. Measured after the change: product name and buy box arrive with the first byte, TTFB 0.58–0.69s, total 0.79–0.91s, 246KB. Same content, same URLs — the work just moved from request time to build time. Two details mattered: The build must never fail because the database is down. The static-params function wraps the database call in try/catch and returns an empty array on failure, so a deploy still succeeds and the pages render on demand. Partial prerendering is real. The routes show as partial prerender in the build output: the static shell ships immediately and the dynamic bits stream in. That is what gets the product name into the first byte. What worked: targeted cache invalidation, not "clear everything" Pre-rendering creates a second problem: when an admin edits a price, the stale page keeps serving. The fix was per-item cache tags — every loader tags exactly what it returns ( product-<slug> , category-<slug> ), and every admin save revalidates only the tags it touched, plus the page path. Changing one product's price refreshes that product's page and the category cards showing it, and nothing else. One bug worth naming: the original code called revalidateTag after the return statement in three admin upsert functions, so it was dead code and admin edits never invalidated anything. The fix was moving the calls before the return. If your admin edits seem to "not take effect", check for code after a return before blaming the cache. What worked: reserve stock at checkout, in the database The checkout reserves stock before creating the order: a live read plus a conditional update on stock_qty (three retries per item), so two simultaneous orders cannot sell the same last unit. Over-ordering returns a 409 with a plain message. Cancelling or deleting an order restores exactly the reserved stock. When stock hits zero, the revalidation above flips the product page to "Out of Stock" on its own. What worked: reviews load in parallel, and moderation is a database flag Product reviews used to load after the product. Loading them in parallel with the product (one Promise.all ) cut a waterfall. New customer reviews are inserted with is_approved = false and only appear publicly after an admin approves them; the product's average rating is recomputed from approved reviews only. Nothing about this is clever — it is just doing the obvious thing in the right order. What did not work: chasing the homepage The homepage is the slowest page on the site (426KB of HTML, 94 images) and the only real lever is cutting content — which the shop owner will not do, because the content is the SEO. The honest answer was to leave it alone and say so, rather than burn the free-plan budget on marginal gains. Not every slow page has a fix you are allowed to ship. The checklist Pre-render product and category pages at build time; never let a database failure fail the deploy. Tag cached queries per item; revalidate only what an edit touched. Reserve stock with a conditional update at checkout; restore it on cancel. Load secondary data (reviews) in parallel, not in sequence. Keep prefetching off product cards — it burns budget for clicks that never happen. When the only fix is one you cannot ship, say so and move on. The live site is POD Shop , and the Juul range I used as the test case is at podshopdubai.com/category/juul . Same stack, same content — just faster, because the work happens at build time instead of on every visit.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/shipon_talukdarallproje/how-i-made-a-400-page-storefront-load-in-under-a-second-1f4p

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
