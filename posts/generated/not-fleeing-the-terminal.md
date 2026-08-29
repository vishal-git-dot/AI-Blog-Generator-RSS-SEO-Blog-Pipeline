---
title: "Not Fleeing the Terminal"
slug: "not-fleeing-the-terminal"
author: "Eric Marchand"
source: "devto_ai"
published: "Sat, 29 Aug 2026 20:31:24 +0000"
description: "There's a YouTube video making the case that it's time to leave the terminal behind. I'm not here to argue with it — I'm doing the opposite. The more AI I us..."
keywords: "terminal, agent, one, which, more, agents, code, what"
generated: "2026-08-29T20:45:19.190262"
---

# Not Fleeing the Terminal

## Overview

There's a YouTube video making the case that it's time to leave the terminal behind. I'm not here to argue with it — I'm doing the opposite. The more AI I use for development, the deeper I sink into the terminal, not out of it. That wasn't the plan. Editors learned to talk back For a while, the pull went the other direction. VS Code and the other IDEs started wiring chat and agents straight into the editor: an agent view, a tidy UI around the conversation, the diff, the status, the whole thing. It made sense — why leave the editor at all if it can show you everything? Then the providers built their own apps Then the model providers did the same thing to themselves. Claude has its own app now. Codex has its own app. Both give you a native, dedicated place to talk to an agent. Peel back the interface, though, and it's often the same engine you'd get from the terminal — Claude Code, Codex, running underneath a nicer coat of paint. Terminal, but still inside the IDE The more I used these agents, the more I found myself preferring a plain terminal for the actual work — at first, just the terminal panel inside VS Code. Convenient, close to the files, one window. Fine, right up until I wanted more than one agent running. Then it turned into a scroll-and-guess exercise: which tab is building, which one's waiting on me, which one finished ten minutes ago without telling anyone. I could lean on the VS Code agent view, or Claude's own app with its code view — both are genuinely good at telling you what an agent is doing, what project it's attached to, whether it's done. But then I wanted a local model, a different coding agent, some one-off tool that doesn't fit inside any of those apps. So more and more of the work moved to a terminal, plain and unopinionated. Too many terminals Then I had too many terminals. A handful of windows turns into a mess fast — no shared sense of which one is doing what, which agent wrapped up, where I left something running three hours ago. The standard fix is a multiplexer, so I started using one. tmux gives me a single place for sessions, panes, projects, agents — one problem solved. But it also throws away most of what I liked about the native apps. The terminal knows Claude is running in that pane; it has no opinion on whether it's done , or which of a dozen panes actually needs me. I'm back to checking each pane by hand, remembering which one belongs to which project. Debugging the UI and DAP for agents were both about the same gap from the other side: giving a program a real view into what's actually running instead of trusting whatever's on screen. I needed that same view for myself. Everyone seems to be building this Turns out this is a fairly popular itch. There's a small wave of projects trying to build a better terminal-native interface for managing coding agents: Herd, Herdr, Muxy — different takes on the same missing layer, and a lot of people apparently arriving at "I should just build my own" independently, myself included. Herdr's pitch is basically this: real panes, same as tmux, but with a sidebar that actually tracks which agent is idle, working, blocked, or done — Claude, Codex, whatever CLI you pointed at that pane. I got as far as sketching what mine would look like. Then I tried Muxy instead. Muxy, for now It's been working well. Still entirely terminal-first — I can run whatever agent or model I want, nothing's locked to one provider — but it gives me a real way to organize projects, terminals, worktrees, and agents without asking me to give up the terminal to get it. There's a short list of things I wasn't willing to give up chasing this, though: a real diff view, clicking through files with a mouse instead of cd and ls , seeing my open issues and the CI status without switching to a browser tab. That's the part of the IDE you don't notice until it's gone. Turns out that's exactly what Muxy's plugins are for. They bolt on the IDE-shaped pieces — diffs, a file explorer, issues, CI — without dragging the rest of the editor in behind them. And when a plugin for something is missing, I just build it. Where this might be going I wouldn't be surprised if IDEs keep drifting this direction too. VS Code now runs agent sessions in a dedicated process, the Agent Host Protocol, so Copilot, Claude, and Codex can sit side by side instead of each hogging its own window. Zed seems to be leaning further into treating the terminal and external agents as first-class citizens rather than guests. Maybe the end state isn't "put the agent inside the IDE" at all. Maybe it's building a genuinely good interface around agents, one that doesn't care where they run or which editor — or terminal — happens to be open. For now, though, the pattern's simple enough: more and more often, when I want to start something, I open a terminal. Not VS Code.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/phimage/not-fleeing-the-terminal-g5a

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
