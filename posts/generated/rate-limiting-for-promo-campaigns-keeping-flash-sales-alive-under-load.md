---
title: "Rate Limiting for Promo Campaigns: Keeping Flash Sales Alive Under Load"
slug: "rate-limiting-for-promo-campaigns-keeping-flash-sales-alive-under-load"
author: "Kadokey"
source: "devto_webdev"
published: "Sat, 10 Oct 2026 05:04:49 +0000"
description: "Promo drops are the sharpest traffic spike a digital storefront will ever see. A campaign that converts a few hundred checkouts a day can suddenly face tens ..."
keywords: "per, code, promo, limits, argv, bucket, tokens, rate"
generated: "2026-10-10T05:17:32.828308"
---

# Rate Limiting for Promo Campaigns: Keeping Flash Sales Alive Under Load

## Overview

Promo drops are the sharpest traffic spike a digital storefront will ever see. A campaign that converts a few hundred checkouts a day can suddenly face tens of thousands of requests in the first minute after a code goes live. If your rate limiting was designed for average traffic, the promotion itself becomes a self-inflicted DDoS: legitimate buyers get errors, bots hoard inventory, and the campaign ends in a support inbox full of complaints. At Kadokey , where promo campaigns run regularly across digital gift cards and top-ups, we treat rate limiting as campaign infrastructure, not an afterthought. Here is the model we use. Why promo traffic is different Normal traffic grows gradually. Promo traffic does not: Thundering herd. Everyone arrives at once, the minute a code is announced on social media or in a newsletter. Bots and code-stuffing. Automated clients try thousands of code combinations per minute against your /apply-promo endpoint. Code sharing. A code meant for limited use ends up on deal forums, multiplying redemption attempts far beyond the plan. A single global requests-per-second cap cannot distinguish a legitimate buyer retrying checkout from a bot brute-forcing codes. You need limits that understand what is being requested. Layer your limits We apply limits at four layers, each with a different job: Edge / CDN. Per-IP request caps and bot management absorb the raw flood before it reaches your origin. This is where you stop dumb volumetric abuse. API gateway. Per-route limits on expensive endpoints: /apply-promo , /checkout , /validate-code . These routes do real database work, so they deserve tighter budgets than static pages. Application. Per-user and per-code budgets. A signed-in user gets a generous but bounded number of promo attempts per minute; a promo code gets a maximum number of validation attempts per minute across all users. Payment. The strictest limits of all at money movement: order creation and payment capture. Abuse here costs real money. Choose the right algorithm per layer Fixed window counters are simple but allow boundary bursts: a full window's quota at 11:59:59 plus another at 12:00:00. Sliding window counters smooth this out and are a good default for /apply-promo . Token bucket allows controlled bursts, which fits checkout well: buyers should be able to move fast once, but not hammer retries. Leaky bucket smooths output to a constant rate, which is useful for downstream webhooks and email receipts during a spike. For promo codes specifically, per-code attempt limits matter more than per-IP ones. Cap both redemptions per code and validation attempts per user per code. That single rule kills most brute-forcing without hurting real buyers. A practical token bucket in Redis A minimal Lua-scripted token bucket keeps the check atomic: -- KEYS[1]: bucket key, ARGV[1]: capacity, -- ARGV[2]: refill rate per sec, ARGV[3]: now (unix time) local bucket = redis . call ( 'HMGET' , KEYS [ 1 ], 'tokens' , 'ts' ) local tokens = tonumber ( bucket [ 1 ]) or tonumber ( ARGV [ 1 ]) local ts = tonumber ( bucket [ 2 ]) or tonumber ( ARGV [ 3 ]) local elapsed = math.max ( 0 , tonumber ( ARGV [ 3 ]) - ts ) tokens = math.min ( tonumber ( ARGV [ 1 ]), tokens + elapsed * tonumber ( ARGV [ 2 ])) if tokens < 1 then redis . call ( 'HMSET' , KEYS [ 1 ], 'tokens' , tokens , 'ts' , ARGV [ 3 ]) redis . call ( 'EXPIRE' , KEYS [ 1 ], 120 ) return 0 end redis . call ( 'HMSET' , KEYS [ 1 ], 'tokens' , tokens - 1 , 'ts' , ARGV [ 3 ]) redis . call ( 'EXPIRE' , KEYS [ 1 ], 120 ) return 1 Key the bucket as promo:{code}:{userId} for per-user-per-code limits, and promo:{code}:global for the code-wide attempt budget. One round trip, atomic, no race conditions. Degrade gracefully Limits only work if the failure mode is kind: Return 429 with a Retry-After header , never a 500. Clients (and your own frontend) can back off intelligently. Put checkout behind a waiting room or queue during mega-drops instead of letting the database fall over. Cache promo validation reads. Code definitions change rarely; serve them from memory and reserve the database for redemption writes. Measure the campaign, not just the servers During a drop, watch four numbers: 429 rate per endpoint, p99 latency on /apply-promo , redemption conversion (validations to completed orders), and bot-block rate at the edge. If 429s spike but conversion holds, your limits are doing their job. If conversion drops, you are throttling real buyers: loosen the per-user buckets first. Closing Rate limiting for promos is not about saying no; it is about making sure the yeses go to real customers. Layer your limits, budget per code as well as per user, fail with 429s instead of 500s, and measure conversion through the spike. If you want to see what this looks like from the buyer side, browse the current gift card and top-up deals at kadokey.com - every campaign there runs behind exactly this kind of layered limiting.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/kadokey/rate-limiting-for-promo-campaigns-keeping-flash-sales-alive-under-load-1i8g

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
