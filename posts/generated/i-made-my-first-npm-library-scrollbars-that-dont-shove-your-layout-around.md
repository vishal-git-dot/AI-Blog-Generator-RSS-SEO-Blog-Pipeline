---
title: "I made my first npm library: scrollbars that don't shove your layout around 🙏"
slug: "i-made-my-first-npm-library-scrollbars-that-dont-shove-your-layout-around"
author: "hwan"
source: "devto_webdev"
published: "Mon, 23 Nov 2026 06:48:09 +0000"
description: "Hey everyone 👋 You know when a list gets one item longer, a scrollbar pops in, and everything jumps a few pixels to the left? Buttons move, text re-wraps, ce..."
keywords: "scrollbar, scroll, plz, first, your, one, what, library"
generated: "2026-11-23T06:53:29.698621"
---

# I made my first npm library: scrollbars that don't shove your layout around 🙏

## Overview

Hey everyone 👋 You know when a list gets one item longer, a scrollbar pops in, and everything jumps a few pixels to the left? Buttons move, text re-wraps, centered stuff is suddenly off-center. That annoyed me enough that I made a little library for it. It's my first one ever. One line, that's it import { MrScroll } from "plz-mr-scroll/react" ; < MrScroll /> Put it at the root of your app. You don't add anything to your components. Not using React? installMrScroll() from plz-mr-scroll does the same thing. What it actually does It finds every scroll area on the page and gives the scrollbar a spot that doesn't move your content: The area has enough right padding → it shrinks that padding by the scrollbar width The content is centered → it balances both sides so the center stays put The padding is on the parent → it floats the scrollbar just outside the area No room anywhere → it floats the scrollbar over the edge of the content No reserved gutter, and it's still the native scrollbar — not a custom-drawn one. Try it 👉 Live demo: https://justicehwan.github.io/plz-mr-scroll/ GitHub: https://github.com/justicehwan/plz-mr-scroll npm: https://www.npmjs.com/package/plz-mr-scroll Please tell me what's wrong with it 🥲 Since it's my first library, I honestly have no idea what I got wrong. If you have a minute, please try the demo and tell me what's broken, confusing, or just dumb. P.S. I'm Korean and English isn't my first language, so sorry if anything here reads a bit off. Thanks for reading!

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/justicehwan/i-made-my-first-npm-library-scrollbars-that-dont-shove-your-layout-around-4b39

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
