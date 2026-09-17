---
title: "Project memory is not chat history: a tiny handoff layer for AI agents"
slug: "project-memory-is-not-chat-history-a-tiny-handoff-layer-for-ai-agents"
author: "Louis Wu"
source: "devto_python"
published: "Thu, 17 Sep 2026 16:05:02 +0000"
description: "I kept running into the same failure mode when switching between AI workers, browser sessions, or machines: the files were still there, but the exact working..."
keywords: "what, resume, project, next, state, handoff, scene, worker"
generated: "2026-09-17T16:39:14.788583"
---

# Project memory is not chat history: a tiny handoff layer for AI agents

## Overview

I kept running into the same failure mode when switching between AI workers, browser sessions, or machines: the files were still there, but the exact working point was gone. Conversation memory can tell a model what was said. RAG can retrieve relevant documents. Neither one is a durable answer to four operational questions: What is true now ? Why is that state trusted? What is already complete and should not be repeated? What should happen next? I built Resume the Scene as a very small, model-agnostic project-memory layer for that gap. GitHub: https://github.com/louisen0o0/resume-the-scene The idea The project keeps the handoff in files that live with the repository. A task state can look like this: @task{id:#t42|goal:#g1|state:active|done:[#e69]|next:#a7} @msg{op:resume|task:#t42|load:[#current,#e81]|skip:[#e69]|next:#a7} The important part is not the syntax. The important part is that another worker can deterministically recover what to load, what to skip, and what to do next without replaying the prior chat. What v0.1 does Resume the Scene is intentionally thin: selects the project files that form the active memory set; gives project documents explicit semantic roles; validates deterministic .rsm frames; produces checkpoint fingerprints; emits a compact resume message for the next worker; keeps project files as the source of truth instead of building a second knowledge base. There is no vector database requirement, no model-specific identity in the core protocol, and no requirement to archive prompts or responses. A small cross-agent fixture The repository now includes a handoff example where one worker has already completed evidence #e2 , and the next worker resumes from the same task state: resume-scene checkpoint examples/handoff resume-scene resume examples/handoff The resume result tells the next worker to skip completed evidence and continue with the next action. That fixture is executed in CI on Python 3.11, 3.12, and 3.13. Why I am sharing it this early The implementation is small enough to change. The state model is the part I want challenged before it grows. If you regularly hand work between coding agents or long-lived AI sessions, I would especially like feedback on this question: What state would you need to trust before allowing a different agent to continue a real project without replaying the previous conversation? The project is MIT licensed and the roadmap is public in GitHub Issues.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/louisen0o0/project-memory-is-not-chat-history-a-tiny-handoff-layer-for-ai-agents-2n03

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
