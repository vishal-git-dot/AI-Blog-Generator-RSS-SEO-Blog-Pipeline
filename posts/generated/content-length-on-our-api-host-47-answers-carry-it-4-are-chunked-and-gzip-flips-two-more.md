---
title: "Content-Length on Our API Host: 47 Answers Carry It, 4 Are Chunked, and gzip Flips Two More"
slug: "content-length-on-our-api-host-47-answers-carry-it-4-are-chunked-and-gzip-flips-two-more"
author: "OnePassApps"
source: "devto_webdev"
published: "Tue, 10 Nov 2026 22:54:17 +0000"
description: "I work on OnePassApps , the team behind app.onepassapps.com. This post is about something our own API host does that I had never measured as a set: how it te..."
keywords: "api, length, content, chunked, one, bytes, routes, body"
generated: "2026-11-10T23:03:02.010651"
---

# Content-Length on Our API Host: 47 Answers Carry It, 4 Are Chunked, and gzip Flips Two More

## Overview

I work on OnePassApps , the team behind app.onepassapps.com. This post is about something our own API host does that I had never measured as a set: how it tells a client how long the answer is. Everything here was measured on 10 November 2026, from outside the browser, signed out, plain HTTPS, no cookies and no JavaScript. The short version Our API host uses two different ways of telling the client how long the body is, and the split falls on the size of the answer. 47 of the 51 answers I fetched carry a Content-Length header. The other 4 arrive chunked, with no length at all. Route Body bytes How the length is sent /api 104 Content-Length: 104 /api/auth/config 371 Content-Length: 371 /api/health 410 Content-Length: 410 /api/runtime 471 Content-Length: 471 the 43 single-record product routes 374 to 464 Content-Length, and the number matches the body exactly /api/config/feature-flags 1,771 Transfer-Encoding: chunked /api/plans 4,020 Transfer-Encoding: chunked /api/voting 4,146 Transfer-Encoding: chunked /api/products 15,650 Transfer-Encoding: chunked The boundary sits between two measured values: the largest body that carried Content-Length was 471 bytes, and the smallest chunked body was 1,771 bytes. I did not find the exact byte where the server switches, so I am not claiming one. It is the uncompressed size that decides Here is the part that surprised me. I asked the same routes for a compressed copy, with Accept-Encoding: gzip. /api/runtime answered 471 bytes with a Content-Length of 471. Asked for gzip it answered 299, 301 and 301 bytes across three fetches, and switched to chunked. /api/health answered 410 bytes with a Content-Length of 410. Asked for gzip it answered 288, 289 and 287 bytes, chunked. So the smaller the body gets, the more likely it is to arrive with no length at all. The rule is not "small answers get a length". The rule is closer to: an answer that is produced in one piece and can be held in memory gets a length, and anything the server streams gets chunked. For the record, the two big routes stayed chunked when compressed: /api/config/feature-flags came back at 520, 523 and 524 gzipped bytes, and /api/products at 1,776, 1,777 and 1,778. A HEAD request still costs a token A HEAD request to our API routes answers 200 with a zero-byte body, the JSON content type and no length header at all. That part is not new. What is new to me is what it costs. I sent five HEAD requests to /api/products in a row, and the remaining-counter header fell by exactly one each time: 71, then 70, then 69, then 68, then 67. The next GET answered 66. A HEAD returns nothing, and it still spends a request from the same 120-request budget that a full GET spends. If a client is probing a list of routes to see which ones exist, those probes are billed like reads. What this measurement does not cover One build, one day, one network, one region, plain HTTPS, no cookies, no JavaScript, no session and no sign-in. I fetched 51 URLs: the 8 fixed routes under /api and the 43 single-record product routes the catalogue lists. I did not fetch the route behind a signed-in view. I sent one request per URL for the census and three requests each on the eight fixed routes to check the split was stable. I read the headers the server sent; there is a CDN in front of both hosts and I cannot see how it stores or rewrites what it receives. And every number here is a snapshot of one build on one day. Try it yourself The home page is where all nine apps are listed, and every one of them runs in your browser tab: the OnePassApps home page Every app and studio has a plain-language guide with its limits and its tool list: the OnePassApps guides

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/onepassapps/content-length-on-our-api-host-47-answers-carry-it-4-are-chunked-and-gzip-flips-two-more-28mi

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
