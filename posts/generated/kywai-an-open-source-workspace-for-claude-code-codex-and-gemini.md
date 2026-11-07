---
title: "kywai: an open-source workspace for Claude Code, Codex and Gemini"
slug: "kywai-an-open-source-workspace-for-claude-code-codex-and-gemini"
author: "yilsander ramirez"
source: "devto_ai"
published: "Sat, 07 Nov 2026 21:21:58 +0000"
description: "Switching between coding agents also means moving context between them, deciding who handles each task, and working out what changed afterward. I'm building ..."
keywords: "agent, you, task, agents, kywai, workflow, one, app"
generated: "2026-11-07T21:39:06.288479"
---

# kywai: an open-source workspace for Claude Code, Codex and Gemini

## Overview

Switching between coding agents also means moving context between them, deciding who handles each task, and working out what changed afterward. I'm building kywai to bring that workflow into one desktop app. It is free and MIT-licensed, with downloads for Windows, macOS and Linux. I'm looking for developers who already use coding agents to try a small task and tell me where the workflow breaks down. What it does kywai brings Claude Code, Codex CLI, Gemini CLI and local models through Ollama or LM Studio into a shared project workspace. A coordinator proposes a plan, delegates work to agents, and can ask another agent to review the changes. For CLI-based agents, kywai runs the underlying CLI with your own agent access. Provider subscriptions, usage limits and any API costs remain separate from the app. The interface combines a chat, task progress and file changes with a live 3D world: each agent has a robot that shows its activity. You can also address an agent directly when a task does not need a coordinated plan. The part I want feedback on: reviewing changes One of the first questions raised after I shared the project was how to tell which agent changed which files, especially when more than one agent touches the same file. That is a useful test of whether coordination is actually helping. The current app has Git-backed task diffs and undo. Those diffs show changes after they have been applied; they are not a pre-apply approval screen. I do not want to describe that as a solved trust problem. The question I want to explore is: does the combination of task progress, file diffs and another agent's review give you enough information to keep working, or do you still need to reconstruct the whole sequence yourself? Under the hood The desktop app uses Electron, React and Three.js. The source is public, so you can inspect how the agents are launched and how the coordination works: Source code on GitHub The 3D view makes agent activity visible, but the practical value has to come from the workflow. Being able to connect several providers is only a starting point; I want to find out which tasks benefit from coordinating them. A small task to try If you already use one of the supported coding agents, try kywai on a small test project: Ask an agent to make one small change, such as improving a validation message or adding a test. Ask another agent to review the result. Inspect the changed files and compare the experience with your normal workflow. If you try it, please share your operating system, the agents you used, and the step that caused the most friction. Was setup straightforward? Could you tell what each agent did? Would you use the same workflow for another task? Demo and downloads I'm the developer. The app is free; provider costs and limits still apply. The desktop builds are not code-signed yet.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/yilsander_ramirez_377a00f/kywai-an-open-source-workspace-for-claude-code-codex-and-gemini-40pa

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
