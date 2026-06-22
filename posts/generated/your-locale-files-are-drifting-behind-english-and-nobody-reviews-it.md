---
title: "Your locale files are drifting behind English and nobody reviews it"
slug: "your-locale-files-are-drifting-behind-english-and-nobody-reviews-it"
author: "Isabelle Hue"
source: "devto_webdev"
published: "Mon, 22 Jun 2026 20:43:55 +0000"
description: "Most teams add a new English string in a PR and forget the other languages exist. The PR gets reviewed for logic. The French, German and Spanish files quietl..."
keywords: "your, locale, english, you, keys, nobody, key, locales"
generated: "2026-06-22T20:55:23.246905"
---

# Your locale files are drifting behind English and nobody reviews it

## Overview

Most teams add a new English string in a PR and forget the other languages exist. The PR gets reviewed for logic. The French, German and Spanish files quietly fall one key behind. A few months of that and your non-English locales are full of holes, and you only find out when a user sends a screenshot with auth.signin.button printed on the page. Nobody owns this. It never shows up in code review, because the diff that caused it looked fine. The manual fix breaks things too When someone finally backfills the missing keys by hand, or pastes them into a chat model, two things tend to go wrong. Placeholders get mangled. A translator, human or model, happily turns {name} or {{count}} into something localized, and your interpolation throws at runtime. Inline HTML gets eaten. A <b> inside a string comes back reworded or stripped. So the manual path costs time and quietly adds runtime bugs that, again, nobody notices until production. What i18n Autopilot does It is a GitHub App that runs on every pull request: Reads your source locale (English by default). Finds the keys that exist in the source but are missing from each other locale. Translates only those keys, and keeps placeholders and HTML exactly as they were. Commits the result back to the PR branch and leaves one short comment. There is nothing extra to review and nothing that drifts between releases. It handles flat layouts ( locales/en.json ) and nested ones ( locales/en/<namespace>.json ), and you can point it at a different source locale or folder with an optional .i18n-autopilot.json . Running it Two options. The free GitHub Action runs in your CI with your own OpenAI key, and public repos are always free. The hosted app needs no key and no CI config: 50 keys a month free, then $19 a month or $190 a year. If you have shipped a missing translation before, I would like to hear how your team deals with it now. You can try it on a single repo at https://i18n.useautopilot.dev

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/isabelle_hue/your-locale-files-are-drifting-behind-english-and-nobody-reviews-it-1b5g

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
