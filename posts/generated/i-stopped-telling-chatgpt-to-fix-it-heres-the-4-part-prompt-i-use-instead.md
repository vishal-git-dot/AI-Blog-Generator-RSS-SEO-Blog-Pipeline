---
title: "I stopped telling ChatGPT to 'fix it.' Here's the 4-part prompt I use instead."
slug: "i-stopped-telling-chatgpt-to-fix-it-heres-the-4-part-prompt-i-use-instead"
author: "Gideon Rüscher"
source: "devto_ai"
published: "Sun, 14 Jun 2026 19:17:46 +0000"
description: "For about a year I used AI to code like a slot machine. Paste a wall of code. Type "fix it" or "make this better." Pull the lever. Sometimes I won. Usually I..."
keywords: "you, what, one, code, before, model, skipped, fix"
generated: "2026-06-14T19:44:48.279256"
---

# I stopped telling ChatGPT to 'fix it.' Here's the 4-part prompt I use instead.

## Overview

For about a year I used AI to code like a slot machine. Paste a wall of code. Type "fix it" or "make this better." Pull the lever. Sometimes I won. Usually I got a confident answer that solved the thing I asked about and quietly broke two things I didn't. I assumed the problem was the model. So I switched models. Same slot machine, nicer graphics. The problem wasn't the model. It was that I was giving it almost nothing to work with and expecting it to read my mind. Once I started prompting with a bit of structure, the difference was bigger than any model upgrade I'd ever seen. Here's the structure. I call it C.O.R.E. , because I needed something I could actually remember at 11pm. C — Context The AI doesn't know what you know. It doesn't know your language version, your framework, or what the code is even supposed to do. If you don't tell it, it guesses — and a confident guess is exactly what produces code that looks right and isn't. So before anything else: language and framework with the version , and one sentence on what this thing does. "I'm working in Python 3.11 with FastAPI. This endpoint returns a user's recent orders." That one line removes about half the wrong answers before they happen. O — Objective "Improve this" is not an objective. The AI has no idea what "better" means to you — faster? shorter? safer? — so it picks one at random. Give it one concrete target : "Make this function return the orders sorted by date, newest first, without changing its signature." One task, stated like you'd state it to a junior dev who's about to touch your codebase. R — Rules This is the part almost everyone skips, and it's the one that saves you. Rules are your guardrails: "Don't refactor anything unrelated." "No new dependencies." "Keep it readable, I'm still learning." And the magic one: "If anything is unclear, ask me instead of guessing." That last rule alone killed most of my hallucination problems. Left to fill a gap, the model invents. Told to ask, it asks. E — Expected output Tell it what good looks like, or you'll get whatever it feels like — usually a 600-word essay when you wanted three lines. "Show me only the changed lines, then a two-sentence explanation." Diff vs. full file. Explanation first or code first. A specific format. Just say it. What it looks like put together Here's the before-and-after that made me a believer. Before: here's my function it's slow fix it [200 lines pasted] After: I'm working in Python 3.11. This function deduplicates a list of user records before we save them. Objective: it's slow on large inputs — make it faster without changing what it returns. Rules: no external libraries, keep it readable, and tell me why the current version is slow before you change it. Output: explanation first, then the rewritten function. The "before" gets you a random rewrite. The "after" gets you an explanation of why it was O(n²), a fix, and code you actually understand well enough to defend in a code review. Same model. Different result entirely. A few quick applications Once C.O.R.E. clicks, you start aiming it at everything: Debugging: "Before changing anything, explain in plain language what's causing this error and where. Then give me the smallest fix for the root cause, not the symptom." Learning: "Explain this code as if I'm a first-year student, using the actual variable names. Then list the 3 concepts I'd need to write it myself." — this turns the AI from an answer machine into a tutor. Refactoring: "Refactor for readability. Keep the exact same behavior and signatures. Explain each change in one line." The "same behavior + signatures" clause is what lets you trust the result. The anti-patterns (these are just missing letters) When an answer disappoints me now, I don't re-roll and pray. I ask which letter I skipped: Bad result, vague request → I skipped O . Answer for the wrong framework version → I skipped C . It rewrote half my file → I skipped R . It confidently made something up → I skipped the "ask me" R . It wrote an essay when I wanted a diff → I skipped E . Add the missing piece, send it again. It's almost never the model. That's the whole thing You don't need a prompt library with 500 entries. You need one structure you can recall from memory and adapt on the fly. Context, Objective, Rules, Expected output. That's it. I'm a student, not a guru — I just got tired of fighting the slot machine. If this saves you some of the time it cost me to figure out, it did its job. I put C.O.R.E. and a copy-paste master template on a single free cheatsheet — grab it here if you want it on hand while you work. (Everything you need is already in this post, though — no catch.)

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/gidschge/i-stopped-telling-chatgpt-to-fix-it-heres-the-4-part-prompt-i-use-instead-2he5

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
