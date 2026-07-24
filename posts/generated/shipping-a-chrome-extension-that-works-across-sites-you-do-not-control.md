---
title: "Shipping a Chrome Extension That Works Across Sites You Do Not Control"
slug: "shipping-a-chrome-extension-that-works-across-sites-you-do-not-control"
author: "Yu'an Zhou"
source: "devto_webdev"
published: "Fri, 24 Jul 2026 19:21:11 +0000"
description: "Building a Chrome extension that saves items from arbitrary third-party sites means every site is a hostile, unstable environment. Here is what actually brok..."
keywords: "you, page, review, chrome, not, dom, than, extension"
generated: "2026-07-24T19:37:11.867030"
---

# Shipping a Chrome Extension That Works Across Sites You Do Not Control

## Overview

Building a Chrome extension that saves items from arbitrary third-party sites means every site is a hostile, unstable environment. Here is what actually broke, and what held. Manifest V3 changes the shape of everything The persistent background page is gone. Service workers terminate — aggressively, after roughly 30 seconds of inactivity — and any in-memory state dies with them. Anything that must survive goes into chrome.storage : // ❌ dies with the worker let cache = {} // ✅ survives await chrome . storage . local . set ({ cache }) This is the single most common source of "works when I test it, fails in the wild" bugs. Your worker is alive during active testing and dead during real usage patterns. Content script isolation cuts both ways Content scripts run in an isolated world: you see the DOM, not the page's JavaScript. You cannot read the page's variables, and the page cannot see yours. Good for safety, awkward when the data you want lives in a framework's state rather than the DOM. Options are injecting into the main world (more risk, more capability) or scraping rendered DOM (fragile but isolated). I default to DOM scraping and accept the fragility. Selectors rot, so degrade instead of breaking Third-party markup changes without warning. A selector working today breaks next week with no notice and no error you will see. What helps: Layered fallbacks — semantic markup first ( article , [itemprop] , OpenGraph tags), site-specific selectors only as a last resort Fail visibly, not silently — if extraction fails, tell the user rather than saving an empty record Never assume shape — el?.textContent?.trim() ?? '' everywhere; a null deref in a content script can break the host page, which is much worse than your feature not working Permissions: ask for less <all_urls> triggers heavier review and scares users at install time. activeTab plus optional_host_permissions requested at first use is a better trade — fewer install-time objections, and review goes faster. Store review realities Justify every permission in the listing, specifically. Vague justifications get rejected. Privacy policy required if you touch user data at all. First review is slow; updates are usually much faster. A permission added later triggers full re-review — worth batching permission changes rather than shipping them one at a time. I shipped one of these for BabyNameAi — cross-site saving, a daily classical-poetry card, and offline lookup. Caveat Extension APIs are still shifting under MV3. Anything you read from before 2023 — including plenty of still-top-ranked results — may describe APIs that no longer exist.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/yuanjzhou/shipping-a-chrome-extension-that-works-across-sites-you-do-not-control-b64

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
