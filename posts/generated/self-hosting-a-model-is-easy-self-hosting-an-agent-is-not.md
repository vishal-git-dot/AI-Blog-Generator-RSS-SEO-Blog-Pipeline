---
title: "Self-Hosting A Model Is Easy, Self-Hosting An Agent Is Not"
slug: "self-hosting-a-model-is-easy-self-hosting-an-agent-is-not"
author: "Paul Crinigan"
source: "devto_ai"
published: "Wed, 26 Aug 2026 01:26:10 +0000"
description: "Running a model on your own hardware is a solved problem. Ollama, LM Studio, llama.cpp, pick one and you have weights answering on localhost in an afternoon...."
keywords: "you, agent, one, your, model, tool, agents, not"
generated: "2026-08-26T01:41:06.770448"
---

# Self-Hosting A Model Is Easy, Self-Hosting An Agent Is Not

## Overview

Running a model on your own hardware is a solved problem. Ollama, LM Studio, llama.cpp, pick one and you have weights answering on localhost in an afternoon. Running an agent on your own hardware is a different job, and the gap between those two is where most self-hosting attempts stall. What The Model Alone Does Not Give You An agent is a loop, not a completion. It needs somewhere to keep what it learned three turns ago, somewhere to queue work it cannot finish now, a tool layer that can actually reach a filesystem or an API, and something watching the whole thing so one bad tool call does not take the process down. In practice that means a vector store, a queue, a database, a tool server and a web UI, on top of the model you already have running. Five moving parts, five sets of version constraints, and five places a request can vanish. You can absolutely wire that yourself. Most people who start do not finish. One Image Instead Of Five Services Auto Learning Agents takes the opposite bet: put all of it in one container and let the install be boring. git clone https://github.com/AIAppsAPI/auto-learning-agents cd auto-learning-agents cp .env.example .env docker compose up The image carries the Elixir runtime, the Python services, the bundled local database and the tool layer. First run prepares the database and brings up the supervision tree of agent nodes, and the dashboard is on localhost. Docker is the only thing you need installed on the host, which is the whole point. The setup requirements and configuration steps are short enough to read before you start. Where Crash Recovery Actually Belongs Here is the part that changed my mind about the stack choice. Agents fail constantly and unremarkably. A tool call times out, a model returns JSON with a trailing comma, a subagent loops on a task it cannot complete. The question that matters is what happens to the other twelve agents when one of them dies. If your runtime is a Python process pool, that answer lives in your application code: a watchdog, a retry decorator, some state you hope was checkpointed. You wrote it, so you maintain it, and it is wrong in ways you find out about at 3am. Elixir answers it at the runtime level. Every agent node is a supervised process. A crash restarts that node from a known state and the rest of the tree carries on without noticing. This is thirty year old BEAM behaviour applied to a new workload, and it is a much better fit for long running agents than anything you would build by hand. Mixing Providers, Or Skipping Them Entirely Keys go in .env . Claude, OpenAI and Gemini can all live in the same install, so you can route a cheap classification agent to one model and a planning agent to another without running two deployments. Or you skip the keys entirely and point it at Ollama. That is the configuration worth trying first if you are still deciding, because the whole loop including inference runs on your machine. Nothing is billed, nothing leaves the box, and you find out whether the platform is useful before you have spent anything on finding out. The Part Worth Checking Storage and search run on the one bundled database. No cloud account, no external service to keep alive, no hosted dependency quietly sitting in the middle of your "local" setup. Conversation history, embeddings, tool results and keys stay on your disk. That last bit is the actual argument for self-hosting an agent platform, and it is worth verifying before you commit a weekend to any of them, this one included.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/paulcrinigan/self-hosting-a-model-is-easy-self-hosting-an-agent-is-not-3ecp

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
