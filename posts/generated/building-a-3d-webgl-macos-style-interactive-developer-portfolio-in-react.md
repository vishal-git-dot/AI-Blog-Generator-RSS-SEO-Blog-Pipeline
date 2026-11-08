---
title: "Building a 3D WebGL & macOS-Style Interactive Developer Portfolio in React"
slug: "building-a-3d-webgl-macos-style-interactive-developer-portfolio-in-react"
author: "Piyush Yenorkar"
source: "devto_webdev"
published: "Sun, 08 Nov 2026 05:28:26 +0000"
description: "Most developer portfolios look identical: a generic hero section, a grid of project cards, and a contact form. When building my own developer space, I wanted..."
keywords: "interactive, three, portfolio, desktop, app, developer, react, webgl"
generated: "2026-11-08T05:28:47.823145"
---

# Building a 3D WebGL & macOS-Style Interactive Developer Portfolio in React

## Overview

Most developer portfolios look identical: a generic hero section, a grid of project cards, and a contact form. When building my own developer space, I wanted to treat it like a full-scale interactive web application rather than a static resume. I wanted visitors to explore, interact with 3D physics, run desktop OS windows, and chat with an autonomous portfolio AI assistant. Here is a breakdown of how I designed and engineered my 3D developer portfolio. ⚡ The Live Experience 🌐 Live Website : piyushyenorkar.vercel.app 💻 Tech Stack : React 19, TypeScript, Three.js, @react-three/fiber, Framer Motion, Tailwind CSS, Groq API (LLaMA 3.3). 🛠️ Key Architectural Features 1. 3D WebGL Robot with Interactive Laser Targeting At the core of the experience is an interactive 3D robot rendered with Three.js and @react-three/fiber : Real-time mouse tracking : The robot's head and limbs dynamically calculate Euler angles based on normalized viewport coordinates. Interactive laser targeting : Clicking on interactive elements triggers an explosive laser beam with jitter physics and glowing particle decay. Asset Optimization : Using Draco-compressed glTF models and deferred texture streaming to ensure sub-second initial load times even on mobile. 2. Desktop OS Window Stacking & Multi-Tasking Dock Inspired by macOS and cyberpunk terminals, the bottom navigation acts as an interactive desktop environment with 5 concurrent apps: Direct Messaging & Anonymous Community Chat Autonomous Portfolio AI Assistant Interactive GitHub & LinkedIn OS Viewers The Engineering Challenge: Real OS Z-Index Layering In traditional modals, clicking one popover closes or conflicts with another. To make it behave like an authentic desktop OS: Windows are portaled directly to document.body to avoid local z-index trapping. Implemented an event-driven bringToFront(windowKey) manager. Touching or clicking any window in the background increments the global z-index counter and transitions it above other windows without unmounting or reloading background states. Draggable with inertia via Framer Motion's useDragControls . 3. Retro Memory Chip Insertion for Blog Articles Instead of standard paginated blog lists, the reader treats articles as physical hardware cartridges: When a user selects an article card, the current memory chip ejects with sound and glowing slot animations. Dynamic bounding box coordinate tracking ( getBoundingClientRect ) maps the exact screen trajectory from the sidebar dock to the central reader mainframe. 4. Embedded Autonomous AI Assistant I integrated a dedicated conversational AI into the OS dock powered by Groq Cloud API and LLaMA 3.3 : Built with client-side key rotation and streaming response fallbacks. Knows my full technical background: Pluto Campus (Play Store app with 1st place product pitch), FlowMind (Axion Hackathon 1st place & HackHazards Top 50), SafeShell, and NHAIFaceID (offline edge facial recognition SDK). Generates interactive follow-up suggestion chips so visitors can click through topics effortlessly. 💡 What I Learned WebGL Performance on Mobile : Mobile GPUs struggle with heavy shadows and post-processing bloom. Implementing adaptive pixel ratios ( dpr={[1, 1.5]} ) and conditionally pausing Three.js render loops when out of view saved over 40% battery and CPU overhead. Layering Architecture : Desktop OS window management inside a modern web app requires strict separation between DOM stacking contexts and portal mounts. Build What Breaks You : As I wrote in one of my blog posts: "A simple todo app will never break in a way that teaches you real engineering. Build something broken and ambitious instead." 🚀 Check It Out & Share Your Feedback Take a look at the live portfolio here: https://piyushyenorkar.vercel.app/ I’d love to hear your thoughts on the Three.js performance, UI/UX feel, and any features you'd like to see next! Connect with me on GitHub and LinkedIn .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/piyushyenorkar/building-a-3d-webgl-macos-style-interactive-developer-portfolio-in-react-4mbh

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
