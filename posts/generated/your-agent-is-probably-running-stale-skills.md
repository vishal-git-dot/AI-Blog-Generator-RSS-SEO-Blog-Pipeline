---
title: "Your agent is probably running stale skills"
slug: "your-agent-is-probably-running-stale-skills"
author: "Louis Esterhuizen"
source: "devto_ai"
published: "Fri, 13 Nov 2026 23:20:55 +0000"
description: "Agent skills are folders with a SKILL.md that teach Claude Code, Codex and other agents how to do something specific: review a React app, plan a feature with..."
keywords: "skill, skills, check, your, version, you, agent, claude"
generated: "2026-11-13T23:25:16.994414"
---

# Your agent is probably running stale skills

## Overview

Agent skills are folders with a SKILL.md that teach Claude Code, Codex and other agents how to do something specific: review a React app, plan a feature with Spec Kit, write a Hugging Face training script. They're easy to share, so most people install them the simple way, by copying the folder into their skills directory. That's where it goes quietly wrong. Once a skill is copied, nothing tracks it. The author fixes a mistake, adapts to a new API, or rewrites the instructions, and your copy stays as it was. And a stale skill doesn't fail. There's no error, just an agent that follows last spring's advice and does slightly worse work, and you have no reason to suspect the skill. How common is this? I counted the 597 SKILL.md files in seven of the biggest public collections: Anthropic's, OpenAI's, GitHub's awesome-copilot, Hugging Face's, Vercel's, obra/superpowers, and the skills bundled with Codex. Only 41 record a version at all ( metadata.version ), and only 17 say where they came from ( metadata.source ). Most of those versions are "1.0" or "1.0.0" , and they stay that way. Vercel's react-best-practices has changed in more than ten commits since January and still says 1.0.0 . So even when a skill has a version number, comparing version numbers would miss most updates. And 580 of the 597 carry no record of where they came from, so a copy of one can't find its way back. What I built skill-check is a small open-source plugin for Claude Code and Codex. At the moment a skill is used, it checks whether a newer version exists and, if so, shows a warning: [skill-check] The skill "speckit-plan" is out of date: installed 0.12.0, latest v0.13.1. Run `specify self upgrade`, then `specify integration upgrade claude` in this project. The agent sees the warning too, mentions it to you, and carries on. Nothing is blocked. It knows a skill is stale in three ways: metadata.source in the SKILL.md. It compares your copy with the upstream copy at that URL: by version when upstream's is higher, otherwise by content and, for GitHub sources, the file's commit history. That's how it catches the 1.0.0 skill that changed ten times: it matches your copy to the commit it came from and sees that upstream has moved on. Spec Kit. speckit-* skills are compared with the latest Spec Kit release. npx skills . Skills installed with npx skills add are compared with the hash in its lock file. A check runs in the background when a session starts, and results are cached for a day, so using a skill is instant. Offline or rate-limited means silence, never a broken session. It has no server and no telemetry, and it only fetches the public files it compares against. The convention matters more than the tool The part I care about most is two lines any skill author can add today, with no changes to the Agent Skills spec: metadata : version : 1.2.0 source : https://github.com/you/your-skills/tree/main/your-skill source is the important one: it travels with every copy, so any tool, not just mine, can find the upstream again. version is a useful hint on top. I've written it up as a short convention ( CONVENTION.md , CC BY 4.0) and shared the evidence on the Agent Skills spec discussion that proposes the same keys. If agents end up checking this natively, skill-check will have done its job. Try it Claude Code: /plugin marketplace add louis8408/skill-check /plugin install skill-check@skill-check Codex: codex plugin marketplace add louis8408/skill-check codex plugin add skill-check@skill-check You need Node.js 20 or later. The README has a two-minute "Try it" that installs an outdated example skill so you can see the warning, and a check command that lists the status of every skill you have. If you maintain skills: please add metadata.source . It's one line, and it's what lets your fixes reach the people who copied your skill. I built skill-check with Claude Code's help, and Claude Code helped draft this post.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/louis_esterhuizen_8aa8bb8/your-agent-is-probably-running-stale-skills-18pe

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
