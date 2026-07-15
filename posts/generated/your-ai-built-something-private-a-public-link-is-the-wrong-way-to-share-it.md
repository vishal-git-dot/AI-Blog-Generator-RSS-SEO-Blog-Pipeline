---
title: "Your AI built something private. A public link is the wrong way to share it."
slug: "your-ai-built-something-private-a-public-link-is-the-wrong-way-to-share-it"
author: "Alex"
source: "devto_webdev"
published: "Wed, 15 Jul 2026 13:31:51 +0000"
description: "Building with AI got fast. You describe a thing, and a page, a dashboard, a small internal report, or a client-facing microsite comes out. The awkward part i..."
keywords: "not, you, link, who, can, public, viewer, site"
generated: "2026-07-15T13:53:37.361230"
---

# Your AI built something private. A public link is the wrong way to share it.

## Overview

Building with AI got fast. You describe a thing, and a page, a dashboard, a small internal report, or a client-facing microsite comes out. The awkward part is the next step: you want exactly three people to see it, and the default way we share a built thing is a public URL that anyone who gets the link can open. For a landing page that is fine. For a client's numbers, an unreleased feature, a draft you only want two colleagues to read, it is the wrong default. I kept hitting this while building Thryvate (disclosure: it is mine, this is a build-log, not a pitch), and the access model turned out to be the hardest and most interesting part. Here is where I landed and the tradeoffs behind it. The problem with a link anyone can open Paste-to-link hosts (Tiiny.host, Static.app, Netlify Drop, and friends) are great at one job: take a file, give back a public URL, done. But "public URL" quietly decides three things for you: Anyone with the link is in. Forward it once and you have lost the guest list. You cannot tell who actually opened it, only that "someone" did. Search engines and link unfurlers can reach it, so "unlisted" is not "private." For a lot of AI-built artifacts, the whole point is that they are not for everyone. A URL that treats every viewer identically cannot express "these people, nobody else." So the model needs an identity for the viewer before it will show anything. The model I settled on: verify before a byte loads The rule I committed to is simple to say and annoying to build: no content renders until the viewer has proven who they are. Concretely, a private site does this: The viewer lands and gets an email-verification step, not the content. They enter their email, click the link, and only then does the page load. Their email is checked against an allowlist the owner controls. Not on it, not in. The important word is before . Verifying after render leaks the content to anyone who loads the page and closes the tab. Verifying before render means the bytes never leave the server for someone who is not on the list. That one ordering decision is most of the security value. Allowlist, not a forwardable link The allowlist is the piece that makes forwarding harmless. The site is bound to a set of email addresses, not to knowledge of a URL. If a viewer forwards the link, the recipient hits the same verification wall and bounces unless the owner added them. Adding and removing people is the owner editing a list, and revoking is immediate: drop the address and their next load fails. This is a different mental model from "unguessable link." An unguessable link is a password you accidentally paste into Slack. An allowlist is a guest list the door checks every time. Password and expiry, layered on top Two smaller controls ride on top of the allowlist because real sharing is messier than a single switch: A per-site password, for when you want a lightweight gate without curating emails. A link expiry, for "this is fine to see this week, not next month." They compose. You can require both an allowlisted email and a password, or set a private allowlisted site to also expire on Friday. The design goal was that the common cases (just me and two people; anyone at this company; public but only for a week) are all expressible without a settings PhD. The origin decision: sandboxed and cookieless One more thing that is invisible until it bites you: an AI-built page can contain arbitrary HTML and JS. If every site renders on the same origin, one site's script can reach another's storage and cookies. So each site renders on its own sandboxed, cookieless origin. It costs some convenience (no shared login state across sites, by design) and buys real isolation between things different people published. What this is not Being honest about the ceiling, because "private by default" oversells easily: It is not DRM. A verified viewer can screenshot or retype what they can see. The model controls who gets in , not what an authorized person does afterward. It is not anonymity for the viewer. The point is the opposite: the owner knows the verified email of who is looking. It is not a replacement for real access control inside a complex app. This is for sharing an artifact, not for building a multi-tenant product's permission system. Why I think the default should flip The public-link hosts were designed for a web where you published things you wanted found. A lot of what we build with AI now is the opposite: specific, personal, meant for a named few. When the making is cheap, most of what gets made is not for the whole internet. So the sane default for sharing it is private, with the owner naming who gets in, and public as the deliberate exception. If you have built something with AI and the "now share it with just these people" step felt wrong, I would genuinely like to hear how you handled it. And if you want to see the access model above in practice, Thryvate is where I built it.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/thryvate/your-ai-built-something-private-a-public-link-is-the-wrong-way-to-share-it-138j

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
