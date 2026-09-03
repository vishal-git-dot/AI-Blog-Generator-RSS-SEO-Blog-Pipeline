---
title: "Three Questions I Ask Myself Before Adding a Dependency"
slug: "three-questions-i-ask-myself-before-adding-a-dependency"
author: "Den"
source: "devto_python"
published: "Thu, 03 Sep 2026 20:02:46 +0000"
description: "Every time I'm about to type npm install or pip install , I pause for a second. Not because I'm against libraries — I use them every day. It's because I once..."
keywords: "but, not, myself, package, question, one, project, three"
generated: "2026-09-03T20:48:32.216756"
---

# Three Questions I Ask Myself Before Adding a Dependency

## Overview

Every time I'm about to type npm install or pip install , I pause for a second. Not because I'm against libraries — I use them every day. It's because I once got burned on a project where package.json grew to 340 lines, and nobody could explain why half of those packages were there. Since then, I ask myself three questions. Nothing philosophical — they take less than a minute, but they save hours of untangling version conflicts and weird bugs six months down the road. Question 1: Can I really not write this myself in 20 lines? This is the most common source of self-deception. A library looks convenient because it "solves the whole problem," but often I only need 5% of what it does. The classic example is left-pad (yes, the one that broke half of the npm ecosystem in 2016). Padding a string on the left is a one-liner. It doesn't need to be a package with dependencies, tests, and versioning — it's literally: const leftPad = ( str , len , ch = ' ' ) => str . padStart ( len , ch ); I'm not saying all utility packages are evil. But if a function fits in 15-20 lines and doesn't need to handle edge cases I'll never actually encounter, I write it myself. The upside: I know exactly how it works when it breaks at 2 a.m. a year from now. The check is simple: I open the package source. If it's 200 lines of code and 15 dependencies for functionality I'm using 10% of — that's a red flag. Question 2: Who maintains this, and what happens if that person disappears tomorrow? This isn't a question about code quality today — it's about risk a year or two from now. I look at a few things: When was the last commit. Not "how long since the last release" — a package can be stable and just not need updates. What I care about is whether the maintainer responds to issues and PRs. How many maintainers. A single person maintaining something in their spare time isn't a dealbreaker, but it's a risk — especially if the package isn't a small utility but something a critical part of my project depends on (auth, money handling, data parsing). Are there active forks. If the original project has gone quiet but a fork is thriving, the community may have already voted with its feet, and that's where I should be looking instead. There's no universal threshold like "three months without a commit is bad." Sometimes a package just does one thing well and there's simply nothing to fix. The real question is: if it breaks, or a vulnerability is found, who fixes it, and how fast? Question 3: What happens to my project if I remove this dependency in a year? This question is about architectural coupling, not the library itself. I try to picture the scenario in advance: the library goes unmaintained, or I just want to swap it for something else. How deeply has it embedded itself in my code? If the dependency is used in one module behind a clean interface, replacing it is a one-day job. If its calls are scattered across the whole project, and its specific abstractions (custom state types, an unusual API) have become part of my own design, I'm stuck with it forever — even if I stop liking it. The practical takeaway: I try to wrap third-party libraries behind my own thin abstraction layer, especially for non-critical things like logging, an HTTP client, or date formatting. Not for the sake of "clean architecture" as an abstract virtue, but because it literally lowers the future cost of replacement from "rewrite half the project" to "rewrite one file." What this actually looks like in practice I'm not anti-dependency. I use React, FastAPI, pytest without a second thought, because the answer to all three questions is obvious: writing something comparable myself is unrealistic, maintenance is strong, and the coupling is so fundamental that replacement isn't even a real question. But every time I'm about to add a package for something small — date formatting, a debounce function, deep object comparison — I spend a minute on these three questions. Sometimes the answer is "yes, install it." Sometimes I close the terminal and write 10 lines myself. Fewer dependencies isn't the goal by itself. But every one I add is a future responsibility I'm taking on without thinking, unless I ask myself these questions first.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/den0011/three-questions-i-ask-myself-before-adding-a-dependency-1fjj

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
