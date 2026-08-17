---
title: "I Let an AI Agent Run My Bug Bounty Recon Overnight — Here's the Setup That Actually Works"
slug: "i-let-an-ai-agent-run-my-bug-bounty-recon-overnight-heres-the-setup-that-actually-works"
author: "ULNIT"
source: "devto_python"
published: "Mon, 17 Aug 2026 01:02:48 +0000"
description: "I Let an AI Agent Run My Bug Bounty Recon Overnight — Here's the Setup That Actually Works Last month I was spending my evenings doing the most boring part o..."
keywords: "agent, diff, recon, bug, out, run, bounty, collectors"
generated: "2026-08-17T01:39:21.437276"
---

# I Let an AI Agent Run My Bug Bounty Recon Overnight — Here's the Setup That Actually Works

## Overview

I Let an AI Agent Run My Bug Bounty Recon Overnight — Here's the Setup That Actually Works Last month I was spending my evenings doing the most boring part of bug bounty hunting by hand: running subfinder, httpx, and nuclei against targets, copy-pasting results between terminal windows, and babysitting a laptop that needed to stay awake. The actual interesting part — reading responses, spotting weird endpoints, testing hypotheses — kept getting pushed to "tomorrow." So I automated the boring part. All of it. The agent I ended up with runs on a Raspberry Pi, costs less than a coffee to operate, and hands me a triaged report every morning. Here's how it works. The Core Idea Most automation tutorials stop at "here's a bash script with a cron job." That's fine for fixed pipelines, but bug bounty targets move: new subdomains appear, services change ports, an endpoint that returned 404 yesterday starts returning 200 today. A static script can't decide that a newly-exposed debug panel on a staging subdomain is worth escalating and a CDN edge is not. An agent can. The architecture is three layers: Collectors — dumb, reliable scripts that gather raw data (subdomains, live hosts, ports, response hashes). Diff engine — compares today's snapshot against yesterday's. Everything unchanged gets discarded. Agent layer — an LLM agent that only ever sees the diff , classifies each change, and decides what deserves deeper probing. The agent never touches the full dataset. That's the trick that keeps API costs sane and keeps the agent focused. The Pipeline in Practice # collectors run at 02:00, diff at 04:00, agent at 05:00 0 2 * * * /opt/recon/collect.sh >> /var/log/recon/collect.log 2>&1 0 4 * * * python3 /opt/recon/diff.py --state /data/state.json 0 5 * * * python3 /opt/recon/agent_triage.py --input /data/todays_diff.json The collectors are the usual suspects: import subprocess , json def collect_subdomains ( target ): out = subprocess . run ([ " subfinder " , " -d " , target , " -silent " ], capture_output = True , text = True ) return set ( out . stdout . splitlines ()) def probe_live ( subdomains ): out = subprocess . run ([ " httpx " , " -silent " , " -status-code " , " -title " ], input = " \n " . join ( subdomains ), capture_output = True , text = True ) return out . stdout . splitlines () The diff engine writes out JSON with three buckets: new_assets , changed_responses , and gone_assets . Gone assets are underrated — a subdomain suddenly disappearing often means it's about to become dangling and takeable over. The agent then gets a prompt roughly like: "Here are 14 changes since yesterday. For each, output a JSON verdict: IGNORE, WATCH, or INVESTIGATE, plus a one-line reason. You have access to a tool that fetches a URL and returns headers + first 500 bytes." It's shocking how well this works. It correctly flagged a /graphql endpoint that appeared on a marketing subdomain as INVESTIGATE and waved through forty "server header changed" noise items as IGNORE. That triage pass used to take me an hour of scrolling. Why a Raspberry Pi? This whole stack idles at a few hundred megabytes of RAM. A Pi 4 or 5 runs the collectors, the state database, and the agent orchestrator without breaking a sweat, draws a few watts, and never needs to be "on" as a separate decision — it's just always there. I've got mine headless on my desk doing recon every night while I sleep. The only thing that isn't local is the LLM call for triage, and because it only sees the diff, a typical night costs pennies in tokens. The one operational lesson: keep your state in a real database (I use SQLite), not flat files. The night a collector crashed mid-write, flat-file state silently corrupted and the diff engine reported 2,000 "new" subdomains. SQLite transactions made that class of bug impossible. The Part That Took Me Too Long to Figure Out Rate-limit yourself before the target does. Run httpx with -rl 10 , spread collectors across the night, and never parallelize nuclei templates that send writes. The goal is to look like the most polite scanner that ever existed. Bonus: slower, spaced-out requests catch flaky endpoints that fast bursts miss. If You Don't Want to Build It From Scratch Honestly, building this from scratch was a weekend of plumbing, not hacking. The interesting work was designing the agent's verdict schema and testing it against real diffs. If you'd rather skip the plumbing, the Bug Bounty Automation Kit packages up exactly this pattern — collectors, diffing, and agent triage wired together for $15, which is less than one hour of my time used to cost me. It's what I started from before customizing it, and it drops straight onto a Pi. If your targets are more general automation than bug bounty, the AI Agent Toolkit ($9) covers the same agent-loop fundamentals for broader use cases. More resources in the agent store . Start Tonight Get subfinder, httpx, and nuclei running against one target, manually. Add the diff layer — even a JSON file in git works at first. Put an LLM call in front of the diff and iterate on the verdict prompt until it stops hallucinating interest in CDN noise. Then sleep in. The morning report will be waiting. What's the most boring part of your recon that you haven't automated yet? That's your next project.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ulnit/i-let-an-ai-agent-run-my-bug-bounty-recon-overnight-heres-the-setup-that-actually-works-2lm4

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
