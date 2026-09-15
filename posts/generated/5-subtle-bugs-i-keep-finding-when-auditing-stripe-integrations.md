---
title: "5 subtle bugs I keep finding when auditing Stripe integrations"
slug: "5-subtle-bugs-i-keep-finding-when-auditing-stripe-integrations"
author: "SaaSFactory"
source: "devto_python"
published: "Tue, 15 Sep 2026 15:53:56 +0000"
description: "I've reviewed a handful of production Stripe integrations lately (mostly Flask/Django/Express repos), and the same handful of bugs keep showing up. None of t..."
keywords: "stripe, request, check, you, session, price, integrations, these"
generated: "2026-09-15T16:40:33.687441"
---

# 5 subtle bugs I keep finding when auditing Stripe integrations

## Overview

I've reviewed a handful of production Stripe integrations lately (mostly Flask/Django/Express repos), and the same handful of bugs keep showing up. None of these throw an obvious error in dev — they just quietly cost someone money or let a bad request through. 1. Webhook signature check with the wrong body Frameworks that auto-parse JSON often hand you the re-serialized body, not the raw bytes Stripe signed. stripe.Webhook.construct_event needs the exact raw payload. If you're reading request.json and re-dumping it before verifying, the signature check will fail for some payloads and silently pass for others depending on key ordering. # wrong: re-serialized body, key order not guaranteed payload = json . dumps ( request . get_json ()) # right: raw bytes exactly as received payload = request . get_data () 2. No timestamp tolerance check (or one that's too loose) Stripe signs with a timestamp and expects you to reject anything older than ~5 minutes to block replay attacks. A lot of handlers verify the HMAC and stop there, skipping the timestamp check entirely, or they've bumped the tolerance to something huge (I've seen 24 hours) to work around clock drift in dev. 3. Handling checkout.session.completed without an idempotency guard Stripe retries webhooks that don't return 2xx fast enough. If your handler fulfills the order (ships digital goods, grants access) without checking whether you've already processed that event.id , a slow database write plus a retry means double fulfillment. 4. Mixing test and live price/product IDs A price_... or prod_... ID hardcoded from a test session ends up in a config file, then deployed to production. The checkout session creation fails with a cryptic "No such price" error, or worse, silently falls back to a default price if there's a try/except swallowing it. 5. Trusting amount_total from the client Some integrations pass the amount from the frontend into checkout session creation instead of only ever referencing a price_id created server-side. That's a direct path to a customer setting their own price. If any of these sound familiar, I put together a small automated audit ($29, instant report, no subscription) that checks a repo against these plus a few more rules: https://buy.stripe.com/8x214m0WFeOudyzeVW7IY04 Happy to also just answer questions about Stripe webhook handling in the comments.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/saasfactory/5-subtle-bugs-i-keep-finding-when-auditing-stripe-integrations-1h61

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
