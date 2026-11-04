---
title: ""Crawled - currently not indexed" on 12 of 13 pages: what I've ruled out on a 3-week-old site"
slug: "crawled-currently-not-indexed-on-12-of-13-pages-what-ive-ruled-out-on-a-3-week-old-site"
author: "Silkline"
source: "devto_webdev"
published: "Wed, 04 Nov 2026 14:00:55 +0000"
description: "A small site I built has 13 pages. Google has indexed one of them, the homepage. Three weeks ago it had six. I've spent more time on this than on building th..."
keywords: "pages, page, indexed, site, what, google, one, october"
generated: "2026-11-04T14:06:42.003149"
---

# "Crawled - currently not indexed" on 12 of 13 pages: what I've ruled out on a 3-week-old site

## Overview

A small site I built has 13 pages. Google has indexed one of them, the homepage. Three weeks ago it had six. I've spent more time on this than on building the site, and I'm stuck. Here's everything I checked, with numbers, so you can tell me what I'm missing. What happened The domain was registered on October 9. Pages went live between October 11 and 23. By October 23, 6 of 13 pages were indexed and the site got about 30 impressions a day, almost all from two pages ranking around position 75–90. October 26: those two pages flipped to "Crawled - currently not indexed". Daily impressions went from 30 to 1, then 0. October 31: five more pages flipped the same way. Only the homepage is left. Weekly impressions: 142, then 16. Three other pages never got that far. They have sat at "URL is unknown to Google" for three weeks, even though they are in the sitemap and other pages link to them. One of them even shows up as a referring page for another URL, which contradicts "unknown". What I ruled out Crawl errors. I pulled the Worker logs and checked each request against Google's published Googlebot IP ranges. Of 3,888 requests from Google's network, 454 were verified Googlebot. Every one got a 200. Googlebot also fetched the JS bundles, so it rendered the pages. Rendering. "Test live URL" in Search Console says the page can be indexed, and the rendered HTML matches what I get from headless Chrome with the Googlebot smartphone user agent: 2,271–3,142 words of rendered text per page, navigation included. Canonicals, noindex, robots. All 13 Google-selected canonicals match the declared ones. Only four legal pages are noindex, by design. Penalties. Manual actions: none. Security issues: none. No Google update was announced in October. Thin or duplicate content. I compared every page's visible text, then ran the same numbers on a sibling site of mine that uses the same template, moved to the same new stack on the same day, and has every page indexed: This site Sibling site (fully indexed) Median words per page 1,949 1,796 Share of text unique to the page 0.64 0.65 Highest overlap with another page 0.33 0.30 Internal links in (median) 10 9 Content structure is not the difference. Internal links. The first two pages that dropped had the fewest links from body text (3 and 2) while the two that stayed had 5 each. That looked like an answer until I noticed the pricing page has 12 and isn't indexed, while one page with a single link is indexed. Sitemap. Read on October 27, 13 URLs, 0 errors. What I've tried Request indexing. On one page, Googlebot came back 2 minutes after I clicked. It's still not indexed. On another, I requested twice and the "last crawled" date never moved. On November 3 I requested five more: three came back "unknown", two "crawled, not indexed". Removing a hidden block. Every page carried a hidden tool panel unrelated to the page topic (about 10 mentions of a different feature). I made it load only when used, and Google recrawled within minutes of my request. No change yet. I'm reading the result on November 13. Backlinks. This is the weak spot. The site has a handful of directory listings and one Dev.to post. I'm now pointing new links at inner pages instead of the homepage. One of the "unknown" pages is save-email-as-pdf , which is part of why I'm writing this. My current guess, with low confidence: a new domain with almost no links, where Google tried the pages, saw little engagement at position 80, and dropped them. But the sibling site is the same age, had a similar handful of links at the time, and kept everything. What I'd like to know If you've had a new site go from partly indexed to almost nothing: Did it come back on its own, and after how long? Was it links that fixed it, or something on the pages? Is there a signal in Search Console or the logs that told you which one it was? I'll post what happens on November 13 either way.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/silkline/crawled-currently-not-indexed-on-12-of-13-pages-what-ive-ruled-out-on-a-3-week-old-site-1ioo

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
