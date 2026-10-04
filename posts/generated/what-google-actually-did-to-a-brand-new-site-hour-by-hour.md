---
title: "What Google actually did to a brand new site, hour by hour"
slug: "what-google-actually-did-to-a-brand-new-site-hour-by-hour"
author: "xg704863664"
source: "devto_webdev"
published: "Sun, 04 Oct 2026 21:00:54 +0000"
description: "I published 51 pages on a brand new domain and then watched what Google did for two days. Here is the actual timeline, with the states Search Console reporte..."
keywords: "not, pages, indexed, crawl, google, two, page, what"
generated: "2026-10-04T21:07:13.179907"
---

# What Google actually did to a brand new site, hour by hour

## Overview

I published 51 pages on a brand new domain and then watched what Google did for two days. Here is the actual timeline, with the states Search Console reported at each stage. The setup A static site on a GitHub Pages subdomain 51 pages, all original, 450-800 words each A verified Search Console property, a sitemap, IndexNow submissions, canonical tags Zero backlinks on day one Hour 0-24: nothing, and no explanation For the first day, the only page in the index was the homepage - and it was a stale version from before a site restructure. The interesting part was not the delay. It was the state Search Console reported when I inspected a page: Web page not indexed: Google could not recognise this URL Discovery Sitemap: no referring sitemap detected Referring page: no referring page detected Crawl Last crawl time: N/A Crawl allowed: N/A "Last crawl time: N/A" means Google had never visited the page. Not rejected - never seen. That is a completely different problem from a quality judgment, and it changes what you should do about it. The mistake I made I assumed the site had a quality problem and wrote more content. For ten days. 51 pages in total, published in batches of five or six. That was probably the wrong instinct for two reasons: Publishing 50 pages in two days on a new domain looks like exactly the pattern spam classifiers are built to catch Content cannot fix a crawl problem. Google was not reading any of it What actually moved it Submitting each URL through Search Console's "Request indexing". Not the sitemap, not IndexNow - the manual request. I built a script to do it at scale, because doing 51 by hand is tedious. Two things about the flow are worth knowing: The request button runs a live test first that takes one to two minutes. The request itself only fires after that completes, and the button has to be clicked again The button is not a <button> element in a predictable place - it is a text node in a div, and its position moves with the layout The state changed, and it changed meaningfully Within hours of the requests, inspected pages went from: Google could not recognise this URL (never crawled) to: Crawled - currently not indexed Last crawl time: [a real timestamp] Crawl allowed: Yes Indexing allowed: Yes That is progress, even though nothing was indexed yet. The problem moved from "Google cannot find this" to "Google found it and is deciding". Day 2: indexing started Roughly 30 hours after the first requests, the site: query went from 3 results to 11. Not all 51 pages - 11. The pages that appeared were the ones from the first two batches of requests, which is a fairly direct confirmation that the requests were what did it. And then: indexed, but invisible Here is the part I did not expect. I searched for exact sentences from the indexed pages: "Crowding is the single biggest cause of pecking, feather-pulling and disease" Nothing. Zero results from my domain, for a sentence that appears verbatim on an indexed page. Indexed is not the same as retrievable. The pages were in the index and had no ranking power for any query at all. For a new domain with no backlinks, that appears to be the normal intermediate state. What I would tell someone starting today Check the crawl state before writing more content. If "last crawl time" is N/A, the problem is discovery, and more pages will not help Use Request indexing aggressively. It is the only lever that directly triggers a crawl Expect the sequence: not crawled -> crawled, not indexed -> indexed, not ranking -> ranking. Each is a separate problem with a different fix Do not publish 50 pages in two days on a new domain. I have no way to prove it hurt, but it is a pattern that looks like something it is not Where it stands now Indexed: 11 of 51 pages. Ranking: zero, for anything. Traffic: zero. The next lever is authority, which means backlinks and time - and neither of those can be rushed. The site in question is a set of reference guides on herbal remedies, gardening and keeping chickens . I wrote up the full indexing diagnosis as it developed.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/xg704863664/what-google-actually-did-to-a-brand-new-site-hour-by-hour-2iei

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
