---
title: "Turso libSQL vs Cloudflare D1 for an Astro monorepo: the practical difference"
slug: "turso-libsql-vs-cloudflare-d1-for-an-astro-monorepo-the-practical-difference"
author: "MORINAGA"
source: "devto_webdev"
published: "Tue, 09 Jun 2026 03:53:06 +0000"
description: "When I set up the shared ETL database for three Astro SSG directory sites , I had two obvious SQLite-at-the-edge options: Turso (libSQL, runs anywhere) and C..."
keywords: "turso, local, cloudflare, etl, workers, same, you, file"
generated: "2026-06-09T04:03:32.528416"
---

# Turso libSQL vs Cloudflare D1 for an Astro monorepo: the practical difference

## Overview

When I set up the shared ETL database for three Astro SSG directory sites , I had two obvious SQLite-at-the-edge options: Turso (libSQL, runs anywhere) and Cloudflare D1 (SQLite inside Workers). I went with Turso. Here's the practical difference that drove the decision. The local dev problem D1 doesn't solve cleanly Cloudflare D1 is native to the Workers runtime. If you're using Cloudflare Workers for server-side rendering, D1 is the obvious choice — it's edge-collocated with zero config and the env.DB binding is automatic. My setup is different. The sites are static Astro 5 SSG on Cloudflare Pages — no Workers, no server runtime. The ETL pipeline that populates the database runs in GitHub Actions. Nothing in my stack executes inside the Workers environment. To use D1 from GitHub Actions you either use the Cloudflare REST API or the wrangler CLI. Both work, but neither gives you a local SQLite file you can query directly during development. You'd be hitting a remote database for every SELECT during local ETL runs or testing schema changes. Wrangler does have a --local flag that writes to a local D1 file, but the path and format differ from the production D1 setup, so you're managing two different code paths. Why Turso's local fallback changes the calculus The @libsql/client package accepts a url that can be either a libsql:// remote URL or a file:// path: export function getClient (): Client { if ( cached ) return cached ; const url = process . env . TURSO_DATABASE_URL ?? " file:./data/local.db " ; const authToken = process . env . TURSO_AUTH_TOKEN ; cached = createClient ({ url , authToken }); return cached ; } In CI, TURSO_DATABASE_URL is set to the Turso remote URL. On my laptop, the variable isn't set, so the client opens file:./data/local.db — a plain SQLite file on disk. Same @libsql/client package, same query API, same schema. The code path is identical. This means I can run ETL scripts locally and inspect the database with any SQLite viewer. Schema migrations apply with the same applyMigrations() call used in production: export async function applyMigrations ( migrations : readonly string [] ): Promise < void > { const client = getClient (); for ( const sql of migrations ) { await client . execute ( sql ); } } No Docker containers. No Wrangler flags. No separate local-vs-remote code path. The same SQL that creates the models table locally creates it in Turso. What the migration pattern actually looks like Each app defines its own migration array. The run.ts entrypoint for the AI tools ETL calls applyMigrations([CREATE_MODELS_TABLE, CREATE_REVIEWS_TABLE, ...]) at startup. If the table already exists, CREATE TABLE IF NOT EXISTS is a no-op. Idempotent, no migration runner needed. This is the same philosophy as the ETL publish step — the article publish pipeline checks published_urls in the frontmatter before posting, so re-running never double-posts. The database migration check follows the same pattern: check-then-act, idempotent by design. Where D1 would actually win If any part of the stack were running inside Cloudflare Workers — a search endpoint, an API route, a middleware layer — D1 would be the stronger choice. The env.DB binding is faster than a network call to Turso's edge, and you don't need to manage auth tokens for a same-datacenter query. My architecture is fully static because the freshness vs. speed trade-off works in SSG's favor for directory content. No Workers means D1's core advantage doesn't apply. If I add a Cloudflare Worker for site search or a revalidation webhook, I'd reconsider. A hybrid Turso (ETL reads/writes in GitHub Actions) + D1 (Workers queries) setup would be more complex than I want right now. Three things I don't know yet Concurrent write performance. The ETL pipeline has max-parallel: 1 set explicitly in the workflow. Writes are serial and controlled. I haven't tested what happens with concurrent writes, and Turso's concurrent write behavior on the free tier is not something I've stress-tested. I'll know more in 30 days. Migration safety at schema evolution. Adding a nullable column to an existing table is straightforward. Renaming a column or changing a type requires a table rebuild. I haven't had to do either yet. When I do, the applyMigrations() approach will require careful ordering. D1 pricing at scale. Turso's free tier covers 500 databases and 1 billion row reads per month. Cloudflare D1's free tier is similar. At the current scale of three sites with daily ETL runs, neither would cost anything. If traffic grows enough to matter, I'll publish actual numbers — not estimates. The database choice was not the interesting part of this project. The local file fallback is the entire reason I made it; everything else is roughly equivalent between the two for my use case. Part of an ongoing 6-month experiment running three AI-curated directory sites. The technical claims here are real; this article was AI-assisted.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/morinaga/turso-libsql-vs-cloudflare-d1-for-an-astro-monorepo-the-practical-difference-4ic4

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
