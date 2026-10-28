---
title: "How I caught a crash by actually running someone's fix"
slug: "how-i-caught-a-crash-by-actually-running-someones-fix"
author: "CH"
source: "devto_python"
published: "Wed, 28 Oct 2026 21:56:39 +0000"
description: "Most code review on open source PRs is reading. Someone looks at the diff, it makes sense, they leave a thumbs up. I've started doing something a bit differe..."
keywords: "windows, click, llm, you, what, running, ran, diff"
generated: "2026-10-28T22:24:29.414368"
---

# How I caught a crash by actually running someone's fix

## Overview

Most code review on open source PRs is reading. Someone looks at the diff, it makes sense, they leave a thumbs up. I've started doing something a bit different: I actually install the PR and run it. On Windows, which turns out to be the part that matters. Today I tried it on three open PRs in simonw/llm , the command-line tool for talking to language models. Here's what happened. PR 1: a clean exit that crashed on start This PR made llm chat exit cleanly when you hit end-of-input, instead of printing "Aborted!". The diff was small and looked fine. But it called click.termui._readline_prompt , a private function inside the click library. That function only exists in click 8.4 and newer, and llm doesn't pin a click version. So I set up a throwaway venv and ran it three ways: main: "Aborted!" (the original bug) the PR with click 8.5: clean exit, works the PR with click 8.3.1: AttributeError the moment chat starts So the fix works on the newest click and breaks chat completely on anything older. Reading the diff, you'd never see that. I posted the results and suggested either pinning click>=8.4 or catching EOFError around a plain input() . PR 2: a Windows fix that still fails on Windows This one was about llm install / llm uninstall , running pip in a separate process so llm can update itself. On Windows I ran the self-reinstall case on main and on the PR. main: pip refuses to modify itself the PR: WinError 5 (access denied) on a .pyd file The running llm process has that compiled extension loaded, and Windows locks loaded files, so the child pip can't replace it. Different error, same result: it still can't reinstall itself while running. Again, nothing in the diff tells you that. You have to run it on Windows. PR 3: a cleanup that was just fine The third PR removed some old Windows-only readline setup lines. The author said they couldn't reproduce the original problem, so nobody was sure it was safe. I ran it on main and on the PR, checked that chat opens and arrow keys still work, and both behaved the same. So I left a short "tested on Windows, looks good as a cleanup". Not every test finds a bug, and a confirmed "it's fine" is useful too. What I took from it Running a PR takes maybe 15 minutes with a throwaway venv. That's often more than the author could do, because they might not have your OS or your versions. Private functions and unpinned dependencies are where "works on my machine" hides. Try the oldest version the project allows, not just the newest. Windows is underrepresented among testers. If you're on Windows, you're already useful. Post exactly what you ran and what happened. Let the maintainer decide what to do with it. Disclosure: I used AI (Claude) to help pick PRs, write the little test scripts, and draft this post. I ran every test myself on my own PC, and the results above are what I saw.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/connabyss/how-i-caught-a-crash-by-actually-running-someones-fix-2pmp

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
