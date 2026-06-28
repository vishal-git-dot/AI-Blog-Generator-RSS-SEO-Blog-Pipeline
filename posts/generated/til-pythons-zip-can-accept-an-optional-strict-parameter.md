---
title: "TIL: Python's `zip()` can accept an optional `strict` parameter"
slug: "til-pythons-zip-can-accept-an-optional-strict-parameter"
author: "qing"
source: "devto_python"
published: "Sun, 28 Jun 2026 04:02:42 +0000"
description: "TIL: Python's zip() can accept an optional strict parameter If you're like me, you've probably used Python's built-in zip() function countless times to itera..."
keywords: "python, zip, optional, strict, parameter, you, lists, til"
generated: "2026-06-28T04:20:44.691027"
---

# TIL: Python's `zip()` can accept an optional `strict` parameter

## Overview

TIL: Python's zip() can accept an optional strict parameter If you're like me, you've probably used Python's built-in zip() function countless times to iterate over multiple lists in parallel. However, have you ever stopped to think about what happens when the lists are of different lengths? Prior to Python 3.10, zip() would simply stop at the end of the shortest list, potentially leading to silent data loss. As of Python 3.10, zip() now accepts an optional strict parameter, which defaults to False . When set to True , zip() will raise a ValueError if the input lists are of different lengths. Here's an example: python --- *Follow me on Dev.to for daily Python tips and quick guides!*

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/qingluan/til-pythons-zip-can-accept-an-optional-strict-parameter-4e9h

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
