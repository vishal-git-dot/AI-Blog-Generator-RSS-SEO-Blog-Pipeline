---
title: "I found an interesting N+1 problem in a Django application..."
slug: "i-found-an-interesting-n1-problem-in-a-django-application"
author: "Bun Rong"
source: "devto_python"
published: "Sun, 13 Sep 2026 10:33:24 +0000"
description: "I recently found an interesting N+1 query problem in a Django application. The code looked completely normal: orders = Order . objects . all () for order in ..."
keywords: "django, queries, query, orders, order, customer, interesting, fetch"
generated: "2026-09-13T11:28:47.306394"
---

# I found an interesting N+1 problem in a Django application...

## Overview

I recently found an interesting N+1 query problem in a Django application. The code looked completely normal: orders = Order . objects . all () for order in orders : print ( order . customer . name ) But Django was actually doing something like: 1 query → fetch all orders + N queries → fetch each customer's data ---------------------------------------- 101 queries for 100 orders 😬 The fix was simple: orders = Order . objects . select_related ( " customer " ) Now Django can fetch the related customer data in the same query instead of querying the database for every order. The interesting part isn't just knowing select_related() . The real challenge is finding where the N+1 queries are happening , especially when they come from serializers, templates, nested relationships, or code you didn't realize was triggering additional database queries. I wrote a practical walkthrough covering how to detect N+1 queries in Django, measure the queries, and fix them with select_related() , prefetch_related() , and assertNumQueries() . 👉 Read the full article: How to Find and Fix N+1 Queries in Django — Rong A practical guide to finding N+1 query problems in Django with django-debug-toolbar and assertNumQueries, and fixing them with select_related, prefetch_related and Prefetch. technicaldev.vercel.app Have you encountered an N+1 query that was surprisingly difficult to find?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/bun_rong_b83c6164be1d2a98/i-found-an-interesting-n1-problem-in-a-django-application-2g5f

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
