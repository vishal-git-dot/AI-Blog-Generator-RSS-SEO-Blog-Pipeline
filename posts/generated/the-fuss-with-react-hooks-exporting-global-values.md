---
title: "The fuss with React hooks exporting global values"
slug: "the-fuss-with-react-hooks-exporting-global-values"
author: "Muhammad Bin Zafar"
source: "devto_webdev"
published: "Wed, 26 Aug 2026 01:29:24 +0000"
description: "TLDR: it doesn't work. You can't ever have a React hook that exports memoized global values. EVER. This is my finding here. I had forgotten the JavaScript es..."
keywords: "values, global, hook, javascript, react, right, object, usecartitems"
generated: "2026-08-26T01:41:06.768261"
---

# The fuss with React hooks exporting global values

## Overview

TLDR: it doesn't work. You can't ever have a React hook that exports memoized global values. EVER. This is my finding here. I had forgotten the JavaScript essentials due to the React essentials. useMemo() caches values and recalculates when the deps change, right? So, when I return an object from a hook like useCartItems(), all components that use the hook should be re-rendered, right? Right??? Having the muscle memory that top-level code in a regular JavaScript file are executed only once, and that the exported values of a file are cached - I mistakenly wrote code thinking the returning values of a hook are being cached as well. A wrong assumption. And the result is 2 days of painful debugging. From a JavaScript POV, I should've at least noticed the '()' at the end of useCartItems(). Meaning, the hooks (which are JavaScript function declarations) are being invoked every time. So, the add, remove, etc operations in this returning object { list: Object[], add: Function, remove: Function, ...} are localized. So, the const ci = useCartItems() instance for the modal and for the are never in sync. They are separate and localized, not global. Conclusion Rookie mistake. Should've used Zustand global stores or the Context API from the get-go - instead of taking up a challenge to explore unorthodox approaches :D

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/midnqp/the-fuss-with-react-hooks-exporting-global-values-6l6

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
