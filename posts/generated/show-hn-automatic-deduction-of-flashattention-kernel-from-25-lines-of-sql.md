---
title: "Show HN: Automatic deduction of FlashAttention kernel from ~25 lines of SQL"
slug: "show-hn-automatic-deduction-of-flashattention-kernel-from-25-lines-of-sql"
author: "alxmrs"
source: "hackernews"
published: "Fri, 30 Oct 2026 20:09:47 +0000"
description: "In this demo, we automatically deduce a FlashAttention kernel with ~25 lines of SQL, which just expresses vanilla attention. This is possible due to three po..."
keywords: "sql, array, model, automatic, flashattention, kernel, lines, vanilla"
generated: "2026-10-30T22:07:19.227523"
---

# Show HN: Automatic deduction of FlashAttention kernel from ~25 lines of SQL

## Overview

In this demo, we automatically deduce a FlashAttention kernel with ~25 lines of SQL, which just expresses vanilla attention. This is possible due to three portable SQL extensions that we’re building: - xarray-sql: a library that efficiently represents petabyte scale array datasets in the cloud as tables (relations). - ddx: a database extension that adds automatic differentiation in the style of JAX to standard SQL, assuming the above array data model. - einfold: a modular query planner for fast tensor contractions in vanilla SQL, again, assuming the above array data model. My hope is that the relational model and algebra provide fresh perspectives on how we might do accelerator programming. Here, our thesis is that separating the logical layers in a tensor program from the physical layers is both more correct and more scalable. If the Bitter Lesson is a central dogma of machine learning, then why not formalize it with relational algebra? If this interests you and you’d like to tinker with us at the intersection of database theory and ML systems, join us on Discord at https://xql.systems (link at the bottom). Cheers. Comments URL: https://news.ycombinator.com/item?id=50309479 Points: 11 # Comments: 1

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://github.com/xqlsystems/xarray-sql/blob/6debe2495dcb4e8fac20ab97df5b89baae2a31a6/benchmarks/ml/01_attention.py

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
