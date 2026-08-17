---
title: "How Python Takes Out Its Own Garbage"
slug: "how-python-takes-out-its-own-garbage"
author: "samconibear"
source: "devto_python"
published: "Mon, 17 Aug 2026 18:28:45 +0000"
description: "Python manages memory automatically, freeing developers from manual allocation and deallocation. It does this through two complementary mechanisms: reference..."
keywords: "reference, generation, collection, objects, collector, cyclic, object, parent"
generated: "2026-08-17T18:47:04.449208"
---

# How Python Takes Out Its Own Garbage

## Overview

Python manages memory automatically, freeing developers from manual allocation and deallocation. It does this through two complementary mechanisms: reference counting and a generational garbage collector for cyclic references. This article covers how garbage collection works in CPython. In other implementations such as PyPy, it works under a different mechanism Reference Counting: The Primary Mechanism Every object in Python carries a reference count, a tally of how many references point to it. This count increments when: A new reference is assigned ( y = x ) It's stored in a container (list, dict, etc.) The object is passed into a function It decrements when: A reference goes out of scope A reference is reassigned del is manually called on a reference import sys x = [] y = x z = { " y " : y } print ( sys . getrefcount ( x )) # 4 (x + y + z + the arg to getrefcount) y = 1 del z print ( sys . getrefcount ( x )) # 2 (x + the arg to getrefcount) When the count hits zero, CPython deallocates the object immediately . This is a key difference from garbage-collected languages like Java, JS or the PyPy implementation, where collection timing is unpredictable. The Problem: Reference Cycles Reference counting alone cannot handle cyclic references, where objects reference each other and keep their counts above zero even when unreachable from the program: class MyClass : def __init__ ( self ): self . ref = None a = MyClass () b = MyClass () a . ref = b b . ref = a del a del b # a and b still reference each other -> the refcount never reaches 0 This causes a memory leak. The Solution: Generational Garbage Collector To catch scenarios like the above, Python includes a separate cyclic garbage collector, implemented in the gc module. It's based on the generational hypothesis : most objects die young, so recently created objects are checked more frequently than long-lived ones. Objects are organized into three generations : Generation Description Collection Frequency 0 Newly created objects Most frequent 1 Survived one collection Less frequent 2 Survived multiple collections Least frequent An object starts in generation 0. If it survives a collection pass, it's promoted to generation 1, then eventually generation 2. Each generation has a threshold count of allocations that triggers a collection pass: import gc print ( gc . get_threshold ()) # e.g. (700, 10, 10) This means generation 0 collects after 700 net allocations; generations 1 and 2 collect after 10 collections of the preceding generation. How Cycle Detection Works The cyclic collector only tracks container objects: lists, dicts, tuples, class instances, closures - anything capable of holding a reference to another object. Each tracked object carries a struct linking it into a per-generation list. When a generation's allocation-minus-deallocation count crosses its threshold, a collection pass runs against that generation: Copy each tracked object's refcount into a scratch field. Subtract references that come from other tracked objects, this strips out the "internal" cycle references. Anything left with a positive count must be referenced from outside the tracked set, so it's kept. Trace outward from those objects to rescue anything reachable from them, even if it's inside a cycle. Whatever's still at zero is unreachable and gets swept away. Objects that survive a pass move to the next generation and get checked less often. The time complexity of this whole operation is O(n). Should we mess with the cyclic collector? Usually not. however... Sometimes disabling the cyclic collector can be done in performance-sensitive code that avoids creating reference cycles. import gc gc . disable () # turn off the cyclic collector gc . enable () # turn it back on gc . collect () # force a full collection, returns count of unreachable objects found gc . get_count () # current object counts per generation gc . set_threshold ( 700 , 10 , 10 ) # adjust collection thresholds Practical Implications Watch allocation-heavy loops Generation-0 collection triggers after a net allocation threshold (default 700), so code that repeatedly creates and discards containers can trigger frequent passes: # Triggers frequent gen-0 collections -> a new dict every iteration for row in range ( 1_000_000 ): record = { " id " : row , " value " : row * 2 } do_something ( record ) # Fewer allocations -> reuse the same container record = {} for row in range ( 1_000_000 ): record [ " id " ] = row record [ " value " ] = row * 2 do_something ( record ) The second version creates one dict instead of a million, so it crosses the gen-0 threshold far less often. Break likely cycles with weakref Parent/child structures are a classic example: a Node with a .parent and .children list creates a cycle every time a child is added: import weakref class Node : def __init__ ( self , parent = None ): self . children = [] self . parent = weakref . ref ( parent ) if parent else None root = Node () child = Node ( parent = root ) root . children . append ( child ) # child -> root is weak, so no cycle forms child.parent doesn't contribute to root's refcount at all. So when del root runs, root's refcount actually hits zero, same for child on del child . No cycle ever exists, so there's nothing for the cyclic collector to have to catch later.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/samconibear/how-python-takes-out-its-own-garbage-326a

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
