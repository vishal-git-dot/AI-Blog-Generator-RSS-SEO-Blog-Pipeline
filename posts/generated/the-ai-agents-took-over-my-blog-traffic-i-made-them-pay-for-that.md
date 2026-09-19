---
title: "The AI Agents Took Over My Blog Traffic. I Made Them Pay For That…"
slug: "the-ai-agents-took-over-my-blog-traffic-i-made-them-pay-for-that"
author: "Dragos Roua"
source: "devto_ai"
published: "Sat, 19 Sep 2026 04:02:54 +0000"
description: "On a good day, Google sends to my blog about 20 people (clicks on the search results). On the same day, though, Google Search Console also shows me around 40..."
keywords: "agents, html, they, now, blog, file, pay, content"
generated: "2026-09-19T04:04:08.805925"
---

# The AI Agents Took Over My Blog Traffic. I Made Them Pay For That…

## Overview

On a good day, Google sends to my blog about 20 people (clicks on the search results). On the same day, though, Google Search Console also shows me around 400-450 AI citations. That means agents consuming my content – either for responses in chat, or for training. The worst part? They never asked for permission, those bots. So I made AI agents pay for that. If you’d rather see this as a video, just check out the link above. If you prefer reading, go on. How Did I Make Agents Pay? The blog you’re reading right now at https://dragosroua.com is a static site. It’s built with astro, which pulls data from my old WordPress engine (I still add content there). Every build generates an .html file that’s served indiscriminately to everyone: humans, Google index bot, AI agents. I added an extra step in the astro build process, that takes the content I’m getting from WordPress, and turns it into a stripped down markdown file, just the title, the publication date and the body. So now there are 2 files with the same slug, but 2 different suffixes: blog-post.html (technically, this is blog-post/index.html, but that is not relevant for now blog-post.md Now, if an agent takes in an .html file, it still needs to do some parsing to get rid of the HTML tags, CSS, header metadata, javascript snippets, etc. This consumes some tokens. On the other side, if they just get the .md , they already have the content, no need for parsing. On average, a model consumes 3x more tokens for HTML content than for markdown. On an expensive model (Opus, Astra, Grok) this may come up to $0.01. So, I hid the .md file behind a x402 paywall (402 is actually part of the http specification, it was around since all the other codes: 404, 301, etc. Only recently there were actual implementations on the protocol, and the most popular one was launched and supported by Coinbase). So what happens now, is that the agents are having a conundrum: parse HTML and spend a variable (not known beforehand) amount of tokens get the parsed .md and pay $0.01 The signal for this is given in the llms.txt file, which is a specification followed (in theory) by all agents. They read that file, and they understand how they can consume my site. Links inside llms.txt used to be all HTML, now they’re pointing specifically to the .md files. Of course, not all of them are complying, and I’m not expecting all agents to pay now, but at least I’m trying. I’m sending the right signal, showing that the data is served on different levels, that it has some value, and that it comes with a bit of convenience – being already stripped down in a format AI agents understand.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dragos_roua/the-ai-agents-took-over-my-blog-traffic-i-made-them-pay-for-that-596g

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
