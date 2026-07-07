---
title: "Why Web Workers Swallow Your Stacktraces (And How to Write Specs to Fix It)"
slug: "why-web-workers-swallow-your-stacktraces-and-how-to-write-specs-to-fix-it"
author: "Bonzai2Carn"
source: "devto_webdev"
published: "Tue, 07 Jul 2026 14:30:00 +0000"
description: "TLDR: A spec that says "the function checks r.bbox.x < pageWidth / 2 " without saying where pageWidth comes from is not a spec. It is a description of behavi..."
keywords: "function, not, pagewidth, spec, write, every, architecture, message"
generated: "2026-07-07T14:49:42.588282"
---

# Why Web Workers Swallow Your Stacktraces (And How to Write Specs to Fix It)

## Overview

TLDR: A spec that says "the function checks r.bbox.x < pageWidth / 2 " without saying where pageWidth comes from is not a spec. It is a description of behavior with a hidden dependency. Every architecture document I have written with that pattern has produced at least one ReferenceError in implementation. The Pattern That Keeps Failing Architecture documents are good at describing what code should do. They are bad at describing where values come from and which function boundaries they cross. The page assembly refactor spec said: Check for FEATURE_LAYOUT: 2 cols, left is all visual, right is text. Compare each region's r.bbox.x against pageWidth / 2 . That is a correct behavioral description. It says nothing about execution context. The implementer writes it into _detectAutoZones , a module-level function, and references pageWidth by name. The spec did not say pageWidth needed to be passed as a parameter. The spec did not say _detectAutoZones was a module-level function. Both facts were implicit. The result: ReferenceError: pageWidth is not defined on every PDF load, with a stacktrace that points at the worker message handler instead of the actual line. Why This Keeps Happening Architecture documents are written in prose. Prose does not have a type system. A sentence like "the function uses pageWidth " can mean: The function receives pageWidth as a parameter. The function reads pageWidth from a module-level variable. The function is nested inside a caller that defines pageWidth and closes over it. The function reads pageWidth from an object passed in. All four are syntactically valid JavaScript. The prose does not distinguish between them. The implementer picks one and moves on. When the spec is written by the same person who will implement it, option 3 is tempting because it is the least-friction path. The value is just "there" without needing to thread it through function signatures. It works when the function is actually nested. It throws when the function ends up at module level for any reason (extracted for reuse, moved for readability, placed outside the call site by default). What Correct Specs Look Like A spec that is actually implementable names the function signature: _detectAutoZones(regions, numCols, pageWidth) : pageWidth is viewport.width || 612 , passed from assemblePage . That is two extra words. It removes all ambiguity. The implementer knows the parameter needs to exist. The reviewer can check that the call site passes it. The bug does not happen. The discipline: any time you write "the function uses X" in an architecture document, immediately write where X comes from. If it is a parameter, name it in the signature. If it is a module constant, name the constant. If it is a derived value, show the derivation. The Stacktrace Problem ReferenceErrors in Web Workers have a specific failure mode: the worker's error handler catches the error, serializes err.message (a string), and posts it to the main thread. The stack is not forwarded. The main thread reconstructs a new Error from the message string and throws it. DevTools shows the main thread throw, not the worker's. This means a ReferenceError in a worker looks like an error in the worker message handler, not in the actual throwing function. The real location is invisible. You find it by grepping for the identifier named in the error message. This is a general problem with any architecture that serializes errors across execution boundaries (workers, iframes, service workers, error-catching middleware). The message string is preserved. The stack is not. Every ReferenceError in such a system requires a grep rather than a stacktrace to locate. The Uncomfortable Implication If your architecture document has not specified where every value used by every function comes from, your implementation will have bugs that grep finds faster than debuggers. That is not a criticism of the implementer. It is a criticism of the spec. The solution is not more thorough prose. It is specifying function signatures explicitly, the same way you would in TypeScript or a statically-typed language. Write the types. Write the parameter names. Write where the values come from. Three lines of explicit signature beats three paragraphs of behavioral description every time.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/bonzai2carn/why-web-workers-swallow-your-stacktraces-and-how-to-write-specs-to-fix-it-56de

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
