---
title: "Python Day 7: Positional-Only, Keyword-Only Arguments and Return Statement"
slug: "python-day-7-positional-only-keyword-only-arguments-and-return-statement"
author: "Vasanthakumari N"
source: "devto_python"
published: "Sat, 21 Nov 2026 06:26:42 +0000"
description: "1. Positional-Only Arguments (/) In Python, / is used as a positional-only argument separator. It means that the parameters written before / must be passed u..."
keywords: "only, positional, keyword, calculate, arguments, parameters, passed, return"
generated: "2026-11-21T06:33:10.792255"
---

# Python Day 7: Positional-Only, Keyword-Only Arguments and Return Statement

## Overview

1. Positional-Only Arguments (/) In Python, / is used as a positional-only argument separator. It means that the parameters written before / must be passed using their position. We cannot pass them using parameter names (keyword arguments). Example: def calculate ( a , b , / ) : print ( a + b ) calculate ( 10 , 20 ) # 30 calculate ( a = 10 , b = 20 ) # TypeError TypeError: calculate() got some positional-only arguments passed as keyword arguments Here, a and b must be passed as positional arguments. 2. Keyword-Only Arguments (*) In Python, * can be used as a keyword-only argument separator. It means that the parameters written after * must be passed using their parameter names. Example: def calculate ( a , * , b ) : print ( a + b ) calculate ( a = 10 , b = 20 ) # 30 calculate ( 10 , b = 20 ) # 30 calculate ( 10 , 20 ) # Error TypeError: calculate() takes 1 positional argument but 2 were given Here: a can be passed as either a positional or keyword argument. b must be passed as a keyword argument. Difference Between / and * Symbol Meaning / Parameters before it are positional-only * Parameters after it are keyword-only Remember: / separates positional-only parameters. * separates keyword-only parameters. Return Statement in Python The return statement is used to send a value from a function back to the place where the function was called. Example: def play ( ) : teamA = 300 teamB = 290 if teamA > teamB : return "Winner Trophy" else : return "Runner Trophy" hand = play ( ) print ( hand ) Output: Winner Trophy

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/vasanthakumari_n/python-day-7-positional-only-keyword-only-arguments-and-return-statement-1j3k

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
