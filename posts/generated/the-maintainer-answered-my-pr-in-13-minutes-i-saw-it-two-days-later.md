---
title: "The maintainer answered my PR in 13 minutes. I saw it two days later."
slug: "the-maintainer-answered-my-pr-in-13-minutes-i-saw-it-two-days-later"
author: "Zhuojun Li"
source: "devto_ai"
published: "Sat, 21 Nov 2026 06:18:12 +0000"
description: "lot-map 0.13.0 came out on Nov 21 with an option I asked for. commandStations puts a shell command on a station of your choice. I set agent-dispatch=agents ,..."
keywords: "command, agents, nov, map, you, two, lot, station"
generated: "2026-11-21T06:33:10.797534"
---

# The maintainer answered my PR in 13 minutes. I saw it two days later.

## Overview

lot-map 0.13.0 came out on Nov 21 with an option I asked for. commandStations puts a shell command on a station of your choice. I set agent-dispatch=agents , so when a Claude Code session hands an order to another model, the map lights Agents instead of Shell. The previous post was about the half lot-map will never show: the queue outside the session. This is the half it can. The timeline All times UTC. Nov 18: I opened issue #103 . The maintainer said yes the same day and told me where the command had to be found: behind sudo , env , bash -c and docker exec , not only as the first word of the line. Nov 19, 01:29: PR #111 . Nov 19, 01:42: his review. One change, then he would merge. Nov 21, 03:58: my reply. Nov 21, 04:13: merged. 04:32: released. The 50 hours in the middle are mine. I missed the notification. In those two days five other PRs changed the same lines of classify.ts , so I had to rebase before I could answer. What he asked for My version said a command you place stays where you put it. That put agent-dispatch status && curl https://example.com/x on Agents, and the curl went unseen. His rule has two parts. A placed command keeps its station whatever its own name says, so gh=agents stays on Agents. Another command on the same line that reaches the network takes the whole line to Network. In his words, "a curl should not hide behind its neighbour." He was right. Network is the station you watch to see whether something left the machine. I had asked for a convenience and nearly traded that away. The change was two commits and four new tests, 202 passing where next had 198. If you run lot-map, update anyway 0.13.0 also fixes a label that could show a secret. A PowerShell line like $token = "ghp_…" with no description was labelled with the value. The release notes list it first. To use the new option: /plugin configure lot-map , then commandStations , then one entry per command, written command=station . The stations are files, shell, web, browser, agents, skills and you. I ran nine of my real command lines through the 0.13.0 classifier. The six that call the dispatcher land on Agents, and the one chained to curl lands on Network. After a restart of VS Code, Agents lit up in a session that was preparing work orders. I have not yet watched it through a day of orders. Zhuojun Li

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/lizhuojunx86/the-maintainer-answered-my-pr-in-13-minutes-i-saw-it-two-days-later-281i

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
