---
title: "Keep an Accessible Combobox Stable When Search Results Arrive Out of Order"
slug: "keep-an-accessible-combobox-stable-when-search-results-arrive-out-of-order"
author: "babycat"
source: "devto_webdev"
published: "Mon, 20 Jul 2026 03:18:24 +0000"
description: "An accessible combobox can follow the correct ARIA pattern and still become unusable when two search responses arrive in the wrong order. Reproduce this sequ..."
keywords: "cat, search, aria, response, generation, combobox, when, arrives"
generated: "2026-07-20T03:39:19.784490"
---

# Keep an Accessible Combobox Stable When Search Results Arrive Out of Order

## Overview

An accessible combobox can follow the correct ARIA pattern and still become unusable when two search responses arrive in the wrong order. Reproduce this sequence: Type ca , then quickly type cat . The cat response arrives first and highlights cat facts . The slower ca response arrives and replaces the list. aria-activedescendant now points to an option that no longer exists. IME input adds another boundary: searching during composition can send partial text the user has not committed. I would model the request generation explicitly: let generation = 0 ; let composing = false ; async function search ( query : string ) { const mine = ++ generation ; const options = await fetchOptions ( query ); if ( mine !== generation || composing ) return ; render ( options ); restoreActiveOptionByKey (); } The stable key matters. An array index cannot preserve the active option when ranking changes. Regression matrix Input Injected failure Expected evidence ca → cat first request delayed only cat results render Arrow Down result refresh active key survives or resets visibly Escape response arrives afterward popup stays closed IME composition network is fast no request until compositionend A Playwright test should assert focus remains on the input, every aria-activedescendant resolves to a live element, and Escape invalidates outstanding generations. A manual screen-reader pass should confirm result-count announcements are not emitted for discarded responses. The WAI-ARIA Authoring Practices combobox pattern defines the keyboard contract. The missing production step is testing that contract under asynchronous replacement, not only against static example data. Which stale-response failure has been hardest to reproduce in your search UI?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/babycat/keep-an-accessible-combobox-stable-when-search-results-arrive-out-of-order-3bdi

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
