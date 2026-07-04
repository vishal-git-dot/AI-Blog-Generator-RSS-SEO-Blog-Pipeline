---
title: "AI For Fun! Électrique Chats at Hack the Kitty, Built with Kiro."
slug: "ai-for-fun-lectrique-chats-at-hack-the-kitty-built-with-kiro"
author: "L. Cordero"
source: "devto_webdev"
published: "Sat, 04 Jul 2026 03:14:14 +0000"
description: "A cat astrologer, spec-driven and running on Amazon Bedrock A companion to A Builder in Paris: Do Devs Dream of Électrique Chats? Last month I wrote about th..."
keywords: "not, one, build, kiro, them, madame, but, sign"
generated: "2026-07-04T03:39:49.959642"
---

# AI For Fun! Électrique Chats at Hack the Kitty, Built with Kiro.

## Overview

A cat astrologer, spec-driven and running on Amazon Bedrock A companion to A Builder in Paris: Do Devs Dream of Électrique Chats? Last month I wrote about the idea. Six rainy days in Paris, a closed laptop, and a hackathon I did not mean to enter, and somewhere between the Musée de l'Orangerie and a lot of walking, an idea arrived. Cats are inscrutable. The people who love them are obsessed with understanding them anyway. Astrology is an old framework for making the unknowable feel readable, and maybe, just maybe, it helps us understand them a little. Her name is Madame Minou , a French cat astrologer who reads your cat's stars from a café terrace. That first article was the idea . This one is the build. Vibe-coded, but on rails Was it vibe-coded? You know it! AI wrote most of the lines, and I said "no, not like that" more times than I can count. But it was vibe-coding on rails, and the rails were Kiro. Before a single line of app code, I wrote the requirements in EARS notation, a design doc, and a build-ordered task list, all living in .kiro/specs . Decide what "done" means before letting anyone, human or model, start building. The specs are what kept the vibes on track. Then the steering files. .kiro/steering held the enduring rules of the project: product principles, security guardrails, technical direction, and UI law. These were the thing that kept a long, multi-session build from drifting. When a new session opened, the steering files were already the shared context. "The café blue" was one token, not five guesses. Security was not optional. The garbled café sign was a deliberate easter egg, not a bug to fix. From there, the loop: Kiro implemented one approved block at a time, ran each task's PASS/FAIL QA gate on itself before moving to the next, and only stopped for my review on the two things that actually mattered. I directed and approved. Kiro proposed and built. Spec first, block by block, human in the loop. The facts are sacred Here is the part that looks like a party trick and isn't. Madame never guesses the chart. The sun sign is computed in code, deterministically. The model only writes the voice over the facts it is handed. It cannot invent a sign, because the facts come first. Deterministic structure, AI flavor. The astrology is the vocabulary; the structure underneath is the catnip. All in on AWS Claude runs through Amazon Bedrock on IAM, which means there is not a single API key anywhere in the stack. Lambda, API Gateway, and DynamoDB run the readings and a real per-IP freemium gate. S3 and CloudFront serve the café. What broke during the build I promised myself limitations language would be a feature, so here is the struggle bus story, not the tidy one. I started on the Claude Platform on AWS path and hit a wall: my hackathon account could not complete the Marketplace subscription. So I pivoted to Amazon Bedrock, where my Claude access actually lived, and the whole thing got simpler. I wanted real ephemeris math for moon and rising signs, but pyswisseph is a native C extension with no Python 3.13 wheel, and it would not compile in the build environment I had. Rather than fight a compiler at nine at night, I shipped a pure-Python sun sign (it is just a date-range lookup, no ephemeris required) and moved moon and rising to v2. Sun sign is most of the value, and now it is rock solid instead of theoretical. And the deploy. A reserved AWS_REGION env var that failed the whole stack. A Lambda that returned "internal server error" because the build packaged the handler but not the server module it imported. CORS. A missing paragraph renderer. Every one of them a real bug, every one of them a one-line fix once I stopped guessing and read the actual error. Powered by NLP but humbled by CORS! What I cut Moon and rising signs. The pyswisseph build wall. A Lambda layer is the v2 fix. Daily nudge and history. Shipped as honest "coming soon" stubs, not half-features. Wider birth-city coverage, a premium tier, a custom domain, the exact Paris Métro font. All real, all v2. Shipped honest, not complete. For Penelope Madame Minou is for Penelope. Tuxedo, my wife's BFF and my fourteen-year frenemy, who I was allergic to the whole time and could barely pet. She passed in February. This is the first thing I have built for a cat I never quite got to hold. There is a quiet link in the app, in her memory, to the Lap of Love Angel Fund. Because the stars are just a beautiful vocabulary for love. Try Madame Minou: https://dghcwayx8gb6b.cloudfront.net Code: https://github.com/earlgreyhot1701D/madame-minou Built for Hack the Kitty AI Assisted. Human Reviewed. Powered by NLP.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/earlgreyhot1701d/ai-for-fun-electric-chats-at-hack-the-kitty-built-with-kiro-849

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
