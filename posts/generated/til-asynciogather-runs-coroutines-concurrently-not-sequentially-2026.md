---
title: "TIL: asyncio.gather() Runs Coroutines Concurrently, Not Sequentially (2026)"
slug: "til-asynciogather-runs-coroutines-concurrently-not-sequentially-2026"
author: "qing"
source: "devto_python"
published: "Sun, 12 Jul 2026 08:05:35 +0000"
description: "TIL: asyncio.gather() Runs Coroutines Concurrently, Not Sequentially When working with asynchronous code in Python, it's essential to understand how to run c..."
keywords: "asyncio, time, gather, coroutines, await, concurrently, sequentially, using"
generated: "2026-07-12T08:25:23.791691"
---

# TIL: asyncio.gather() Runs Coroutines Concurrently, Not Sequentially (2026)

## Overview

TIL: asyncio.gather() Runs Coroutines Concurrently, Not Sequentially When working with asynchronous code in Python, it's essential to understand how to run coroutines efficiently. I recently discovered that using asyncio.gather() can significantly improve performance by running coroutines concurrently, rather than sequentially. To demonstrate this, let's consider an example where we have two coroutines, each simulating an I/O-bound operation with a 2-second delay. import asyncio import time async def io_bound_operation ( id ): await asyncio . sleep ( 2 ) return id async def main (): start_time = time . time () # Sequential await await io_bound_operation ( 1 ) await io_bound_operation ( 2 ) print ( f " Sequential await: { time . time () - start_time } seconds " ) start_time = time . time () # Concurrent execution using asyncio.gather() await asyncio . gather ( io_bound_operation ( 1 ), io_bound_operation ( 2 )) print ( f " Concurrent execution: { time . time () - start_time } seconds " ) asyncio . run ( main ()) Running this code, you'll notice that the sequential await takes approximately 4 seconds, while the concurrent execution using asyncio.gather() takes around 2 seconds. This is because asyncio.gather() allows the coroutines to run concurrently, overlapping their execution time. The key takeaway is that using asyncio.gather() can significantly improve the performance of your asynchronous code by running coroutines concurrently, rather than sequentially. Follow me on Dev.to for daily Python tips and quick guides!

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/qingluan/til-asynciogather-runs-coroutines-concurrently-not-sequentially-2026-1kja

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
