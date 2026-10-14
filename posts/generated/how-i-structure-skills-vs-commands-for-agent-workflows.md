---
title: "How I structure skills vs. commands for agent workflows"
slug: "how-i-structure-skills-vs-commands-for-agent-workflows"
author: "Nirmal"
source: "devto_ai"
published: "Wed, 14 Oct 2026 04:05:36 +0000"
description: "Skills hold knowledge and commands hold intent. Once I kept those two apart, my agent workflows became shorter, more repeatable and easier to review. Disclos..."
keywords: "one, you, what, agent, commands, skill, how, skills"
generated: "2026-10-14T04:22:01.696176"
---

# How I structure skills vs. commands for agent workflows

## Overview

Skills hold knowledge and commands hold intent. Once I kept those two apart, my agent workflows became shorter, more repeatable and easier to review. Disclosure: I'm the founder of AgentKrew , a kit for coding agents that I use as the example throughout. The ideas work without it, and I'll say where they stop working. The trouble with one big prompt A common starting point is one long prompt pasted at the start of every session: the conventions, the reminders, the list of things not to touch. It works for a while. Then it grows until nobody reads it, and the results shift with how it was phrased that day. The fix is to stop treating instructions as one thing. Some of it is knowledge, such as how migrations are done here. Some of it is intent, such as "plan this feature." Mixing both in one prompt is what makes it fragile. Skills: knowledge the agent pulls in A skill is a reusable set of instructions for one job, such as how migrations are done, how auth is handled or how tests are written. The agent loads it when the task calls for it. The point is that you write the convention once instead of re-explaining it every session. Rules I follow when writing one: One job per skill . If you can't name the job in a few words, split it. Reference, not orders . A skill says what the agent should know. What to do right now belongs elsewhere. Project facts live here . Billing rules, naming conventions and the files never to touch all belong in a skill. Short enough to review . When something goes wrong, you should be able to read the skill in a minute and find the cause. Commands: one-word entry points A command is the short thing you type to start a repeatable step: plan, review, test. It carries intent and points at the knowledge needed to carry it out. Name the action, not the topic . "plan", "review" and "test" are commands. "migration notes" is a skill. Keep commands thin . If a command is full of knowledge, move that knowledge into a skill and let the command call it. One step each . If you can't describe what it does in a sentence, it is two commands. A useful test: skills answer "what should the agent know?" and commands answer "what should it do now?" Agents and workflows tie it together Skills and commands still need someone to run them, and an order to run them in. Agents are named specialists defined by role: tech lead, builder, reviewer, security auditor. Each has a routing description so the right one picks up the right work. A reviewer's job doesn't change when the tool running it does. Workflows are fixed sequences, not improvisation. The tech lead plans, specialists build in parallel, and then a reviewer, a security auditor and a shipper act as gates before anything goes out. Because the sequence is fixed, two runs of the same workflow follow the same steps. That predictability is the point: you review a plan and a gated result, not a stream of improvised decisions. One source of truth for every tool If you use more than one coding agent, instruction files drift. Two files that start identical slowly come to disagree. The cheapest fix is to keep AGENTS.md as the source and have CLAUDE.md point to it, so there is one place to edit. AgentKrew takes the same idea further. The same kit renders to Claude Code, Codex and OpenCode, so the roles and workflows you define don't depend on which tool runs them. End every workflow with a release gate The last step of a workflow shouldn't be "looks good." It should be a check that runs the type check, the tests, lint and the build, and returns one of two answers: ready or blocked. The gate works no matter which tool wrote the code, because it only looks at the result. It also gives the human a clear moment to step in. A blocked result tells you what failed before anything ships, instead of a green-looking diff that hides a problem. A quick way to decide which piece you need Each piece answers a different question. If you can't say which question an instruction answers, split it. Piece Question it answers Example Skill What should the agent know? How migrations are done here Command What should it do now? Plan, review, test Agent Who does it? Reviewer, security auditor Workflow In what order? Plan, parallel build, gate Limits, and where AgentKrew fits Agents don't learn between sessions. A human teammate remembers the billing module after six months, while an agent starts fresh every time. Putting context in skills and files is a workaround, and you still maintain those files. Treat them like code and review changes to them. A separate reviewer helps, but it doesn't replace tests you can trust. Whatever tool you use, check who writes the tests: if one pass writes the code and its own assertions, a green run proves very little. AgentKrew is my attempt to package this structure: agents, skills, commands and workflows as one versioned, validated kit that renders to Claude Code, Codex and OpenCode, with updates that don't touch your own files. If you want to look at it, it's at agentkrew.com. I'd like to hear what's missing.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/nandy121/how-i-structure-skills-vs-commands-for-agent-workflows-m73

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
