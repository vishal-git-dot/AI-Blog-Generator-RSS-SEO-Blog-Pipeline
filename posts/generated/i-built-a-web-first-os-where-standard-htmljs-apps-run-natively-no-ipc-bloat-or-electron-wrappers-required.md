---
title: "I built a web-first OS where standard HTML/JS apps run natively — no IPC bloat or electron wrappers required"
slug: "i-built-a-web-first-os-where-standard-htmljs-apps-run-natively-no-ipc-bloat-or-electron-wrappers-required"
author: "Max"
source: "devto_webdev"
published: "Sat, 25 Jul 2026 19:05:25 +0000"
description: "Building desktop applications with web tech usually means wrestling with heavy frameworks, writing clunky IPC bridge code, or shipping a 200MB Chromium bundl..."
keywords: "infinity, web, app, system, your, filename, file, standard"
generated: "2026-07-25T19:16:03.117127"
---

# I built a web-first OS where standard HTML/JS apps run natively — no IPC bloat or electron wrappers required

## Overview

Building desktop applications with web tech usually means wrestling with heavy frameworks, writing clunky IPC bridge code, or shipping a 200MB Chromium bundle just to render a simple window. I wanted something simpler: What if the web runtime was the system runtime? That’s why I’ve been developing Infinity OS — a lightweight, web-native operating system designed to run pure HTML, JS, and CSS applications directly, complete with a decentralized app ecosystem and zero-friction developer tooling. ⚡ The Core Idea: Stop Reinventing the Web Platform Instead of forcing developers to learn new desktop APIs or setup complex build targets, Infinity OS lets you build apps using standard web technologies. If it runs in a browser, it’s 90% of the way to running natively on Infinity OS. Here are three core features designed specifically around developer experience: 1. async/await System Dialogs (No Callback Hell) Standard web prompt() and confirm() are blocking and notoriously hard to style. Custom modal implementations often mean writing tedious state tracking or promise wrappers. On Infinity OS, native system overlays are rebuilt using non-blocking, async-first wrappers directly in the global scope. You get clean, linear logic without freezing the UI thread: // Clean, linear async flow for native user prompts async function handleUserSave () { const fileName = await prompt ( " Enter a filename for your project: " ); const file = new File ( ' alert(0) ' , fileName + " .js " , { type : " text/javascript " }); if ( ! fileName ) return ; const shouldOverwrite = await confirm ( `File " ${ fileName } " exists. Overwrite?` ); await saveFileToDB ( file ); alert ( " Project saved successfully! " ); } 2. Zero-Friction Web App Porting Porting an existing web application, game, or utility to Infinity OS requires virtually no code changes. The OS provides standard overrides for system interactions (print, alert, Notification), meaning your web code behaves like a first-class desktop app right out of the box. 3. The Infinity Store & Transparent tester Metrics Most app marketplaces rely on vague "minimum system requirements" that don't tell the full story for lightweight or web-based hardware. The Infinity Store introduces a structured "tester" configuration field in app manifests. Instead of guesswork, app creators and QA testers write human-readable, detailed performance reports directly into the metadata: { "name" : "Infinity Torrent" , "type" : "html" , "desc" : "Decentralized P2P torrent client for downloading files directly within the OS environment using WebRTC." , "banner" : "" , "tester" : "Stable. Requires high network quality. Downloads are saved on your drive. Large files may lag on 2GB devices. Adds TORRENT file type support in Infinity OS." , "deps" : [], "minOS" : "24062026" , "entry" : "InfinityTorrent/torrent.zip" , "developer" : "Infinity Systems" } , Additionally, the Infinity Store natively supports third-party repositories, allowing developers or communities to host, distribute, and manage their own app catalogs freely. 🚀 Low-Spec Friendly Infinity OS is built to run cleanly even on older or resource-constrained devices (like vintage laptops or low-spec x86 hardware with 1–2 GB of RAM), breathing new life into older machines without the overhead of heavy desktop environments. 🛠️ Get Involved Infinity OS is actively being built and refined. The latest ISO builds and project updates are hosted on GitHub under Infinity-Systems-UA. Try porting an app: If you have an existing web game or tool, try running it on Infinity OS. Build a repo: Check out the manifest structure to set up your own app repository for the Infinity Store. I’d love to hear your thoughts! What APIs or system-level features would make web app development on custom OS platforms better for your workflow?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/max_f2ab6697eb4060d4bc660/i-built-a-web-first-os-where-standard-htmljs-apps-run-natively-no-ipc-bloat-or-electron-wrappers-37a1

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
