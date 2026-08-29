---
title: "How I test my React app on real devices without deploying it"
slug: "how-i-test-my-react-app-on-real-devices-without-deploying-it"
author: "Leo Brown"
source: "devto_webdev"
published: "Sat, 29 Aug 2026 20:37:23 +0000"
description: "How I test my React app on real devices without deploying it I recently needed to test a React app outside my own computer. Opening another browser tab wasn'..."
keywords: "react, portpreview, app, local, url, test, tunnel, development"
generated: "2026-08-29T20:45:19.187720"
---

# How I test my React app on real devices without deploying it

## Overview

How I test my React app on real devices without deploying it I recently needed to test a React app outside my own computer. Opening another browser tab wasn't enough. I wanted to use the app on my phone, try it on another device, and sometimes share the current build without deploying it first. The app was running locally: npm run dev Depending on the project, that usually gives me an address like this: http://localhost:3000 But localhost only exists on my machine. What I tried There are several ways to expose a local development server to the internet. I tried a few tunneling services and approaches, and they worked, but I wanted something simpler for this workflow. My requirements were straightforward: one command to start a tunnel; HTTPS without configuring certificates; no deployment; a URL I could open from my phone; something convenient for React and Vite development; preferably a hostname I could keep instead of receiving a new URL every time. I ended up using PortPreview . Starting a tunnel There isn't much to configure. With the React development server already running, I can expose its port from the terminal: npx portpreview 3000 My local address: http://localhost:3000 is then available through a public HTTPS URL. I can open that URL on my phone and test the app there without making a temporary deployment. Why I use it for React development Chrome DevTools responsive mode is useful, but it doesn't cover everything. Some things need a real device: touch interactions; mobile Safari and Chrome behavior; viewport quirks; authentication redirects; camera or browser APIs; network behavior; links opened from messaging apps; sharing a work-in-progress build with someone else. Instead of pushing a branch and waiting for a preview deployment, I leave the React dev server running and expose it directly: Edit React code ↓ Local dev server ↓ PortPreview tunnel ↓ Real phone / remote browser Changes from the local server appear through the tunnel immediately, so the workflow still feels like local development. Why I kept using it PortPreview lets me reserve one domain for free. That matters more than I expected because temporary URLs get annoying once you use tunnels regularly. A tunnel URL may be configured in several places: OAuth callbacks; webhook endpoints; API dashboards; test integrations; mobile devices; bookmarks; configuration files. With a reserved hostname, I don't have to update those places whenever I restart my development environment. The free plan lets me reserve one domain permanently, which covers many personal development and testing projects. It isn't limited to React I started using PortPreview for a React app, but it works with anything listening on a local port, including: React / Vite Next.js Vue Angular Node.js Express NestJS local APIs webhook handlers For example, I can expose an API running on port 3000 with: npx portpreview 3000 The API can then receive external requests without being deployed. This is particularly handy for services that need to send requests back to my machine. Tunnels and preview deployments serve different jobs I still use preview deployments when a team needs a stable environment or when the app must stay online independently of my computer. A preview deployment looks like this: code → commit → push → build → deploy → test A local tunnel is shorter: code → localhost → test For a quick test, I usually prefer the second workflow. Using a permanent subdomain After trying the random tunnel URL, I wanted a stable address for the project. PortPreview lets me reserve a subdomain and use it when starting the tunnel: npx portpreview 3000 --subdomain my-project --token pp_live_... This gives the project a predictable URL instead of a new random address each time. I can also save the token instead of passing it with every command: npx portpreview config set-token pp_live_... After that, starting a tunnel takes one command: npx portpreview 3000 My normal workflow is: Run the React app ↓ npx portpreview 3000 ↓ Open the public HTTPS URL ↓ Test on a real device When a project needs a stable URL, I use the reserved subdomain. Once the initial setup is done, exposing a local app is a one-command job. Final thoughts There are plenty of established tunneling tools, and no single option will suit everyone. For my React workflow, I wanted as little friction as possible: start the app, run one command, get an HTTPS URL, and open it on a real device. The permanent free hostname also solves one of the more irritating parts of using temporary tunnels regularly. If you're dealing with the same problem, take a look at PortPreview . I'm also curious what other developers use for local React testing and webhook development.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/leobrown/how-i-test-my-react-app-on-real-devices-without-deploying-it-1ko

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
