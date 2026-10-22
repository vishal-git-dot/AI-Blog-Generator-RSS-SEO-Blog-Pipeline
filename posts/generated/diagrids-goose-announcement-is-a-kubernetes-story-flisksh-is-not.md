---
title: "Diagrid's Goose Announcement Is a Kubernetes Story. flisk.sh Is Not."
slug: "diagrids-goose-announcement-is-a-kubernetes-story-flisksh-is-not"
author: "flisk"
source: "devto_ai"
published: "Thu, 22 Oct 2026 21:19:38 +0000"
description: "Diagrid announced a Catalyst integration for Goose on 22 October 2026. A Goose recipe can commit each step before the next one starts: every LLM call, extens..."
keywords: "flisk, you, goose, not, catalyst, recipe, diagrid, run"
generated: "2026-10-22T21:22:57.095421"
---

# Diagrid's Goose Announcement Is a Kubernetes Story. flisk.sh Is Not.

## Overview

Diagrid announced a Catalyst integration for Goose on 22 October 2026. A Goose recipe can commit each step before the next one starts: every LLM call, extension tool call, and sub-recipe. If the process or the node dies, the run resumes at the last committed step instead of replaying completed calls. Catalyst plugs in through Goose's existing extension mechanism. Goose itself does not have to be forked. The same release adds LangChainGo and Mastra. Diagrid says this brings the integration count past 15, across Python, TypeScript, Java, and C#. That is a real announcement. It is also the wrong layer to bolt onto flisk up . Two failure domains Goose + Catalyst flisk.sh What dies A long agent run: minutes, hours, days A local container while you edit code What resumes The recipe, at the last committed step Tilt live-update, or a container restart Where it runs Kubernetes, any cluster Catalyst supports, via Dapr Your laptop. Docker + Tilt. No local cluster What you pay twice if you get this wrong Tokens for repeated LLM calls Nothing. You just rebuild an image What you must not do Treat flisk up as the durability log Put Catalyst inside the generated Dockerfile Yaron Schneider's line in the release is the useful one: Go and TypeScript agents on Kubernetes hit the same failure every long-running process hits. Something breaks, and the work starts over. Flisk's daily loop is the opposite problem. You want the API to restart when you save a file. You do not want a migration, a billing call, or a Goose recipe to restart because Tilt synced a directory. Flisk's own contract is narrow. service.json is the file you own. flisk up <stack> generates Dockerfiles, Traefik routes, and a Tiltfile, then starts that stack. flisk up shop --dry-run prints URLs and starts nothing. Dev ports bind to 127.0.0.1 unless you set TDK_BIND_ADDRESS . Production stays on Helm or whatever you already ship. A warm start of 14 tiny services was reported at 4.6 seconds on a 16 GB M1 after images existed. That number is a laptop boot, not a crash-recovery guarantee. Where people will wire this badly The bad design is one container that is the API, the Goose process, and the migrator. Tilt restarts the container because you changed a handler. Goose starts the recipe again from step 0, because nothing committed the steps. The API's entrypoint runs goose up again because someone thought the database migrator and the AI agent were the same word. GET /health goes green while step 4 of the recipe runs twice. Split them. Process Owner Restart orders-api flisk resource orders-api --type backend --language go Yes, with Tilt Postgres Flisk's local database for that stack With the stack, data in a volume Schema job pressly/goose, one-shot, exits Never, except when you run the job Agent Goose CLI or desktop, on the host or in its own service Catalyst only if this run must survive a node death The agent may call flisk doctor , flisk up shop --dry-run , and curl the health URL Flisk prints. It should not be the process inside the API image. Catalyst's promise is "do not pay for the same tokens twice." That promise is void if Flisk's file watcher kills the process between commits, and it is void if you never turned Catalyst on and assumed Flisk would remember the step. What the release does not give you I am not pasting a Catalyst install. Diagrid says the integration is available through Catalyst, with a write-up at diagrid.io/solutions and docs at docs.diagrid.io . Read those before you add an extension. The release does not say Flisk knows about Catalyst, and Flisk's docs do not list it. Also unchanged today: Goose's repo is still aaif-goose/goose , not a Diagrid repo. Diagrid is an AAIF member. It did not take the project. No Flisk flag starts a durable recipe. LangChainGo support is not flisk resource --language go . The Go provider is a net/http service scaffold. LangChainGo is a library you would put in a service you already own. A boundary that survives both announcements Use Flisk when the question is "how does this service start on my machine." Use Goose when the question is "which commands is an agent allowed to run." Use Catalyst only when the question is "this recipe must survive a dead node, and I am already on Kubernetes." If the recipe's only job is flisk doctor and a health check, you do not need durable execution. You need a short recipe and a human reading the diff. Durable execution is for the run you cannot afford to replay. A laptop Tilt sync is not that run. Source: Diagrid, 22 October 2026 . Flisk behavior: flisk.sh and the 22 October walkthrough flisk.sh is one service.json, then the laptop starts .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/flisk/diagrids-goose-announcement-is-a-kubernetes-story-flisksh-is-not-1pl6

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
