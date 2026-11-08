---
title: "How much data can a QR code actually hold?"
slug: "how-much-data-can-a-qr-code-actually-hold"
author: "Rahman"
source: "devto_webdev"
published: "Sun, 08 Nov 2026 21:35:46 +0000"
description: "Short answer: more than you'll ever need for a link, and less than you'd think once you care about scanning. Let's unpack it. It's a grid of modules A QR cod..."
keywords: "code, version, you, modules, more, data, short, grid"
generated: "2026-11-08T21:52:37.461309"
---

# How much data can a QR code actually hold?

## Overview

Short answer: more than you'll ever need for a link, and less than you'd think once you care about scanning. Let's unpack it. It's a grid of modules A QR code is a square grid of little cells called modules. The spec defines 40 sizes, called versions: version 1 is 21x21 modules, version 40 is 177x177. The more data you encode, the higher the version the generator has to use, so the more modules get packed into the same printed square. The theoretical maximums At the largest version with the lightest error correction, a single QR code can hold roughly: 7,089 numeric digits 4,296 alphanumeric characters 2,953 bytes of raw binary Those are ceilings, not targets. Hitting them means a dense version-40 code that a phone struggles to read unless it's printed large and scanned up close. Error correction eats into the budget QR codes have four error-correction levels: L, M, Q, H, recovering roughly 7, 15, 25, and 30 percent of the code if it's damaged. Higher protection is great for stickers and logos, but it costs capacity: the recovery data lives in the same grid, so the more you reserve for resilience, the less room is left for your actual content. The practical takeaway You almost never want to approach these limits. A long URL or a full contact card bloats the version, shrinks every module at print size, and makes the code fragile. Keep the content short, or point the code at a short link that redirects. A low-version code has big, chunky modules that scan fast from across a room, and that's the whole game. I help build QRolling , so I'm not neutral, but this holds with any generator.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/rehman258/how-much-data-can-a-qr-code-actually-hold-1gpb

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
