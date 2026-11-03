---
title: "The health check returned 200 while every buyer submission failed"
slug: "the-health-check-returned-200-while-every-buyer-submission-failed"
author: "Manh Liem"
source: "devto_webdev"
published: "Tue, 03 Nov 2026 22:57:30 +0000"
description: "A buyer page returned 200. A health check read that status, declared the service healthy, and reported success every five minutes for a full evening. In the ..."
keywords: "check, origin, page, buyer, every, same, one, request"
generated: "2026-11-03T23:03:46.607149"
---

# The health check returned 200 while every buyer submission failed

## Overview

A buyer page returned 200. A health check read that status, declared the service healthy, and reported success every five minutes for a full evening. In the same window, every submission from that page failed. The page was served by a CDN edge. The submission went to an origin tunnel that had died hours earlier. Two different things behind one status code A GET to a cached HTML page and a POST to a JSON API travel different paths. The CDN can answer the GET from cache with the last good copy, long after the origin stopped responding. The POST has no cache to fall back on, so it reaches the origin and returns whatever the origin returns. When the origin is a dead tunnel, the edge returns a 1033 error page. So the same hostname answered 200 to the check and an error page to the buyer. Both responses were accurate about their own request. The check measured the wrong request. Why the shortcut got added An earlier incident had the reverse shape. The origin was dead and the health check was probing a path that the edge answered statically, so the check said healthy while the buyer page was down. The fix was to probe the buyer page instead, because it depends on the origin. That fix was correct about which path to probe and wrong about which method to use. A cached GET does not prove the origin is up. The check improved and stayed broken at the same time. The check that actually proves it A POST that the origin has to answer with a specific value. In this case, a JSON-RPC tools list that must contain a named tool. That request cannot be satisfied from cache, cannot be satisfied by the edge, and cannot be satisfied by a dead tunnel. Either the origin answered with the expected content or it did not. One POST every five minutes costs nothing and covers the exact path a buyer takes. A GET to the same page would have cost the same and proved nothing. The general rule A status code is evidence about one request, not about a service. When a health check is written, the question to ask is not "does this endpoint return 200" but "is this the same request a customer makes". If the customer sends a POST with a body and the check sends a GET, the check is measuring a different system. Caches make this failure mode quiet. A dead origin produces a cached 200 that looks exactly like a healthy one, and every log line agrees with it. There is no anomaly to alert on until someone reads the buyer's error page. The cost of getting it wrong Five real submissions arrived from three separate networks. Every one of them failed at the origin. The health check reported success throughout, so nothing escalated. The traffic was real, the demand was real, and the product was down. The fix took one line. Finding it required reading the buyer's request instead of the checker's response.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/llmrt/the-health-check-returned-200-while-every-buyer-submission-failed-543b

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
