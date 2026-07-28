---
title: "I Built a Reaction Time Test in 150 Lines of Vanilla JS (Here's Why)"
slug: "i-built-a-reaction-time-test-in-150-lines-of-vanilla-js-heres-why"
author: "dayu2333-jinyul"
source: "devto_webdev"
published: "Tue, 28 Jul 2026 14:20:27 +0000"
description: "I've always been curious about reaction time. How fast can my brain send a signal to my finger? Am I getting slower as I age? Do I react faster after coffee?..."
keywords: "you, reaction, time, click, your, test, average, built"
generated: "2026-07-28T14:22:20.798396"
---

# I Built a Reaction Time Test in 150 Lines of Vanilla JS (Here's Why)

## Overview

I've always been curious about reaction time. How fast can my brain send a signal to my finger? Am I getting slower as I age? Do I react faster after coffee? So I built a thing. The tool It's dead simple: click a box, wait for it to turn green, click again. 5 trials, get your average in milliseconds. Zero dependencies, one HTML file, works offline. Try the live demo → checkreaction.com Open source on GitHub → How it works under the hood The whole thing is ~150 lines of vanilla JavaScript. The timing is handled by performance.now() which gives sub-millisecond precision — way better than Date.now() . The tricky part was the "wait for green" phase. I randomize the delay between 1–4 seconds so you can't game it by anticipating. If you click before green, it calls you out and makes you redo that trial. const delay = 1000 + Math . random () * 3000 ; waitTimeout = setTimeout (() => { readyTime = performance . now (); waitingForGreen = true ; }, delay ); After 5 trials it gives you your average, best, worst, and a rating: Time Rating < 150 ms World Class < 180 ms Elite < 210 ms Excellent < 250 ms Above Average > 350 ms ...maybe try again after that coffee? What's a "good" score? The average human reaction time to visual stimuli is 200–250 milliseconds . If you're consistently under 200, you're doing great. Competitive gamers and F1 drivers often hit the 150–180 range. My personal best is 187ms. I'm not a professional gamer, just a dev who drinks too much cold brew. Why I built this Honestly? I wanted to know if I was getting slower. I'm in my early 30s and reaction time supposedly peaks around 24. I also wanted something simpler than the neuroscience lab tools — no signup, no download, no 15-minute test battery. Just click and see. The full version at checkreaction.com includes 17+ free games and a few other brain training tools (aim trainer, typing speed, sequence memory). But the core reaction test is the most popular by far. Try it yourself Go to checkreaction.com Click "Start Test" Post your score in the comments Or grab the source from GitHub and host your own. What's your reaction time? I genuinely want to know if anyone here is under 150ms.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dayu2333jinyul/i-built-a-reaction-time-test-in-150-lines-of-vanilla-js-heres-why-2eb0

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
