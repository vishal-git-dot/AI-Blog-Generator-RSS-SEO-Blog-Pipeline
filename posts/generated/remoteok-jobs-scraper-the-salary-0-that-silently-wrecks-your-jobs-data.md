---
title: "RemoteOK Jobs Scraper: the salary 0 that silently wrecks your jobs data"
slug: "remoteok-jobs-scraper-the-salary-0-that-silently-wrecks-your-jobs-data"
author: "Devil Scrapes"
source: "devto_python"
published: "Mon, 03 Aug 2026 09:24:25 +0000"
description: "Quick answer RemoteOK publishes a public JSON feed, which makes collection straightforward — but the raw feed ships HTML-laden descriptions, 0 sentinels wher..."
keywords: "string, null, feed, you, remoteok, jobs, job, what"
generated: "2026-08-03T09:55:50.592657"
---

# RemoteOK Jobs Scraper: the salary 0 that silently wrecks your jobs data

## Overview

Quick answer RemoteOK publishes a public JSON feed, which makes collection straightforward — but the raw feed ships HTML-laden descriptions, 0 sentinels where salaries are unknown, and empty strings where locations are unknown. The RemoteOK Jobs Scraper normalizes all of that into 15 typed fields per posting at $0.0015 per job ($1.50 per 1,000) plus a $0.02 run start. An honest framing: this one isn't a fight 🤝 We normally write about targets that actively resist collection. RemoteOK isn't one of them, and it would be dishonest to dress it up as a heroic anti-bot conquest. The site publishes a JSON feed on purpose. So what are you paying for? Normalization, schema stability, and not having to maintain the integration yourself. That's a smaller value proposition than "we get you data you otherwise couldn't have," and it should be priced accordingly — which is why this is one of our cheapest Actors at $1.50 per 1,000 rows. If you want to hit the feed yourself, you can. If you'd rather have validated rows landing in a dataset on a schedule, with the sentinel-value handling already correct, that's what this does. The sentinel-value problem 🧹 Raw job feeds are full of values that look like data and aren't. Getting these wrong is the single most common source of bad analysis on jobs data. Salary 0 does not mean "this job pays nothing." It means the field wasn't filled in. If you average salary_min across a feed without handling this, every unspecified posting drags your average toward zero and your comp analysis is wrong by a wide margin. We convert 0 to null on both salary_min and salary_max , so unknowns are excluded from aggregates instead of silently counted as zeros. Empty-string location does not mean "no location." Same class of bug: an empty string is a value, and it will happily group as its own category in a GROUP BY . We convert it to null . Descriptions arrive as HTML. They contain tags, entities, and inconsistent whitespace. We clean them to plain text once, so every consumer doesn't have to. Job IDs are occasionally missing. When id is absent we fall back to slug , which is always present and unique. A row without a stable identifier is a row you can't deduplicate on across runs — so the fallback isn't a nicety, it's what makes incremental collection possible. company_url is not published by the feed. We ship the field as always-null rather than dropping it, so the schema stays stable if RemoteOK adds it later. Documented as such, not hidden. Full output schema 📦 Fifteen fields, extra="forbid" : Field Type Notes job_id string Falls back to slug when the feed omits id slug string RemoteOK URL slug position string Job title company string Hiring company company_url string | null Not published by the feed — always null for now location string | null Free-text; empty string → null tags list[string] Tags / skills salary_min int \ null salary_max int \ null description string HTML cleaned to plain text apply_url string Direct application URL url string RemoteOK job page date_posted string ISO-8601 epoch_posted int Unix seconds — for cheap range filtering logo string \ null Shipping both date_posted and epoch_posted is deliberate: one is human-readable and one sorts and filters without a parse step. Date handling is where jobs pipelines rot, and giving you the epoch removes an entire class of timezone bug. What people build with this Job aggregators and niche boards. Remote-only listings, filtered by tag, republished for a specific audience. tags plus epoch_posted is most of what a curated board needs. Remote-comp benchmarking. salary_min / salary_max with proper null handling gives you a defensible distribution of advertised remote salaries by tag. Pair it with our Glassdoor Salaries Scraper or Dice Tech Jobs Scraper for a cross-source view. Hiring-signal tracking for sales teams. A company posting remote engineering roles is a company with budget and a growing team — a legitimate buying signal for dev-tools and recruiting vendors. Labour-market research. Tag frequency over time is a clean proxy for which skills the remote market is actually paying for. Frequently asked questions What does a full sweep cost? $1.50 per 1,000 postings plus a $0.02 run start. A daily incremental pull is a few cents. Do I need an API key or account? No. The feed is public and unauthenticated. Why is company_url always null? The feed doesn't publish it. We keep the field for forward-compatibility and document the gap rather than quietly omitting it and breaking your schema later if it appears. How do I run this incrementally? Deduplicate on job_id and filter on epoch_posted greater than your last run's high-water mark. That's why both fields ship on every row. Is the salary data reliable? It's advertised salary, self-reported by the poster, and often absent — which is exactly why the 0 → null conversion matters. Treat it as a distribution of what employers are willing to publish, not as realized compensation. Try it Live on the Apify Store: RemoteOK Jobs Scraper . Part of our jobs family — Dice , BuiltIn , Workday , Greenhouse , Lever and more, all sharing consistent field naming so cross-board datasets merge without a translation layer. Built by Devil Scrapes — we build scrapers for the targets that fight back.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/devil_scrapes/the-salary-0-that-silently-wrecks-your-jobs-data-3lo4

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
