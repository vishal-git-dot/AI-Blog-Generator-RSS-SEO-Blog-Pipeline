---
title: "Boards: a Kanban board your agents run"
slug: "boards-a-kanban-board-your-agents-run"
author: "JackHamr"
source: "devto_ai"
published: "Tue, 29 Sep 2026 21:57:47 +0000"
description: "We spent the spring making one agent excellent and then giving it the ability to fan out. Boards are where that pays off. This is the release that turns Jack..."
keywords: "agent, agents, card, ten, boards, one, you, task"
generated: "2026-09-29T22:04:59.852407"
---

# Boards: a Kanban board your agents run

## Overview

We spent the spring making one agent excellent and then giving it the ability to fan out. Boards are where that pays off. This is the release that turns JackHamr from a very capable agent into a fleet you direct from one screen. How it works Boards are a new top-level surface beside Agents. A board is a Kanban board, and every card on it is a task an agent will execute through a workflow. Write the card, drop it in Ready, and it dispatches. The card moves across the stages on its own as the workflow progresses, showing the agent's latest message and any question it is waiting on. Open a card and you get a full-page task view: the conversation, milestones, and an embedded browser, terminal, editor, and publish panel. Everything about that task, in one place, without leaving the board. Execution modes The interesting part is what happens when you drop ten cards at once. Queue mode runs them one after another on the same agent, for work that has to happen in order Clone mode gives every card its own dedicated clone of the agent, with its own machine, so ten cards means ten agents working in parallel Distribute mode hands cards to whichever teammate agent is idle Per card, you choose the stages and the model. Some tasks deserve Opus and a full review; some deserve a fast model and a quick pass. The morning we started using it ourselves Ten ideas written down before coffee. Ten cards in Ready. By lunch, ten agents had specs waiting for approval, and the approvals took about four minutes. The bottleneck was never implementation. It was always deciding what to build. Boards make that the only thing you have to do. Many agents in parallel, on real machines, and the only interruptions are the decisions that need your taste. Boards grew fast after this: a Done column, archiving, attention flags, organization-wide task numbers, attachments, and per-task pre-approval all arrived within weeks. A full redesign followed in September. But the idea has not changed since day one. Originally published on the JackHamr blog . JackHamr is an AI agent platform where agents plan, build, test, and review software end to end. Free to start.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/jackhamr/boards-a-kanban-board-your-agents-run-2n6f

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
