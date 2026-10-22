---
title: "Agents won't forgive your docs"
slug: "agents-wont-forgive-your-docs"
author: "Katarina Supe"
source: "devto_ai"
published: "Thu, 22 Oct 2026 11:19:06 +0000"
description: "I spent the last year in a black box. Maternity leave does that: the world keeps moving, and you only find out how far when you come back. I returned just to..."
keywords: "docs, every, they, agent, how, one, agents, experience"
generated: "2026-10-22T11:30:26.387292"
---

# Agents won't forgive your docs

## Overview

I spent the last year in a black box. Maternity leave does that: the world keeps moving, and you only find out how far when you come back. I returned just to land in another black box 😂 While I was away, working alongside AI went from an interesting experiment to the standard. On my first day, I already saw how much it helps. I also saw that it's a double-edged sword, and the first edge I noticed was the one closest to my job: documentation. Our users didn't change. How they reach us did. I lead developer experience at Memgraph. Developers mostly experience a product by using it, and they learn how to use it from the docs. That has always made docs quality a priority for me. Developers are fairly forgiving readers. They hit an outdated sentence, notice it doesn't match what they see in the terminal, shrug, and move on. Agents don't shrug. A developer often asks an agent now, and the agent reads the docs for them. If one page says one thing and another page says the opposite, I can't be sure which one the agent will pass on. Whichever it picks, it will say it with confidence. Our users are the same people. The way they interact with the product has changed, and we have to follow them. That's where agent experience comes in. Agent experience is mostly developer experience At its core, I don't think agent experience is very different from good developer experience. There are agent-specific pieces, like llms.txt and AGENTS.md , that help agents find their way. But the definition of well-written docs stays the same: a developer or an agent can use the product quickly, without struggling because of poor resources. And when they do run into a problem with the product, which will happen, they can find the workaround in the docs. What changes is how much a mistake costs. Agents read by mention, not by title Say a developer wants to understand durability. They'll open the pages with "durability" in the title, read them, and stop. An agent reads those pages too. Then it reads every page that mentions durability: a configuration reference, a migration guide, an old how-to written three releases ago. It takes them all in at once and builds its answer from all of them. If one of those pages still describes how things worked two versions ago, the agent has no idea. It has two claims that contradict each other and no reliable way to tell which one is current. Your user gets the right answer or the wrong one, and from where they sit, both look the same. Accuracy and coverage matter more than ever. A stale sentence used to be a small flaw on a page few people visited. Now it can end up in answers it was never meant for. What I'm doing about it This was the first red flag I noticed when I came back, so it's the first thing I decided to tackle. I group the rules into three questions. Is it true? Every code example should run. If it doesn't, it isn't an example. Every claim in the release notes should be checked against the docs. Every procedure, function and flag the docs name should exist in the product. Is it still true? When something new ships, documenting it isn't enough. Every page that mentions the feature needs a look too. Every docs PR is a chance to catch another mistake. Fixing one page often turns up an outdated sentence on the next. Can you find it? All links and redirects have to work. Every new page needs to sit in the right place and link to the right pages, so both people and agents can reach it. None of these are new rules. Any good docs team would have agreed with all of them ten years ago. But they were expensive to enforce by hand, so they mostly stayed good intentions. With AI, running every example, checking every mention and comparing claims across pages is finally practical. Some of this already runs on every docs PR. A project without a finish line I don't think this project ever ends. Products change with every release, and every change can quietly make a sentence somewhere untrue. That has always been the case with docs. What's new is that something now reads every sentence, then repeats it to your users. If agents read our docs, the docs have to be worth trusting. Keeping them that way is how we keep up with the AI world.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/katelatte/agents-wont-forgive-your-docs-3lb7

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
