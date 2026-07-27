---
title: "Show HN: Port Zero – how I learned to stop worrying and love PORT=0"
slug: "show-hn-port-zero-how-i-learned-to-stop-worrying-and-love-port0"
author: "octopoc"
source: "hackernews"
published: "Mon, 27 Jul 2026 00:03:48 +0000"
description: "Hi HN, Recently I wasted several hours wrangling my dev environment only to find out that the browser frontend was talking to the wrong version of the backen..."
keywords: "port, you, portzero, virtual, your, https, process, local"
generated: "2026-07-27T03:38:46.275080"
---

# Show HN: Port Zero – how I learned to stop worrying and love PORT=0

## Overview

Hi HN, Recently I wasted several hours wrangling my dev environment only to find out that the browser frontend was talking to the wrong version of the backend. This got me thinking--why on earth are we still using simple numbers to describe which process to connect to? Why not use names instead? I thought of all the times a program wouldn't start because of port conflicts. The more I thought about it, the crazier it seemed. Modern operating systems already offer no-conflict ports: if you make your TCP server listen on port 0, the OS assigns you a random available port. But that only solves half the problem. I built the other half: PortZero. It's a GPLv3 program that watches for processes (and docker containers!) with a special PZ_TUNNEL environment variable: PZ_TUNNEL=myapp-{branch}.portzero.local:80 npm run dev When it sees such a process or container, PortZero does this: 1. Create a virtual NIC (if it hasn't already) 2. Create a new virtual IP address 3. Create a DNS record that substitutes things like {branch} based on the working directory of the process, and points at that virtual IP address 4. Start listening on that virtual IP address on the port of your choice (e.g. port 80 for http, port 443 for https, port 5432 for postgresql) 5. Forward any TCP connections to that virtual IP address / virtual port to the random, OS-assigned port that your process or container is actually listening on The result is you don't have to think about ports anymore, you just have to think about subdomains. You can have multiple services available on port 80 without conflicts, as long as they have different portzero.local subdomains. It does some other cool stuff like: - Enable HTTPS on local HTTP services by creating a local CA and registering it on your machine - Enable cloud tunnels so you can access your apps on other devices (paid feature) Links: https://portzero.net/docs/ https://github.com/PortZeroNetwork/portzero Comments URL: https://news.ycombinator.com/item?id=49063648 Points: 12 # Comments: 4

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://portzero.net/

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
