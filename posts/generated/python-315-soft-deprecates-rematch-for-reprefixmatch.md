---
title: "Python 3.15 soft-deprecates re.match() for re.prefixmatch"
slug: "python-315-soft-deprecates-rematch-for-reprefixmatch"
author: "techaiwire"
source: "devto_python"
published: "Sat, 12 Sep 2026 20:12:29 +0000"
description: "Python 3.15 adds a function called re.prefixmatch() and marks the 30-year-old re.match() as soft deprecated in its place. The two do exactly the same thing. ..."
keywords: "python, match, prefixmatch, soft, name, new, pattern, not"
generated: "2026-09-12T20:23:47.691060"
---

# Python 3.15 soft-deprecates re.match() for re.prefixmatch

## Overview

Python 3.15 adds a function called re.prefixmatch() and marks the 30-year-old re.match() as soft deprecated in its place. The two do exactly the same thing. The change is about the name, because match has meant the wrong thing in Python for as long as the function has existed. The Python 3.15 documentation for the re module states the reasoning directly. The new name is "more explicitly descriptive," it says, and developers should "use it to better express intent." In most other languages, the documentation notes, match refers to the behavior Python has always called search() . The naming problem Python's re.match() only looks at the start of a string. It anchors at position zero, and it stops there. re.search() scans the whole string for the pattern anywhere in it. Most other languages do the opposite. Their "match" is Python's "search." A developer arriving from JavaScript, Ruby or Go reads re.match() and reasonably expects it to find the pattern anywhere. It does not, and the bug that follows is silent: the code simply returns None on input it should have handled. re . match ( " world " , " hello world " ) # None - anchored at the start re . prefixmatch ( " world " , " hello world " ) # None - same function, clearer name re . search ( " world " , " hello world " ) # matches Hugo van Kemenade laid out the case in a blog post published September 10, 2026 , citing the Zen of Python: "Explicit is better than implicit. Anyone reading the name prefixmatch() is likely to understand the intended semantics." Both the module-level function and the compiled-pattern method get the new name. re.Pattern.prefixmatch() joins re.prefixmatch() in 3.15. What "soft deprecated" actually means Soft deprecation is a specific process defined in PEP 387 , Python's backwards compatibility policy. It is much weaker than a normal deprecation, and the difference matters for anyone maintaining older code. Soft deprecation Normal deprecation Runtime warning None DeprecationWarning Removal scheduled No Yes, in a named version Stays documented and tested Yes Yes, until removal Receives new features No No PEP 387 defines it as "using an API which should no longer be used to write new code, but it remains safe to continue using it in existing code." It also says plainly that soft deprecation "does not issue a warning: it's only mentioned in the documentation." So re.match() keeps working. It is not scheduled for removal. Your test suite will not start printing warnings when you move to 3.15, and python -W error will not fail on it. Which of the four to reach for The re module now offers four ways to run a pattern against a string, and they differ only in where the pattern is allowed to sit. Function Matches Added in re.prefixmatch() At the start only 3.15 re.match() At the start only, soft deprecated 1.5 re.search() Anywhere in the string 1.5 re.fullmatch() The entire string, start to end 3.4 What this means for developers Do nothing urgent. This is the rare API change that asks for no migration, sets no deadline and breaks no code. For new code on 3.15 or later, write re.prefixmatch() . The name tells the next reader what the call actually does, which is the whole point of the change. For existing code, the useful exercise is not a find-and-replace. It is an audit. Every re.match() call in your codebase is a place where someone may have meant re.search() . The tests would not catch it if they only ever passed input where the pattern sat at the front. Those are real bugs that predate 3.15, and a quick grep will find the candidates faster than any tool. Be careful about jumping straight to re.prefixmatch() in a library, though. Calling it makes your package require Python 3.15 or newer, and re.match() is the version-portable spelling until your minimum supported version catches up. Large codebases live with that gap for years; EVE Online's developers began their Python 3 migration long after the version split. The wider signal is worth noting. The Python core team is willing to spend a new name and a documentation note purely to make an old API read correctly, without forcing anyone to change a line. That is a cheap kind of cleanup, and the more of it Python does, the fewer silent None returns the next generation of Python developers has to debug. This article was first published on Tech AI Wire . Also available in Deutsch · 日本語 · Français · Español · Português Related on Tech AI Wire EVE Online begins moving 2.4 million lines of Python 2 to Python 3 Sources Soft-deprecating re.match() - hugovk.dev re - Regular expression operations (Python 3.15) - Python documentation What's New In Python 3.15 - Python documentation PEP 387 - Backwards Compatibility Policy - Python Enhancement Proposals

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/techaiwire/python-315-soft-deprecates-rematch-for-reprefixmatch-4o59

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
