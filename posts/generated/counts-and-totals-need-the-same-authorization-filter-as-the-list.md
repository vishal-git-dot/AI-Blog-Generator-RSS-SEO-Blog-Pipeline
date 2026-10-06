---
title: "Counts and totals need the same authorization filter as the list"
slug: "counts-and-totals-need-the-same-authorization-filter-as-the-list"
author: "Auth By Example"
source: "devto_webdev"
published: "Tue, 06 Oct 2026 05:43:22 +0000"
description: "You locked down GET /invoices so it only returns rows the caller can see. Then the dashboard says "Invoices this month: 4,812", and that number comes from SE..."
keywords: "invoices, user, filter, can, count, tenant, query, counts"
generated: "2026-10-06T05:48:43.497032"
---

# Counts and totals need the same authorization filter as the list

## Overview

You locked down GET /invoices so it only returns rows the caller can see. Then the dashboard says "Invoices this month: 4,812", and that number comes from SELECT count(*) FROM invoices with no tenant filter. Counts leak. So do sums, search facets like "Overdue (37)", and the "20 of 3,104" line under a paginated table. When those run on their own query path they can tell a user how large another tenant's account is, or whether a given customer exists at all, without returning a single row. What I'd do: Build the authorization filter in one place and pass it to the list query, the count query and every aggregate. Check search facets and pagination totals separately. They often come from a different index call than the hits. Add a test: a user who can see 3 invoices gets 3 from the count endpoint, and the facet numbers add up to 3. If dashboard numbers are cached, put the tenant (or the user, when access is per user) in the cache key.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/authbyexample1/counts-and-totals-need-the-same-authorization-filter-as-the-list-4d3m

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
