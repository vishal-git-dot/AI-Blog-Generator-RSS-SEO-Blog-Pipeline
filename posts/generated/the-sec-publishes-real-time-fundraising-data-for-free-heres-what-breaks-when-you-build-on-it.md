---
title: "The SEC publishes real-time fundraising data for free — here's what breaks when you build on it"
slug: "the-sec-publishes-real-time-fundraising-data-for-free-heres-what-breaks-when-you-build-on-it"
author: "0xGollum"
source: "devto_python"
published: "Mon, 03 Aug 2026 09:42:47 +0000"
description: "Every US company raising private capital under Reg D has to file a Form D with the SEC within 15 days of the first sale. It's public, structured, free, no AP..."
keywords: "data, you, form, filings, not, sec, feed, only"
generated: "2026-08-03T09:55:50.591410"
---

# The SEC publishes real-time fundraising data for free — here's what breaks when you build on it

## Overview

Every US company raising private capital under Reg D has to file a Form D with the SEC within 15 days of the first sale. It's public, structured, free, no API key, no login. Most people don't know it exists because nobody points a UI at it. I built a small scanner on top of it recently (part of a data-actor portfolio I run on Apify — my precious, data). Two things broke in ways worth sharing, because neither is specific to SEC data — they're generic lessons for anyone building on a "real-time government feed." 1. The "current filings" feed filters by prefix, not exact match EDGAR exposes a getcurrent endpoint that returns the latest filings as an Atom feed, filterable by type . Pass type=D expecting only Form D filings back, and you'll also get D/A (amendments) and totally unrelated forms like DEFA14A — because the filter is a prefix match on the form type string, not an exact one. If you don't re-filter client-side, you'll silently ingest amendments and unrelated filings as if they were fresh new filings. Cheap fix, but easy to miss if you only smoke-test with a handful of examples that happen to be clean. candidates = [r for r in parsed_feed if r["form_type"] == "D"] # not "D".startswith(...) 2. A "working" URL can still be silently doing 2x the work Each filing's actual structured data lives in a predictable path: /Archives/edgar/data/{CIK}/{accession}/primary_doc.xml. The feed gives you the CIK zero-padded to 10 digits (e.g. 0002123924). Build the URL with that padded form and... it works. You get a 200, the XML parses, the data is correct. Except it doesn't directly work — it 301-redirects to the unpadded form (2123924) first. My HTTP client had follow_redirects=True set (a reasonable default), so every single request was silently doing two round trips instead of one. Nothing looked wrong: correct data, no errors, tests green. It only showed up when I deliberately turned redirect-following off to double check what was actually happening on the wire. The lesson generalizes past SEC data: whenever you build a URL from an ID that a source hands you in more than one textual form (padded vs not, mixed case, trailing slash), a "successful" run doesn't prove your requests are efficient — only that redirects saved you. Worth an explicit no-redirect check anywhere you're rate-limit-sensitive. Both were caught by testing against live data before shipping, not by staring at the code — the redirect one in particular produces zero visible symptoms until you go looking for it. Part of a small portfolio of data actors I maintain — signal over data dump, always tested against the real source before shipping. 0xGollum, feeding the data mines.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/0xgollum/the-sec-publishes-real-time-fundraising-data-for-free-heres-what-breaks-when-you-build-on-it-3k08

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
