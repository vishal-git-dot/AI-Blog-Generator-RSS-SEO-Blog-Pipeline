---
title: "Untyped Python? Let Antigravity /goal Do the Cleanup"
slug: "untyped-python-let-antigravity-goal-do-the-cleanup"
author: "Giorgio Boa"
source: "devto_python"
published: "Thu, 09 Jul 2026 14:49:44 +0000"
description: "Python projects have a special way of aging. At first, everything feels light and fast. A few scripts, some helper functions, maybe a small API. Then six mon..."
keywords: "ruff, goal, antigravity, you, python, project, agent, until"
generated: "2026-07-09T15:22:18.571537"
---

# Untyped Python? Let Antigravity /goal Do the Cleanup

## Overview

Python projects have a special way of aging. At first, everything feels light and fast. A few scripts, some helper functions, maybe a small API. Then six months pass. The project grows. Functions start returning "whatever works." Dictionaries become informal data models. Tests still pass, mostly, but every refactor feels like walking through a dark room full of furniture. That is exactly where Antigravity CLI 's new /goal command becomes useful. The idea behind /goal is simple: instead of giving the agent one instruction and waiting for a single pass, you define an end state. Antigravity keeps working until that goal is reached, or until it has a clear reason to stop. For refactoring, this is a very natural fit, because cleanup work is rarely one-and-done. You fix one issue, run the toolchain, uncover ten more, repeat. A great example is taking an older Python project with little or no type discipline and moving it toward a cleaner, more maintainable baseline. My preferred first step is not "add perfect typing everywhere." That is usually too big, too vague, and too easy to derail. Instead, start with formatting and linting. Install Ruff , let it enforce consistency, and use Antigravity's /goal command to loop until the codebase is clean. First, add Ruff: uv add --dev ruff or, if the project still uses pip: pip install ruff Then configure a basic pyproject.toml if one does not exist: [tool.ruff] line-length = 100 target-version = "py314" [tool.ruff.lint] select = [ "E" , "F" , "I" , "UP" , "B" ] Now the useful part: give Antigravity a measurable goal. /goal Refactor this Python project toward a clean Ruff baseline. Run `ruff check --fix; ruff format;` repeatedly, inspect remaining errors, and update the code until Ruff reports no errors. Preserve behaviour and avoid broad rewrites unless required. That prompt works because the finish line is concrete: Ruff must pass. The agent is not guessing what "clean up the project" means. It has a command to run, feedback to read, and a clear loop: fix, format, check, repeat. This is where Antigravity CLI feels different from a normal chat-style coding session. The asynchronous workflow lets the agent keep running commands and iterating without turning every lint error into a manual back-and-forth. You can stay focused on the higher-level direction while the tool handles the mechanical cleanup. For untyped Python projects, Ruff is a good first refactor gate because it catches high-signal problems without requiring a full typing migration. Unused imports disappear. Import order becomes consistent. Risky patterns get flagged. Old syntax can be modernised. Formatting stops being a debate. After Ruff passes, you can raise the bar: /goal Add lightweight type hints to the public functions in this project. Keep changes minimal, run tests after each batch, and stop when tests and Ruff both pass. That second goal is much safer after the first cleanup. The code is already formatted, obvious lint issues are gone, and the agent has less noise to fight through. The most important lesson: /goal works best when paired with verifiable commands. "Make this better" is weak. "Run Ruff until it passes" is strong. "Add types while tests keep passing" is strong. "Refactor without changing behavior" becomes much more realistic when the agent has tests, linters, and formatters as feedback. For me, this is the real value of Antigravity CLI's /goal : it turns refactoring from a single fragile prompt into a controlled loop. The agent is not just editing code. It is working against a measurable definition of done and for messy Python projects, that is exactly what you want. You can follow me on GitHub , where I'm creating cool projects. I hope you enjoyed this article, until next time 👋 Giorgio Boa Follow Giorgio Boa is a full stack developer and the front-end ecosystem is his passion. He is also international public speaker, active in open source ecosystem, he loves learn and studies new things.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/gioboa/untyped-python-let-antigravity-goal-do-the-cleanup-10mh

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
