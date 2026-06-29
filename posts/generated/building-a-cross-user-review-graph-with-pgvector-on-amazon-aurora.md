---
title: "Building a cross-user review graph with pgvector on Amazon Aurora"
slug: "building-a-cross-user-review-graph-with-pgvector-on-amazon-aurora"
author: "Jared Lewis"
source: "devto_webdev"
published: "Mon, 29 Jun 2026 04:19:03 +0000"
description: "Every review app is a silo. Yelp reviews places, Amazon reviews its own catalog, Letterboxd reviews film. I wanted to build the opposite: one place where you..."
keywords: "one, embedding, canonical, vector, aurora, pgvector, same, log"
generated: "2026-06-29T04:27:36.038869"
---

# Building a cross-user review graph with pgvector on Amazon Aurora

## Overview

Every review app is a silo. Yelp reviews places, Amazon reviews its own catalog, Letterboxd reviews film. I wanted to build the opposite: one place where you can log and rate anything — a ball-point pen, a burger, a cruise — and have your review pool together with everyone else's. The hard part isn't the form. It's this: when I log "In-N-Out Double-Double" and you log "in n out double double burger," those need to become the same thing so our ratings aggregate. No shared product ID, no barcode, no agreement on spelling. Just two humans describing the same item differently. That's a similarity problem, and I solved it with pgvector running inside Amazon Aurora PostgreSQL (Serverless v2) — the whole app, deployed on Vercel at opinlog.com . The data model is the product Two tables carry the entire idea: user_items — " I logged this, paid $X, rated it 4★." One row per logging event. Personal. canonical_items — "the one shared thing everyone's rows point to." Deduplicated; aggregates everyone's ratings. The matcher's only job is connecting a user_item to the right canonical_item . That edge is the product. Every item carries a 1024-dim embedding. The canonical row's embedding is a vector(1024) , indexed with HNSW for cosine ANN search: // db/schema.ts (Drizzle) embedding : vector ( " embedding " , { dimensions : 1024 }). notNull (), // ... index ( " idx_canon_embedding " ). using ( " hnsw " , t . embedding . op ( " vector_cosine_ops " )), I made the canonical embedding NOT NULL on purpose : a canonical entry must always be matchable, so every creation path supplies a vector and the recompute logic preserves it rather than ever averaging to NULL. "Is this one of these?" — the matcher On every add, I embed the new item and run an approximate-nearest-neighbour search over the canonical catalog. Drizzle doesn't model vector operators, so the query is a raw sql template: SELECT id , name , photo_url , rating_avg , rating_count , 1 - ( embedding <=> : q ) AS similarity FROM canonical_items WHERE embedding IS NOT NULL ORDER BY embedding <=> : q LIMIT 10 ; <=> is pgvector's cosine distance; 1 - distance is similarity. A high-confidence hit auto-suggests as the default ("we think this is it"); otherwise the user sees the top candidates plus a "None of these — create new" escape hatch. Matching is optional and non-blocking : the user_item is saved instantly with canonical_item_id = NULL , and the match just fills it in — at upload time or from a queue later. The base loop (track my own stuff) never has friction. The self-sharpening catalog Here's the part I'm proud of. A canonical item's embedding is the running centroid of its linked members' embeddings. When you link your burger log to mine, the canonical vector moves to the average of both. The more people log the same thing, the sharper and more representative that vector becomes — the catalog improves itself with use. And because "sort by rating" needs to stay fast at scale, the rating aggregates are denormalized onto the canonical row , with rating_avg as a stored generated column: rating_avg real GENERATED ALWAYS AS ( CASE WHEN rating_count > 0 THEN rating_sum :: real / rating_count END ) STORED So the canonical page — the payoff screen — reads one row to show "4.6★ from 11 reviews across strangers," no aggregation query at render time. Why Aurora PostgreSQL specifically I evaluated the three qualifying AWS databases: DynamoDB — great scale story, but no native vector search; I'd have to bolt on OpenSearch. Aurora DSQL — distributed Postgres, but it lacks the pgvector and PostGIS extensions, so it can't do the core matching feature. Aurora PostgreSQL — does vectors (pgvector), geo (PostGIS), and relations in one engine . One connection, one query planner, transactional joins between "the vector match" and "the rating rollup." That last point is the whole reason this was buildable by one person on a deadline. The matcher result and the relational aggregation live in the same database, so linking an item and recomputing its canonical's centroid + ratings is a single transaction — not a dance between a vector store and an RDBMS. The stack Next.js 16 (App Router, Server Actions) on Vercel → Aurora PostgreSQL Serverless v2 via pg /Drizzle, with pgvector + PostGIS + pg_trgm . Embeddings come from Amazon Bedrock (more on that in the next post). Swapping local Docker Postgres for Aurora was a one-line DATABASE_URL change — same driver, same SQL. The result is a universal, cross-user review graph for literally anything, and the magic is one line of SQL: ORDER BY embedding <=> :q . Built for the H0 Hackathon ("Hack the Zero Stack with Vercel and AWS Databases"). I created this content for the purposes of entering this hackathon. #H0Hackathon

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/jareddlewis/building-a-cross-user-review-graph-with-pgvector-on-amazon-aurora-7ni

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
