---
title: "I built gessi: playful OS-style interfaces with just HTML"
slug: "i-built-gessi-playful-os-style-interfaces-with-just-html"
author: "Paul Contreras"
source: "devto_webdev"
published: "Thu, 25 Jun 2026 19:58:38 +0000"
description: "Meet gessi, a dependency-free CSS and Web Component library for building retro desktops, draggable windows, and expressive interfaces without framework lock-..."
keywords: "gessi, you, can, html, like, components, feel, css"
generated: "2026-06-25T20:09:21.020873"
---

# I built gessi: playful OS-style interfaces with just HTML

## Overview

Meet gessi, a dependency-free CSS and Web Component library for building retro desktops, draggable windows, and expressive interfaces without framework lock-in. I’ve been working on Gessi , an open-source CSS and Web Component library for building playful web interfaces with plain HTML. The idea behind it is simple: Websites do not always have to feel like landing pages. They can feel like desktops. They can feel like tiny operating systems. They can feel like archives, control panels, old computers, personal desks, or interactive product demos. That is the kind of web I wanted to make easier to build. So I made Gessi . A tiny desktop in HTML Here is the smallest example: <script type= "module" src= "https://cdn.jsdelivr.net/npm/@pol-cova/gessi/dist/gessi.js" ></script> <gessi-desktop menu= "◆ My OS,File,View,Help" clock= "09:41" > <gessi-window title= "hello.html" width= "38rem" active draggable > <h1> Hello from Gessi </h1> <p> This is normal HTML inside a draggable window. </p> </gessi-window> </gessi-desktop> That is a complete working page. The script registers the components and loads the styles automatically. No React runtime. No build setup. No package installation. No framework required. Just HTML. What Gessi helps you build Gessi is made for interfaces that want to feel more expressive than a normal page. You can use it to build things like: a personal website that feels like a desktop a portfolio that opens projects inside windows a retro product demo a media archive with folders and panels an experimental blog layout a tiny browser-based operating system a playful docs or internal tool interface a landing page that feels more like an app The goal is not to replace your whole stack. The goal is to give you a set of reusable interface pieces so you can build something more memorable without starting from zero. Components included Gessi includes the common pieces needed for small desktop-like interfaces: desktops draggable windows minimizable and zoomable windows dialogs nested child windows menus toolbars docks tabs trees desktop icons control panels alerts notifications tooltips meters responsive maps carousels image effects pixel patterns classic OS-inspired themes You can combine these pieces to create different kinds of browser-based environments. For example, the docs include complete examples like: Product OS Classic OS Media OS Each one uses the same idea: normal HTML content wrapped inside reusable Gessi components. Multiple visual systems Gessi currently includes five visual systems: neo minimal retro old-tech classic-os The idea is that your structure can stay mostly the same while the visual style changes. You can start with something clean and minimal, then move into a more nostalgic or old-tech look without rebuilding the whole interface. Why I made it framework-independent I wanted Gessi to work in as many projects as possible. You can use it with: a single static HTML file Astro Eleventy Hugo Jekyll server-rendered templates React Vue Svelte any project that only wants the CSS layer The components are built with Web Components and use light DOM. That means your content remains normal HTML. It exists before JavaScript runs, stays available to your own CSS, and still has a readable fallback if the interactive layer does not load. Gessi handles the reusable interface behavior and visual chrome. Your project still owns the content, layout, and personality. It also works with npm You can install it from npm: npm install @pol-cova/gessi Then import the CSS and components: import " @pol-cova/gessi/css " ; import " @pol-cova/gessi/components " ; The component module is safe to import during SSR, and it does not inject CSS when used through a bundler. Why this exists A lot of modern websites are starting to feel very similar. Same cards. Same dashboards. Same layouts. Same generic sections. There is nothing wrong with that. Those patterns are useful, and I use them too. But I also think the web is more fun when interfaces have personality. I wanted a small library that makes it easier to build websites that feel unusual, nostalgic, playful, or simply less generic. That is what Gessi is trying to become. The project is early Gessi already has working components, examples, and documentation, but it is still early. There is a lot of room to improve the project. Some areas I would love help with: new components better component APIs Markdown and MDX support a first-party pixel icon set more themes a public custom-theme API accessibility and keyboard testing Firefox and WebKit testing examples with real static-site generators documentation improvements design feedback You do not need to contribute a huge feature. A small bug report, browser test, accessibility fix, documentation correction, or example of something you built would already be valuable. Try Gessi Documentation: https://pol-cova.github.io/gessi/ GitHub: https://github.com/pol-cova/gessi npm: https://www.npmjs.com/package/@pol-cova/gessi If Gessi helps you build something weird, nostalgic, playful, or simply less generic, I would genuinely love to see it. Feel free to try it, open an issue, share feedback, or contribute to the project.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/paulcontr_/i-built-gessi-playful-os-style-interfaces-with-just-html-9p0

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
