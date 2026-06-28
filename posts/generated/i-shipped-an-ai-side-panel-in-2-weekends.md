---
title: "I shipped an AI side panel in 2 weekends"
slug: "i-shipped-an-ai-side-panel-in-2-weekends"
author: "AI Buddy"
source: "devto_webdev"
published: "Sun, 28 Jun 2026 04:06:28 +0000"
description: "I am going to talk about shipping speed, because that is what the last two months have been about for me. The setup I had an idea for a Chrome extension: hig..."
keywords: "panel, chrome, side, had, hours, two, saturday, openai"
generated: "2026-06-28T04:20:44.692994"
---

# I shipped an AI side panel in 2 weekends

## Overview

I am going to talk about shipping speed, because that is what the last two months have been about for me. The setup I had an idea for a Chrome extension: highlight text, send it to ChatGPT, see the reply in a side panel. I had used three different tools that did parts of this and none of them worked the way I wanted. I gave myself two weekends. Saturday and Sunday, week one, build the MVP. Saturday and Sunday, week two, polish. Monday, submit to the Chrome Web Store. That was the plan. Weekend 1 I started Saturday morning at 9. By lunch I had a popup window that opened ChatGPT with the selected text pre-filled. That was the wrong UX. It broke the workflow because now I had two things on screen and the original page was pushed aside. I ate lunch, came back, and decided to do a side panel instead. The Chrome side panel API exists. It is documented in like 4 paragraphs and most of the documentation is about coloring and sizing. I had to read the source of one example extension to figure out how to make the panel persist across page navigations. By Sunday evening I had: select text, click a button, see a ChatGPT-style reply in a side panel. The reply was hardcoded to a single fake response. The selected text was passed via chrome.storage.session . Nothing was wired to a real model yet. Total weekend 1 time: about 14 hours. That included a 2-hour detour into the popup-window approach that I threw away. Weekend 2 Saturday was wiring it to the OpenAI API directly. No backend. The user's API key goes into Chrome local storage. The selected text gets sent to OpenAI with a system prompt I wrote. The reply streams into the side panel. That was the day I learned that Chrome extensions cannot use fetch from a side panel because of a CSP issue I did not know about. I burned 3 hours on it. The fix was to put the fetch call in the background service worker and stream the response back to the side panel via chrome.runtime.sendMessage . By Saturday night it worked end to end with OpenAI. Sunday was multi-model. Add Claude, add Gemini, add DeepSeek. Each one needed a different base URL, a different request shape, a different way to parse the streaming response. The OpenAI-compatible APIs (Claude via OpenRouter, Gemini via OpenRouter, DeepSeek direct) made this easier than it would have been, but it still took 6 hours of testing each one. By Sunday night I had 4 models working. I packaged it and uploaded it to the Chrome Web Store. Total weekend 2 time: about 16 hours. The CSP debugging ate a real chunk of Saturday. After submission Chrome Web Store review took 3 days. It was approved on Wednesday. I posted about it on Reddit, X, and Indie Hackers. The first 48 hours I got about 9 users. That is much fewer than I hoped. The next 5 weeks I got 6 more. So 15 users after about 5 weeks total. What I learned 1. Shipping is faster than I thought. Two weekends was realistic because the side panel API is small and most of the work was plumbing I had done before. 2. CSP is going to waste your time. If you build a Chrome extension with a side panel that talks to external APIs, budget 4 hours for the service worker + sendMessage dance. There is no good documentation for it. 3. The OpenAI-compatible API ecosystem is the real win. Three of the four models I support are reachable through the OpenAI request shape. That cut my integration work in half. 4. 15 users in 5 weeks is not enough. I knew this intellectually. Now I know it from sitting at my dashboard at 11pm refreshing the count. Distribution is the whole game. Building is the easy part. 5. The thing that slowed me down the most was not building. It was convincing myself the side panel UX was the right one. I should have started there instead of the popup window. What I would do differently I would spend more time on the listing page before submission. The first 48 hours of traffic came mostly from people who clicked my Reddit post, landed on the Chrome Web Store page, and bounced. The description was not clear enough about what the extension does in the first sentence. That is a fixable problem. The hard part is done. If you are building a Chrome extension and want to see how the side panel is wired, the source is on GitHub. The relevant file is sidepanel.js and the service worker is background.js . There are comments. Chrome Web Store GitHub What did your last two-weekend project look like?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/cwsaibuddy/i-shipped-an-ai-side-panel-in-2-weekends-5e5h

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
