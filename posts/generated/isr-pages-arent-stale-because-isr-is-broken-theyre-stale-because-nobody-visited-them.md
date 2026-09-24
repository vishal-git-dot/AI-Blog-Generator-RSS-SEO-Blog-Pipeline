---
title: "ISR pages aren't stale because ISR is broken. They're stale because nobody visited them."
slug: "isr-pages-arent-stale-because-isr-is-broken-theyre-stale-because-nobody-visited-them"
author: "Cherry Harambe"
source: "devto_webdev"
published: "Thu, 24 Sep 2026 21:16:14 +0000"
description: "I run a Next.js content site on Vercel. A few hundred pages, revalidate set to 300 seconds, App Router, nothing exotic. I changed a number on one of the deta..."
keywords: "page, stale, next, you, age, request, old, your"
generated: "2026-09-24T21:21:41.118864"
---

# ISR pages aren't stale because ISR is broken. They're stale because nobody visited them.

## Overview

I run a Next.js content site on Vercel. A few hundred pages, revalidate set to 300 seconds, App Router, nothing exotic. I changed a number on one of the detail pages, waited the five minutes, reloaded, and saw the old number. Waited an hour. Still the old number. My first instinct was that ISR was broken. It wasn't. The behaviour is documented, it's just easy to misread — and the thing that finally made it obvious was reading the response headers instead of guessing. Read the headers before you debug anything else curl -I against any page served by Next.js on Vercel gives you enough to diagnose this in about ten seconds: $ curl -sI https://example.com/some-detail-page | grep -iE 'age|x-vercel-cache|x-nextjs' age: 529343 x-nextjs-prerender: 1 x-nextjs-stale-time: 300 x-vercel-cache: STALE Four things worth knowing: x-nextjs-prerender: 1 — this page was prerendered, so ISR applies to it. If this header is missing, you're looking at a dynamically rendered page and none of the rest matters. x-nextjs-stale-time: 300 — your revalidate value, in seconds. This is the window , not a schedule. x-vercel-cache — HIT means the edge served a fresh copy, STALE means it served an expired copy and kicked off a regeneration, MISS means it had to go to the origin. age — how many seconds ago this cached entry was created. That age: 529343 is just over six days. On a page whose revalidate window is five minutes. Why the numbers don't match ISR regeneration is lazy and request-triggered. There is no background job walking your routes and refreshing them on a timer. What actually happens when a request arrives: Edge checks the cached entry's age against stale-time . If it's inside the window — HIT , serve it, done. If it's outside the window — serve the stale copy immediately, and start a regeneration in the background. The next request, some time later, gets the fresh copy. Read step 3 again. The request that discovers the page is stale does not get fresh content. It gets the old content and pays the cost of triggering the rebuild for whoever comes next. Now apply that to a site with a long tail. Here's what I measured across five routes on the same deployment, all with the same 300-second revalidate: Route age x-vercel-cache / 64s HIT /list 3,945s STALE /index-page 3,945s STALE /detail/one-item 529,343s STALE /about 1,207,507s HIT The homepage is fine — it gets traffic constantly, so it's always within a few minutes of fresh. The detail page is six days old and the about page is fourteen days old, because almost nobody requests them. They aren't being refreshed because the refresh only happens when someone asks. revalidate: 300 does not mean "this page is at most 5 minutes old". It means "once someone requests this page more than 5 minutes after it was cached, start rebuilding it." For a popular page those are nearly the same thing. For a long-tail page they are wildly different. Which is usually fine, until it isn't For most content this is exactly the behaviour you want. Nobody is served a slow page, nobody hits your origin, and pages that matter stay fresh because traffic keeps them fresh. It stops being fine when the content is something people act on. Prices. Availability. Scores and rankings. Anything where a six-day-old page is not merely out of date but actively misleading. On the site I run the detail pages carry ratings and pricing that change, and "correct within five minutes" turned out to be "correct whenever someone last happened to load it". The other place it bites: you ship a fix, check the page, see the old version, and conclude the deploy failed. It didn't. You were the request that triggered the rebuild, and you'll see your change on the next load. Fixing it Use on-demand revalidation for content you control. This is the real answer. When the underlying data changes, tell Next.js explicitly instead of hoping a visitor shows up: import { revalidatePath , revalidateTag } from ' next/cache ' export async function POST ( request : Request ) { const { slug } = await request . json () revalidatePath ( `/detail/ ${ slug } ` ) return Response . json ({ revalidated : true }) } Call it from whatever writes the data — your CMS webhook, your admin action, your import script. The page rebuilds because something changed, which is the correct trigger, rather than because a stranger happened to load it. revalidateTag is the better tool when one change affects several routes. Tag the fetches, invalidate the tag, and every page built from that data goes at once: // in the page await fetch ( url , { next : { tags : [ ' catalogue ' ] } }) // wherever the data changes revalidateTag ( ' catalogue ' ) Don't just lower revalidate . Dropping it from 300 to 60 changes nothing for a page nobody visits — it's still stale until the next request, whenever that is. It only adds load to pages that were already fine. Check age in CI or a cron. A small script that curls your important routes and alerts when age exceeds some multiple of stale-time will catch this long before a user does. The short version x-vercel-cache: STALE with a large age isn't a bug report. It's telling you the page is unvisited. If freshness matters for that route, stop waiting for traffic to trigger the rebuild and revalidate on demand when the data changes.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/cherryslist/isr-pages-arent-stale-because-isr-is-broken-theyre-stale-because-nobody-visited-them-1ic7

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
