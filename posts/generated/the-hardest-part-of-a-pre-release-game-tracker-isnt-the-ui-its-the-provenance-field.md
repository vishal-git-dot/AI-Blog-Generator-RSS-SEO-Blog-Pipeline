---
title: "The hardest part of a pre-release game tracker isn't the UI, it's the provenance field"
slug: "the-hardest-part-of-a-pre-release-game-tracker-isnt-the-ui-its-the-provenance-field"
author: "Mark"
source: "devto_webdev"
published: "Wed, 01 Jul 2026 09:45:09 +0000"
description: "I started sketching a small reference page for a game that hasn't launched yet, and the first schema I wrote was embarrassingly naive. { "character" : "Examp..."
keywords: "release, game, tracker, gets, pre, you, not, official"
generated: "2026-07-01T09:59:55.960925"
---

# The hardest part of a pre-release game tracker isn't the UI, it's the provenance field

## Overview

I started sketching a small reference page for a game that hasn't launched yet, and the first schema I wrote was embarrassingly naive. { "character" : "Example Unit" , "element" : "Ice" , "role" : "Support" } That looks fine until you ask a simple question: where did this come from? For a game that's still in beta or pre-release, "where did this come from" is not a nitpick. It's the whole problem. Why this is easy to underestimate Most content models for a wiki-style tracker assume the data is settled. You pick a schema for a character or item, fill in the fields, done. That works for a game that already shipped, because the publisher's own patch notes are the ground truth. Pre-release communities don't have that luxury. Information arrives in layers: Official trailers and dev posts (solid, but sparse). Datamined values pulled from client files (often accurate, sometimes from a build that never ships). Community translation or paraphrase of the above (frequently where small errors creep in). Pure speculation dressed up as a "leak" because it gets more clicks that way. If your tracker stores all of that in the same flat table with the same visual weight, you've built a rumor amplifier, not a reference site. And once a wrong number gets copied from your page onto three other fan wikis, it's basically impossible to walk back. A concrete case: the stat that wasn't final A recurring pattern in creature-collector and gacha communities is a skill value or character kit that circulates from an early build, gets treated as fact, and then quietly changes before release. Nobody posts a correction thread with the same energy as the original "leak." If a tracker's schema doesn't have a place to record "this came from a datamine of build X, not an official announcement," that context disappears the moment the entry gets copy-pasted somewhere else. The reader has no way to tell a confirmed detail from a snapshot of unfinished work. So the fix isn't a UI problem. It's a data modeling problem: { "entity" : "Example Unit" , "field" : "role" , "value" : "Support" , "status" : "unconfirmed" , "source_type" : "datamine" , "last_checked" : "pre-release build" } Once status and source_type exist as first-class fields instead of afterthoughts, the rendering layer can do something useful with them: gray out unconfirmed rows, add a small label, sort official info above speculation instead of interleaving it. Where this actually gets built I've been using this as the underlying model for a small Honkai: Nexus Anima reference tracker , which exists mainly to organize public, official information about the game ahead of release. It's an independent fan project, not an official HoYoverse resource, and it isn't trying to be a leak aggregator or a prediction engine. That narrow scope is intentional. The whole point is to give people a place to see what's actually been confirmed, separated from what's still floating around as speculation, without pretending the site has some special pipeline into unreleased information it doesn't have. The limits are part of the design A tracker like this is only as good as its restraint. It won't tell you what a character's kit will be before it's announced. It won't resolve a debate between two conflicting datamines. Pre-release game data changes, sometimes substantially, right up until launch, and any static page claiming otherwise is quietly lying to its readers. Practically, that means: Entries need a visible confirmed/unconfirmed distinction, not just a mental one the maintainer keeps in their head. "Last updated" matters more than usual, since the ground truth itself is moving. The maintenance cadence can be light early on and only needs to tighten up as the actual release window gets close. The takeaway for anyone building something similar If you're building any kind of tracker for something that hasn't shipped yet — a game, a product roadmap, a spec still in draft — the interesting engineering problem isn't the list view or the search box. It's whether your schema can honestly represent "I don't fully know this yet" instead of forcing every field into a false certainty. That one field is the difference between a reference site and a rumor mill with better formatting.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/mark_b5f4ffdd8e7cd58/the-hardest-part-of-a-pre-release-game-tracker-isnt-the-ui-its-the-provenance-field-341h

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
