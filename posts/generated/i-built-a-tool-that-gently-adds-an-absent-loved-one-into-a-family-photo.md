---
title: "I built a tool that gently adds an absent loved one into a family photo"
slug: "i-built-a-tool-that-gently-adds-an-absent-loved-one-into-a-family-photo"
author: "KunStudio"
source: "devto_webdev"
published: "Sun, 05 Jul 2026 03:50:44 +0000"
description: "Some family photos have a person-shaped gap in them. A grandparent who passed before the reunion. A family member deployed or living overseas who couldn't ma..."
keywords: "photo, one, not, person, picture, photos, light, image"
generated: "2026-07-05T03:58:51.639122"
---

# I built a tool that gently adds an absent loved one into a family photo

## Overview

Some family photos have a person-shaped gap in them. A grandparent who passed before the reunion. A family member deployed or living overseas who couldn't make the shot. Memorial Merge gently adds that person into the group photo as one natural picture, with matched light and tones. I want to be careful about how I describe this. It is not a novelty face-swap. It is meant for a specific, tender use: bringing someone who couldn't be there into a picture, with care. Why I built it People already do this by hand in Photoshop, badly, for exactly this reason, and it takes skill most families don't have. The hard part is not pasting a cutout in, it is making the added person look like they were standing in the same room under the same light. That is a matching problem, not a collage problem. How it works technically Hosting : Cloudflare Pages with Functions. Serverless, fast, nothing to maintain. Image model : It uses fal.ai to blend the two photos into a single image, matching lighting and color tones so the added person reads as part of the original scene rather than pasted on top. Two inputs, one output : You upload the group photo and a clear photo of the person to add. The result is one combined picture. Privacy : The uploaded photos are used only to produce your image. Given the subject matter, this is not a nice-to-have, it is the point. Payment : A one-time PayPal charge. No subscription, because this is a once-in-a-while, meaningful purchase, not a recurring habit. Price validation : The charge is verified server-side before the combined image is delivered. Using it in three steps Upload the group photo. The picture you want your loved one to join. Upload their photo. A clear photo of the person to add. Receive one photo. The two are blended into a single natural picture, with matched light and tones. Try it here: memorial-merge.pages.dev What I'd tell another builder For sensitive products, the technical work and the tone of the product are not separate tracks. The privacy stance, the careful copy, and the light-matching quality are all the same promise: treat these photos with the weight they carry. If you build in a space like this, the restraint is a feature, not a limitation.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/kunstudio/i-built-a-tool-that-gently-adds-an-absent-loved-one-into-a-family-photo-1p6i

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
