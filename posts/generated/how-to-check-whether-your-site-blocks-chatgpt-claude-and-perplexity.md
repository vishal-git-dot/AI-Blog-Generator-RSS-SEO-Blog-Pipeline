---
title: "How to check whether your site blocks ChatGPT, Claude and Perplexity"
slug: "how-to-check-whether-your-site-blocks-chatgpt-claude-and-perplexity"
author: "David Black"
source: "devto_webdev"
published: "Mon, 12 Oct 2026 14:50:16 +0000"
description: "Plenty of sites turn AI crawlers away without anyone having decided to. A security plugin, a CDN setting or a line copied into robots.txt years ago is enough..."
keywords: "user, agent, your, crawler, robots, txt, you, not"
generated: "2026-10-12T14:59:14.188339"
---

# How to check whether your site blocks ChatGPT, Claude and Perplexity

## Overview

Plenty of sites turn AI crawlers away without anyone having decided to. A security plugin, a CDN setting or a line copied into robots.txt years ago is enough. If an assistant cannot fetch your pages, it cannot quote them, and you will not hear about it. Here is how to check, in about ten minutes. Two kinds of crawler, and why the difference matters AI companies run more than one crawler, and they do different jobs. Answer fetchers read a page so an assistant can answer a question with it, often while someone is waiting: OAI-SearchBot and ChatGPT-User (OpenAI) PerplexityBot and Perplexity-User (Perplexity) Claude-SearchBot and Claude-User (Anthropic) Training crawlers collect pages to train future models: GPTBot (OpenAI) ClaudeBot (Anthropic) CCBot (Common Crawl, whose data many labs use) Google-Extended (a robots.txt token rather than a separate crawler; it controls use of your pages for Gemini) You may reasonably want to block the second group and allow the first. Blocking everything with "AI" in the name is how a business ends up invisible in answers it would have liked to be in. Step 1: read your robots.txt Open https://yourdomain.com/robots.txt in a browser and look for any of the names above. This blocks one crawler from the whole site: User -agent: OAI-SearchBot Disallow: / Things to know while reading it: A crawler obeys the most specific group that names it. If there is a User-agent: GPTBot group, GPTBot ignores the User-agent: * group entirely. Disallow: / blocks everything. Disallow: with nothing after it blocks nothing. A crawler that is never mentioned falls back to the * group, so check that one too. Step 2: check for a block that is not in robots.txt This is the one people miss. Firewalls, bot-protection plugins and CDN "block AI bots" switches refuse requests before robots.txt is ever consulted. Your robots.txt can look fine while every AI request gets a 403. You can get a rough signal by sending a request that identifies itself as a crawler: curl -s -o /dev/null -w "%{http_code} \n " \ -A "Mozilla/5.0 (compatible; OAI-SearchBot/1.0)" \ https://yourdomain.com/ A 200 is a good sign. A 403 , 406 or 429 means something in front of your site is refusing that name. Be honest about what this proves. You are not the real crawler, and some protection checks the IP address as well as the name. A refusal here is strong evidence of a block. A 200 is weaker evidence that you are open. Your server or CDN logs are the final word: search them for the crawler names and look at the status codes they actually received. Step 3: decide, then write it down If you want to be quoted in AI answers but not used for training, say so explicitly rather than relying on defaults: User -agent: OAI-SearchBot User -agent: ChatGPT-User User -agent: PerplexityBot User -agent: Perplexity-User User -agent: Claude-SearchBot User -agent: Claude-User Allow : / User -agent: GPTBot User -agent: ClaudeBot User -agent: CCBot User -agent: Google-Extended Disallow: / Then find the setting that caused any firewall block and add the same exceptions there. Changing robots.txt does nothing if the request never gets that far. What this does not do Letting a crawler in means it can read you. It does not mean an assistant will recommend you. That depends on what your pages say and who else says it. A shortcut for step 1 I build MentionMachine, which has a free robots.txt checker for AI crawlers . It reads your file, shows which crawlers are allowed, blocked or never mentioned, and gives you a patch to copy. It writes nothing to your site and needs no account.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dcblack87/how-to-check-whether-your-site-blocks-chatgpt-claude-and-perplexity-31nl

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
