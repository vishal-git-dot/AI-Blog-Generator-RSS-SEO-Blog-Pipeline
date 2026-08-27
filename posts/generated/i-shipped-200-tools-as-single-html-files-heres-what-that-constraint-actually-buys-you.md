---
title: "I shipped 200 tools as single HTML files. Here's what that constraint actually buys you."
slug: "i-shipped-200-tools-as-single-html-files-heres-what-that-constraint-actually-buys-you"
author: "Salman Ahsan"
source: "devto_webdev"
published: "Thu, 27 Aug 2026 22:00:24 +0000"
description: "Most of the tools I ship are one HTML file. Inline CSS, inline JavaScript, no build step, no bundler, no CDN, no npm install. You download the file, open it,..."
keywords: "one, file, you, because, tool, what, tools, single"
generated: "2026-08-27T22:04:47.423222"
---

# I shipped 200 tools as single HTML files. Here's what that constraint actually buys you.

## Overview

Most of the tools I ship are one HTML file. Inline CSS, inline JavaScript, no build step, no bundler, no CDN, no npm install. You download the file, open it, it works. Offline, forever, on any browser. I've built a couple hundred this way now, and I want to lay out what that constraint actually buys and what it costs, because the internet's default answer to "should I use a framework" is unhelpfully binary. What it buys Zero dependency rot. A file with no dependencies has nothing to break. No transitive vulnerability alerts, no deprecated package, no build that stops working because a toolchain moved on. A tool I wrote two years ago opens today and behaves identically. If you've maintained anything with a node_modules directory across a couple of years, you know what that's worth. Distribution is a file. No hosting, no deploy pipeline, no uptime. Email it, put it on a USB stick, commit it, drop it in a Slack channel. It runs from file://. For a paid tool this is the entire product: the customer owns the artifact and cannot lose access to it because of anything I do, including going out of business. Real privacy, not a privacy policy. No server means no server-side logs. Whatever the user types stays in their tab. For anything touching documents, keys, financial data, or client work, "this can't leave your machine because there's nowhere for it to go" is a categorically stronger claim than a promise, and it takes one sentence to explain. Speed you don't have to work for. One request, no hydration, no waterfall. There's nothing to optimize because there's nothing there. Auditability. View source and the whole program is in front of you. That's a genuine feature for security tooling. Anyone can read the entire thing in one sitting. What it costs I'd be lying if I framed this as free. No shared state. Every file is an island. A bug fixed in one is fixed in one. I've solved this with generation and templating rather than runtime sharing, which trades runtime coupling for build-time discipline, and that trade only works because I keep the tools small. No component reuse across files. Same header written in eighty files. When the header design changes, eighty files change. Again: tooling, not architecture. Real ceiling on complexity. This works beautifully up to a point and then it doesn't. Anything with auth, persistence across devices, collaboration, or genuinely complex state should not be a single file. I have a rough limit around 3,000 lines and once something wants to cross it, that's a signal the thing wants to be a real application. No ecosystem. No component library, no state management, no router. For most single-purpose tools you don't need any of it, and if you do need it, that's the same signal as above. The actual rule I use Single file when the problem fits in one screen of concept. A calculator, a converter, a checker, a generator, a formatter, an analyzer. One input, some processing, one output. The moment it needs a login or a database, it stops being a file and becomes an app, and I build it as one. That line is much further out than most developers assume. A surprising number of tools that ship as SaaS with an account and a subscription are, functionally, a form and a function. The account exists to enable the subscription, not because the tool needed one. Where this connects to AI tooling The single-file approach turns out to pair well with BYOK. The user pastes their own API key, it lives in localStorage, the tool calls the provider directly from the browser. No proxy, no backend, no key ever touching my infrastructure. Which means an AI tool can also be one file. That still surprises people, and it's mostly a consequence of every provider offering a plain HTTPS endpoint and CORS being solvable. The constraint that started as an aesthetic preference turned out to be the thing that made a whole category of product possible at a price point that wouldn't otherwise work. There are a couple hundred of these at digitaldfy.com if you want to read the source of one. That's the point of shipping them this way: you can. I build with AI and I am not coy about it. The facts, the decisions, and the judgment here are mine. The drafting is a tool, the same as every other tool I write about.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/salmanahsan/i-shipped-200-tools-as-single-html-files-heres-what-that-constraint-actually-buys-you-45pi

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
