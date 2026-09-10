---
title: "My AI agent copy-pasted SEO tags across 20 files instead of generating them"
slug: "my-ai-agent-copy-pasted-seo-tags-across-20-files-instead-of-generating-them"
author: "Sergei Ivantsov"
source: "devto_webdev"
published: "Thu, 10 Sep 2026 16:01:55 +0000"
description: "I wrote a small generator to stop an AI coding agent from hand-duplicating SEO metadata across a multilingual static site. It has a --check flag that verifie..."
keywords: "data, than, one, seo, site, agent, files, check"
generated: "2026-09-10T16:09:48.922892"
---

# My AI agent copy-pasted SEO tags across 20 files instead of generating them

## Overview

I wrote a small generator to stop an AI coding agent from hand-duplicating SEO metadata across a multilingual static site. It has a --check flag that verifies the generated files still match their data source. The day after I shipped it, I found that when the generator silently corrupted all 20 pages, --check reported it as "out of date" — the exact same message it prints when you legitimately edit the data file and haven't regenerated yet. That's the part worth writing down. A verification flag that can't distinguish "you changed something on purpose" from "the tool just wrote broken URLs into every page you have" isn't verifying much. Here's how I got there. The site A free, direct-from-owner property listing site for North Cyprus — girne-apartment-sale.com , no agency, no commission. Vanilla HTML/CSS/JS, zero npm dependencies, deployed to Cloudflare Pages. Four languages (EN/RU/TR/PL), each language a real indexable URL rather than a client-side toggle, so 5 page types × 4 languages = 20 HTML files. Written together with Claude Code. I have a professional translation background, so my bar for "done" here was a genuinely correct multilingual site, not a page that renders. That bar is the only reason the rest of this happened — nothing below was surfaced by the agent on its own. The first bug: no single source of truth The agent put <title> , og:title , and the JSON-LD name into each of those 20 files by hand, as literal strings, rather than deriving them from one place. That works right up until you update 19 files and miss one. I caught it by re-running the site against an old GEO/AEO audit checklist I had lying around, written for a completely unrelated niche (health, not real estate) and used purely as a generic methodology pass — hreflang, canonicals, structured data. The second listing's Polish version had different wording in its title and description than the other three languages. Not a typo: drift. Individually harmless, collectively the exact failure a site that advertises itself as multilingual cannot afford. Worth noting what didn't happen: reference material of mine describing the practices I wanted — zero dependencies, one source of truth for data, structured data over keyword stuffing — was sitting in the working environment the whole time. None of it got applied unprompted. Every item had to be asked for explicitly, one at a time. Being available in context is not the same as being pulled forward. The fix, and why it isn't Hugo The obvious objection first: this is a solved problem, and Eleventy, Hugo, Jinja, or any templating layer solves it out of the box. True. I didn't use one, deliberately. Adopting an SSG here means moving the entire page body — layout, listing copy, gallery markup, four languages of it — into a template system, to fix a problem that lives in roughly 15 lines of <head> . The migration is the whole site; the bug is the header. So instead: build/seo-data.js holds title, meta description, Open Graph, hreflang, and JSON-LD for every page in one place, and build/generate-seo.js injects it into each file between <!-- SEO:START --> / <!-- SEO:END --> markers. Everything outside those markers is never touched — the HTML stays hand-written HTML, editable without knowing the generator exists. Plain Node, no dependencies. --check verifies without writing, run before deploy. That closed the drift class structurally. There's no second copy of the string left anywhere for me or the agent to forget. Standalone, genericized version with an example data file, if you want the code rather than the description: https://github.com/sergei-swh/seo-generator The second bug: the tool built to stop looking Then I tested adding a fifth language — German — to see what the generator did with it. Adding "de" to the language list without the matching paths / perLang / homeLabel data didn't error. The hreflang builder loops over every configured language for every page, found no path for German, and wrote href="https://girne-apartment-sale.comundefined" into all 20 existing pages. Pages that were correct a minute earlier. And --check dutifully reported: out of date. Same string as any ordinary pending edit. The fix was a validateData() pass that runs before anything is written and fails loudly with an explicit list of what's missing. But the lesson generalizes past this one script: if your verification step reports "different from expected" without a notion of how different, it is a diff, not a check. Mine was a diff pretending to be a check from the moment I wrote it, and I only found out because I went poking at a tool I had specifically built so I could stop poking. Limits I didn't run this at max capability — Sonnet 5, reasoning effort medium, not higher — so none of this is a claim about what these agents do at their best, or in general. It's what happened in this setup, starting from an existing foundation rather than a cold start. What I'd take from it: an AI agent will reliably produce something that works, and it optimizes hardest for the layer you can see. The failure modes live one layer down, in duplication it introduces because duplication is locally cheaper than structure, and they surface as drift rather than as errors. Nothing about that is exotic — it's the same failure mode as any copy-paste — but it arrives faster and across more files than a human would manage, and it doesn't get flagged, because from the inside every individual file looks fine.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/sergei-swh/my-ai-agent-copy-pasted-seo-tags-across-20-files-instead-of-generating-them-4lg2

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
