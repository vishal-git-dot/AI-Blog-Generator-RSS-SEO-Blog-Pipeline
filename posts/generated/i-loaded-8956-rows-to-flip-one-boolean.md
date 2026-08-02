---
title: "I Loaded 8,956 Rows to Flip One Boolean"
slug: "i-loaded-8956-rows-to-flip-one-boolean"
author: "Sukhpinder Singh"
source: "devto_webdev"
published: "Sun, 02 Aug 2026 08:13:03 +0000"
description: "Every system I've worked on has a nightly job shaped like this: archive delivered orders older than 90 days. Mine was four lines of EF Core that had survived..."
keywords: "one, rows, orders, where, them, isarchived, sql, same"
generated: "2026-08-02T08:30:38.167106"
---

# I Loaded 8,956 Rows to Flip One Boolean

## Overview

Every system I've worked on has a nightly job shaped like this: archive delivered orders older than 90 days. Mine was four lines of EF Core that had survived a dozen code reviews, several of them mine. Then I ran it with SQL logging switched on and watched it haul 8,956 complete rows out of the database so it could write 8,956 booleans back. Nobody read those rows. They existed for the length of a foreach and died. I wanted the actual bill, not a feeling, so I measured it. The habit The demo table is 20,000 orders in SQLite, seeded with Random(42) so every run produces the same data. 8,956 of them match the archive predicate. A DbCommandInterceptor counts every command EF Core sends, timings are the median of 5 rounds after a warmup, and allocations come from GC.GetAllocatedBytesForCurrentThread . EF Core 10, Release build, small Linux container, in-process SQLite. Not a lab — I care about the ratios. Here's the version of the job I'd been writing since EF Core 1: var stale = ctx . Orders . Where ( o => o . Status == OrderStatus . Delivered && o . PlacedAtUtc < cutoffUtc ) . ToList (); foreach ( var order in stale ) order . IsArchived = true ; ctx . SaveChanges (); It reads like exactly what you mean, which is why it survives code review. And for five rows it's fine. Here's what it costs for 8,956: [A: load entities + SaveChanges] rows touched : 8,956 SQL commands : 8,957 median time : 355.3 ms allocated : 75,143 KB That command count isn't a typo. One SELECT to fetch the rows, then one UPDATE per order — the SQLite provider ships each as its own command. SQL Server would batch them into multi-statement round trips, which helps, but EF still generates, ships, and executes one UPDATE statement per row. WHERE "Id" = @p0 , 8,956 times. The 75 MB is the part that surprised me more. Materializing 8,956 entities doesn't cost that much on its own. Change tracking does: EF snapshots every property of every tracked entity so SaveChanges can diff them later. Two full copies of the table's matching slice, held in memory, to change one column whose new value I already knew before the query ran. The one-statement version EF Core has had a set-based answer since EF 7, and I'd been treating it as an exotic tool instead of the obvious one: var archived = ctx . Orders . Where ( o => o . Status == OrderStatus . Delivered && o . PlacedAtUtc < cutoffUtc ) . ExecuteUpdate ( s => s . SetProperty ( o => o . IsArchived , true )); [B: ExecuteUpdate] rows touched : 8,956 SQL commands : 1 median time : 10.6 ms allocated : 68 KB Same predicate, same 8,956 rows changed, one command. This is the SQL the interceptor caught: UPDATE "Orders" AS "o" SET "IsArchived" = @ p WHERE "o" . "Status" = 1 AND "o" . "PlacedAtUtc" < @ cutoffUtc 33x faster and roughly 1,100x fewer allocations, and remember my numbers have no network in them — SQLite is in-process. On a real connection, strategy A pays latency per round trip while strategy B still pays it once. The gap you'd see in production is wider than mine, not narrower. There's no magic here, and that's sort of the point. The database could always do this in one statement. The load-modify-save pattern was me routing a one-line UPDATE through a full object graph because that's the shape the framework made comfortable. Where it bites ExecuteUpdate goes around the change tracker entirely. That's the whole trick, and it's also the sharp edge: var tracked = ctx . Orders . First ( o => o . Status == OrderStatus . Delivered && o . PlacedAtUtc < cutoffUtc ); ctx . Orders . Where ( o => o . Status == OrderStatus . Delivered && o . PlacedAtUtc < cutoffUtc ) . ExecuteUpdate ( s => s . SetProperty ( o => o . IsArchived , true )); == the stale-tracker gotcha == tracked entity says IsArchived = False database says IsArchived = True The tracked entity never hears about the update. If code later in that request reads tracked.IsArchived , it gets a confident wrong answer, and if SaveChanges runs afterwards for an unrelated edit, nothing corrects it. Mixing tracked work and set-based updates on the same data in the same context is where the bugs live. When I still load the entities There are real reasons to keep the old pattern, and they're worth naming rather than waving at. If flipping the flag triggers per-entity behavior — domain events, an audit interceptor on SaveChanges , business rules that can veto individual rows — ExecuteUpdate skips all of it. It ignores optimistic concurrency tokens too: last write wins, silently. And each ExecuteUpdate runs as its own implicit transaction, so if the job needs to be atomic with other changes, you're wrapping it in an explicit one yourself. My rule after this experiment, stated as the opinion it is: load-modify-save is for entities with behavior, and it earns its cost a handful of rows at a time. Any query that ends in "load them all, set one property, save" is a maintenance job, and maintenance jobs speak SQL. Let them. The delete side is the same story with a shorter name. Purging old cancelled orders went from a fetch-and-remove loop to: var purged = ctx . Orders . Where ( o => o . Status == OrderStatus . Cancelled && o . PlacedAtUtc < purgeCutoff ) . ExecuteDelete (); 2,086 rows gone in 23.7 ms, one command, nothing materialized. Full runnable sample: https://github.com/ssukhpinder/dev-to-code-samples/tree/main/019-efcore-execute-update Got a nightly job that fetches everything it's about to overwrite? Run it with an interceptor counting commands and tell me your number in the comments — I'll admit mine was embarrassing for years. — still benchmarking things nobody asked me to, 8,956 statements at a time

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ssukhpinder/i-loaded-8956-rows-to-flip-one-boolean-596e

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
