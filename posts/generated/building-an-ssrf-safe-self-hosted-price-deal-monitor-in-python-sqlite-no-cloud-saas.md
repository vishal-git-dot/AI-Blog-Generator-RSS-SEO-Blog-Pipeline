---
title: "Building an SSRF-Safe Self-Hosted Price & Deal Monitor in Python + SQLite (No Cloud SaaS)"
slug: "building-an-ssrf-safe-self-hosted-price-deal-monitor-in-python-sqlite-no-cloud-saas"
author: "huu thong tue"
source: "devto_python"
published: "Wed, 25 Nov 2026 07:41:54 +0000"
description: "Most lightweight price-tracking scripts break in production in one of three ways: A store switches from plain HTML to Schema.org JSON-LD AggregateOffer or Sh..."
keywords: "self, hosted, price, deal, monitor, json, ssrf, sqlite"
generated: "2026-11-25T07:53:48.782938"
---

# Building an SSRF-Safe Self-Hosted Price & Deal Monitor in Python + SQLite (No Cloud SaaS)

## Overview

Most lightweight price-tracking scripts break in production in one of three ways: A store switches from plain HTML to Schema.org JSON-LD AggregateOffer or Shopify /products/<handle>.json and the regex scraper silently reads 0 . An HTTP alert webhook fails during a 10-second network blip and drops the price-drop notification permanently instead of retrying. A monitored URL redirects HTTPS -> HTTP or into an SSRF/internal IP range ( 169.254.169.254 , 10.0.0.0/8 , loopback) during automated fetches. Architecture of Deal Monitor Self-Hosted v1.2 (Pure Python + SQLite + Docker) Instead of paying monthly SaaS per-URL fees or renting a cloud browser fleet for simple catalogs, Deal Monitor Self-Hosted v1.2 runs locally in Docker or Python 3.10+ with: 6 Deterministic Storefront Adapters: Schema.org JSON-LD ( Offer & AggregateOffer ), Shopify product JSON, Steam Storefront API, GOG catalog API, generic JSON-Path extractors, and optional Playwright DOM fallback. SQLite Transactional Outbox: Discord, Telegram, ntfy, and HMAC-signed generic Webhooks queued inside SQLite so transient 429 / 5xx outages never drop alerts. HTTPS-Only Redirect & SSRF Validation: Rejects insecure protocol downgrades and private/link-local IP targets at redirect resolution time before reading response bodies. 30-Day Zero-JS SVG Price History & CSV Export: Single-command audit dashboard ready for cron or docker compose up -d . Verified Local Test Suite Every release ships with an isolated pytest suite covering adapter parsing, outbox retries, redirect downgrade rejection, and SSRF IP blocking before packaging ( deal-monitor-self-hosted-v1.2.zip ). Self-Host It in 60 Seconds Get Deal Monitor Self-Hosted v1.2 — 19 USDC one-time (Solana Mainnet USDC QR checkout · instant signed ZIP + Dockerfile + docker-compose.yml , MIT licensed, no account required) Also pairing price monitors with MCP tool reliability checks in CI? See MCP Guard Kit Pro v1.2 (19 USDC) or explore both on the overview page .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/huu_thongtue_ce04bfd5f54/building-an-ssrf-safe-self-hosted-price-deal-monitor-in-python-sqlite-no-cloud-saas-45lp

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
