---
title: "Two hotfixes in one day"
slug: "two-hotfixes-in-one-day"
author: "Nathan C."
source: "devto_python"
published: "Sun, 27 Sep 2026 04:03:03 +0000"
description: "This morning I shipped Flash 0.5.6. A hotfix. By the evening I shipped 0.5.7. Also a hotfix. What broke Flash kept forgetting what it said two messages ago. ..."
keywords: "flash, two, before, one, day, shipped, hotfix, what"
generated: "2026-09-27T04:44:48.251926"
---

# Two hotfixes in one day

## Overview

This morning I shipped Flash 0.5.6. A hotfix. By the evening I shipped 0.5.7. Also a hotfix. What broke Flash kept forgetting what it said two messages ago. The model was fine. The math wasn't. Flash reserved room for the model's reply, and on my setup that reservation was the entire context window. The conversation got whatever was left: about two messages. The fix The reply gets a quarter of the window, max. Your last three exchanges always stay word for word. Old tool output shrinks before anything else is dropped. Summarizing is now off by default. The history budget on my machine went from 1,024 tokens to about 114,000. One line of math. While I was in there A rewritten system prompt: reread the conversation, check before guessing, verify before saying done. Update Flash from the browser, with a restart that keeps you signed in. Flash can send HTML pages now, sandboxed in the web UI. The lesson Ship small. When it breaks, ship again. Same day is fine. curl -fsSL https://raw.githubusercontent.com/Natuworkguy/Flash/main/install.sh | bash Release notes: https://github.com/Natuworkguy/Flash/releases/tag/v0.5.7

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/natuworkguy/two-hotfixes-in-one-day-kpf

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
