---
title: "The Codebase Was 40,000 Lines and the Engagement Was Three Days Long"
slug: "the-codebase-was-40000-lines-and-the-engagement-was-three-days-long"
author: "Rocky"
source: "devto_ai"
published: "Sat, 29 Aug 2026 16:27:49 +0000"
description: "A source-available pentest starts with the client handing over a repo, not a URL. This one was a mid-size monorepo, north of 40,000 lines across a dozen serv..."
keywords: "you, reading, instead, where, three, days, repo, not"
generated: "2026-08-29T16:32:00.482551"
---

# The Codebase Was 40,000 Lines and the Engagement Was Three Days Long

## Overview

A source-available pentest starts with the client handing over a repo, not a URL. This one was a mid-size monorepo, north of 40,000 lines across a dozen services, and the engagement window was three days. Reading all of it line by line, tracing every input from request to database, was never going to fit. The instinct on day one is to start at the top and read forward, hoping the important part turns up before the clock runs out. It usually doesn't. You burn the first day on files that turn out clean and reach the actual auth module, the one with the bug, on day three with no time left to write it up properly. The fix isn't reading faster. It's not reading everything. Used correctly, an LLM in this workflow isn't a hacker and isn't a substitute for the read. It's a fast, occasionally wrong research assistant whose only job is to tell you which 2,000 of the 40,000 lines deserve a human's full attention. That reframe changes what you ask it. "Find the vulnerabilities in this file" is the wrong question. It's broad enough that the model will confidently answer it anyway, whether or not there's anything real to find, and now you're fact-checking an essay instead of triaging a codebase. The useful version is narrow and mechanical: where does user-controlled input reach a raw SQL string instead of going through the ORM. Where does a request parameter get concatenated into a shell command or a file path. Where does an authorization check happen relative to the privileged action it's supposed to gate, and is there a code path that reaches the action without passing the check. Where does deserialization happen, and with what library. Each of those has a checkable answer: a file, a line, a specific claim you can go verify by reading the actual code path yourself in under a minute. Feeding it diffs instead of the whole repo helps the same way. When the question is "did this recent change introduce a bug" rather than "audit everything ever written here," a focused diff against a known-good baseline gets a sharper answer than the same question asked of the entire history at once. None of this replaces the manual trace. Every flagged line still gets read and confirmed by a human before it goes anywhere near a report, because the model is wrong often enough that treating its output as a finding instead of a lead is how a report ships with a claim nobody actually verified. What it changes is where the three days go: instead of spending day one reading clean code in file order, you spend an hour generating a heat map of the repo and two and a half days on the parts of it that are actually worth reading closely. This is the discipline Codelivly's AI for Penetration Testing book is built around: not an AI that hacks for you, but a red team workflow for prompt engineering, recon, code review and reporting that treats the model as a triage layer with a human doing every verification. If the last thing standing between you and a finding on a source-available engagement was running out of hours to read the whole repo, this is the part of the job that book is actually written for.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/rockyyy/the-codebase-was-40000-lines-and-the-engagement-was-three-days-long-4cl

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
