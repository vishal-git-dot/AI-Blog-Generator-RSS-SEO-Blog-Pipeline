---
title: "Why I'm Building ShrekOS When Containers Already Exist"
slug: "why-im-building-shrekos-when-containers-already-exist"
author: "Leon Odor"
source: "devto_ai"
published: "Wed, 02 Sep 2026 16:16:13 +0000"
description: "An AI agent should not have to be trusted with the whole machine in order to be useful on the machine. That trust decision keeps getting dumped on the model ..."
keywords: "not, agent, machine, model, operating, what, did, have"
generated: "2026-09-02T16:20:36.993698"
---

# Why I'm Building ShrekOS When Containers Already Exist

## Overview

An AI agent should not have to be trusted with the whole machine in order to be useful on the machine. That trust decision keeps getting dumped on the model or the agent framework. It belongs lower down, in the operating system. I wanted agents to do mundane, genuinely useful computer work. Install ffmpeg. Compile something. Poke at a project. Launch a tool. Hit a network resource. The surprise was that getting an LLM to emit the right shell commands was the easy part. The hard part was deciding what authority those commands should carry. Every time I made an agent more useful, I drifted toward one of two bad places. Either I locked the environment down so hard that ordinary tasks became awkward and I spent all day widening permissions by hand, or I kept handing the agent more of the real machine until a single hallucination, a poisoned dependency, a prompt injection, or a plain bug could do real damage. Restrict until useless, or trust until dangerous. I kept ping-ponging between them. This is not about theoretical edge cases. This is about the daily grind of trying to make software that helps you actually get things done. I am not claiming there are only two sandboxes in the world. Sophisticated sandboxes exist. Containers exist. This is about MY operating model, the way the authority question kept landing back on the agent's judgment instead of on something underneath it. Containers, namespaces, cgroups, egress filtering, package managers, mandatory access control, immutable filesystems, signed boot. Each already solves a PIECE of this. None of them, by itself, gave me a coherent operating model for a workload that decides at runtime which capabilities it needs and then asks the machine for them. That gap is the whole project. I did not write a kernel. I did not invent containers. I did not invent sandboxing. If this project required me to invent any of those, something would have gone badly wrong. The work is composition, not invention. ShrekOS is not a from-scratch operating system. It is an attempt to stitch existing mechanisms into a coherent operating model for a workload that asks for capabilities as it goes. The clearest way to explain what I mean is the example that made the whole problem concrete for me. ffmpeg. Walk through what "the agent needs ffmpeg" actually implies if you do it the naive way. I have an agent that needs to transcode a video file. It sees the tool missing. It decides to install it. It runs apt install ffmpeg on the host. This permanent mutation of my machine touches the package database. It pulls dependencies I did not audit. It runs install scripts as part of a normal operation. It creates symlinks. It writes configuration files in places I did not expect. It assumes root privileges to write to system directories. Multiply that by every tool an agent decides it needs, over months, and the host becomes an unpredictable pile of state that some program I do not fully control has been editing. That is the moment the discomfort became concrete for me. The problem was never ffmpeg. It was that installing it meant giving an unpredictable program authority over my actual machine. I started building on an immutable Linux base so the host could not be casually mutated. I leaned Fedora at first, because its sealed verified boot story was landing upstream and looked like a free win. Then I un-chose it the same afternoon. The base turns out to be maybe fifteen percent of this project. The interesting part is base independent, the immutable image based update model I wanted is not Fedora specific, and I am simply faster in Debian on a build I will live in for years. So the base is Debian, sealed and immutable, with atomic updates I can roll back if one goes bad. AppArmor gives me a path based model with policy in plain readable files, which suits the kind of deterministic wall I want. Fedora survives only as a reference image I study in a VM and as a cheap escape hatch through the build tooling. The point of telling you this: I will reverse a "hard security win" the moment I realize it is not load bearing. That reflex is the whole methodology. I am not married to a distribution. I am married to the principle that the base layer should be stable and auditable. The agent is a client. Whether it is a cloud model, a local one, or something I swap next month does not change the security story, because the security is not supposed to live inside the agent. If it did, I would be trusting the least trustworthy component to police itself. The agent cannot be the thing that decides the limits of its own authority. That is the whole principle. It can be trusted to make a request. The operating system decides whether to grant it, and under what constraints. The useful version of this is not the agent promising to use curl responsibly. It is the agent asking for what it needs and the machine deciding what that request is actually allowed to touch. This is not about preventing the agent from working. It is about ensuring that when the agent works, it does so within a boundary that I defined before it started. The boundary is not a suggestion. It is a hard limit. Before I could have anything worth calling an operating system for agents, I needed something much smaller and more concrete. A place where an agent could be temporarily powerful without that power automatically becoming authority over my machine. That is where the next post starts. But first I have to answer the question sitting underneath all of it. What should an agent be allowed to change?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/the_leon_odor/why-im-building-shrekos-when-containers-already-exist-1lg6

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
