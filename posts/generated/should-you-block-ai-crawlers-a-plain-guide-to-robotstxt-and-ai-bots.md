---
title: "Should You Block AI Crawlers? A Plain Guide to robots.txt and AI Bots"
slug: "should-you-block-ai-crawlers-a-plain-guide-to-robotstxt-and-ai-bots"
author: "Nadeem Akram"
source: "devto_ai"
published: "Thu, 24 Sep 2026 21:07:43 +0000"
description: "Originally published at seopeck.com . Alongside Googlebot and Bingbot, most websites are now visited by crawlers from AI companies. Some collect text to trai..."
keywords: "user, crawlers, robots, txt, you, crawler, agent, not"
generated: "2026-09-24T21:21:41.121330"
---

# Should You Block AI Crawlers? A Plain Guide to robots.txt and AI Bots

## Overview

Originally published at seopeck.com . Alongside Googlebot and Bingbot, most websites are now visited by crawlers from AI companies. Some collect text to train language models; others fetch pages so an AI assistant can answer a question and cite its source. Site owners are increasingly asking the same question: should I let them in? There is no single right answer. It depends on what you publish and what you want in return. This guide explains the main crawlers, what they are used for, and how to control them. Two kinds of AI crawler Training crawlers collect content to build and improve AI models. Examples are OpenAI's GPTBot , Anthropic's ClaudeBot , Meta's Meta-ExternalAgent and Common Crawl's CCBot , whose open dataset is used by many AI projects. Blocking these keeps your future content out of new training runs. It does not remove anything that was collected before. Search and user crawlers fetch pages in response to what people ask right now. Examples are OAI-SearchBot and ChatGPT-User from OpenAI, Claude-SearchBot and Claude-User from Anthropic, and PerplexityBot . These are the bots that can show your page as a source and send visitors to it. There are also control tokens that are not separate crawlers at all. Google-Extended lets you opt out of your content being used for Google's Gemini models without affecting Google Search. Applebot-Extended does the same for Apple's AI training. How robots.txt rules work robots.txt is a plain text file at the root of your site, for example https://example.com/robots.txt . It is made of groups. Each group names one or more crawlers with User-agent lines, followed by Allow and Disallow rules: User-agent: GPTBot Disallow: / User-agent: * Disallow: /admin/ Two details trip people up: A crawler follows only the most specific group that names it. In the example above, GPTBot obeys its own group and ignores the * group completely. A crawler that is not named anywhere falls back to * . Within a group, the longest matching rule wins. Disallow: / with Allow: /blog/ means the blog is allowed and everything else is blocked. Common setups Block AI training, allow AI search. This is a popular middle ground for publishers who want citations and visits but do not want their work used to train models: User-agent: GPTBot User-agent: ClaudeBot User-agent: CCBot User-agent: Google-Extended User-agent: Applebot-Extended User-agent: Meta-ExternalAgent Disallow: / Allow everything. If you want the widest possible reach, including being part of the data AI tools learn from, you do not need any AI-specific rules at all. Block everything AI. Add the search and user crawlers to the list above as well. Be aware that you will no longer appear as a source in those assistants' answers. What robots.txt cannot do robots.txt is a request, not a wall. The large AI companies say their crawlers respect it, but a badly behaved bot can ignore it. If you need to stop a crawler for certain, block it at the server or firewall level as well. Also remember that robots.txt is public: anyone can read it, so never use it to hide private areas. Protect those with a login. Check what your site allows today It is easy to get a rule slightly wrong, for example by adding a crawler to a group you did not intend, or leaving a typo in its name. A few free resources: AI Crawler Checker : reads your live robots.txt and shows, crawler by crawler, whether it is allowed, blocked or partly blocked. ai-crawlers-robots-txt on GitHub : an open list of 14 AI crawlers with their operator, purpose and official docs link, plus copy-paste templates (CC0). Robots.txt Generator : builds a full robots.txt with per-crawler rules. Disclosure: I build SEOpeck and maintain the GitHub list. Corrections and new crawlers are welcome as PRs.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/nadeemakram035/should-you-block-ai-crawlers-a-plain-guide-to-robotstxt-and-ai-bots-2ham

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
