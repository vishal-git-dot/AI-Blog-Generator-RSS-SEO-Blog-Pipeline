---
title: "The test is working — going deep on React Router"
slug: "the-test-is-working-going-deep-on-react-router"
author: "BlackJosh007"
source: "devto_webdev"
published: "Sun, 20 Sep 2026 20:30:58 +0000"
description: "Last post I laid out a rule to stop learning-while-building from turning into copy-pasting: learn the concept first, attempt it myself, only ask for hints af..."
keywords: "page, routing, more, route, url, react, post, only"
generated: "2026-09-20T20:35:13.099408"
---

# The test is working — going deep on React Router

## Overview

Last post I laid out a rule to stop learning-while-building from turning into copy-pasting: learn the concept first, attempt it myself, only ask for hints after real stuck effort. I said I'd test it for a few weeks and switch to a structured course if it wasn't producing real understanding. Verdict so far: it's working. This week was routing, and I actually get it — not "I followed a tutorial" get it, but "I can explain why it's built this way" get it. Why routing isn't just "HTML but React" My first assumption was that routing would mean more ceremony than plain HTML anchor tags — more imports, more setup, more friction. It's the opposite reason it's built the way it is: a normal <a> tag triggers a full page reload, which defeats the point of a Single Page Application. React Router exists specifically to swap what's rendered without reloading the page. So the pieces aren't extra complexity for its own sake — they're there to avoid unnecessary re-renders: BrowserRouter — tells React the app uses routing at all Routes — the set of possible routes Route — maps a specific URL to a specific component Link — behaves like an anchor tag, but changes the URL instead of reloading the page Dynamic routes, with a mini blog app Practiced this with a small blog: a home page listing all post titles, and a blog page that reads the post's ID out of the URL and renders the matching post. useParams is what makes this possible — it hands you whatever's sitting in the dynamic segment of the URL so you can look up the right data. I also went into nested routing and the Outlet API — genuinely one of the more satisfying things I've learned so far, seeing a parent route render a shared layout while the child route slots into a specific spot. Picked up the catch-all "not found" route too (my mental label for it: the universal route). Protected routes — concept only, not implemented yet This part I want to be honest about: I only went as deep as the mental model, no real implementation yet. Using a dashboard as the scenario, the idea clicked fast though — auth is just a gate sitting between login and the protected page. Without it, the URL alone is the only thing stopping someone from reaching the dashboard. /dashboard ↓ ┌─────────────┐ │ Auth check │ └─────────────┘ ↓ ↓ YES NO ↓ ↓ Dashboard Login Next stop: custom hooks.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/blackjosh007/the-test-is-working-going-deep-on-react-router-3bdk

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
