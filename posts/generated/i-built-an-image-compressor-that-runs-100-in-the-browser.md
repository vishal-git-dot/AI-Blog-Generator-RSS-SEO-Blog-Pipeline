---
title: "I Built an Image Compressor That Runs 100% in the Browser"
slug: "i-built-an-image-compressor-that-runs-100-in-the-browser"
author: "Devanshu Biswas"
source: "devto_webdev"
published: "Wed, 17 Jun 2026 15:40:13 +0000"
description: "Most "compress your image" websites upload your photo to a server. You don't need one. The browser's own canvas can re-encode an image at any quality — I bui..."
keywords: "image, canvas, file, img, drop, blob, browser, your"
generated: "2026-06-17T15:50:36.572819"
---

# I Built an Image Compressor That Runs 100% in the Browser

## Overview

Most "compress your image" websites upload your photo to a server. You don't need one. The browser's own canvas can re-encode an image at any quality — I built a drag-and-drop compressor in about 30 lines , and your photo never leaves your machine. 🗜️ Try it (drop a photo): https://dev48v.infy.uk/solve/day9-image-compressor.html 1. Catch the dropped file — locally drop . addEventListener ( " drop " , e => { e . preventDefault (); const file = e . dataTransfer . files [ 0 ]; // stays in the tab, 0 bytes uploaded loadImage ( file ); }); For sensitive images (IDs, screenshots), "never uploaded" is a real feature, not just a nicety. 2. Decode it into an <img> A dropped file is just bytes. Load it via a local blob: URL: const img = new Image (); img . src = URL . createObjectURL ( file ); await img . decode (); 3. Draw it onto a canvas Now the browser holds the raw pixels, detached from the original file format: canvas . width = img . naturalWidth ; canvas . height = img . naturalHeight ; canvas . getContext ( " 2d " ). drawImage ( img , 0 , 0 ); 4. Re-encode at a quality (this IS the compression) canvas . toBlob ( blob => { preview . src = URL . createObjectURL ( blob ); showSize ( blob . size ); }, " image/jpeg " , 0.7 ); // 0.7 = 70% quality JPEG and WebP are lossy — they discard detail the eye barely notices. That third argument is the entire compression dial; a small quality drop often halves the file size. 5. Hand the result back as a download link . href = URL . createObjectURL ( blob ); link . download = " compressed.jpg " ; // the browser saves it, no server The takeaway FileReader → Image → Canvas → toBlob is a surprisingly powerful local image pipeline. The same four steps do resizing, format conversion, cropping, watermarking — all client-side, all private. A whole category of "image tools" needs no backend at all. Open it and drop a photo.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dev48v/i-built-an-image-compressor-that-runs-100-in-the-browser-5e91

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
