---
title: "PSEC-99: A 3D Browser Game in C# and WASM, Without WebGL"
slug: "psec-99-a-3d-browser-game-in-c-and-wasm-without-webgl"
author: "Umberto Giacobbi"
source: "devto_webdev"
published: "Mon, 19 Oct 2026 03:46:47 +0000"
description: "Take a look at what the OpenSilver team has built. This game shows what C# and WebAssembly can do in the browser. How fast? Play it and see for yourself. Dis..."
keywords: "game, what, they, browser, opensilver, code, net, wasm"
generated: "2026-10-19T04:06:19.788544"
---

# PSEC-99: A 3D Browser Game in C# and WASM, Without WebGL

## Overview

Take a look at what the OpenSilver team has built. This game shows what C# and WebAssembly can do in the browser. How fast? Play it and see for yourself. Disclosure: I used to work with this team, so I know what they’re capable of. For those who don't know, OpenSilver was born long ago as a replacement for Silverlight, a kind of competitor to Flash (but way better). But, as usual, Microsoft killed it. Classic: from "this is the future" to "nah, HTML5 and React are the future." It compiles high-level code into pure WebAssembly, which is fast, really fast. It can do a lot more nowadays (it supports WPF, third-party controls, MAUI, full C#/WebAssembly interop and more). To be honest, a demo like this also raises an awkward question: why do so many web apps struggle with CPU and memory usage just to display a few hundred divs? One day I will have an answer to this. So, what did they do? They took a 1982 TI-99/4A game and turned it into a 3D browser experience using C#/WASM and an int[] pixel buffer. No WebGL. In other words, they write the pixels directly, without a middleman. Everything is done through their code. I repeat their buffer is one pixel! The result is PSEC-99 , an unofficial 3D tribute to PARSEC . Try it yourself Both the game and OpenSilver are open source, so you can study the code, extend it or just play. What caught my attention is the rendering approach. Their entire 3D scene is drawn in C# into a single pixel buffer (yes, just one!) in .NET memory, then displayed on an HTML canvas through OpenSilver 3.4 Preview’s new WriteableImage XAML control. That means no game engine, WebGL or WebGPU renderer: the 3D math, projection and rasterization happen in C#. Terrain, stars, buildings, enemies, lasers and explosions all end up in that array. They kept other parts deliberately old-school too: The terrain is rendered row by row, filling pixels directly rather than drawing terrain polygons. Buildings start as ASCII grids in C#. Sounds and voices are synthesized at runtime. If you remember PARSEC on the TI-99/4A, give it a try. And if you’re into .NET, retro computing or software rendering, the source is well worth exploring. Explore the MIT-licensed source code — open it in the .NET IDE to run, edit, fork or download it. Play directly in your browser — it runs on .NET 10/WASM, including on phones. Heads up: it has sound!

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/umbertogiacobbi/psec-99-a-3d-browser-game-in-c-and-wasm-without-webgl-2a0i

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
