---
title: "Exit code 3 means it's the agent's turn: an agent-first CLI for sports film review"
slug: "exit-code-3-means-its-the-agents-turn-an-agent-first-cli-for-sports-film-review"
author: "Marius"
source: "devto_python"
published: "Fri, 23 Oct 2026 11:15:19 +0000"
description: "Disclosure: this post was drafted by my coding agent (Claude Code) and posted with my permission; the project itself was built with Claude Code. Every comman..."
keywords: "agent, video, sports, review, coach, run, code, what"
generated: "2026-10-23T11:19:44.657402"
---

# Exit code 3 means it's the agent's turn: an agent-first CLI for sports film review

## Overview

Disclosure: this post was drafted by my coding agent (Claude Code) and posted with my permission; the project itself was built with Claude Code. Every command and message below is copied from the tool. The problem I play in an adult rec basketball league. There is no coach watching film with us, only hours of phone video. A coding agent like Claude Code can already look at images and write. What it lacks is the boring part: cutting clips, rendering a page a teammate opens on a phone, narrating it, making a video with freeze frames. So I built sports-video-coach (MIT): you give your agent a video of your own game or workout, the agent reviews it, and the CLI turns the review into a coaching page (clips, narration audio) and an explained video (freeze frames, rings, subtitles). The CLI never calls a model The agent is already in the terminal. So the CLI has no API key and no prompt inside; it does what code does well (ffmpeg, rendering, bookkeeping) and stops when it needs eyes or words. That also means the same loop works in Claude Code, Codex or any agent that reads AGENTS.md . The contract: four exit codes 3 an agent step is waiting: do what the output names, then run again 1 a command failed: read the stage log it names 0 done: report the deliverable paths 2 usage error: read the message A run looks like this: $ sports-video-coach run drill.mp4 --sport tennis frames: 4 sheets (0.5 s per tile) in .../run/frames [run] waiting for the agent: review ... # exit 3 The agent opens the contact sheets, writes review.json following sports-video-coach guide review , and runs again. Validators instead of prompt tweaks Each agent step has a check. A thin review does not produce a silent bad page; the run exits 3 again with: review.json: needs a `moments` list with at least 3 entries In practice this did more for output quality than rewording guides. Agents follow file paths and exit codes better than long instructions. Resumable steps and staleness The driver is a step table. Each step is cmd or agent , with a done check, so every run is safe to repeat: it resumes at the first undone step. Command steps record what they read and the settings they used. Edit the review later and the run lists, in one message, every downstream agent step whose files no longer follow it. Fix them or keep them with --accept . Plugins, and what is still hard generic works for any sport with no computer vision: the review is the agent looking at frame sheets. basketball adds player tracking and a league box score. sports-video-coach new-plugin <name> scaffolds your own sport. 8 report languages (zh, en, ja, ko, es, fr, de, pt). Limits, honestly: the review is only as good as the agent's eyes on contact sheets; basketball tracking needs a GPU; narration uses online edge-tts. Try it See the output with no install: the demo page (a synthetic drill). Or run every deliverable locally, no agent needed (about a minute, needs ffmpeg): uv tool install git+https://github.com/mariusDing/sports-video-coach sports-video-coach demo In Claude Code: /plugin marketplace add mariusDing/sports-video-coach . Repo: https://github.com/mariusDing/sports-video-coach . Feedback from sports other than basketball is what I want most.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/mariusd/exit-code-3-means-its-the-agents-turn-an-agent-first-cli-for-sports-film-review-3pjk

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
