---
title: "I Built a Bot That Reproduces GitHub Bugs Automatically — Here's What Broke (and What I Learned)"
slug: "i-built-a-bot-that-reproduces-github-bugs-automatically-heres-what-broke-and-what-i-learned"
author: "qxmcu"
source: "devto_python"
published: "Fri, 28 Aug 2026 10:35:36 +0000"
description: "The problem As a maintainer, even a solo one on a small project, the most time-consuming part of fixing a bug usually isn't writing the fix. It's reproducing..."
keywords: "issue, what, bug, ghost, bot, github, open, reproduction"
generated: "2026-08-28T10:48:56.454636"
---

# I Built a Bot That Reproduces GitHub Bugs Automatically — Here's What Broke (and What I Learned)

## Overview

The problem As a maintainer, even a solo one on a small project, the most time-consuming part of fixing a bug usually isn't writing the fix. It's reproducing it. Someone files an issue, the description is vague, and you spend twenty minutes just trying to get your machine into the same broken state theirs is in before you can even start debugging. I wanted that step gone. What I built Ghost Hunter is an open-source CLI + webhook bot that automates bug reproduction on GitHub. Comment bot/reproduce on any issue, and it: Parses the issue text with an LLM to extract environment details and repro steps Spins up an isolated Docker container matching that environment Actually runs the reproduction steps inside the sandbox Posts the crash logs back to the issue automatically No more "can you share more details?" back and forth. No more manually setting up an environment just to confirm a bug is real. ghost init # set up auth + LLM keys ghost serve # start the webhook listener Comment bot/reproduce on an issue, and Ghost Hunter takes it from there. What I didn't expect: the community feedback This is my first real solo open-source project, and I underestimated how valuable critical feedback would be the moment it went public. Within the first day, two commenters independently flagged real security concerns I hadn't fully thought through: Prompt injection risk : since the LLM parses raw, untrusted issue text into commands that run inside the container, a maliciously crafted issue could try to manipulate what actually executes. Network isolation : Docker's container isolation protects the host filesystem and processes — but by default, it doesn't restrict network access. A poisoned issue could still reach out to arbitrary hosts or scan a local network unless egress is explicitly locked down. My first instinct was mild panic. My second was: this is exactly the kind of feedback that makes a project better before it gets a chance to actually hurt someone. I dug in, understood the actual attack surface in my sandbox code, and shipped fixes rather than brushing the comments aside. Turns out I wasn't the only one who's had to think about this — Metabase's own internal bug-reproduction tool deliberately requires a human-in-the-loop trigger specifically to prevent this exact class of attack on public repos. That was a useful gut-check: a team with real security resources treated this as a hard requirement, not an afterthought. What's still a work in progress I'd rather be upfront about this than pretend the README says everything's perfect: GitHub App authentication (as opposed to Personal Access Token auth) is documented but not yet battle-tested end-to-end. Free-tier LLMs on OpenRouter vary a lot in reliability for the structured JSON output this tool depends on — I hit this myself with a model that would occasionally hallucinate a false "internal error" even when the underlying reproduction actually succeeded. Both are called out explicitly in the repo's README rather than hidden. Try it / break it It's fully open-source (MIT licensed): github.com/qxmcu/ghost-hunter I'd genuinely welcome more of the kind of feedback I got this week — bug reports, security concerns, "this is a bad idea because X," all of it. That back-and-forth is the best part of building in the open. Plus I have been working on my README a LOT. Be sure to check it out :)

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/qxmcu/i-built-a-bot-that-reproduces-github-bugs-automatically-heres-what-broke-and-what-i-learned-3b12

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
