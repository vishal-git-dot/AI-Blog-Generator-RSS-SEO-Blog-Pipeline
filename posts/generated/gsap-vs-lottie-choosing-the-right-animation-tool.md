---
title: "GSAP vs Lottie: Choosing the Right Animation Tool"
slug: "gsap-vs-lottie-choosing-the-right-animation-tool"
author: "Fazal Shah"
source: "devto_webdev"
published: "Mon, 08 Jun 2026 20:00:27 +0000"
description: "GSAP and Lottie are both excellent animation tools, but they solve different problems. Here's how to decide which one to reach for — and when to use both. Th..."
keywords: "lottie, gsap, animation, when, designer, use, animations, you"
generated: "2026-06-08T20:25:42.489621"
---

# GSAP vs Lottie: Choosing the Right Animation Tool

## Overview

GSAP and Lottie are both excellent animation tools, but they solve different problems. Here's how to decide which one to reach for — and when to use both. The Core Difference GSAP animates DOM elements you create with code. You define what moves where, and GSAP handles the timing and easing. Lottie plays back animations created in After Effects (or similar tools). Your designer defines what happens; Lottie renders it exactly as designed. When to Use GSAP UI transitions : page transitions, accordion opens/closes, element reveals Scroll-driven animations : parallax, sticky elements, reveal-on-scroll Dynamic data visualization : animating charts, counters, progress bars with real values Interactive animations : reactions to user input that are hard to pre-define When you have no designer : building animations entirely in code // GSAP example: animate an element based on user interaction import gsap from ' gsap ' ; button . addEventListener ( ' click ' , () => { gsap . to ( ' .card ' , { scale : 1.05 , duration : 0.2 , ease : ' back.out(1.7) ' , yoyo : true , repeat : 1 }); }); When to Use Lottie Brand animations : logos, mascots, illustrations — designed by someone who knows After Effects Icon animations : animated checkmarks, loading spinners, hover states Onboarding flows : multi-scene character animations Empty states / error states : illustrated feedback When a designer owns the animation : you want pixel-perfect rendering of their work // Lottie example: designer-created animation, zero code for the animation itself import { DotLottieReact } from ' @lottiefiles/dotlottie-react ' ; import successAnim from ' ./success.lottie ' ; // ← designer made this < DotLottieReact src = { successAnim } autoplay loop = { false } /> File Size Comparison Format Typical Size Notes GSAP bundle 33KB (core) Code only, no asset file Lottie JSON 10–150KB Depends on animation complexity dotLottie (.lottie) 3–40KB ~75% smaller than JSON GIF equivalent 80–500KB For comparison GSAP has no animation asset file — the animation is in your code. Lottie ships a separate asset file per animation. Using Both Together The real power comes from combining them: // Use GSAP to control WHEN Lottie plays import gsap from ' gsap ' ; import { ScrollTrigger } from ' gsap/ScrollTrigger ' ; import lottie from ' lottie-web ' ; const anim = lottie . loadAnimation ({ container : document . getElementById ( ' hero-lottie ' ), renderer : ' svg ' , loop : false , autoplay : false , path : ' /animations/hero.json ' , }); // Play the Lottie animation when user scrolls to it ScrollTrigger . create ({ trigger : ' #hero-lottie ' , start : ' top 80% ' , onEnter : () => anim . play (), onLeaveBack : () => anim . stop (), }); GSAP handles the scroll logic; Lottie renders the designer's work. Practical Decision Matrix Situation Use Animating a div's position/opacity GSAP Playing a designer-made loading spinner Lottie Scroll-triggered section reveals GSAP Animated logo or mascot Lottie Counter animation (0 → 1,234) GSAP Animated empty state illustration Lottie Draggable, physics-based UI GSAP Branded animated icons Lottie Preparing Lottie Files Before integrating any Lottie file, preview it at IconKing — you can check that it renders correctly, edit colors to match your brand, and convert from .json to .lottie (75% smaller). No account required. Summary Use GSAP when you're building the animation in code. Use Lottie when a designer made the animation in After Effects. Use both when you need scroll/interaction triggers around designer-made content.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/fazalshah/gsap-vs-lottie-choosing-the-right-animation-tool-3d03

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
