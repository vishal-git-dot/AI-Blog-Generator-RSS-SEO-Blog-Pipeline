---
title: "I built a background remover that keeps the fine hair edges"
slug: "i-built-a-background-remover-that-keeps-the-fine-hair-edges"
author: "KunStudio"
source: "devto_webdev"
published: "Sun, 05 Jul 2026 03:51:35 +0000"
description: "Background removal is a solved problem right up until the image has hair, fur, or fine detail, and then most tools smear it into a halo. I built BG Remover t..."
keywords: "image, background, fine, hair, png, built, edges, clean"
generated: "2026-07-05T03:58:51.638904"
---

# I built a background remover that keeps the fine hair edges

## Overview

Background removal is a solved problem right up until the image has hair, fur, or fine detail, and then most tools smear it into a halo. I built BG Remover to get a clean, HD transparent PNG with crisp edges, including the hard parts like flyaway hair, and to do it per image without a subscription. It is aimed at the practical cases: product photos, portraits, and logos that need a transparent cutout to drop onto any background. Why I built it The two common options are a free tool that outputs a low-res result with rough edges, or a subscription service you pay monthly whether you cut out one image or a hundred. For someone who occasionally needs a clean cutout for a product listing or a portrait, both are a bad deal. I wanted HD quality and per-image pricing. How it works technically Hosting : Cloudflare Pages with Functions. Static front end, serverless image processing, fast globally. Model : It uses fal.ai's BiRefNet for the segmentation. BiRefNet is a strong matting model specifically because it handles fine boundaries, so hair and fur come out clean instead of as a blurry outline. Output : A transparent HD PNG, ready to place on any background. Payment : PayPal, priced per image. The single-image tier is $2.99. No subscription and no monthly lock-in. Price validation : The per-image charge is confirmed server-side before the processed PNG is returned, so the price can't be changed in the browser. Using it in three steps Upload your image. A product, a person, or a logo. It cuts it out. Clean HD edges, including fine hair and detail, in seconds. Download the PNG. A transparent PNG, ready to drop onto any background. Try it here: bg-remover-ks.pages.dev What I'd tell another builder The differentiator in a "solved" category is the edge case, literally. Anyone can remove a background from a photo shot against a white wall. The reason to pick one tool over another is what happens at the hairline. Choosing a matting model built for fine boundaries, rather than a generic segmentation model, is what makes the output usable instead of just fast.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/kunstudio/i-built-a-background-remover-that-keeps-the-fine-hair-edges-1c69

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
