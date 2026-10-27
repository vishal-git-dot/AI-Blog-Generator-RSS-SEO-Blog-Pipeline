---
title: "Why markdown plans break when you run multiple AI agents"
slug: "why-markdown-plans-break-when-you-run-multiple-ai-agents"
author: "Ahmad Shawar"
source: "devto_ai"
published: "Tue, 27 Oct 2026 21:55:01 +0000"
description: "Most of us coordinate AI coding agents the same way: a markdown file in the repo with a checklist. The agent reads it, picks an item, does the work, ticks th..."
keywords: "agent, agents, what, same, task, can, you, two"
generated: "2026-10-27T22:00:01.246100"
---

# Why markdown plans break when you run multiple AI agents

## Overview

Most of us coordinate AI coding agents the same way: a markdown file in the repo with a checklist. The agent reads it, picks an item, does the work, ticks the box and commits. For one agent in one session, it works well. Then you start a second session. And a third. What goes wrong Two agents pick the same item. Nothing in a markdown file stops two readers from choosing the same line at the same moment. You find out when both open a PR for the same fix. An agent dies mid-task. The session times out, the laptop sleeps, the context runs out. The item stays marked "in progress" and no other agent will touch it. Edits race each other. Two agents update the plan at once, and one change is lost or turns into a merge conflict an agent then "resolves" badly. History lives in git diffs. Who claimed what, when, and why it was rejected is buried in commit history, if it was recorded at all. Nobody can see it. You can't tell at a glance which agent is on what, or what has been stuck for an hour. None of these are agent problems. They're the classic problems of shared mutable state, and a file is the wrong place for it. What a fix needs Atomic claims. Two claimers can never get the same item. Expiry. A claim that isn't refreshed goes back to the pool. Legal transitions only , with an error that tells the model what is allowed instead. Review as a step , not an afterthought: approve, send back, or escalate. An append-only history of every change. Visibility : a live view for people, and updates where the team already looks, without making agents wait on GitHub or Slack. How workstream-mcp does it I built workstream-mcp to cover that list. It's an MCP server, so agents use it through ordinary tool calls. Claims run in one Postgres transaction with SELECT ... FOR UPDATE SKIP LOCKED . Concurrent claimers skip rows that are already locked instead of waiting on them, so 32 agents claiming at once each get a different task, and none of them block. A test suite runs exactly that. Each claim has a TTL. If an agent stops refreshing it, the task returns to the pool. A plan can also cap how long a claim lives and refuse refreshes when the holder hasn't recorded any progress, so an agent stuck in a loop that keeps its heartbeat going still lets go. Dependencies decide what can run in parallel. When the orchestrator breaks work into tasks, it declares which ones depend on which, typically because they touch the same module. claim_next_task skips a task until its dependencies are done, so two agents never work the same code at once, and tasks that don't overlap run side by side. The state machine is data. Each plan type stores its statuses, transitions, allowed roles and retry caps in a JSON graph. If an agent tries an illegal move, the tool returns illegal_transition along with allowed_next . In practice the model reads that and corrects itself. Reviews are part of the flow. A developer agent submits an attempt; a reviewer approves it or sends it back to the pool for another pass. After the retry cap, the task goes to a human. Every change writes an event. Database triggers block updates and deletes on the event log, so the history can't be rewritten after the fact. GitHub and Slack go through an outbox. The change and its notification commit in the same transaction, and a background worker delivers it with retries. A GitHub outage never fails an agent's tool call. The dashboard shows each plan as a board: who holds each task, how long their claim has left, what is waiting on what, and what is stuck. It reads through the same tools the agents call. Try it docker run --rm -p 127.0.0.1:8080:8080 -e WORKSTREAM_ADMIN_TOKEN = local-admin \ ghcr.io/ahmad-codex/workstream-mcp:demo Open http://localhost:8080/demo-insecure-token/ui/ . From a clone of the repo, WORKSTREAM_ADMIN_TOKEN=local-admin node scripts/simulate-agents.mjs runs two developer agents and a reviewer against a ten-task plan, so you can watch claims move across the board. To connect your own agent: claude mcp add --transport http workstream-demo http://localhost:8080/demo-insecure-token/mcp , then ask it to claim the next task. For a real setup, clone the repo, open Claude Code in it and paste the setup prompt from the README. It's MIT licensed. The roadmap is public, with good first issues for webhooks, connectors and SDKs. Several of these details came straight from the first Reddit thread: the outbox transaction and the refresh limits both shipped within a day of someone pointing at them. I'd especially like to hear how you coordinate multiple agents today, and what breaks.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ahmad_shawar_de8d35d546cf/why-markdown-plans-break-when-you-run-multiple-ai-agents-h11

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
