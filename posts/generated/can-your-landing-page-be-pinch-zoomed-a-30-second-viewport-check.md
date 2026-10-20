---
title: "Can your landing page be pinch-zoomed? A 30-second viewport check"
slug: "can-your-landing-page-be-pinch-zoomed-a-30-second-viewport-check"
author: "Kai Mercer"
source: "devto_webdev"
published: "Tue, 20 Oct 2026 11:06:16 +0000"
description: "One line in the <head> can stop people with low vision from reading your page, and it takes about thirty seconds to check. <meta name= "viewport" content= "w..."
keywords: "page, text, can, viewport, zoom, you, scale, user"
generated: "2026-10-20T11:14:04.643943"
---

# Can your landing page be pinch-zoomed? A 30-second viewport check

## Overview

One line in the <head> can stop people with low vision from reading your page, and it takes about thirty seconds to check. <meta name= "viewport" content= "width=device-width, initial-scale=1, user-scalable=no" > That user-scalable=no (or a low maximum-scale , like maximum-scale=1 ) is often copied in from a starter template to stop the page jumping around on mobile. The side effect is that people who need to zoom in can't. What the standards say MDN's page on the viewport meta tag has a warning about exactly this: setting user-scalable to no prevents people with low vision from being able to read and understand the page. It adds that WCAG requires a minimum of 2x scaling, and that the best practice is to allow 5x. It also notes that some browsers ignore the rule (iOS 10 and later does by default), so the line may not even do what you wanted. The WCAG requirement is success criterion 1.4.4, Resize Text: text can be resized without assistive technology up to 200 percent without loss of content or functionality. The W3C's "Understanding" page says the author's responsibility is to create content that does not prevent the browser from scaling it effectively. MDN, viewport meta: https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport W3C, Understanding 1.4.4 Resize Text: https://www.w3.org/WAI/WCAG22/Understanding/resize-text The 30-second check Open View Source (or DevTools, Elements) and search for viewport . If you see user-scalable=no , user-scalable=0 , or a maximum-scale below 2, remove it. Keep width=device-width, initial-scale=1 . That is all most pages need. On a phone, or in device mode in DevTools, pinch-zoom the page. Then zoom the browser text to 200% on desktop. What to look for after you fix it Removing the restriction can reveal layout problems that were hidden before. Check these at 200%: Does text get cut off or overlap other elements? Does a fixed header or cookie banner take up most of the screen? Do buttons stay reachable, or do they slide off-screen to the right? Does a form input still show what you typed? If the layout breaks, fix the layout (relative units, flexible containers), not the zoom setting. Blocking zoom hides the problem from you and leaves the people who need zoom to deal with it. It's a small thing, but it's one of the few accessibility checks that is a single line you can find with a text search.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/mercerk17/can-your-landing-page-be-pinch-zoomed-a-30-second-viewport-check-558h

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
