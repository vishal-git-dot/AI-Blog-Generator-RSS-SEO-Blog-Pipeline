---
title: "Outwards - i build app that help you secure your company by finding exposed data"
slug: "outwards-i-build-app-that-help-you-secure-your-company-by-finding-exposed-data"
author: "else54"
source: "devto_ai"
published: "Sat, 03 Oct 2026 15:38:21 +0000"
description: "Hey, AI has changed the way we work quite a lot. We’re more productive than ever, but at the same time it’s becoming harder to keep track of where company da..."
keywords: "company, files, data, google, publicly, public, whether, outwards"
generated: "2026-10-03T16:02:08.705261"
---

# Outwards - i build app that help you secure your company by finding exposed data

## Overview

Hey, AI has changed the way we work quite a lot. We’re more productive than ever, but at the same time it’s becoming harder to keep track of where company data actually ends up. I’ve personally come across situations like these: someone prepares a client proposal and uploads internal files directly into an AI tool , an internal PDF is left somewhere under wp-uploads and eventually gets indexed by Google, working notes from NotebookLM or files on Google Drive turn out to be publicly accessible, an API key is hardcoded in source code and ends up in a public repository. They’re just small mistakes that anyone can make. That’s why I’ve been working on a project called Outwards — a tool for monitoring publicly exposed confidential company data. The idea is that a company first verifies that it actually owns the domain. Then Outwards builds a map of its public assets: domains, repositories, accounts, documents and other related resources. After that, it looks at the company from the outside and checks things like: AI tools - whether AI models or publicly shared AI conversations can surface information about the company that probably shouldn’t be easy to find. Search engines - whether Google or Bing are indexing internal documents, employee data, contracts, email addresses or other sensitive material. Public repositories - whether API keys, credentials, config files or other secrets were accidentally committed to public code. Cloud files - whether Google Drive files, shared documents, boards or similar resources are publicly accessible. If something is found, the user gets an alert, an explanation of the risk, and guidance on how to remove or secure it. In practice, I think of it as continuous OSINT performed on your own company - trying to find the problem before someone else does. I’ve opened an early waitlist and I’m currently looking for feedback: getoutwards.com What do you think about the idea? Would you see a real use case for something like this in software companies?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/else54/outwards-helping-you-secure-your-company-by-finding-exposed-data-5hdg

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
