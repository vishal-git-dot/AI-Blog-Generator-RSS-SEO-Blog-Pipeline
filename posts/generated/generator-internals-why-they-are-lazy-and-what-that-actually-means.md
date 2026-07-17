---
title: "Generator Internals: Why They Are Lazy and What That Actually Means"
slug: "generator-internals-why-they-are-lazy-and-what-that-actually-means"
author: "Ameer Abdullah"
source: "devto_python"
published: "Fri, 17 Jul 2026 13:32:00 +0000"
description: "Tracing a generator's execution reveals a fundamentally different way Python can run code. A generator function looks like a regular function but behaves in ..."
keywords: "generator, print, yield, next, value, calling, function, when"
generated: "2026-07-17T13:49:54.402900"
---

# Generator Internals: Why They Are Lazy and What That Actually Means

## Overview

Tracing a generator's execution reveals a fundamentally different way Python can run code. A generator function looks like a regular function but behaves in a fundamentally different way. Understanding that difference requires tracing through what Python actually does when it executes one. The Key Difference A regular function runs to completion when called. A generator function returns an iterator object immediately without running any of its code. def regular (): print ( " regular function running " ) return 42 def generator (): print ( " generator running " ) yield 42 r = regular () # prints "regular function running" g = generator () # prints nothing When you call generator() , Python creates a generator object and returns it. None of the code inside the function has executed yet. The print statement does not run until you ask the generator for its first value. How yield Suspends Execution def count_to_three (): print ( " about to yield 1 " ) yield 1 print ( " about to yield 2 " ) yield 2 print ( " about to yield 3 " ) yield 3 print ( " generator finished " ) gen = count_to_three () print ( " calling next the first time " ) value = next ( gen ) print ( f " got { value } " ) print ( " calling next the second time " ) value = next ( gen ) print ( f " got { value } " ) Trace the execution: count_to_three() — creates generator object, no code runs print("calling next the first time") — prints next(gen) — generator starts executing print("about to yield 1") — prints yield 1 — suspends execution, returns 1 to the caller print(f"got 1") — prints print("calling next the second time") — prints next(gen) — generator resumes from where it stopped print("about to yield 2") — prints yield 2 — suspends again, returns 2 Output: calling next the first time about to yield 1 got 1 calling next the second time about to yield 2 got 2 The generator's execution is interleaved with the calling code. It runs up to a yield, suspends, and resumes from exactly that point when asked for the next value. Generator Exhaustion def small_gen (): yield 1 yield 2 yield 3 gen = small_gen () print ( list ( gen )) print ( list ( gen )) Output: [1, 2, 3] [] Once a generator has yielded all its values, it is exhausted. Calling next() on an exhausted generator raises StopIteration . list() catches this exception and returns an empty list. Exhaustion is permanent. You cannot restart a generator. To get the values again you must create a new generator object by calling the function again. Generator Expressions gen_expr = ( x ** 2 for x in range ( 5 )) list_comp = [ x ** 2 for x in range ( 5 )] print ( type ( gen_expr )) print ( type ( list_comp )) print ( next ( gen_expr )) print ( next ( gen_expr )) Output: <class 'generator'> <class 'list'> [0, 1, 4, 9, 16] 0 1 The list comprehension computes all values immediately and stores them in memory. The generator expression computes each value only when requested. For large sequences this is a significant memory difference. The send() Method def accumulator (): total = 0 while True : value = yield total if value is None : break total += value acc = accumulator () next ( acc ) # prime the generator print ( acc . send ( 10 )) print ( acc . send ( 20 )) print ( acc . send ( 5 )) send() resumes the generator and passes a value that becomes the result of the yield expression. Output: 10 30 35 This is advanced generator behavior tested in senior-level interviews. The generator receives values from the caller through send() , processes them, and yields results back. When to Use Generators Generators are appropriate when you need to process a sequence of values but do not need all of them in memory at once. Reading a large file line by line, generating an infinite sequence of numbers, processing a data pipeline where each step produces values for the next step — all of these are natural fits for generators. For small sequences or when you need to access elements by index, a list is more appropriate. Practice generator problems on pycodeit.com — the hard difficulty level includes several generator tracing problems that test exhaustion, send(), and generator expression behavior.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ameer_abdullah_68d48c8496/generator-internals-why-they-are-lazy-and-what-that-actually-means-1eh1

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
