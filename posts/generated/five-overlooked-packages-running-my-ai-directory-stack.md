---
title: "Five overlooked packages running my AI directory stack"
slug: "five-overlooked-packages-running-my-ai-directory-stack"
author: "MORINAGA"
source: "devto_webdev"
published: "Tue, 09 Jun 2026 03:54:02 +0000"
description: "The interesting parts of a project are not always the AI model or the hosting platform. This week I spent time reading source code for five dependencies that..."
keywords: "etl, but, typescript, client, yaml, week, turso, tsx"
generated: "2026-06-09T04:03:32.527995"
---

# Five overlooked packages running my AI directory stack

## Overview

The interesting parts of a project are not always the AI model or the hosting platform. This week I spent time reading source code for five dependencies that sit quietly in my package.json files. None of them are trending. All of them are load-bearing. My stack is Astro 5 SSG + Turso libSQL + GitHub Actions cron + Claude Haiku 4.5. Three sites: Top AI Tools, Find Games Like, Open Alternative To. Seven weeks in, still under 400 total pageviews, but the infrastructure is solid enough that I can focus on content rather than firefighting. tsx — TypeScript without the build ceremony tsx by Hiroki Osame is how I run every ETL script in the monorepo. The command tsx src/etl/run.ts just works — no tsconfig fiddling, no ts-node --esm flags, no separate compile step. Under the hood it uses esbuild, which means startup is fast enough that a five-second cron warm-up doesn't matter. What surprised me when I read the repo: tsx strips types with esbuild rather than the TypeScript compiler, so it doesn't type-check. That's intentional. For ETL scripts where I want pnpm typecheck to catch structural errors at CI time but not slow down the hot path, this is exactly the right tradeoff. The README calls this out clearly. I wish I'd read it three weeks ago instead of assuming tsx did full type checking. Pagefind — static full-text search with no server Pagefind runs as my postbuild step: pagefind --site dist --output-subdir _pagefind . It crawls the built HTML, creates a compressed WASM index, and the client-side JS loads only the chunk it needs per query. The result is search that works on a static Vercel or Cloudflare Pages deploy with zero additional infrastructure. I read through the index format docs this week. The segment files are stored as zstd-compressed binary blobs, and the JS client fetches them lazily based on the query prefix. For three sites each under 2,000 pages, the index stays under 500 KB total. The PageFind UI component is optional — I replaced it with a plain <input> that calls the JS API directly so I could control the result rendering in Astro components. Crawlee — TypeScript scraping with built-in queue management I haven't shipped Crawlee yet, but it's been on my bookmarks list since I started building the itch.io ETL. My current approach is fetch + manual parsing, which works for known endpoints. Crawlee adds request queue persistence, rate limiting, and a cheerio integration for HTML extraction, all in TypeScript with native ESM support. The reason I haven't switched: my ETL runs inside GitHub Actions where I want simple, auditable scripts over a full crawl framework. But if I start scraping product pages from sites that don't have APIs — which is the next natural expansion for the OSS alternatives directory — Crawlee is the tool I'd reach for. The Apify team maintains it actively and the TypeScript types are genuinely good. eemeli/yaml — small footprint, strict spec compliance The yaml package by Eemeli Aro parses the frontmatter in my article files before cross-posting to Dev.to and Hashnode. It's 35 KB minified, has zero dependencies, and handles multi-line strings and nested objects without surprises. I switched from js-yaml six weeks ago because eemeli/yaml has better ESM exports and the parse errors are more actionable when frontmatter has a typo. One thing I didn't know until this week: the yaml package can also stringify back to YAML, preserving comments. I don't use that feature yet, but it matters for a workflow where I want to programmatically update article frontmatter without clobbering the human-readable structure. That's on the roadmap for automating canonical_url injection after Dev.to publish. @libsql/client — batched writes are the underrated feature The @libsql/client TypeScript client is what connects my ETL scripts to Turso. I wrote about Turso vs Cloudflare D1 earlier this week, but I didn't cover the batch API, which is the feature I actually rely on most. A single db.batch([...]) call wraps multiple INSERT OR REPLACE statements in one network round trip, which matters when seeding a 500-row table from a GitHub Actions runner. The client supports both remote Turso connections and an embedded file: mode that runs libSQL in-process with no network. I use the in-process mode for local ETL development so I don't burn Turso API quota while iterating on the seed logic. Switching between modes is one environment variable. That's the kind of DX detail that makes a dependency feel considered rather than assembled. None of these packages announced anything dramatic this week. They're just the boring infrastructure that lets the AI parts of the stack do their job. I'll write up actual traffic and content metrics in 30 days when I have a month of data worth publishing. Part of an ongoing 6-month experiment running three AI-curated directory sites. The technical claims here are real; this article was AI-assisted.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/morinaga/five-overlooked-packages-running-my-ai-directory-stack-21e7

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
