---
title: "Why I never built a backend for a site with 290+ calculators"
slug: "why-i-never-built-a-backend-for-a-site-with-290-calculators"
author: "Alex Morgan"
source: "devto_webdev"
published: "Tue, 18 Aug 2026 18:28:52 +0000"
description: "Why I never built a backend for a site with 290+ calculators I run calculate.at , a free site with 290+ online calculators — mortgage payments, BMI, unit con..."
keywords: "one, site, what, backend, its, twice, calculator, const"
generated: "2026-08-18T18:44:45.285332"
---

# Why I never built a backend for a site with 290+ calculators

## Overview

Why I never built a backend for a site with 290+ calculators I run calculate.at , a free site with 290+ online calculators — mortgage payments, BMI, unit conversions, percentages, that kind of thing. No account system, no analytics pixels chasing you around, no backend at all. Every calculation runs entirely in the browser, computed with plain JavaScript on the same page you're looking at. That sounds like an obvious choice for a site that's "just math," but it wasn't the default I started with, and a couple of the decisions that came out of it turned out to matter more than I expected — one for engineering, one for SEO. The case against a backend The first instinct for a "calculator platform" is to reach for an API: POST /api/calculate , validate the inputs server-side, return a JSON result. It's the pattern everyone knows, and for something like a mortgage amortization schedule it even sounds reasonable — there's real math involved. But walking through what that actually buys you for a site like this: Nothing to validate that matters. The worst outcome of bad input to principal * rate / 12 is a wrong number on the user's own screen. There's no shared state to corrupt, no other user affected, no data to protect. No latency wins. A network round-trip to compute bill * (tip / 100) is strictly slower than just computing it. The server can't do the math faster than the browser that already has both operands. No privacy story to worry about. If I never receive the numbers, I never have to think about what happens to them. A backend calculator design usually ends up needing a "we don't log your inputs" line in a privacy policy; here there's nothing to write because there's no server-side code path that could log them. The infrastructure would exist purely to add latency and a failure mode. A calculator that depends on an API call now has an outage mode. A calculator that's a <script> tag doesn't. So every calculator on the site — from a one-line percentage formula to a full mortgage amortization table — runs as plain client-side JavaScript against the DOM. Here's roughly the shape of it, stripped down: function calcTip () { const bill = parseFloat ( document . getElementById ( ' bill ' ). value ); const tipPct = parseFloat ( document . getElementById ( ' tip-pct ' ). value ); const people = parseInt ( document . getElementById ( ' people ' ). value ) || 1 ; const tip = bill * ( tipPct / 100 ); const total = bill + tip ; const perPerson = total / people ; renderResult ({ tip , total , perPerson }); } No framework state management, no server round-trip, no loading spinner. The result updates the moment the input changes. For a site whose entire value proposition is "get the number fast," that responsiveness isn't a nice-to-have — it's most of the product. The unit converter decision that was really an SEO decision The one place this got genuinely interesting was unit conversion, because the natural engineering instinct fights the natural SEO instinct. Engineering instinct: build one <UnitConverter direction="bidirectional"> component, pass it miles and km as props, add a little swap button. One component, two use cases, DRY. What I actually shipped: /conversion/miles-to-km/ and /conversion/km-to-miles/ as two separate static pages, each with its own H1, its own worked examples, its own FAQ section — genuinely duplicated content structure, not just a shared component rendered twice. The reasoning: someone searching "miles to km" and someone searching "km to miles" are expressing different intent, even though the underlying math is a one-line multiplication either way. A single bidirectional page has to split its relevance signal across both queries — its title, its H1, its default state all have to pick a side or hedge. Two pages each get to be unambiguously about one direction, which is what search engines want to see when they're deciding what a page is for. The cost is real: twice the pages to generate, twice the worked examples to write, twice the FAQ content to keep in sync if the underlying conversion factor or presentation ever changes. For ~45 unit conversion tools that's not a small multiplier. But it's a one-time templating cost, not an ongoing one — the site is statically generated (Astro), so "twice the pages" means twice the build-time output, not twice the runtime complexity. What this bought and what it cost Bought: Zero backend to operate, monitor, or pay for Instant results with no network dependency No privacy policy paragraph explaining what happens to numbers I never receive Search pages that map cleanly to search intent instead of hedging between two Cost: More pages to template and maintain (mitigated by static generation) No server-side validation layer, which is fine here but wouldn't be for anything with real stakes Every calculator's logic has to ship to the client, which is a non-issue for arithmetic but would matter for something computationally heavier For a site that's fundamentally "type numbers in, see a result," none of the usual reasons to reach for a backend actually applied once I wrote them down. The interesting lesson wasn't "don't build a backend" in general — it's that the decision is worth actually deriving from what the product needs, instead of defaulting to the API-shaped architecture because that's the shape most examples come in.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/calculate_at/why-i-never-built-a-backend-for-a-site-with-290-calculators-3ea7

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
