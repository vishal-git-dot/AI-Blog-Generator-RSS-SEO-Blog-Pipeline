---
title: "I built 1,500+ browser tools that never upload your files"
slug: "i-built-1500-browser-tools-that-never-upload-your-files"
author: "Joseph Orduna"
source: "devto_webdev"
published: "Fri, 23 Oct 2026 20:49:50 +0000"
description: "The site is Practical Web Tools . It has 1,500+ free tools: file converters, PDF tools, a couple hundred calculators, some dev utilities, and twelve creative..."
keywords: "tools, one, tool, you, your, file, wasm, which"
generated: "2026-10-23T21:14:15.043399"
---

# I built 1,500+ browser tools that never upload your files

## Overview

The site is Practical Web Tools . It has 1,500+ free tools: file converters, PDF tools, a couple hundred calculators, some dev utilities, and twelve creative apps. The one thing they all share is that your files never leave your device. There is no upload step, because there is no server doing the work. It started much smaller, a few dozen converters, and it grew for a reason that surprised me: client-side meant every new tool cost me nothing to run. I want to walk through how the thing actually works, because "it runs in your browser" gets hand-waved a lot. From file to WebAssembly Every tool starts the same way. You pick a file, the page gets a File object through the File API, and the bytes go into WebAssembly. What happens next depends on the tool: Audio and video run through ffmpeg.wasm, which is ffmpeg compiled to WebAssembly. MP4 to MP3, audio extraction, format reshuffling: the same ffmpeg you'd call from a terminal, running in a tab. PDF operations use qpdf.wasm. Merging PDFs means concatenating page trees in wasm and handing you back a Blob to download. Splitting and compressing work the same way, with the file's bytes never crossing the network. Images are mostly the canvas API. The HEIC to JPG converter decodes the HEIC in wasm, draws the decoded image to a canvas, and re-encodes it as JPEG at whatever quality you picked. That last category is the one I like demoing, because the privacy claim is checkable by the person using it. Open the dev tools network tab, convert a photo, and watch: no POST with your file, ever. Nothing to take my word for, which beats reading a privacy policy. One wrinkle worth knowing if you go this route: the heavy wasm binaries are lazy-loaded per tool, so someone landing on a converter only downloads the module that converter needs. The HEIC decoder doesn't ship to the mortgage calculator page. Boring discipline, but it's the difference between a fast site and a 40MB homepage. How 1,500+ tools stay maintainable The count is only possible because most tools share plumbing. Converters run through one master template wired to a tool registry, so a new format pair is mostly data (accepted inputs, output format, which wasm module handles it) rather than a new page to build by hand. That's also an honest caveat about the number, which I'll get to. The heavier piece is threading. Some of the creative apps want multithreaded wasm, which needs SharedArrayBuffer , which means serving COOP and COEP headers on those routes so the browser treats the page as cross-origin isolated. Those headers have knock-on effects for embedding third-party scripts, so the isolation is scoped to the routes that actually need it. Small detail, real hours. The Studio end of the pool The converters are table stakes. The part people don't expect is the Studio : twelve free creative apps, all client-side. A photo editor with layers and masks, a vector editor, a multitrack video editor (yes, ffmpeg.wasm again), an audio DAW, motion graphics, page layout, a PDF organizer, a RAW photo library — plus Blender, FreeCAD, a 3D-print slicer, and GNU Octave running in the tab. None of them are Photoshop. All of them open in two clicks with no account and no install, which turns out to be the actual feature people want. Why client-side beats a server here Two reasons, one principled and one embarrassingly practical. The principled one: people convert private things. Contracts, tax documents, ID scans, photos they'd rather not explain. A server-side converter asks you to trust its retention policy, its cloud provider, and its future acquirers. A client-side converter doesn't have anything to retain. I couldn't leak your file if I wanted to, because I never receive it. The practical one: compute is what kills sites like this. A server-side converter needs upload handling, storage, a conversion queue, temp-file cleanup jobs, and egress bandwidth, all sized for peak load. My version needs static hosting and a CDN. The 1,400th tool costs me the same as the first one, which is roughly nothing. That is the only reason a solo dev can run 1,500+ tools on ad revenue. It's also an installable PWA. Tools you've opened keep working offline, since the code is already on your machine. Honest limitations Every "free and private" pitch deserves this list: Ads pay for it. They're on the site. That's the whole business model, no mystery. Some tools are thin. The 460+ unit converters are a formula with a UI wrapped around them, and the tool count is big partly because format pairs multiply: every input format times every output format. Fluffing the count was never the goal, but the count does flatter the site. A browser tab is not a native app. WebAssembly is slower than native code and browsers cap tab memory. A desktop ffmpeg install beats the browser on large files every time. If you convert video daily, use a native tool. This site is for the person who needs it once and doesn't want to install anything. The first conversion has a wait. The heavy wasm binaries are several megabytes and only load when you open a tool that needs one. Quality varies. Exotic codecs and badly-built PDFs don't always survive conversion. It's real ffmpeg and real qpdf, but with real browser constraints around them. What I'd like feedback on If you try it: does a specific tool misbehave in your browser, Safari quirks especially? Which converter is too limited for your actual workflow? And is there a task where "in the browser" genuinely doesn't cut it? That list is basically my roadmap. The site is here .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/joseph_orduna_b458c7df808/i-built-1500-browser-tools-that-never-upload-your-files-46h5

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
