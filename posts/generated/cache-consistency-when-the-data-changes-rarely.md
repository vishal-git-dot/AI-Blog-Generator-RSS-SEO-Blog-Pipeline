---
title: "Cache consistency when the data changes rarely"
slug: "cache-consistency-when-the-data-changes-rarely"
author: "aleax h"
source: "devto_python"
published: "Wed, 04 Nov 2026 23:08:45 +0000"
description: "Fee schedules are the ideal shape of data for a cache: small, read constantly, and almost never change. That last property is also what makes them dangerous...."
keywords: "version, you, not, cache, schedule, ttl, one, when"
generated: "2026-11-04T23:27:35.554751"
---

# Cache consistency when the data changes rarely

## Overview

Fee schedules are the ideal shape of data for a cache: small, read constantly, and almost never change. That last property is also what makes them dangerous. A cache that is right for eleven months and silently wrong for three days does not look like a bug — it looks like the exchange changed its rates and nobody updated the site. Here is the cache design I ended up with, and the three failure modes that pushed me there. Failure 1: a TTL is a bet on someone else's release schedule The obvious cache is a TTL. Pick 24 hours, store the schedule, refresh once a day. The problem is that the TTL has to be wrong in one of two directions: Too short , and you hammer an endpoint that returns the same bytes 364 days a year, paying latency and rate limit for nothing. Too long , and every time a venue changes a tier you serve a wrong number until the TTL happens to expire. There is no TTL that is correct, because the event you care about — the schedule changing — is not periodic. A TTL is a bet that the data changes on average every TTL, and fee schedules do not work that way. Failure 2: conditional requests that the API does not support The textbook answer is a conditional request: send If-None-Match with the stored ETag , get a 304 Not Modified when nothing changed, and refresh only when it did. That is exactly what HTTP caching is for, and RFC 9111 spells out the semantics. The catch is that plenty of exchange endpoints return 200 with no ETag and no Last-Modified . You cannot send a validator the server never gave you. So conditional requests become an optimisation you use when they are available, not the mechanism you depend on. Failure 3: several workers, several opinions Once the same schedule is cached in more than one process, you have a consistency problem that no TTL solves. Two workers that refreshed at different times will disagree, and the disagreement is invisible — both are "correct" as far as their own cache is concerned. This is the failure that actually bit me: a page rendered by one worker showed a 0.08% fee and a page rendered by another showed 0.10%, for the same pair, within the same minute. Nobody reports a bug like that as a cache bug. It gets reported as "your site is wrong". What the design looks like instead Three decisions, in order: 1. The schedule is a document with an identity, not a row of numbers. { " exchange " : " okx " , " version " : 7 , " fetched_at " : " 2026-11-04T09:12:00Z " , " content_hash " : " b41c… " , " tiers " : [...], " rounding " : " ceiling " } The version increments only when content_hash changes. That gives you two useful properties: a change is detectable without diffing the whole document, and every derived value can be tied to the version it came from. 2. Fetch unconditionally, compare on hash. You cannot rely on the server telling you what changed, so fetch and compare locally. The cost is one request per refresh interval; the benefit is that "did it change" is answered by data rather than by trust. def refresh ( current ): fresh = fetch () digest = sha256 ( canonical_json ( fresh )) if digest == current [ " content_hash " ]: return current # unchanged, version stays return { ** fresh , " version " : current [ " version " ] + 1 , " content_hash " : digest } 3. Serve stale data with a marker, never silently. When a refresh fails — timeout, rate limit, a 500 — you have two options: serve nothing, or serve the last known schedule with its age attached. Serving nothing makes the product unusable for a transient network problem. Serving silently makes it wrong. So the response carries the version and the age, and the UI shows "based on the schedule from 3 days ago" once the age passes a threshold. A calculator that admits its data is old is more trustworthy than one that does not mention it. The part that makes it testable The property worth testing is not "the cache returns the right value" — it is "a version bump invalidates everything derived from the old version". That is easy to assert and it catches the real bug, which is a computed value that survives a schedule change because something memoised it keyed on the exchange name instead of the version. Two tests cover it: change the schedule, assert the derived fee changes and the version increments; serve from a stale cache, assert the staleness flag is set and the version is the old one, not a fabricated current one. Where this ends up The working version of this — schedules as versioned documents, hash-compared refresh, staleness surfaced in the UI — is what runs the spot fee calculator I use for comparisons: the fee calculator with versioned schedules . The short version: cache the document, not the computation; compare hashes instead of trusting TTLs; and never let a stale number look current. The first two are performance, the third is correctness, and only the third one gets noticed by a user.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/aleax_h_9843add3eb7d8575e/cache-consistency-when-the-data-changes-rarely-34p0

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
