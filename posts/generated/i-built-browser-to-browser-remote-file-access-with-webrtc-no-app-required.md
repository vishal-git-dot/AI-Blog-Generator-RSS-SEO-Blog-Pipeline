---
title: "I built browser-to-browser remote file access with WebRTC – no app required"
slug: "i-built-browser-to-browser-remote-file-access-with-webrtc-no-app-required"
author: "Yousiff Taqi"
source: "devto_webdev"
published: "Sat, 29 Aug 2026 20:36:36 +0000"
description: "I’ve been building a browser-first project called RelicBeam, and one feature I wanted was simple in theory: Open a folder on one device and temporarily brows..."
keywords: "remote, files, device, file, relicbeam, host, browser, one"
generated: "2026-08-29T20:45:19.188038"
---

# I built browser-to-browser remote file access with WebRTC – no app required

## Overview

I’ve been building a browser-first project called RelicBeam, and one feature I wanted was simple in theory: Open a folder on one device and temporarily browse it from another device without installing anything. That became Remote Files, part of RelicBeam’s Device Portal. The host selects a folder, another device joins with a QR/code, the host approves the connection, and the second device can browse, preview and download files. The folder itself is never uploaded to RelicBeam. File data travels over a WebRTC DataChannel. If a direct connection isn’t possible, my own TURN server relays the encrypted traffic. Device Portal traffic is end-to-end encrypted between the connected browsers. The interesting problems The file browser itself was actually the easy part. Android file pickers kept killing sessions When I added optional uploads, I noticed something odd during testing. The first upload worked, but after opening the Android file picker a few times, the Remote Files session could suddenly disconnect. It turned out Android can background or suspend the browser while the native file picker is open. That could temporarily drop the Socket.IO signaling connection, and my server was treating any disconnect as the viewer leaving permanently. The fix was a short reconnect grace period. Temporary disconnects now get time to recover, while explicit Leave and End session actions still terminate access immediately. Firefox and Safari can browse, but not host uploads Remote Files works read-only across browsers, but writable folder access is more limited. Chrome and Edge expose writable directory handles through the File System Access API, so a host can optionally allow remote uploads into the selected folder. Firefox and Safari don’t currently expose the same writable directory picker. So today: Chrome / Edge host Browse ✅ Preview ✅ Download ✅ Optional uploads ✅ Firefox / Safari host Browse ✅ Preview ✅ Download ✅ Host uploads ❌ Firefox and Safari can still be the remote device and upload to a compatible Chrome/Edge host. Instead of silently hiding the feature, RelicBeam now explains when the host browser is operating in read-only mode. I kept uploads deliberately non-destructive Remote Files has no controls for: delete rename move intentional overwrite If an incoming filename already exists, the upload is rejected. The goal is to keep remote access useful without turning it into full remote filesystem control. WebRTC vs malware scanning There’s also an interesting security tradeoff. RelicBeam’s normal file-sharing modes send uploaded files through the server so they can be malware-scanned with ClamAV and then encrypted at rest. Those transfers are therefore not E2EE. Device Portal uses WebRTC instead, so Remote Files and Remote View are E2EE between browsers, but Remote Files uploads cannot be server-side malware-scanned because RelicBeam never receives the plaintext. I’d rather make that distinction clear than slap one vague security claim over everything. The rest of RelicBeam Remote Files is one part of the project: Room — share files/text with a group using one QR/code Quick Beam — one-to-one file/text sharing Beam Link — temporary direct-download links Device Portal — Remote Files + view-only Remote View Convert — local PDF/image tools before sharing No accounts, and no permanent RelicBeam file library. You can try it here: https://relicbeam.com Device Portal: https://relicbeam.com/device-portal I’m at the point where I’m trying to find rough edges rather than add more features. If anyone tries Remote Files, I’d especially appreciate feedback on browser compatibility, mobile behavior, WebRTC failures, or anything that feels confusing.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/fencer/i-built-browser-to-browser-remote-file-access-with-webrtc-no-app-required-84b

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
