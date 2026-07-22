---
title: "The Tech Stack Behind a Canadian Healthcare SaaS: ChartPilot Phase 2"
slug: "the-tech-stack-behind-a-canadian-healthcare-saas-chartpilot-phase-2"
author: "Dhiraj Chatpar"
source: "devto_python"
published: "Wed, 22 Jul 2026 14:02:06 +0000"
description: "The Tech Stack Behind a Canadian Healthcare SaaS: ChartPilot Phase 2 We just completed Phase 2 of ChartPilot — a clinical documentation SaaS for Canadian hea..."
keywords: "stack, phase, data, write, log, behind, canadian, healthcare"
generated: "2026-07-22T14:08:21.362998"
---

# The Tech Stack Behind a Canadian Healthcare SaaS: ChartPilot Phase 2

## Overview

The Tech Stack Behind a Canadian Healthcare SaaS: ChartPilot Phase 2 We just completed Phase 2 of ChartPilot — a clinical documentation SaaS for Canadian healthcare organizations. The compliance requirements were non-trivial: PHIPA, PIPEDA, BCPIPA, and a dozen other acronyms. Here's the full stack and the decisions behind it. The Core Requirements Data residency : All data must stay in Canada (no US hyperscaler sub-processors) Encryption at rest and in transit : AES-256, TLS 1.3 Audit logging : Every read/write must be logged with timestamp, user, and action Access controls : Role-based with minimum 5 roles (admin, physician, nurse, clerk, viewer) Availability : 99.5% uptime SLA, self-healing infrastructure The Stack Backend Python 3.11 + FastAPI — async-first, Pydantic v2 for data validation PostgreSQL 16 — on a dedicated LXD container, not a managed service SQLAlchemy 2.0 with async driver (we can't use RDS due to data residency) Idempotency layer — every write gets a content hash; duplicate requests are rejected Outbox pattern — event-driven updates without distributed transactions Frontend Next.js 14 (App Router) — SSR for initial load, then client-side navigation TanStack Query — server state management, background refetching Tailwind CSS v4 — component-based design system Framer Motion — clinical workflow animations Infrastructure LXD containers on a dedicated host in Vancouver BC Cloudflare for DNS, CDN, WAF, and DDoS protection Cloudflare R2 for document storage (S3-compatible, no egress fees) Cloudflare D1 for lightweight edge metadata cache Self-hosted monitoring : Grafana + Prometheus + Loki The Compliance Engineering The hardest part was the audit log . Every API call generates a structured log entry with timestamp, user ID, action, resource ID, IP address, and content hash. These logs are append-only, replicated to a separate container, and retained for 7 years. What We'd Do Differently Start with the compliance infrastructure first . We built it in Phase 2 and had to retrofit. Use SQLite + Litestream for the audit log specifically. Write-ahead log semantics with SQLite's simplicity would have saved us significant engineering time. More aggressive caching upfront . Clinical apps have high read-to-write ratios. We underestimated this at the architecture stage. Results 27 automated tests passing 25 API endpoints documented 13 named staff roles supported 0 PHI incidents in 6 months of operation The full architecture documentation is available on request. Building something similar? info@netwit.ca

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dhiraj_chatpar_e54b46b388/the-tech-stack-behind-a-canadian-healthcare-saas-chartpilot-phase-2-3k73

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
