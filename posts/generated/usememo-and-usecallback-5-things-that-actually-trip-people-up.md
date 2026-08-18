---
title: "useMemo and useCallback: 5 things that actually trip people up"
slug: "usememo-and-usecallback-5-things-that-actually-trip-people-up"
author: "Tarun Sharma"
source: "devto_webdev"
published: "Tue, 18 Aug 2026 12:47:54 +0000"
description: "Both of these get memorized as syntax pretty fast. What doesn't get memorized is what they're actually doing under the hood, and that's where the bugs show u..."
keywords: "you, function, usememo, usecallback, every, render, actually, value"
generated: "2026-08-18T12:55:35.958851"
---

# useMemo and useCallback: 5 things that actually trip people up

## Overview

Both of these get memorized as syntax pretty fast. What doesn't get memorized is what they're actually doing under the hood, and that's where the bugs show up. Here's the stuff that actually trips people up once you go past "wrap it in useMemo I guess." 1. They solve different problems, not the same one useMemo caches a value. useCallback caches a function reference. People treat them like interchangeable "make it faster" hooks, but useCallback(fn, deps) is really just useMemo(() => fn, deps) under the hood, it just hands you back the function itself instead of calling it for you. 2. Neither one makes your code faster by default Wrapping something in useMemo has a cost too, it runs the dependency comparison on every render. If the calculation inside is cheap, you're paying more than you save. Reach for these when the calculation is genuinely expensive, or when the value needs to keep the same reference across renders (see #3), not as a reflex on every derived value. 3. The real reason you need useCallback: keeping props stable for React.memo If you pass a normal inline function as a prop to a memoized child, that child re-renders anyway, because the function is a new reference every single render. useCallback is what actually keeps that reference stable across renders so React.memo 's shallow comparison has something to bail out on. Without it, memo is comparing a new function to another new function every time and always finding them "different." 4. The dependency array lies just as easily here as with useEffect Same stale closure trap you'd hit with useEffect . If you memoize a function with useCallback(fn, []) and fn reads a prop or state value from outside, you get a function frozen with whatever that value was on the first render. The fix is the same one as always: put it in the deps array, don't fight the linter into silence. 5. Object and array literals as deps break memoization silently useMemo(() => doSomething(config), [config]) looks safe until config is { foo: bar } created inline on every render, in which case the dependency is a new reference every time and the memo never actually hits, it recalculates every render while looking like it's working. Move the object outside the render, or memoize it too. Curious what the actual useMemo or useCallback bug was that got you. Drop it below, would love to hear it.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/101beardo/usememo-and-usecallback-5-things-that-actually-trip-people-up-4o0l

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
