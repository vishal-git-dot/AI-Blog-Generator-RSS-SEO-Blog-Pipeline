---
title: "Another Tale of Two Threads (C or C++ vs. Python)"
slug: "another-tale-of-two-threads-c-or-c-vs-python"
author: "Paul J. Lucas"
source: "devto_python"
published: "Fri, 03 Jul 2026 13:44:33 +0000"
description: "Introduction This article is sort-of a sequel to A Tale of Two Threads (APIs) , but this time it’s about a significant difference between either C or C++ and..."
keywords: "threads, python, either, you, pthreads, thread, programmer, all"
generated: "2026-07-03T14:21:09.819021"
---

# Another Tale of Two Threads (C or C++ vs. Python)

## Overview

Introduction This article is sort-of a sequel to A Tale of Two Threads (APIs) , but this time it’s about a significant difference between either C or C++ and Python threads. If you’re either a C or C++ programmer who’s dabbling with Python threads, you should be aware of what follows. For the purposes of this article, all of POSIX threads (aka, pthreads ), standard C threads , and standard C++ threads can be considered equivalent and will all be referred to simply as pthreads. (On POSIX systems, both C and C++ threads are typically implemented as a thin layer on top of pthreads anyway.) Background During my career, I’ve mostly used pthreads from either C or C++ programs. I’m not a Python expert. At most, I’ve written a handful of scripts in Python, the longest of which was around 350 lines, and none used threads. I have a love-hate relationship with Python. No, it has nothing to do with Python using the off-side rule . Primarily, I dislike that Python isn’t statically typed. In late 2024 (after officially retiring ), I agreed to do some work part-time for an application written in Python that necessarily makes heavy use of threads. Python has its own threading library that looks like pretty much every other threading library and apparently contains no surprises for a C or C++ programmer. Apparently . Threads in C and C++ Either a C or C++ programmer would know that when either: main() returns; or: Any function calls exit . then the entire process terminates immediately.* * In C and C++, atexit handlers are performed before termination; in C++, destructors for global objects are also performed. But this doesn’t matter for this article. As I previously wrote: Even though nascent “threads” appeared as early as 1966, they weren’t supported by any major programming language of that era. POSIX threads, aka pthreads (“pea-threads”), didn't appear until 1995. Consequently when C was created in 1972, it didn’t support threads at all until pthreads came along. One consequence of this is that the addition of pthreads couldn’t change the behavior of either 1 or 2 above, that is the process still terminates even if other threads are still running . To prevent #1 from happening, the main thread (which is the thread main runs on) has to join every thread it created. Threads in Python The significant difference in Python is that the main thread will wait until all (non-daemon) threads have terminated, i.e., it does an implicit join on all of them. Consequently, this means that, unless you either need to synchronize with or want the return values from threads’ main functions, you don’t need to join them yourself explicitly. If you’re a native Python programmer, this likely isn’t news to you; but for a C or C++ programmer, it might be. It was to me. As it happens, Java handles threads the same way as Python. Go and Rust handle threads the same way as C and C++. Conclusion If you’re doing thread programming and are coming from either C or C++ to Python, know that process lifetime is handled differently. Why does Python (and Java) handle threads differently? On the whole, the behavior makes thread programming slightly easier.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/pauljlucas/another-tale-of-two-threads-c-or-c-vs-python-hhl

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
