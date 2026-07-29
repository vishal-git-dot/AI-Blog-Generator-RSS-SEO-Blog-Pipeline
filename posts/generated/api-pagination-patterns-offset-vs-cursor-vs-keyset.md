---
title: "API Pagination Patterns: Offset vs Cursor vs Keyset"
slug: "api-pagination-patterns-offset-vs-cursor-vs-keyset"
author: "Stack Horizon"
source: "devto_python"
published: "Wed, 29 Jul 2026 08:00:19 +0000"
description: "Why Pagination Matters If you've ever built an API endpoint that returns a list, you've probably faced the question: what happens when the list has 10,000 it..."
keywords: "items, cursor, pagination, offset, you, page, get, order"
generated: "2026-07-29T08:48:13.034035"
---

# API Pagination Patterns: Offset vs Cursor vs Keyset

## Overview

Why Pagination Matters If you've ever built an API endpoint that returns a list, you've probably faced the question: what happens when the list has 10,000 items? Returning them all at once is a recipe for slow responses, memory exhaustion, and angry mobile users. Pagination is the answer, but not all pagination is created equal. Let's look at the three most common patterns: offset, cursor, and keyset pagination. Offset Pagination (The Classic) This is the simplest approach. The client sends page and per_page (or limit and offset ), and the server skips that many rows. # Flask example @app.route ( ' /items ' ) def get_items (): page = request . args . get ( ' page ' , 1 , type = int ) per_page = request . args . get ( ' per_page ' , 20 , type = int ) offset = ( page - 1 ) * per_page items = db . execute ( ' SELECT * FROM items ORDER BY id LIMIT ? OFFSET ? ' , ( per_page , offset )) return jsonify ( items ) Pros: Easy to implement and understand. Works with any database, even in-memory lists. Allows jumping to any page directly. Cons: Performance degrades with large offsets. The database still scans all skipped rows. On a table with 1 million rows, OFFSET 999980 is painfully slow. Inconsistent results if rows are inserted/deleted. If a new row is added between requests, the same page might show different items. Cursor Pagination (The Reliable One) Instead of page numbers, the client passes a cursor (an opaque string) that points to the last item seen. The server returns items after that cursor. @app.route ( ' /items ' ) def get_items (): cursor = request . args . get ( ' cursor ' ) per_page = request . args . get ( ' per_page ' , 20 , type = int ) if cursor : # Decode cursor (e.g., base64 encoded ID) last_id = decode_cursor ( cursor ) items = db . execute ( ' SELECT * FROM items WHERE id > ? ORDER BY id LIMIT ? ' , ( last_id , per_page )) else : items = db . execute ( ' SELECT * FROM items ORDER BY id LIMIT ? ' , ( per_page ,)) next_cursor = encode_cursor ( items [ - 1 ][ ' id ' ]) if len ( items ) == per_page else None return jsonify ({ ' items ' : items , ' next_cursor ' : next_cursor }) Pros: Fast and stable. Uses indexed columns (like id ) to filter, so it scales to any offset. Consistent. New rows don't shift pages because you always move forward from a specific point. Real-time friendly. No duplicate or missed items when data changes. Cons: No random page access. You can't jump to page 5; you must traverse sequentially. Cursor encoding adds complexity. You need to encode/decode the cursor (base64 is common). Only works with sortable, unique fields. You need a column to order by (usually id or created_at ). Keyset Pagination (The SQL Optimized) Similar to cursor, but uses the actual column values from the last row instead of an opaque token. Often used with composite keys. @app.route ( ' /items ' ) def get_items (): last_id = request . args . get ( ' last_id ' , type = int ) last_created = request . args . get ( ' last_created ' ) per_page = request . args . get ( ' per_page ' , 20 , type = int ) if last_id and last_created : items = db . execute ( ''' SELECT * FROM items WHERE (created_at, id) > (?, ?) ORDER BY created_at, id LIMIT ? ''' , ( last_created , last_id , per_page )) else : items = db . execute ( ' SELECT * FROM items ORDER BY created_at, id LIMIT ? ' , ( per_page ,)) return jsonify ({ ' items ' : items }) Pros: Best performance. Uses database indexes efficiently, no OFFSET at all. No cursor encoding needed. The client just passes raw column values. Cons: Tied to sort order. If you change the sort, the keyset changes. Requires exposing column values. The client needs to know the last id or timestamp , which might be sensitive. No random access. Like cursor pagination. When to Use What Offset pagination: Use for small datasets (under 10k rows) or when random page access is critical (e.g., admin panels). Cursor pagination: Use for large, dynamic datasets where consistency matters (e.g., social feeds, activity logs). Keyset pagination: Use when you need maximum performance and control over the sort order (e.g., real-time dashboards). A Practical Compromise Sometimes you can combine both: offer offset-based pagination for the first few pages (where performance is fine) and switch to cursor-based once the offset passes a threshold. But in most modern APIs, cursor pagination is the go-to choice. It's reliable, scalable, and the extra complexity is minimal. Final Thought Whichever pattern you choose, document it clearly. Your API consumers will thank you when they don't have to guess how to get the next page. And always test with large datasets to catch performance issues early.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/stackhorizon/api-pagination-patterns-offset-vs-cursor-vs-keyset-30gl

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
