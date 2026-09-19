---
title: "I Crawled 4 Major Dev Sites' First 10 Pages. Two Had Real Structural Bugs"
slug: "i-crawled-4-major-dev-sites-first-10-pages-two-had-real-structural-bugs"
author: "Hermis"
source: "devto_webdev"
published: "Sat, 19 Sep 2026 03:14:19 +0000"
description: "On 2026-09-19 I ran four well-known developer-facing sites through the free crawler on my own SEO tool — smashingmagazine.com, freecodecamp.org, tailwindcss...."
keywords: "pages, internal, org, mozilla, authority, page, news, site"
generated: "2026-09-19T04:04:08.805637"
---

# I Crawled 4 Major Dev Sites' First 10 Pages. Two Had Real Structural Bugs

## Overview

On 2026-09-19 I ran four well-known developer-facing sites through the free crawler on my own SEO tool — smashingmagazine.com, freecodecamp.org, tailwindcss.com, and mozilla.org — 10 pages each, starting from the homepage. I wasn't looking for anything specific, just comparing internal-link health across sites that presumably have real engineering teams behind them. Two of the four had a genuine structural bug in the crawled sample; the other two were clean. What I ran No account needed, so this is reproducible: POST https://rankforge.cc/api/analyzer with {"seed_url": "..."} , then poll GET /api/analyzer/<id> until status is completed . The crawler follows internal links breadth-first from the seed, caps at 10 pages for the anonymous tier, and runs a PageRank-style authority simulation restricted to the crawled subgraph. Raw JSON for all four runs: content/analyzer_20260919_<host>.json . The clean pair tailwindcss.com was the healthiest of the four: 1,608 internal links found across the 10 pages, average internal authority 63.24, and only 1 of the 10 pages fell into the weakest-20%-authority bucket. Dense internal linking, nothing orphaned, nothing redirecting strangely. smashingmagazine.com was solid too — 847 links, average authority 32.39, zero orphan or near-orphan pages in the sample. It does carry 9 internal redirects (mostly old article URLs 301'd to canonical ones), which cost a hop each but nothing broken. freecodecamp.org: 8 of 10 crawled pages were orphans This is the one that surprised me. Starting from the freeCodeCamp homepage, 8 of the 10 pages the crawler reached had zero internal links pointing to them — they were only reachable because something on an earlier page happened to link to them once, then nothing else in the crawled set linked back. All 8 were the same kind of page: old supporter/contributor "thank you" and wallpaper pages — /news/freecodecamp-supporter-happy-2023-wallpaper /news/thank-you-for-donating /news/super-secret-supporter-wallpaper /news/thank-you-for-being-a-supporter /news/2025-supporter-wallpaper /news/podcast-guest-checklist /news/top-contributor-happy-2023-wallpaper /news/2025-top-contributor-wallpaper freeCodeCamp is enormous — this is a 10-page sample, not a site-wide audit, so it doesn't mean the whole site is 80% orphaned. What it does show is that whatever internal navigation path the crawler followed from the homepage dead-ends into a cluster of donor/supporter pages that don't link to anything else in the main content graph and aren't linked from each other. All 8 landed on the exact same authority score (12.82), which is what the simulation produces for pages that form an isolated cluster fed by identical inbound paths rather than genuine cross-linking — a distinct signature from a healthy content page that earns varied internal links from different sections of the site. If you maintain a site with a similar "supporter wall" or campaign-page pattern, this is worth checking: pages like this often get created once, linked from a single sitewide footer or CTA, and never touched again. They're not broken, but they're structurally isolated from the rest of the site's internal link graph. mozilla.org: pages that redirect to themselves The odder result. Average internal authority for the mozilla.org sample came back as 0 — every page in the 10-page crawl showed up in the redirect audit instead of the normal authority table. The redirect audit flagged 9 of the 10 pages, and the entries look like this: https://www.mozilla.org/en-US/about/manifesto -> redirects to: https://www.mozilla.org/en-US/about/manifesto ( 2 hops, status 301 ) https://www.mozilla.org/en-US/privacy/websites/cookie-settings -> redirects to: https://www.mozilla.org/en-US/privacy/websites/cookie-settings ( 1 hop, status 301 ) https://www.mozilla.org/en-US/products/vpn -> redirects to: https://www.mozilla.org/en-US/products/vpn ( 1 hop, status 302 ) Each URL's redirects_to field is identical to the URL itself. That reads as a locale/trailing-slash redirect loop that resolves back to the same canonical path — plausible causes are a www vs. non- www normalization step, an en-US locale rewrite, or a cookie-consent gate that 302s every request through itself once before serving content. Functionally it's harmless to a human visitor (the browser follows the hop instantly and lands on the right page), but it means every internal link on the site is spending a redirect hop it doesn't need to, and it's why the crawler's authority table came back empty — the simulation attributes authority to the final resolved URL, and here that bookkeeping collapsed the whole sample into the redirect audit instead. Neither of these is a catastrophic SEO problem. freeCodeCamp's orphan cluster is old campaign pages that were probably never meant to rank on their own. Mozilla's self-redirect is a normalization quirk that costs milliseconds, not rankings. But both are the kind of thing that's invisible from a normal site walkthrough and only shows up once you crawl the actual link graph and check what points to what — which is the whole reason a link-structure crawl is worth running occasionally even on sites that already have dedicated engineering teams. Try it on your own site Same four checks (orphan pages, near-orphans, internal authority distribution, redirect chains) run in one pass, no signup: rankforge.cc/audit .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/hermis_rf/i-crawled-4-major-dev-sites-first-10-pages-two-had-real-structural-bugs-4bm4

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
