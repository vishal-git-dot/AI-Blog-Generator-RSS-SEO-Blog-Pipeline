---
title: "Free, Zero-Dependency YouTube Website Embed (Self-Hostable PHP/JS)"
slug: "free-zero-dependency-youtube-website-embed-self-hostable-phpjs"
author: "Scott Peterson"
source: "devto_webdev"
published: "Sat, 08 Aug 2026 18:34:00 +0000"
description: "Hey DEV community! 👋 If you've ever tried to embed a dynamic YouTube channel feed, a live stream detector, or playlist carousel on a client site, you've prob..."
keywords: "your, live, free, youtube, proxy, data, you, channel"
generated: "2026-08-08T18:45:17.904546"
---

# Free, Zero-Dependency YouTube Website Embed (Self-Hostable PHP/JS)

## Overview

Hey DEV community! 👋 If you've ever tried to embed a dynamic YouTube channel feed, a live stream detector, or playlist carousel on a client site, you've probably run into two major issues: Expensive SaaS widgets that slap watermarks on your site unless you pay a monthly fee. Leaking your YouTube API Key directly in the frontend script. To solve this, we built YT Widget —a free, self-hostable, dependency-free JavaScript library that handles YouTube feeds, playlists, channel stats, and live stream status seamlessly. 📦 Where to Get It The project is fully open-source and ready for your production projects: Source Code & Contributions: scott8462 / YT-Widget A free, self-hostable, dependency-free JavaScript library for embedding YouTube feeds, playlists, channel stats, single videos, and live stream status on any website. YT Widget — Free Open-Source YouTube Website Embed A free, self-hostable, dependency-free JavaScript library for embedding YouTube feeds, playlists, channel stats, single videos, and live stream status on any website — just like SociableKIT, but 100% free and open-source. Created and provided free to the developer community by R&S Development . ✨ Features 📺 5 Widget Types feed : Latest channel uploads grid or list live : Auto-detects live broadcasts and embeds the live player — shows a custom Offline Card with recent uploads when offline playlist : Show videos from any YouTube playlist stats : Channel metrics cards (Subscribers, Views, Videos count) single : Responsive single video player with metadata 🔒 Secure PHP Server Proxy ( proxy/ ) : Keep your YouTube API key hidden server-side with built-in CORS, rate limiting, and 5-minute response caching. 🎨 Full Color Customization Light & Dark themes Custom Accent / Button… View on GitHub Alternative Downloads & Mirrors: Download on SourceForge ✨ Core Features 📺 5 Widget Types: Switch layouts instantly ( feed grid/list, live stream detector, playlist fetcher, profile stats , or single responsive video). 🔒 Secure PHP Server Proxy ( proxy/ ): Keeps your YouTube API key safely hidden server-side with built-in CORS, rate limiting, and 5-minute response caching. 🎨 Full Color Customization: Includes a smart Auto-Contrast Engine for text layers, light/dark themes, and custom accent controls ( data-accent-color ). ⚡ Zero Dependencies: Pure Vanilla JS & HTML5. No jQuery, no React, and no heavy layout frameworks. 🎛️ Visual Builder Dashboard: Comes with a local index.html GUI to generate code parameters dynamically. 🚀 Quick Start (2-Minute Setup) You can run this project in direct API key mode, but we highly recommend using the included PHP Proxy to secure your credentials. Step 1: Drop the Proxy on Your Server Upload the proxy/ folder and insert your key into proxy/config.php : define ( 'YTW_API_KEY' , 'AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXX' ); Step 2: Add the HTML5 Embed Snippet Place the semantic HTML container anywhere on your site: <!-- YouTube Widget Container --> <div data-yt-widget data-proxy-url= "https://yoursite.com/proxy/api-proxy.php" data-channel-id= "UCxxxxxxxxxxxxxxxxxxxxxx" data-type= "feed" data-layout= "grid" data-max-results= "9" data-load-more= "true" > </div> <!-- Include script before your closing body tag --> <script src= "yt-widget.js" ></script> 🔴 The Live Stream Detector + Offline Card One of our favorite features is the data-type="live" parameter. When your channel is Live , it builds a responsive 16:9 player with a pulsing ● LIVE badge and counter. When you are Offline , it renders a customized offline hero card featuring your latest video, a call to action to subscribe, and a custom 16:9 placeholder banner. 🤝 Open For Feedback & Contributions We built this tool under the MIT License to give web developers an actual free tier option for website embeds. If you use it, we would love your feedback! What features or layout modes should we add next? If you find it helpful, please consider starring the repository or throwing us a link back at R&S Development . Let us know what you think in the comments below! 👇

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/scott_peterson_bf7b8ea3f7/free-zero-dependency-youtube-website-embed-self-hostable-phpjs-338h

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
