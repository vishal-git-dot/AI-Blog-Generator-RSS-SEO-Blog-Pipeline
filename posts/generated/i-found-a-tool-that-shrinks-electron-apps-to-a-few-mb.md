---
title: "I Found a Tool That Shrinks Electron Apps to a Few MB"
slug: "i-found-a-tool-that-shrinks-electron-apps-to-a-few-mb"
author: "Alex"
source: "devto_webdev"
published: "Sat, 20 Jun 2026 19:33:10 +0000"
description: "I stumbled on Pake today. It’s sitting at 2,400 stars on GitHub. That kind of jump in one day made me curious. Here’s what it does. Pake turns any webpage in..."
keywords: "app, you, pake, electron, like, your, real, apps"
generated: "2026-06-20T19:45:32.624534"
---

# I Found a Tool That Shrinks Electron Apps to a Few MB

## Overview

I stumbled on Pake today. It’s sitting at 2,400 stars on GitHub. That kind of jump in one day made me curious. Here’s what it does. Pake turns any webpage into a desktop app. You give it a URL. It builds you a native app file. That’s it. The interesting part is how small the output is. Most tools like this use Electron. Electron bundles a whole copy of Chromium. Your app ends up 100+ MB, even for something simple. Pake skips that. It uses your system’s built-in WebView instead. No bundled browser. The apps come out to a few MB. That’s a real difference if you’re shipping something to users. It’s built in Rust, on top of Tauri. Tauri is the framework doing the heavy lifting. Pake is more like a thin layer on top, focused on one job: wrap a URL, output an app. I tried picturing how I’d use it. Turning ChatGPT into its own desktop app, with its own icon, its own dock space. Same for Notion or YouTube Music. Or wrapping an internal tool at work so it feels like a real app instead of another browser tab. You can tweak things too. Window size. Menu bar behavior. Keyboard shortcuts. There’s an ad-block option. Nothing fancy, but enough to make the app feel like yours. Now the honest part. This isn’t magic. You’re still just running a webpage in a window. If the site needs constant internet, your “app” needs constant internet too. Offline support depends entirely on the site, not on Pake. Native WebView also means inconsistency. Safari’s WebView on Mac and whatever Windows uses don’t render exactly the same. An app that looks perfect on your machine might look slightly off on someone else’s. And it’s not built for complex desktop integrations. If you need deep OS-level features, file system access, background processes, this isn’t that. It’s for wrapping a website. Nothing more. Still, for the use case it targets, it does the job without the bloat. If you’ve ever wanted a webpage to feel like a real app, without installing an Electron-sized file, this is worth a look. I think the star count makes sense. Electron fatigue is real. People want lighter tools. Pake is a clean answer to a specific problem, not a universal one. Worth trying if you’re tired of 150 MB apps that are really just a browser tab in disguise. See today’s top AI tools → https://saas.pet

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/mikaai/i-found-a-tool-that-shrinks-electron-apps-to-a-few-mb-1k5j

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
