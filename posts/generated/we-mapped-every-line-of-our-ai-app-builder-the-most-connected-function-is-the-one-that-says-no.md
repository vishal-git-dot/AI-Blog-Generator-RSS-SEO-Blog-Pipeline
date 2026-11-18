---
title: "We mapped every line of our AI app builder. The most connected function is the one that says "no"."
slug: "we-mapped-every-line-of-our-ai-app-builder-the-most-connected-function-is-the-one-that-says-no"
author: "SPLEX"
source: "devto_webdev"
published: "Wed, 18 Nov 2026 00:42:58 +0000"
description: "We're a team of five in India building SPLEX, an AI app and website builder built for one thing: the most accurate code AI can write. This week we ran an ope..."
keywords: "code, every, app, most, build, our, builder, one"
generated: "2026-11-18T00:48:50.459512"
---

# We mapped every line of our AI app builder. The most connected function is the one that says "no".

## Overview

We're a team of five in India building SPLEX, an AI app and website builder built for one thing: the most accurate code AI can write. This week we ran an open-source tool called graphify over our whole codebase. It reads every file, finds every function, type, table and import, and draws how they connect. Here's what came out: 662 code files 5,226 pieces (functions, types, tables, routes) 12,203 connections between them 340 groups of code that work together A few things surprised us. 1. The most connected functions are fail() and ok() Not the AI engine. Not the build pipeline. The two tiny helpers every request handler returns through: fail("message", status) and ok(data) , with 126 and 125 connections. That's the shape you get when every path has to decide, explicitly, whether it worked. In a product whose whole point is code that works, the most-used function in the codebase is the one that says "this didn't work, and here's why in plain words". We think that's the right centre of gravity. 2. The builder file is a hub, and that's a warning apps.ts (where a build starts, runs, is checked and is saved) has 265 connections. That's the biggest single file hub in the project. Hubs are where bugs hide, because a change there touches everything. The worst bug we fixed this week lived right in it: A change to an app could get stuck at "planning" forever. A database check limited a build plan to 64 KB. Big apps went over, the update failed, and the error was ignored, so the build never started and never ended. The fix: a bigger limit, and the code now fails loudly and refunds the credit instead of waiting forever. A background sweep also cleans up any build that stalls. The map didn't find this bug. It did show us why it hurt so much: it sat on the busiest crossroads in the code, where one ignored error blocks everything behind it. 3. The database is its own continent Our migrations file has 248 connections and sits in its own cluster, far from the app code. That's healthy: the app talks to the database through a small number of doors (row-level security, a handful of functions), not from everywhere. 4. Old code shows up as islands The map made dead code obvious: small groups that connect to nothing current. This week we deleted a set of retired features from both the code and the database (30+ tables). Islands are the easiest code to delete safely, because nothing points at them. What we changed because of it The busiest files get the most tests. Every change to the builder runs 580 backend tests before it ships. New features go behind a clear entry point instead of adding more lines to the biggest hub. We re-run the map after big changes and look for new islands. Try it on your own code graphify is open source. Point it at a repo and you get an interactive map plus a plain-English report: the most connected pieces, surprising links across folders, and import cycles. It took about a minute on our codebase, and the code part needed no AI at all. And if you want to see what all that code does: describe an app in plain words at splex.in . It's free to start, and there are 24 ready-made templates (shop, booking site, invoice maker, games) that open in a second. Built in India by Steve Stephen, Sohan RK, Gunavantha, Surya and Sharvil.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/splex_ai/we-mapped-every-line-of-our-ai-app-builder-the-most-connected-function-is-the-one-that-says-no-53d2

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
