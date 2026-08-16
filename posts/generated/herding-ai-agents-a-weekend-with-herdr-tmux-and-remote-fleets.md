---
title: "Herding AI Agents: A Weekend with Herdr, Tmux, and Remote Fleets"
slug: "herding-ai-agents-a-weekend-with-herdr-tmux-and-remote-fleets"
author: "Onur Cinar"
source: "devto_ai"
published: "Sun, 16 Aug 2026 18:33:50 +0000"
description: "I like making life harder for myself most of the time (check out Pushing the Limits: Turning a 4GB Lenovo Duet Chromebook into My Primary Development Machine..."
keywords: "you, agents, herdr, can, agent, your, running, like"
generated: "2026-08-16T18:35:30.117339"
---

# Herding AI Agents: A Weekend with Herdr, Tmux, and Remote Fleets

## Overview

I like making life harder for myself most of the time (check out Pushing the Limits: Turning a 4GB Lenovo Duet Chromebook into My Primary Development Machine ). As AI agents have gotten better, to the point where you can actually delegate work and let them run without steering every few minutes, you start getting bored. Then you start tackling multiple things at once, which means multiple agents running around in parallel doing different tasks. After all, compute is cheap and agent labor is even cheaper, so you can tackle projects you'd normally avoid as an engineer: converting a legacy codebase from Go to Rust, rewriting Vue into React, and so on. These are massive refactoring jobs you'd typically only undertake with a very compelling reason (like Microsoft porting TypeScript to Go ), but with AI agents doing the heavy lifting, why not? Running multiple agents is easy on paper: open up a bunch of terminal windows, fire them up, and you're good to go. The challenge begins when you step away from your desk and wonder what they're up to. Sure, you could pay extra for hosted cloud platforms or mobile clients from AI providers, but that's expensive and too easy. Per paragraph one, I like making life harder for myself, so I'm not paying for that anyway. Naturally, the self-hosted solution is running them inside a terminal multiplexer like tmux or Zellij . My muscle memory is hardwired to tmux, and I navigate panes without thinking. Zellij is great too (especially with its web support), and I've tried switching a few times. My typical workflow is running these agents on a machine at home. When I'm out, I use Tailscale to dial back into my home network, SSH in, and attach to the running sessions. It works, but the trouble with tmux is that it isn't agent-aware. You have to constantly cycle through windows and panes just to check if an agent is still working, crashed, or waiting for confirmation. This weekend, I gave Herdr a spin, a terminal multiplexer built specifically for running AI coding agents. Herdr organizes your screen cleanly from the get-go. You have workspaces to switch between different projects, and underneath, a live overview of all your running AI agents and their current state (working, idle, blocked, or done). From there, you can jump straight into specific tabs and panes to interact with whichever agent needs input. Herdr is clever enough to detect what agents are doing out of the box, but it also provides direct integrations (via a local socket API) so agents can report their status directly instead of the multiplexer having to guess. On the road: Remote client mode Just like tmux, Herdr runs as a persistent server daemon in the background, so you can keep everything running on your home rig and reconnect on the go. One neat capability here is its native remote client mode. Instead of just doing a raw SSH session and attaching to a remote terminal, you can run herdr --remote user@host . If you're on a laptop away from home, your local Herdr installation acts as a thin client talking directly to the remote Herdr server over SSH. Stopping the compulsive status-checking The biggest win for this kind of mobile workflow is that you don't have to keep checking your phone like a nervous parent. Because Herdr actually understands agent states (knowing when an agent transitions from working to blocked or done ), you can take advantage of notification plugins or webhooks (like Telegram alerts). When an agent hits a prompt and sits there waiting for your [y/N] confirmation, you get pinged. You jump in via Tailscale, unblock it, and get back to your life. What's next: Letting agents drive the multiplexer? I've also heard, though I haven't ventured into this rabbit hole yet, that the Unix socket API goes both ways. In theory, agents can actually drive Herdr themselves: programmatically opening new panes, spinning up sub-agents for subtasks, and managing their own workspaces. A fleet of autonomous agents dynamically reconfiguring their own terminal environment sounds both wildly futuristic and slightly terrifying for my CPU fans, but it's on my radar to try. Final thoughts While it's fundamentally still a multiplexer with some new keybindings to get used to (though you can customize them in herdr.toml ), it feels significantly better suited for multi-agent workflows. Instead of manually polling terminal panes to see who needs help, having that top-level agent awareness built into your multiplexer makes managing a fleet of agents feel manageable without having to hack together custom status scripts.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/onurcinar/herding-ai-agents-a-weekend-with-herdr-tmux-and-remote-fleets-4cb8

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
