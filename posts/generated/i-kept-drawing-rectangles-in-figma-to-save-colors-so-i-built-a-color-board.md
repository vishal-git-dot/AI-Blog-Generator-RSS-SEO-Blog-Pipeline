---
title: "I kept drawing rectangles in Figma to save colors, so I built a color board"
slug: "i-kept-drawing-rectangles-in-figma-to-save-colors-so-i-built-a-color-board"
author: "Mike"
source: "devto_webdev"
published: "Wed, 21 Oct 2026 21:22:05 +0000"
description: "For years my color workflow was this: see a color I liked, open Figma, draw a rectangle, eyedrop the color into it, type the hex code underneath. Repeat unti..."
keywords: "color, hex, you, rectangles, figma, board, code, picker"
generated: "2026-10-21T21:27:30.864193"
---

# I kept drawing rectangles in Figma to save colors, so I built a color board

## Overview

For years my color workflow was this: see a color I liked, open Figma, draw a rectangle, eyedrop the color into it, type the hex code underneath. Repeat until the file was a mess of rectangles. Color picker apps solved half of it. They pick a color and copy the hex code, and then the color is gone. I wanted the rectangles, just without Figma. So I built PickXColor: a free color picker where every color you pick lands on an infinite board. What it does Press I and click any pixel on your screen. It uses the browser's EyeDropper API, so it works outside the browser tab too (Chrome, Edge and other Chromium browsers; Safari and Firefox get the system picker). Each color becomes a card named after the closest of about 5,000 color names. Click a card for HEX, RGB, HSL, HSV, OKLCH and CMYK values, Tailwind-style shades, WCAG contrast, and export code for CSS, Tailwind, SCSS, SwiftUI, Jetpack Compose and design tokens. Group cards with ⌘G, duplicate them, undo, pan and zoom. It's meant to feel like a design tool. Decisions I made No account. The board lives in your browser's local storage. That keeps the app free to run (it's a static site) and means there's nothing to sign up for. Paste anything. ⌘V accepts HEX, rgb(), hsl(), oklch() and CSS color names, in bulk. ⌘C copies a selection as a hex list you can paste anywhere. Names over numbers. "Radical Red" is easier to talk about in a design review than #FF385C. What's next If you work with color, I'd love your feedback: https://pickxcolor.com . What's the one thing you'd want on a color card that isn't there?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/mikepick/i-kept-drawing-rectangles-in-figma-to-save-colors-so-i-built-a-color-board-1k87

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
