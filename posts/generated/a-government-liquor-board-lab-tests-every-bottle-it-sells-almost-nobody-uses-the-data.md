---
title: "A Government Liquor Board Lab-Tests Every Bottle It Sells. Almost Nobody Uses the Data."
slug: "a-government-liquor-board-lab-tests-every-bottle-it-sells-almost-nobody-uses-the-data"
author: "Sakurai Ts"
source: "devto_webdev"
published: "Sat, 08 Aug 2026 12:43:47 +0000"
description: "The best datasets aren't hidden. They're published in plain sight by bureaucracies that have no idea anyone might want them — collected for compliance, expos..."
keywords: "data, sugar, lab, every, one, field, page, lcbo"
generated: "2026-08-08T12:58:39.637039"
---

# A Government Liquor Board Lab-Tests Every Bottle It Sells. Almost Nobody Uses the Data.

## Overview

The best datasets aren't hidden. They're published in plain sight by bureaucracies that have no idea anyone might want them — collected for compliance, exposed out of habit, and abandoned one page at a time. Here's my favorite example. The LCBO — Ontario's government liquor monopoly, and one of the largest single buyers of beverage alcohol in the world — runs a quality-assurance lab. Products it sells get tested, and each product page on lcbo.com quietly lists a field most shoppers scroll past: Sugar Content , in grams per litre. Lab-measured residual sugar, for essentially the entire catalogue. Roughly thirty thousand SKUs. Now the punchline: the site gives you no way to use it . You can sort the catalogue by price, rating, novelty, name — everything except sugar. The single field that matters to diabetics, keto dieters, and every person who's ever asked "is this wine actually sweet?" is right there on every page and completely inert. Meanwhile, wine bottles themselves carry no nutrition labels at all in North America. Public data, real audience, zero interface. That's not a gap in the market; that's an open door with a welcome mat. What I built winesugarcontent.com — the missing interface: 12,635 in-stock products, each with its lab-verified g/L, searchable and sortable by sugar, price, category, country, grape, and a five-tier sweetness scale (bone dry < 1 g/L → sweet > 120 g/L). The pipeline, for the technically curious: Ingestion. The LCBO frontend is driven by Coveo (search-as-a-service). Rather than scraping HTML, you can speak to the same search API the site itself uses — the field is called lcbo_sugar_gm_per_ltr . A headless browser grabs a short-lived API token; after that it's structured JSON with rate limiting and checkpointed batches. ~30k raw records. Cleaning. Dedupe, normalize, drop delisted items, derive a sweetness tier from measured g/L (never from the marketing "style" field — more on that below). Result: one wines.json as the single source of truth. Site. Astro static generation: one build fans out to ~12,900 pages (a page per product, paginated category lists, a ranked red-wine chart). Tables are server-rendered HTML — crawlable, fast, no client-side data fetching. Postgres (Supabase) holds canonical data; images are re-hosted as WebP on Cloudflare R2; deploys to Cloudflare Pages via GitHub Actions. Refresh. The scrape → clean → rebuild loop is scripted end to end, so the database tracks the live catalogue instead of decaying into a snapshot. Three rules that shaped the build 1. Never let a language model invent a number. This project has an audience of diabetics making dosing-adjacent decisions. Every g/L on the site traces to an LCBO lab reading, and every product page links back to the original listing for verification. During development, placeholder rows rendered with a banner reading SAMPLE DATA — DO NOT SHIP . Data provenance isn't a nice-to-have here; it's the entire product. 2. Trust measurements, not descriptors. The LCBO data includes a human-facing style field ("Off-dry & Fruity"). It disagrees with the lab numbers constantly — same descriptor, 3× sugar difference. The tier system uses g/L thresholds only. When measurement and marketing conflict, measurement wins. 3. The interface is the product. I added nothing to the data. No scores, no AI summaries, no editorial. Sort-by-sugar — the one feature the source refuses to offer — turns out to be the whole value proposition. My favorite artifact: of 6,172 red wines, exactly 3 measure above 120 g/L. Every sweet-red seeker in Ontario has been searching for three bottles their whole lives without knowing it. (They're all visible in the red wine sweetness chart .) The replicable part This pattern generalizes further than wine. Government purchasing monopolies are accidental data publishers: Sweden's Systembolaget, Norway's Vinmonopolet, Finland's Alko and Quebec's SAQ all publish comparable sugar figures. Same schema, different flag — each one a weekend project waiting for someone whose audience needs it. The formula: find a field a bureaucracy measures but doesn't surface, verify it's genuinely public, respect the source (rate limits, attribution, link back), and build the missing index. You're not creating information. You're creating access — and access, it turns out, is most of what people were missing.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/sakurai_ts_745cc85d7d4294/a-government-liquor-board-lab-tests-every-bottle-it-sells-almost-nobody-uses-the-data-1j4d

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
