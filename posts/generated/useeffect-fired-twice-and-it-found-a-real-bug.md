---
title: "useEffect Fired Twice and It Found a Real Bug"
slug: "useeffect-fired-twice-and-it-found-a-real-bug"
author: "Rohit Bhadani"
source: "devto_webdev"
published: "Sat, 05 Sep 2026 03:34:36 +0000"
description: "useEffect fired twice, on mount, every single time, in development only. The API call inside it — a POST that created a resource — ran twice, and for about a..."
keywords: "strict, mode, double, bug, effect, useeffect, development, twice"
generated: "2026-09-05T03:53:09.692992"
---

# useEffect Fired Twice and It Found a Real Bug

## Overview

useEffect fired twice, on mount, every single time, in development only. The API call inside it — a POST that created a resource — ran twice, and for about a day we had duplicate records showing up in a table that should have had exactly one insert per page load. The first reaction, and why it was wrong The instinct is to assume a bug — a rerender loop, a missing dependency, something actually broken. React 18's Strict Mode, in development, deliberately mounts, unmounts, and remounts every component once, specifically to surface effects that aren't properly cleaned up. It's not a bug in your code causing a double-fire; it's a bug in your code being caught by a feature built to catch exactly this. useEffect (() => { console . log ( ' mount ' ); // logs twice in dev, once in production const subscription = subscribeToUpdates (); // no cleanup — this is the actual problem Strict Mode is surfacing }, []); Production builds don't do this double-invocation — it's development-only, and specifically Strict-Mode-only, which is why the duplicate inserts we saw locally would eventually have shown up in production too, just less predictably, under a race condition instead of a guaranteed double-fire. Why this is a feature and not noise to suppress An effect that safely tolerates being mounted, torn down, and mounted again is an effect that correctly declares its dependencies and cleans up after itself — which is exactly the property you need for effects to behave correctly under React's concurrent features generally, not just under Strict Mode specifically. The double-invocation in development is a cheap, automatic test for that property, running on every single page load without you writing a test for it. The actual fix useEffect (() => { const subscription = subscribeToUpdates (); return () => subscription . unsubscribe (); // cleanup makes remounting safe }, []); For our specific case — a POST that shouldn't fire twice regardless of mount behavior — the deeper fix was recognizing that a side effect with real-world consequences (creating a database row) needs to be idempotent or explicitly guarded, because "this only runs once" was never a guarantee useEffect actually made, even before Strict Mode started enforcing the point loudly: useEffect (() => { let cancelled = false ; ( async () => { const result = await createResource (); if ( ! cancelled ) setResource ( result ); })(); return () => { cancelled = true ; }; }, []); The cancelled flag doesn't stop the double mount from happening — it stops the second mount's effect from acting on a component that's already been torn down, which is the actual property that matters. Why we caught this before it reached more customers The double-insert bug was already live before Strict Mode's double-fire made us go looking for it, which is the more important point: local development would have looked completely fine without Strict Mode enabled, and the race condition in production might have taken far longer to notice, showing up as an occasional support ticket about duplicate items rather than an obvious, reproducible pattern. We keep Strict Mode on for every environment we can, including staging deployments on disposable Krova Cubes that mirror production traffic patterns, specifically because catching this class of bug before a customer does is worth the minor noise of double-logged console output. I run Krova, so take the staging setup as informed rather than neutral, but enabling Strict Mode everywhere you reasonably can is free advice regardless of host. What I'd check first If an effect behaves differently than expected only in development, check whether you're running React 18+ with Strict Mode before assuming a logic bug. Then check whether the effect has a cleanup function and whether it would still behave correctly if mounted, unmounted, and mounted again in rapid succession — because that's the actual property Strict Mode is testing, and it's a property your effect needs regardless of whether Strict Mode is the thing that exposed its absence.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/rbonweb/useeffect-fired-twice-and-it-found-a-real-bug-5438

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
