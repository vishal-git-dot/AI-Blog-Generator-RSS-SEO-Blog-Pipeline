---
title: "Google found my side page before my main feature"
slug: "google-found-my-side-page-before-my-main-feature"
author: "TattooTryOn"
source: "devto_webdev"
published: "Mon, 19 Oct 2026 03:40:26 +0000"
description: "I launched TattooTryOn a few days ago. You upload a photo of your arm or leg, drop a design on it, place it yourself, and an AI model turns the flat artwork ..."
keywords: "you, tattoo, page, photo, font, design, one, model"
generated: "2026-10-19T04:06:19.789214"
---

# Google found my side page before my main feature

## Overview

I launched TattooTryOn a few days ago. You upload a photo of your arm or leg, drop a design on it, place it yourself, and an AI model turns the flat artwork into something that looks like actual ink in skin. That's the product. That's the thing I spent most of my time on. Google doesn't care. This morning (Oct 19), Search Console showed the site's first impressions. Two queries: "tattoo design font generator" and "tattoo text font generator". Average position 24.8, so page three, nobody clicking. Still, it's the first signal I've had from search, and it points at the tattoo font generator , a side page I built almost as an afterthought. Nothing about the try-on. I find this a little funny and a little annoying. The numbers so far Plausible says that through Oct 18 the site had 13 unique visitors and 100 pageviews. Tiny. But the average visit was close to 11 minutes, which I didn't expect for a tool you could, in theory, use in one go. Where they came from: 7 direct, 6 from V2EX, 1 from Google. One V2EX post brought in about 40% of the visits. Visitors came from the US, China, Japan, and Thailand, which is a wider spread than 13 people should honestly produce. I'm not going to pretend these numbers mean much. They don't. But writing them down is useful, because in a month I'll want to know where I started. Why the font page might be the easier one to rank Thinking about it for more than five minutes, it makes sense. A query like "tattoo text font generator" describes exactly what the page does. Type some text, see it in a bunch of fonts, download a transparent PNG. The search intent and the page line up one-to-one. There's no explaining needed. "AI tattoo try-on" is a newer kind of thing. People search for it, but they phrase it a dozen different ways ("see tattoo on my arm", "tattoo preview app", "how would a tattoo look on me"), and the page has to convince you before it's useful. That's harder for a brand-new domain to win. Also, the font page is just text and fonts. No model, no credits, no waiting. It works the instant it loads, which probably doesn't hurt. Why it has no AI in it This is the part I actually care about from a dev point of view. Lettering is where image models are weakest. Ask one to render a name and you'll get letters that look plausible and are sometimes wrong. For a tattoo, one wrong letter is the whole problem. So the font generator just renders real font files on a canvas. A font file doesn't hallucinate. The try-on side is built around the same idea of not letting the model decide things it shouldn't. Placement happens in the browser by hand, before any model runs. The editor keeps a center point (normalized to the photo, so it survives resizing), a scale, and an angle. Before calling the renderer, those get baked into pixels. The model gets two pixel-aligned images: the original photo, and a composite with the design drawn onto it. // simplified function bake ( photo , design , { cx , cy , scale , angle }) { const c = new OffscreenCanvas ( photo . width , photo . height ); const ctx = c . getContext ( ' 2d ' ); ctx . drawImage ( photo , 0 , 0 ); ctx . translate ( cx * photo . width , cy * photo . height ); ctx . rotate ( angle ); ctx . scale ( scale , scale ); ctx . globalCompositeOperation = ' multiply ' ; ctx . drawImage ( design , - design . width / 2 , - design . height / 2 ); return c ; } The composite uses multiply blending, so ink can only darken skin, never lighten it. Skin texture shows through, and the preview you see in the editor looks the same as what gets sent to the model. There's also a body segmentation step that cuts the design out wherever it lands on clothes, hair or jewelry, so the model doesn't paint a tattoo onto your sleeve. Placement is free, too. You can move things around as long as you want and nothing is generated until you press the button. Maybe that's where some of those 11 minutes go. I don't know yet. What I'm doing with this Not much, honestly, other than paying attention. I'm not going to rebuild the homepage around fonts because of two queries at position 24.8. But it's a reminder that the simple, boring, clearly named page is often the one search engines understand first, and I should probably write landing pages for the try-on that describe it in plain words people actually type. And I should post on V2EX again, apparently. If you've launched something where the side tool got noticed before the main product, I'm curious whether you leaned into it or ignored it.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/tattootryon/google-found-my-side-page-before-my-main-feature-40fb

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
