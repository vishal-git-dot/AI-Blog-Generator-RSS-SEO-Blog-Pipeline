---
title: "Why *= 2 is slower than = col * 2 in Pandas — and what strace shows about abstraction cost"
slug: "why-2-is-slower-than-col-2-in-pandas-and-what-strace-shows-about-abstraction-cost"
author: "Patrick Ryan"
source: "devto_python"
published: "Sat, 27 Jun 2026 19:08:53 +0000"
description: "This problem looks trivial, but I got curious about what different Pandas update strategies actually cost. I separated the benchmark into two layers: Warm in..."
keywords: "pandas, slower, assignment, cost, even, salary, than, benchmark"
generated: "2026-06-27T19:36:59.124609"
---

# Why *= 2 is slower than = col * 2 in Pandas — and what strace shows about abstraction cost

## Overview

This problem looks trivial, but I got curious about what different Pandas update strategies actually cost. I separated the benchmark into two layers: Warm in-memory execution — how fast each Pandas update strategy runs after imports are already complete. Cold-start syscall surface — how much work the runtime performs before the useful operation even begins. On 20,000 rows with 1,000 randomized round-robin iterations, the result surprised me: Direct assignment, df["salary"] = df["salary"] * 2 , was the fastest standard Pandas API. df["salary"] *= 2 was slower, even though it looks more "in-place." .loc[] assignment was much slower because it goes through label-indexing machinery. .apply(lambda) was roughly 28x slower than direct assignment. .iterrows() was roughly 2,800x slower than direct assignment. The fastest Pandas-backed path was dropping to the underlying NumPy buffer with .to_numpy(copy=False)[:] *= 2 , which beat standard Pandas assignment by about 5x. Even that cheatcode still costs ~2.3x over a bare NumPy array — the DataFrame wrapper overhead is irreducible even when you bypass the Pandas API entirely. That last point was the most surprising. Escaping the Pandas API is not the same as escaping Pandas. Then I looked at cold-start cost with strace . Before the actual salary multiplication runs, Pandas pays a large initialization tax: imports, filesystem probing, memory-mapping compiled extensions, dtype/index machinery, and runtime setup. In my local environment, the tiny Pandas script had about 8,500 syscalls before useful work, compared with 4 for a tiny ASM program and 88 for a small C++ binary. The import cost is paid once in production. The row-wise cliff is real regardless. Full benchmark table with Pandas methods, NumPy buffer mutation, ASM/C++/Rust/Polars comparisons, and syscall breakdown is in my full benchmark results .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/patrickryankenneth/why-2-is-slower-than-col-2-in-pandas-and-what-strace-shows-about-abstraction-cost-10kb

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
