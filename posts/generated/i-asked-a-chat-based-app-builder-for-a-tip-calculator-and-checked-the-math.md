---
title: "I asked a chat-based app builder for a tip calculator and checked the math"
slug: "i-asked-a-chat-based-app-builder-for-a-tip-calculator-and-checked-the-math"
author: "Kai Mercer"
source: "devto_webdev"
published: "Fri, 23 Oct 2026 11:09:54 +0000"
description: "Disclosure: I work on marketing for Hyde, the tool in this post. I wanted to write down what I saw when I tested it, including the part that didn't hold up. ..."
keywords: "tip, one, bill, chat, calculator, what, didn, app"
generated: "2026-10-23T11:19:44.659503"
---

# I asked a chat-based app builder for a tip calculator and checked the math

## Overview

Disclosure: I work on marketing for Hyde, the tool in this post. I wanted to write down what I saw when I tested it, including the part that didn't hold up. Hyde ( https://hyde.pixelverse.tech ) is a chat-based app builder: you describe an app, and it writes the code and shows a live preview. I tried it on one small thing, a tip calculator, because the correct answers are easy to check by hand. The prompt I gave it one message: A tip calculator: bill amount, tip percent buttons (10, 15, 20) and a custom percent, number of people to split between, and a clear result showing tip and amount per person. What it did It listed two tasks, edited src/pages/Index.tsx and src/index.css , and then ran a build check. The chat showed the work as it went, with the files it touched. The whole build took 1 minute 34 seconds and the interface showed it as 1 credit on the free plan. The result was a styled page with a bill field, 10/15/20 buttons, a custom percent field, a people counter, a reset button and a breakdown panel. The chat said the app builds and renders without errors. What I tested I typed values into the preview and checked the arithmetic by hand. Bill 87.50, custom tip 18%, 1 person. Tip $15.75, total $103.25. Correct. Same bill, 3 people. Per person: bill $29.17, tip $5.25, total $34.42. Each figure is right when rounded. Bill of -20. The breakdown shows $0.00 everywhere, so nothing breaks. The field still shows -20, though. What didn't hold up Three people paying $34.42 each is $103.26. The calculator's own total is $103.25. That is a one-cent gap between the per-person amounts and the full bill, which is the classic split-bill rounding problem. It shows both numbers on the same screen, so a careful user would notice. Nothing in my one-message prompt asked for rounding rules, so I can't say this is a bug in the tool. It's a case the first draft didn't cover. The chat also offered follow-up suggestions, such as remembering the last-used tip and adding rounding controls for splits. I didn't run those, so I can't say how they'd turn out. What I did not test The Hyde site also describes publishing to a custom domain, GitHub sync and a built-in backend. I haven't tried those, so I'm not making claims about them here. This was one prompt, one project, one afternoon. Takeaway For a small, well-defined app, one plain-English message got a working and good-looking calculator with correct core math. The thing to check is the edge cases you didn't mention. Splitting money is a good test for any code you didn't write by hand: try an amount that doesn't divide evenly and see whether the parts add up to the whole. What edge case would you test first on a calculator built from one chat message?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/mercerk17/i-asked-a-chat-based-app-builder-for-a-tip-calculator-and-checked-the-math-35i4

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
