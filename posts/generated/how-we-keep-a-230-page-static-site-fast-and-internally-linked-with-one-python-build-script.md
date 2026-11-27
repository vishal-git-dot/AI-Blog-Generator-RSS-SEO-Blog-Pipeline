---
title: "How we keep a 230-page static site fast and internally linked with one Python build script"
slug: "how-we-keep-a-230-page-static-site-fast-and-internally-linked-with-one-python-build-script"
author: "DiziGoo Digital"
source: "devto_python"
published: "Fri, 27 Nov 2026 07:29:11 +0000"
description: "Our agency site has about 230 pages: services, software, guides and city pages. Instead of a CMS, one Python script builds every page as plain HTML. Here is ..."
keywords: "page, pages, every, dizigoo, build, script, software, links"
generated: "2026-11-27T07:44:07.267928"
---

# How we keep a 230-page static site fast and internally linked with one Python build script

## Overview

Our agency site has about 230 pages: services, software, guides and city pages. Instead of a CMS, one Python script builds every page as plain HTML. Here is what worked for speed and for search. 1. Compress images at build time The build converts every JPG and PNG to WebP (quality around 74, lower for blog photos) and rewrites the HTML to point at the WebP files. Pages stay light without any manual work. 2. Generate internal links from the page list Orphan pages are easy to create when you add pages by hand. After all pages are built, the script groups them (services, software, guides, cities) and appends a small related-links block to each page: the next few siblings in the same group, a few pages from other groups, and the key hubs. A quick check afterwards counts inbound links per page, and every page now has at least five. 3. Keep the sitemap honest The XML sitemap and the human sitemap page come from the same page list, so the counts match. Queued posts that are not published yet stay out of both until they go live. 4. Verify after every deploy We fetch a handful of live URLs with curl and grep for the new markup, then submit changed URLs through IndexNow and Search Console. It takes a minute and catches stale caches. If you are curious how the result looks, our local pages for Pilibhit and Bareilly are here: https://dizigoo.com/locations/india/pilibhit/ and https://dizigoo.com/locations/india/bareilly/ . We are DiziGoo, a digital marketing and software team from Uttar Pradesh: https://dizigoo.com/

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dizigoo_digital_933f500cf/how-we-keep-a-230-page-static-site-fast-and-internally-linked-with-one-python-build-script-1a55

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
