---
title: "How I Built an AI Watchdog Agent That Keeps My Raspberry Pi Fleet Alive"
slug: "how-i-built-an-ai-watchdog-agent-that-keeps-my-raspberry-pi-fleet-alive"
author: "ULNIT"
source: "devto_python"
published: "Sun, 23 Aug 2026 01:03:09 +0000"
description: "A few months ago one of my Raspberry Pis went down at 2am. I didn't notice for two days. That's embarrassing for someone who runs half a dozen boards as a li..."
keywords: "one, board, agent, fleet, runs, telegram, when, json"
generated: "2026-08-23T01:43:25.005308"
---

# How I Built an AI Watchdog Agent That Keeps My Raspberry Pi Fleet Alive

## Overview

A few months ago one of my Raspberry Pis went down at 2am. I didn't notice for two days. That's embarrassing for someone who runs half a dozen boards as a little home lab, and it's exactly the kind of thing an agent should catch. So I built one. This is the story of how I built a watchdog agent that pings every device in my fleet, watches disk space, temperature and memory, and messages me on Telegram when something looks off — before it becomes a dead board. Everything runs on the AI Agent Toolkit ($9 on LemonSqueezy) , because I wanted plain Python I could read and own rather than a hosted monitoring subscription. The problem I kept ignoring I have six Raspberry Pis doing different jobs: one runs the agent toolkit itself, one is a DNS sinkhole, one is a backup target, one scrapes data, one is a media box, and one is a spare test board. I'd check on them when I remembered, which meant I found failures days late. The sinkhole died once and my whole network lost ad filtering — I only noticed because ads started showing up. I needed something that checks constantly, understands what "normal" looks like for each board, and only bothers me when it matters. A cron job can ping; an agent can reason. Design: checks, thresholds, and a brain I split it into three layers. Collect. Every 10 minutes a small script SSHes into each board (or hits a tiny local endpoint) and pulls uptime, load, temperature, disk usage, and free memory. It's deliberately dumb — just gather and write JSON. Analyze. This is the agent part. Instead of hardcoding "alert if disk > 90%", I give the LLM the last several readings plus the current one and ask it to flag anything trending wrong. It catches things fixed thresholds miss — like a temperature that's climbing 2°C an hour even though it's still under the limit. Notify. When something's flagged, it fans out to Telegram with the board name, the metric, the trend, and a suggested fix. If Telegram is down it falls back to writing a report file, so an alert never silently disappears. The config that runs it all The whole thing is one YAML task the toolkit schedules: # tasks/pi_watchdog.yaml name : pi_watchdog trigger : { type : cron , at : " */10 * * * *" } steps : - { type : shell , cmd : " python collect_fleet.py" } - { type : llm , model : " anthropic/claude-3-5-sonnet" , prompt : " fleet_check.md" } - { type : notify , channel : telegram } The fleet_check.md prompt is where the logic lives. It tells the model the healthy baselines for each board and asks it to return structured JSON: which boards are fine, which need attention, and why. Here's the gist: You are a fleet health monitor. For each board compare the current readings against the last 12 samples. Flag: temps rising steadily, disk filling faster than usual, load spikes, or a board that stopped reporting. Return JSON: {"alerts": [{"board":..., "issue":..., "severity":..., "fix":...}]}. Only alert on real problems. Silence is better than noise. That last line matters. My first version alerted on everything and I muted it within a day. Tuning it to stay quiet unless it's genuine took longer than writing the code. The code that collects The collector is a short async loop. One snippet so you can see there's no magic: import asyncio , json , paramiko async def read_board ( host : str ) -> dict : out = await run_ssh ( host , " uptime; vcgencmd measure_temp; df -h / | tail -1; free -m | grep Mem " ) return { " host " : host , " raw " : out , " ts " : now ()} async def main (): boards = [ b [ " host " ] for b in load_config ( " fleet.yaml " )] results = await asyncio . gather ( * ( read_board ( h ) for h in boards )) save_state ( " fleet " , results ) State is just JSON in a folder, so the whole history is git -diffable. I can see exactly when a board started heating up by reading the log. What actually happened Two weeks in it caught a microSD card that was filling up with runaway logs — flagged the growth rate a full day before it would have hit 100%. It also noticed the media box's temperature climbing after I moved it next to a radiator, which I'd have never attributed correctly on my own. And the one time a board genuinely died, I got a Telegram ping within ten minutes instead of two days. What I'd tell someone rebuilding this Separate collection from judgment. Keep the data-gathering dumb and put the reasoning in the prompt. It makes both parts easy to change. Default to silence. An alert system that cries wolf gets disabled. Require a real reason before notifying. Own the code. The reason this has survived is that it's ~600 lines of Python I fully understand. If something breaks I fix it in an editor, not a support ticket. If you want the base to build from, the AI Agent Toolkit on LemonSqueezy ships the runner, the LLM adapter, the memory layer, and the notification fan-out this watchdog uses — plus a dozen other task templates. The full catalog is in the agent store repo . It's $9 once, runs on a $35 board, and every line is yours to read and change. That's exactly how I wanted it.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ulnit/how-i-built-an-ai-watchdog-agent-that-keeps-my-raspberry-pi-fleet-alive-2nn0

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
