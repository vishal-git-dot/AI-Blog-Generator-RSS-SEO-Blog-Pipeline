---
title: "Python Without the GIL: Is It Actually Faster? I Measured It"
slug: "python-without-the-gil-is-it-actually-faster-i-measured-it"
author: "Muiduzzaman Lipu"
source: "devto_python"
published: "Sat, 21 Nov 2026 18:34:50 +0000"
description: "For about thirty years, Python threads couldn't run Python code in parallel. Now there's an official build of Python without that limit: the free-threaded bu..."
keywords: "gil, threads, python, count, code, without, threaded, free"
generated: "2026-11-21T18:56:47.821605"
---

# Python Without the GIL: Is It Actually Faster? I Measured It

## Overview

For about thirty years, Python threads couldn't run Python code in parallel. Now there's an official build of Python without that limit: the free-threaded build. So I measured it: the same code on the same Mac, with the GIL and without it. Short version: about 3× faster on 8 threads for CPU-heavy code, no change for code that mostly waits, slightly slower single-threaded, and it exposes race conditions the GIL was hiding. Video version: What is the GIL? The Global Interpreter Lock lets only one thread run Python bytecode at a time. Threads still help when your code waits (network, files, databases, sleep ), because Python releases the GIL while waiting. But CPU-heavy threads just take turns. More threads, same speed. The free-threaded build ( python3.15t , the t is for "threaded") removes the lock. It's been officially supported since Python 3.14 (PEP 779). The test Count the primes below 2,000,000 in pure Python, split the range into equal chunks, and give each chunk to a thread. The total work is the same no matter how many threads. import sys , time from concurrent . futures import ThreadPoolExecutor def count_primes ( start , end ) : count = 0 for n in range ( start , end ) : if n < 2 : continue i = 2 while i * i <= n : if n % i == 0 : break i += 1 else : count += 1 return count N = 2_000_000 def run ( threads ) : step = N // threads chunks = [ ( i * step , ( i + 1 ) * step ) for i in range ( threads ) ] t = time . perf_counter ( ) with ThreadPoolExecutor ( threads ) as ex : total = sum ( ex . map ( lambda c : count_primes ( * c ) , chunks ) ) return time . perf_counter ( ) - t , total Setup: Python 3.15.2, the regular build vs the free-threaded build, on an Apple M4 (4 performance + 6 efficiency cores). I ran both builds interleaved, five rounds, and report the median. Both found the same 148,933 primes. The results Threads With GIL Without GIL Speedup 1 4.27 s 4.46 s 0.96× 2 4.02 s 2.92 s 1.4× 4 4.12 s 1.95 s 2.1× 8 4.32 s 1.45 s 3.0× With the GIL, adding threads does nothing: it's about 4 seconds every time. Without it, the same code scales: 1.45 s on 8 threads, about 3× faster. Two honest details: Single-threaded, the free-threaded build was about 4% slower (4.46 s vs 4.27 s). Making the interpreter safe without one big lock adds a small cost everywhere. Why not 8× with 8 threads? This chip has only 4 performance cores; the other threads land on slower efficiency cores. Your speedup depends on your CPU and your workload. Code that waits: no difference with ThreadPoolExecutor ( 8 ) as ex : list ( ex . map ( lambda _ : time . sleep ( 1 ) , range ( 8 ) ) ) GIL=True 8 x sleep(1): 1.01 s GIL=False 8 x sleep(1): 1.01 s Python already releases the GIL while waiting, so I/O-bound code (web requests, database calls, file reads) gets nothing extra from free-threading. It only helps CPU-heavy Python code . The bug the GIL was hiding Eight threads, each adding 1 to a shared counter a million times: count = 0 def work ( _ ) : global count for _ in range ( 1_000_000 ) : count += 1 with ThreadPoolExecutor ( 8 ) as ex : list ( ex . map ( work , range ( 8 ) ) ) Three runs on each build: GIL=True count = 8,000,000 (expected 8,000,000) GIL=False count = 1,323,734 (expected 8,000,000) GIL=False count = 1,193,764 GIL=False count = 1,419,542 count += 1 is not atomic : it reads the value, adds one and writes it back, and threads overwrite each other's updates. Even with the GIL this isn't guaranteed safe, but it almost never showed up. Without the GIL, it loses over 80% of the updates instantly. The fix is to protect shared data: import threading lock = threading . Lock ( ) def work ( _ ) : global count for _ in range ( 1_000_000 ) : with lock : count += 1 # → 8,000,000 on both builds Better still, avoid shared mutable state: have each thread return its own result and combine them at the end, like count_primes above does. Try it yourself With uv : uv python install 3.15t uv run --python 3.15t bench.py Or tick the free-threaded option in the official python.org installer. Then check what you're running: $ python3.15t -VV Python 3.15.2 free-threading build ( main, Nov 11 2026, 00:11:29 ) [ Clang 23.1.3 ] >>> import sys >>> sys . _is_gil_enabled ( ) False One gotcha: if you import a C extension that hasn't declared free-threading support, Python turns the GIL back on and warns you. I compiled a minimal old-style extension to check: RuntimeWarning: The global interpreter lock (GIL) has been enabled to load module 'legacy', which has not declared that it can run safely without the GIL. before False after True So check that your dependencies ship free-threaded ( cp315t ) wheels, or your speedup quietly disappears. Should you use it? ✅ CPU-heavy pure Python that you can split into threads: a real speedup, without the overhead of multiprocessing . ➖ Code that mostly waits (web, DB, files): no change. ⚠️ Single-threaded code: a few percent slower. ⚠️ Shared mutable data: needs locks (or better, don't share it). ⚠️ C extensions: old ones turn the GIL back on. What would you speed up without the GIL? 👇 I post one tested coding tip every day on YouTube at Refactorly . The 30-second version of this one is here .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/refactorly/python-without-the-gil-is-it-actually-faster-i-measured-it-55oo

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
