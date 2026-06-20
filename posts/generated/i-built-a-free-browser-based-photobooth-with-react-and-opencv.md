---
title: "I Built a Free Browser-Based Photobooth with React and OpenCV"
slug: "i-built-a-free-browser-based-photobooth-with-react-and-opencv"
author: "Roshani"
source: "devto_python"
published: "Sat, 20 Jun 2026 18:29:28 +0000"
description: "Whee Photobooth — a free, browser-based photobooth where you can pick a photo strip template, capture photos with your webcam, apply filters, doodle on your ..."
keywords: "photobooth, filters, based, frontend, backend, free, opencv, whee"
generated: "2026-06-20T19:45:32.622780"
---

# I Built a Free Browser-Based Photobooth with React and OpenCV

## Overview

Whee Photobooth — a free, browser-based photobooth where you can pick a photo strip template, capture photos with your webcam, apply filters, doodle on your strip, and download the result. No app, no signup. 🔗 Live site: wheephotobooth.site 💻 Frontend repo: https://github.com/Roshaniiii/whee-photobooth 💻 Backend repo: https://github.com/Roshaniiii/whee-photobooth-api Tech Stack Frontend: React + Vite, deployed on Vercel Backend: FastAPI, deployed on Render Image processing: OpenCV for face-detection-based filters (blush, cat ears), plus canvas-based CSS filters on the frontend for things like vintage and grayscale effects How the Filters Work The backend uses Haar Cascade classifiers to detect faces and eyes in real time. Once detected, I calculate cheek/face positions and overlay transparent PNG assets (like a blush mark or cat ears) using alpha-channel compositing. The frontend sends a base64-encoded frame to the API, the backend processes it with OpenCV, and sends back the filtered image. For lighter effects (vintage, grayscale, warm tones), I went with pure CSS filters and canvas pixel manipulation instead — much faster and doesn't need a server round-trip. Building the Photo Strip Templates Each template has a transparent PNG overlay with defined "slots" (x, y, width, height) where captured photos get drawn on a canvas. The template image draws on top, so decorations sit naturally over the photos without any clipping tricks. What's Next I'm planning to add more templates and possibly a way to save/share strips with a shareable link. Would love any feedback on the UX or the build — feel free to check it out!

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/roshyy/i-built-a-free-browser-based-photobooth-with-react-and-opencv-4c1c

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
