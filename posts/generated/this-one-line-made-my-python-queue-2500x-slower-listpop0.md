---
title: "This One Line Made My Python Queue 2,500x Slower (list.pop(0))"
slug: "this-one-line-made-my-python-queue-2500x-slower-listpop0"
author: "Muiduzzaman Lipu"
source: "devto_python"
published: "Sat, 21 Nov 2026 18:35:21 +0000"
description: "A queue of one million tasks. Processing them took 58 seconds . Changing one line made it take 0.023 seconds . All timings below are the best of 3 runs on Py..."
keywords: "out, tasks, list, deque, one, pop, items, range"
generated: "2026-11-21T18:56:47.821140"
---

# This One Line Made My Python Queue 2,500x Slower (list.pop(0))

## Overview

A queue of one million tasks. Processing them took 58 seconds . Changing one line made it take 0.023 seconds . All timings below are the best of 3 runs on Python 3.15.2, on an Apple M4. Video version: The code tasks = list ( range ( 1_000_000 ) ) while tasks : task = tasks . pop ( 0 ) # take the oldest task # ... process it First in, first out. It looks fine, and with a few hundred tasks you'd never notice a problem. Measured Items list.pop(0) deque.popleft() 10,000 0.004 s 0.0002 s 100,000 0.548 s 0.0018 s 1,000,000 57.96 s 0.023 s Look at the left column: 10× more items, roughly 100× more time . That's the signature of O(n²). The deque column grows linearly: 10× the items, about 10× the time. Why pop(0) is O(n) A Python list is a dynamic array: one contiguous block of memory holding pointers. # [ t0 | t1 | t2 | t3 | ... | t999999 ] tasks . pop ( ) # remove the end: nothing moves → O(1) tasks . pop ( 0 ) # remove the front: 999,999 items move left → O(n) Removing the first element leaves a gap, so every remaining element shifts one slot left. Do that n times and you get about n²/2 moves: half a trillion for a million tasks. The fix: collections.deque from collections import deque tasks = deque ( range ( 1_000_000 ) ) while tasks : task = tasks . popleft ( ) deque (double-ended queue) supports O(1) appends and pops at both ends. If you write breadth-first search, this is the queue to use. Trap 2: insert(0, x) The mirror image has the same cost: inserting at the front shifts everything right. items = [ ] for i in range ( 100_000 ) : items . insert ( 0 , i ) # 1.377 s items = deque ( ) for i in range ( 100_000 ) : items . appendleft ( i ) # 0.002 s Trap 3: out = out + [x] out = [ ] for i in range ( 50_000 ) : out = out + [ i ] # 1.988 s: builds a NEW list and copies everything out = [ ] for i in range ( 50_000 ) : out . append ( i ) # 0.0007 s out + [i] creates a brand-new list every iteration. out.append(i) and out += [i] modify the list in place ( += took 0.002 s in my test). Trap 4 (half a myth): str += You'll often read that building a string with += in a loop is O(n²). I measured 300,000 iterations of s += 'x' : Case Time plain local variable 0.008 s with another reference ( alias = s in the loop) 0.665 s on an attribute ( obj.s += 'x' ) 0.658 s CPython has an optimization: when the string has only one reference, += can resize it in place . That's why the plain case is fast. As soon as anything else holds a reference, or the target is an attribute, the optimization can't apply, and every += copies the whole string: about 80× slower here. Other Python implementations (like PyPy) don't promise this optimization at all. The reliable pattern: parts = [ ] for chunk in chunks : parts . append ( chunk ) result = "" . join ( parts ) Recap list.pop(0) and list.insert(0, x) are O(n). Use deque.popleft() / deque.appendleft() . out = out + [x] copies the list. Use append or += . s += ... is only fast on a plain local string. Build strings with "".join(parts) . Warning sign: 10× more data, ~100× slower means O(n²) is hiding somewhere. Now go search your code for pop(0) . 👀 I post one tested coding tip every day on YouTube at Refactorly . The 30-second version of this one is here .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/refactorly/this-one-line-made-my-python-queue-2500x-slower-listpop0-54cj

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
