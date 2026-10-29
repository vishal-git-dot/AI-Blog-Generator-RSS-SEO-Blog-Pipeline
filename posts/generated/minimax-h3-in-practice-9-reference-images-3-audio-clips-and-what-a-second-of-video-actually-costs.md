---
title: "MiniMax H3 in practice: 9 reference images, 3 audio clips, and what a second of video actually costs"
slug: "minimax-h3-in-practice-9-reference-images-3-audio-clips-and-what-a-second-of-video-actually-costs"
author: "chet100"
source: "devto_ai"
published: "Thu, 29 Oct 2026 12:35:10 +0000"
description: "MiniMax H3 is one of the few video models that accepts reference audio alongside reference images, which makes it interesting for anything with dialogue, amb..."
keywords: "reference, video, not, output, you, api, tier, job"
generated: "2026-10-29T12:39:59.120040"
---

# MiniMax H3 in practice: 9 reference images, 3 audio clips, and what a second of video actually costs

## Overview

MiniMax H3 is one of the few video models that accepts reference audio alongside reference images, which makes it interesting for anything with dialogue, ambience or a beat. But most write-ups stop at the demo reel. This post is the part I actually needed: what the tiers allow, how the credits are calculated, and the failure modes that cost us real debugging time. I work on Callirra, which exposes H3 through an API. The numbers below come from its live quote, including the ones that are inconvenient. The capability matrix is not one table, it is four H3 is sold in four output tiers, and each tier has its own duration window, aspect list and reference limits. Getting this wrong produces a 400 before the job exists, so you are not charged for the mistake, but you do lose the time. Tier Text to video Image to video Video to video 480P 1-15 s, 16:9 / 9:16 / 1:1 1-15 s, up to 9 images + 3 audio, first and last frame - 768P 1-15 s, 16:9 / 9:16 / 1:1 same as above 4-15 s, reference clip 1080P 1-10 s, 16:9 / 9:16 1-10 s, up to 9 images + 3 audio, lip sync - 2K 4-15 s, six ratios incl. 21:9 4-15 s, single first frame, six ratios 4-15 s Three things that are easy to miss: 1080P and 2K have different minimums. 1080P stops at 10 s; 2K starts at 4 s. A UI that offers "1-15 s" everywhere will fail on both ends. A 1:1 canvas at 1080P requires a reference image. Text-to-video at that ratio is rejected. Lip sync is an image-to-video mode , and it exists at 480P, 768P and 1080P, but not at 2K. What a second actually costs One credit is US$0.01. The tiers price per output second : Tier Credits / s USD / s 5 s 10 s 480P 1 $0.01 $0.05 $0.10 768P 2 $0.02 $0.10 $0.20 1080P 3 $0.03 $0.15 $0.30 2K 10 $0.10 $0.50 $1.00 Two caveats worth more than the table: Video-to-video is billed on input + output seconds , so a 10-second reference feeding a 10-second output is 20 seconds of charge. Reference clips are accepted in the 2-15 s range; anything outside is rejected before the job is created. The reservation is not the final bill. It is computed from duration multiplied by the tier rate up front, then settled; a failed, cancelled or expired job releases it in full. For comparison: MiniMax's own published list price for 768P output was $0.08/s when I checked on 25 October 2026. Check their pricing page before you quote that number anywhere, because provider prices move. Calling it https://api.callirra.com , bearer key, two calls: create, then poll. const headers = { authorization : `Bearer ${ process . env . CALLIRRA_API_KEY } ` , ' content-type ' : ' application/json ' , }; const created = await fetch ( ' https://api.callirra.com/v1/videos ' , { method : ' POST ' , headers , body : JSON . stringify ({ model : ' minimax-h3 ' , mode : ' image_to_video ' , prompt : ' Slow push in as the wind lifts the scarf; the camera settles on the eyes. ' , resolution : ' 768p ' , duration_seconds : 5 , aspect_ratio : ' 16:9 ' , frame_images : [ ' https://example.com/ref-01.jpg ' ], }), }); const { job } = await created . json (); // { id, status, credits_reserved } let state ; for ( let i = 0 ; i < 120 ; i += 1 ) { const r = await fetch ( `https://api.callirra.com/v1/videos/ ${ job . id } ` , { headers }); state = ( await r . json ()). job ; if ([ ' completed ' , ' failed ' , ' cancelled ' , ' expired ' ]. includes ( state . status )) break ; await new Promise (( done ) => setTimeout ( done , 5000 )); } console . log ( state . status , state . content_url ); // signed URL, short lived credits_reserved comes back as a string of internal units; divide by 100 for public credits if you are building a cost display. Failure modes that cost me an afternoon content_policy is a real error code , and it refunds. H3 runs a provider-side safety check on the output; a rejected render bills nothing but does end the job. Aspect ratios are validated per scene, not per model. 1:1 at 1080P needs a reference image; 21:9 only exists at 2K. Duration is integer seconds. Fractional durations are rounded, which silently changes the price you quoted a user. Free-tier output is watermarked; paid output is not. If you build a demo on a free account, the watermark is a product decision, not a bug. What I would build with it Nine reference images plus three audio clips is enough to hold a character, a location, a wardrobe and a voice across a series of shots, which is the actual bottleneck in short-form production. The 480P tier at a cent a second is cheap enough to storyboard at volume, and 1080P at three cents is where you render the takes you keep. The full tier table and per-model quotes are at callirra.com/minimax-h3 , and the API contract at callirra.com/api . If something here does not match what the API returns today, tell me; I would rather correct the post than leave a wrong table on the internet.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/chet103cc/minimax-h3-in-practice-9-reference-images-3-audio-clips-and-what-a-second-of-video-actually-costs-44a6

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
