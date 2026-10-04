---
title: "Your Database Is Small. That Doesn’t Mean Your Queries Are Fast"
slug: "your-database-is-small-that-doesnt-mean-your-queries-are-fast"
author: "Flaviu Z"
source: "devto_webdev"
published: "Sun, 04 Oct 2026 20:43:38 +0000"
description: "“My database is only 50 MB. Why is my API slow?” It's an easy assumption to make. Small database = fast database. Unfortunately, database size tells you surp..."
keywords: "database, you, your, query, can, fast, queries, application"
generated: "2026-10-04T21:07:13.180940"
---

# Your Database Is Small. That Doesn’t Mean Your Queries Are Fast

## Overview

“My database is only 50 MB. Why is my API slow?” It's an easy assumption to make. Small database = fast database. Unfortunately, database size tells you surprisingly little about how quickly a particular request will execute. You can have gigabytes of data and extremely fast queries. You can also have a tiny database and an endpoint that takes two seconds. The interesting question isn't: How big is the database? It's: What are you asking the database to do? One request might actually be 50 queries Imagine loading a page containing 50 products. You query the products: SELECT * FROM products LIMIT 50; Fast. Then, for every product, your application separately requests the seller. Suddenly: 1 query for products 50 queries for sellers = 51 queries You haven't got a large database. You've got an inefficient access pattern. This is the classic N+1 query problem. Depending on your ORM, it can also be surprisingly easy to create without noticing. Indexes matter Suppose you frequently search users by email: SELECT * FROM users WHERE email = ?; With a suitable index, the database can locate matching records efficiently. Without one, it may need to examine far more data. As your dataset grows, the difference becomes increasingly noticeable. But adding indexes everywhere isn't the solution either. Indexes consume storage and have a cost when writing data. The goal is to index based on actual query patterns. Your database may not even be the bottleneck Let's say an API endpoint takes 800ms. It's tempting to blame PostgreSQL or MySQL. But maybe the query takes 40ms. The rest could be: authentication, external API calls, serialization, application logic, network latency, file operations, or several sequential operations. Optimizing a 40ms database query down to 20ms won't fix an 800ms endpoint. Measure before optimizing. Sequential requests add up Consider: Get user 100ms Get orders 150ms Get messages 200ms Get statistics 180ms If these operations unnecessarily run sequentially, the user could wait around 630ms. If independent operations can safely run concurrently, the experience may be very different. The individual operations weren't necessarily slow. The architecture made them slow together. Location matters too Imagine: User → US Application server → Europe Database → Europe Even if your database query is extremely fast, the user still has to communicate with infrastructure thousands of kilometers away. Now imagine the frontend makes several sequential requests. Network latency gets multiplied by application design. This is one reason a site can feel fast for the developer and slow for users elsewhere. Cache what makes sense Not everything needs to hit the database every time. Some information changes constantly. Other information might remain identical for hours. If something is expensive to calculate and frequently requested, caching may help significantly. But caching everything introduces its own problems. Now you have to think about invalidation and stale data. As usual, the answer isn't: “Use caching.” It's: “Understand what you're caching and why.” Look at the query plan When a query becomes suspicious, don't immediately start rewriting your entire backend. Ask the database what it's doing. For PostgreSQL, EXPLAIN and EXPLAIN ANALYZE can show how the database plans and executes a query. That can reveal things like sequential scans, expensive joins, unexpected row counts, and inefficient execution plans. It's much better than optimizing based on intuition. Measure first Before changing infrastructure, collect some basic numbers: Request duration: 920ms Database: 85ms External API: 610ms Application logic: 40ms Other/network: 185ms Now the problem is obvious. Changing database providers probably won't save you. That 610ms external request deserves your attention. Small doesn't mean fast Performance isn't determined by how many megabytes your database consumes. It depends on: queries + indexes + application logic + network + architecture + workload So the next time an API feels slow, don't start with: “Do I need a bigger server?” Start with: “Where are those milliseconds actually going?” That question will usually save you a lot more time — and potentially a lot more money.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ioan_flaviuzsoldos_a3bf4/your-database-is-small-that-doesnt-mean-your-queries-are-fast-1130

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
