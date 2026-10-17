---
title: "I Built SpeedPulse: An Open-Source Internet Speed Tester with ASP.NET Core 10 and TypeScript"
slug: "i-built-speedpulse-an-open-source-internet-speed-tester-with-aspnet-core-10-and-typescript"
author: "Sanskar"
source: "devto_webdev"
published: "Sat, 17 Oct 2026 15:10:55 +0000"
description: "I Built SpeedPulse: An Open-Source Internet Speed Tester with ASP.NET Core 10 and TypeScript After working on its testing interface, diagnostics, backend, an..."
keywords: "speedpulse, github, speed, testing, asp, net, core, measurements"
generated: "2026-10-17T15:18:37.847909"
---

# I Built SpeedPulse: An Open-Source Internet Speed Tester with ASP.NET Core 10 and TypeScript

## Overview

I Built SpeedPulse: An Open-Source Internet Speed Tester with ASP.NET Core 10 and TypeScript After working on its testing interface, diagnostics, backend, and release pipeline, I'm excited to introduce SpeedPulse v1.0.0 , the first stable release of my open-source internet speed testing project. SpeedPulse is designed to provide an approachable way to measure connection performance while giving developers additional tools to explore network behavior. What is SpeedPulse? SpeedPulse is a browser-based internet speed testing application. It provides measurements for download and upload throughput, HTTP latency, approximate jitter, and failed HTTP probes, alongside interactive charts and results history. You can try it directly on GitHub Pages: https://sanskarin.github.io/SpeedPulse/ Features in v1.0.0 1. Connection speed testing SpeedPulse provides: Download and upload speed measurements HTTP latency and approximate jitter Failed HTTP probe monitoring Live progress and visualizations These are browser-level estimates, rather than laboratory-grade or packet-level network measurements. 2. Interactive dashboard The application includes visualizations for exploring connection performance, along with locally stored results history. Users can export results as CSV and share their measurements. 3. Developer Labs One part of SpeedPulse that I'm particularly interested in developing further is Developer Labs. It brings together diagnostic utilities including backend health checks, HTTP probes, browser capability reporting, diagnostic exports, and explicitly labeled simulations. The goal is to make network behavior easier to inspect and understand. 4. Optional ASP.NET Core 10 backend SpeedPulse supports two deployment approaches. Hosted web version The GitHub Pages deployment uses a static frontend and public Cloudflare testing endpoints. Self-hosted version The optional ASP.NET Core 10 backend provides local HTTP testing endpoints, health and configuration APIs, bounded transfers, and request limiting. An important distinction: tests against a server running on the same computer measure the local loopback path, not your internet service provider's speed. Technology stack The project brings together: C# and ASP.NET Core 10 TypeScript and JavaScript HTML and CSS Chart.js Node.js build tooling GitHub Actions GitHub Pages Improving measurement reliability An important part of preparing v1.0.0 was improving how the application handles partial test failures. Previously, an upload failure could interrupt the experience even after earlier measurements had succeeded. The stable release now preserves completed measurements and marks an unavailable upload result appropriately instead of treating it as zero. I also corrected live chart behavior and added regression coverage for these scenarios. Download SpeedPulse v1.0.0 The release includes a static web archive and self-hosted ASP.NET Core packages for Windows x64, Linux x64, and Apple Silicon macOS. GitHub release: https://github.com/sanskarIN/SpeedPulse/releases/tag/v1.0.0 Source code: https://github.com/sanskarIN/SpeedPulse Live application: https://sanskarin.github.io/SpeedPulse/ What's next? Future development can continue improving measurement reliability, developer diagnostics, usability, and testing across different environments. Since the project is open source under the MIT License, contributions and technical feedback are welcome. If you explore SpeedPulse, I'd particularly love to hear about browser compatibility, unexpected measurement behavior, or ideas for making the diagnostics more useful. Thanks for checking out SpeedPulse! Built by Sanskar GitHub: https://github.com/sanskarIN Website: https://sanskarin.github.io

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/sanskarcodes/i-built-speedpulse-an-open-source-internet-speed-tester-with-aspnet-core-10-and-typescript-4i2m

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
