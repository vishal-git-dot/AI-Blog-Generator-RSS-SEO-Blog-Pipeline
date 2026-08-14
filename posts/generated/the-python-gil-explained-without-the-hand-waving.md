---
title: "The Python GIL, explained without the hand-waving"
slug: "the-python-gil-explained-without-the-hand-waving"
author: "websilvercraft"
source: "devto_python"
published: "Fri, 14 Aug 2026 07:27:00 +0000"
description: "Every Python developer eventually hits this conversation: "Just use threads to speed it up." "Python threads don't run in parallel. The GIL." "So threads are..."
keywords: "threads, gil, python, you, time, they, one, waiting"
generated: "2026-08-14T07:39:24.494780"
---

# The Python GIL, explained without the hand-waving

## Overview

Every Python developer eventually hits this conversation: "Just use threads to speed it up." "Python threads don't run in parallel. The GIL." "So threads are useless in Python?" "No, they're great for—" "You just said they don't run in parallel!" Both people are half right. Here's the actual model, and the decision rules that follow from it. What the GIL actually is The Global Interpreter Lock is a mutex inside CPython that allows only one thread to execute Python bytecode at any moment . Ten threads can exist, be scheduled by the OS, and hold live stack frames — but only the thread holding the GIL advances Python code. The interpreter forces a handoff every few milliseconds, so threads interleave rapidly rather than run simultaneously . Why does CPython have it? Memory management. CPython uses reference counting; every object carries a counter that threads would corrupt if two of them incremented/decremented it at once. One big lock around the interpreter makes every refcount operation safe — and, as a bonus, makes single-threaded code (the vast majority of Python ever run) faster than fine-grained locking would. The part everyone skips: the GIL is released constantly The GIL is only required while executing Python bytecode . Blocking operations release it: Waiting on I/O — network calls, file reads, time.sleep , database queries: the waiting thread gives up the GIL and another thread runs. Heavy C-extension work — NumPy matrix multiplication, hashing, compression, image transforms in Pillow: these release the GIL around their C loops. This is why the "threads are useless" take is wrong. The real rule: Threads give you parallel waiting , not parallel computing . See it in numbers CPU-bound work — threads buy you nothing: import time from concurrent.futures import ThreadPoolExecutor def crunch (): return sum ( i * i for i in range ( 10_000_000 )) start = time . perf_counter () crunch (); crunch () print ( f " serial: { time . perf_counter () - start : . 1 f } s " ) # ~2.0s start = time . perf_counter () with ThreadPoolExecutor () as pool : list ( pool . map ( lambda _ : crunch (), range ( 2 ))) print ( f " threads: { time . perf_counter () - start : . 1 f } s " ) # ~2.0s — no gain I/O-bound work — threads shine: import urllib.request def fetch ( url ): return urllib . request . urlopen ( url ). read () urls = [ " https://example.com " ] * 20 # serial: ~20 × latency. threads: ~1 × latency. with ThreadPoolExecutor ( max_workers = 20 ) as pool : pages = list ( pool . map ( fetch , urls )) Twenty threads all waiting on sockets coexist happily — the GIL is free while they wait. The decision table Your workload Use Why Many network calls / file ops threading or asyncio GIL released while waiting Very many (1000s) of connections asyncio Threads get heavy; the event loop multiplexes one thread CPU-heavy pure Python multiprocessing / ProcessPoolExecutor Each process has its own GIL CPU-heavy numeric code NumPy / Numba / Cython C code releases the GIL, parallelism inside one process Mixed pipeline Processes for compute + threads/async for I/O Compose them The one-liner upgrade when you need real parallelism: from concurrent.futures import ProcessPoolExecutor # was ThreadPoolExecutor with ProcessPoolExecutor () as pool : # same API, real cores results = list ( pool . map ( crunch , range ( 8 ))) Mind the caveats: processes don't share memory, arguments get pickled across, and on Windows/macOS you need the if __name__ == "__main__": guard. "But I heard they're removing the GIL" Sort of, and it's genuinely exciting — but slowly. PEP 703 made a free-threaded build of CPython official as an experimental option (the python3.13t / 3.14t builds). It removes the GIL at the cost of some single-threaded overhead, and it only pays off once the packages you depend on ship free-threaded wheels. The default CPython you get from python.org or your distro still has the GIL, and will for years. So for code you ship today, the mental model above is the one that matters. What to remember The GIL serializes Python bytecode , not your program's waiting time . Threads are for I/O-bound work. They're not broken; they're specialized. Processes (or C extensions) are for CPU-bound work. asyncio competes with threads for I/O concurrency, not with processes for parallelism.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/websilvercraft/the-python-gil-explained-without-the-hand-waving-10jo

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
