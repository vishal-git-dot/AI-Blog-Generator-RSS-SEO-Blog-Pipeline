---
title: "The Day I Realised Our Code Reviews Were Making Us Worse"
slug: "the-day-i-realised-our-code-reviews-were-making-us-worse"
author: "Om Keswani"
source: "devto_ai"
published: "Wed, 01 Jul 2026 09:59:05 +0000"
description: "Two years ago, I submitted a pull request I was genuinely proud of. It fixed a gnarly concurrency bug that had been causing random 502s in production for wee..."
keywords: "but, had, comment, not, our, one, code, been"
generated: "2026-07-01T09:59:55.961562"
---

# The Day I Realised Our Code Reviews Were Making Us Worse

## Overview

Two years ago, I submitted a pull request I was genuinely proud of. It fixed a gnarly concurrency bug that had been causing random 502s in production for weeks. The fix wasn’t pretty—a carefully placed mutex, a refactored retry loop, and a comment block longer than the method itself explaining why the obvious approach would deadlock under load. I pushed the branch, opened the PR, and went to grab coffee, feeling that rare mix of relief and competence that comes from actually solving something hard. By the time I sat back down, I had six comments. None of them mentioned the race condition. The first one flagged that I’d named the mutex syncLock instead of mu, which wasn’t our standard. Fair enough. The second suggested I extract the retry logic into a helper—fair, but not urgent. The third asked if the comment block should be a docstring instead. The fourth wanted to know why I hadn’t used context.WithTimeout in a place where it genuinely didn’t matter. The fifth pointed out a typo in a log message. The sixth was an approving emoji on the typo catch. I remember staring at the screen, waiting for someone—anyone—to ask the hard question. Does this actually eliminate the race, or just shrink the window? What happens if the mutex is held during a pod restart? I had answers, but nobody asked. The review thread hummed with activity, and every single comment was correct in isolation, yet the sum total of that review was zero added safety. It was a masterclass in being technically right while being functionally useless. That afternoon, the PR was approved. The bug fix shipped, and it worked. But I couldn’t shake the feeling that I’d been let down—not by my teammates, who were smart and well-intentioned, but by the machine we’d built together. Our review process had evolved into a game where points were scored by spotting superficial inconsistencies, while the big, scary questions sat silently in the corner, hoping not to be called on. A month later, I was on the other side of the table, reviewing a colleague’s PR. It introduced a new caching layer that, on the surface, looked impeccable. Small functions, clear names, full test coverage. My cursor hovered over a section that handled cache invalidation, and a quiet voice in my head said, I don’t think this handles backfill correctly. But I’m not 100% sure, and asking would mean reading a lot of upstream code. Instead, I left a comment about a misleading variable name. It got resolved quickly. The PR merged. Two sprints later, we spent a weekend debugging stale cache entries that were serving wrong data to paying users. The variable name had been perfect, though. I started bringing this up in retros, not as an accusation but as a puzzle. Why do we gravitate toward the small stuff? My manager, who had been unusually quiet, finally said something that stuck: “Because the small stuff is safe to be wrong about. If I tell you to rename a variable and I’m mistaken, the worst thing that happens is a slightly awkward follow-up comment. If I ask a question about your concurrency model and I’m wrong, everyone sees that I don’t understand a critical part of the system. Our process rewards looking smart over being thorough.” That was it. Pedantry wasn’t a character flaw; it was a rational response to an environment where surface-level correctness earned social credit and deep uncertainty cost it. We’d accidentally gamified our reviews to punish the very vulnerability that makes them useful. We changed one small rule the next week. Every reviewer had to leave at least one comment that started with “I wonder…” or “What happens if…”—a prompt that could only be answered by thinking about behaviour, not syntax. It felt clunky at first, like learning to write with your other hand. But slowly, the nature of our threads shifted. Someone “wondered” if the mutex approach would hold up during a leader election. That question led to a short, productive discussion and a follow-up task that probably saved us another late-night page. The typos still got caught—they always do—but they stopped being the whole conversation. I still think about that concurrency PR sometimes. Not because the bug fix was brilliant, but because it showed me something I needed to see: a team can be technically impeccable and still be dangerously negligent, simply by letting comfort steer the feedback. The scariest code review isn’t the one with a lot of red ink. It’s the one where every comment is a minor style note and nobody asks what the code actually does when the lights go out.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/omieee_24/the-day-i-realised-our-code-reviews-were-making-us-worse-53m8

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
