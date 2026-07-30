---
title: "SnowLens: Free Snowflake Observability — 9 Detectors, Zero Data Egress"
slug: "snowlens-free-snowflake-observability-9-detectors-zero-data-egress"
author: "Abin Alex"
source: "devto_python"
published: "Thu, 30 Jul 2026 02:40:40 +0000"
description: "If you run Snowflake in production, you've probably asked yourself: which queries are burning credits? Why did costs spike last Tuesday? Are any warehouses j..."
keywords: "snowflake, snowlens, sql, your, data, queries, warehouse, cost"
generated: "2026-07-30T02:47:02.165974"
---

# SnowLens: Free Snowflake Observability — 9 Detectors, Zero Data Egress

## Overview

If you run Snowflake in production, you've probably asked yourself: which queries are burning credits? Why did costs spike last Tuesday? Are any warehouses just sitting there idle? Most observability tools answer these questions by shipping your query logs to an external SaaS — data egress, vendor lock-in, another subscription. SnowLens takes a different approach: it's a Streamlit app that installs directly into your Snowflake account and runs on your own compute. Your data never leaves your environment. And it's completely free. What It Detects — 9 Rules Performance: Slow queries — configurable threshold (10s/20s/30s/60s) with SELECT-only toggle Cancelled queries — manually stopped or killed by timeout Failed queries — non-cancellation errors (syntax, permissions, resource limits) Disk spill — local vs remote classification, remote flagged as high-risk Queuing — warehouse contention when QUEUED_OVERLOAD_TIME exceeds 60s Cost: Credit spikes — hourly usage > 2 standard deviations above warehouse baseline Idle-but-running — credits burned with zero queries Oversized warehouses — big warehouse, tiny workload Workload cost spikes — cost outliers by QUERY_TAG or role Plus a cost attribution engine that groups credit usage by QUERY_TAG, dbt model, or role. How It Works SnowLens reads from three Snowflake metadata views that every account already has: SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY SNOWFLAKE.ACCOUNT_USAGE.WAREHOUSE_METERING_HISTORY SNOWFLAKE.ACCOUNT_USAGE.QUERY_ATTRIBUTION_HISTORY These are Snowflake's own internal metadata — not your business data. No tables, stages, or query results are touched. Privacy Model Only reads ACCOUNT_USAGE metadata No outbound network calls (Streamlit-in-Snowflake runs in isolation) Runs on XSMALL warehouse with 60s auto-suspend (cents per session) Least-privilege role with only the grants the app needs Clean uninstall in 3 lines of SQL Memory Safety Streamlit-in-Snowflake has a ~32 MB memory limit. SnowLens handles large accounts with: Query text truncated to 300 characters Each detector capped at top 200 findings via QUALIFY ROW_NUMBER() Cost attribution aggregated in SQL before loading into Python Warehouse scope selector to limit detection to individual warehouses Install in 5 Minutes Download the ZIP from snowlens.vizcanvaz.com Run sql/01_setup.sql as ACCOUNTADMIN in Snowsight Upload streamlit_app.py and environment.yml to the stage, run sql/02_create_app.sql Done. Open Projects > Streamlit > SNOWLENS_APP. Links Product page: snowlens.vizcanvaz.com GitHub: github.com/abysabin/snowlens Full blog post with SQL logic: vizcanvaz.com Built by Abin Alex — 15+ years in data engineering. Questions or feedback welcome at vizcanvas@gmail.com .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/abin_alex_863f65bd6a1a77f/snowlens-free-snowflake-observability-9-detectors-zero-data-egress-1dln

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
