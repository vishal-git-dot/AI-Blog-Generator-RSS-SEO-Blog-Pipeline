---
title: "RightClick Unchained is on the Chrome Web Store"
slug: "rightclick-unchained-is-on-the-chrome-web-store"
author: "Jehadur Rahman Emran"
source: "devto_webdev"
published: "Fri, 27 Nov 2026 20:51:17 +0000"
description: "Some websites turn off the context menu, stop you from selecting text, or intercept Ctrl+C and Ctrl+V. RightClick Unchained turns those browser basics back o..."
keywords: "site, you, text, click, copy, page, chrome, ctrl"
generated: "2026-11-27T20:56:45.961220"
---

# RightClick Unchained is on the Chrome Web Store

## Overview

Some websites turn off the context menu, stop you from selecting text, or intercept Ctrl+C and Ctrl+V. RightClick Unchained turns those browser basics back on, and you choose where it runs. It is now live on the Chrome Web Store as v1.0.2 (the public listing was updated 23 November 2026). The source is MIT: JehadurRE/rightclick-unchained . What it unblocks Right-click: the normal browser context menu comes back Text selection and drag, including pages that set user-select: none Copy and cut (Ctrl+C / Ctrl+X) Paste into form and password fields that block Ctrl+V Each of the four can be switched on or off on its own. The store listing and the source agree on this; I am not adding claims beyond that. Two modes, per site Smart (the default) lets the site's own scripts keep running, but they can no longer cancel right-click, select, copy, or paste. Menus and widgets on the page should keep working. Absolute is for stubborn pages: blocking listeners for those actions are never attached, and stronger selection CSS is applied. The popup has one switch for the current site, and you can pick Smart or Absolute per domain. There is also a settings page to add, change, pause, or delete site rules. Tools and shortcuts Text Lasso : click a block of text, or drag a box over part of the page, and the text is copied Force Copy : copies the current selection even when the site blocks copying Keyboard shortcuts (changeable at chrome://extensions/shortcuts ): Alt+Shift+U opens the popup, Alt+Shift+R toggles the current site, Alt+Shift+C force-copies the selection Why it is Manifest V3 Older "enable right-click" extensions were written for Manifest V2. This one is built as Manifest V3, with a content script in the page's own world ( world: "MAIN" ) at document_start , plus a separate isolated script for UI, CSS, and settings. The idea is to be in place before the site's own listeners attach, without violating the page's Content Security Policy. Privacy No analytics, no ads, no tracking, no remote code, and no network requests from the extension itself. Site rules stay in chrome.storage.local . You can export or import settings as JSON. It has to run on the pages you visit, because copy and right-click blocking can happen on any site. It only changes how those pages handle right-click, select, copy, cut, paste, and drag. It does not send page content anywhere. Please respect copyright and each site's terms when you copy content. Install Chrome Web Store listing Or load the repo as an unpacked extension from GitHub . I am JehadurRE. If a specific site still blocks selection after you try Absolute mode and Text Lasso, open an issue with the URL and I will take a look.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/jehadurre/rightclick-unchained-is-on-the-chrome-web-store-55dg

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
