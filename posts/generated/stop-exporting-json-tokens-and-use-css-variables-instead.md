---
title: "Stop exporting JSON tokens and use CSS variables instead"
slug: "stop-exporting-json-tokens-and-use-css-variables-instead"
author: "Alexander"
source: "devto_webdev"
published: "Wed, 14 Oct 2026 16:30:41 +0000"
description: "A designer tagged me in a Figma comment on Tuesday morning. They wanted to know if we could start exporting our brand tokens as deeply nested JSON files. The..."
keywords: "you, just, json, css, they, web, variables, figma"
generated: "2026-10-14T16:54:47.642415"
---

# Stop exporting JSON tokens and use CSS variables instead

## Overview

A designer tagged me in a Figma comment on Tuesday morning. They wanted to know if we could start exporting our brand tokens as deeply nested JSON files. They had just read an article about complex token pipelines. I just stared at my screen for a minute. We are a web team building a React application. We do not need a massive parsing engine just to read a blue hex code. This happens all the time in our industry. Teams get obsessed with the idea of a universal format. They build massive configurations to transform JSON into something the browser can actually use. It feels like everyone is overcomplicating the simplest part of frontend development. The pipeline trap I see this pattern everywhere. A team decides they need a design system. They set up a pipeline that exports something like this from Figma. { "color" : { "brand" : { "primary" : { "value" : "#0052cc" , "type" : "color" } }, "background" : { "base" : { "value" : "#ffffff" , "type" : "color" } } } } Then the web developers have to write a script to flatten this object. They have to map it to their styling solution. Maybe they are using Tailwind. Maybe they are using styled-components. Either way, it adds a completely unnecessary layer of complexity. If a colour breaks in production, you cannot just inspect it easily. You have to trace the error back through your build script. You have to figure out if the JSON was malformed or if your parser failed. That is a lot of wasted time for a background colour. The browser already solved this CSS variables are the only token format that actually matters for the web. You do not need a build step to use them. You just load the file and the browser understands it immediately. Look at how much cleaner the CSS approach is. :root { --color-brand-primary : #0052cc ; --color-background-base : #ffffff ; } You can inspect this directly in Chrome DevTools. You can change the values on the fly to test new designs. You can scope them to specific components. JSON cannot do any of that natively. Theming is where CSS variables really show their power. If you want to add a dark mode using JSON, you usually have to output multiple files. Then you have to write JavaScript logic to swap those themes in your application. With CSS variables, the browser does all the heavy lifting for you. [ data-theme = "dark" ] { --color-brand-primary : #4c9aff ; --color-background-base : #111111 ; } You just toggle a data attribute on your HTML tag. The browser updates every single component instantly. There is no JavaScript required. There is no complex state management. It just works. What about native apps? This is always the counter-argument I hear. People say you need JSON so iOS and Android can consume the exact same tokens. That is technically true if you work at a massive tech company with dedicated mobile teams. But most teams are web-first. Even if you do have mobile developers, forcing the web team to parse JSON just to appease iOS is backwards. Let the mobile teams compile what they need. The web should just get CSS. You should optimise for the platform where your users actually spend their time. A better workflow We stopped doing the JSON dance months ago. Now we just push CSS variables straight from Figma to our repository. The designer updates a colour in Figma. A pull request automatically appears in our GitHub repository with the raw CSS file. The developer reviews the visual diff and merges it. The pipeline is entirely transparent. There are no build scripts to maintain. This is exactly why I built Design System Sync. I got incredibly tired of writing parsing scripts for different teams. I wanted a tool that respects how the web actually works. It exports your Figma variables directly to GitHub or Bitbucket as ready-to-use CSS variables. It handles the formatting automatically. You can check it out at https://ds-sync.netlify.app?utm_source=devto&utm_medium=post&utm_campaign=bot or grab the plugin directly from the Figma Community at https://www.figma.com/community/plugin/1561389071519901700?utm_source=devto&utm_medium=post&utm_campaign=bot . It also supports W3C formats if you really need them. But honestly, you probably just need CSS. Are you still maintaining custom build scripts to parse JSON tokens for your web application?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/alexandersstudi/stop-exporting-json-tokens-and-use-css-variables-instead-3c33

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
