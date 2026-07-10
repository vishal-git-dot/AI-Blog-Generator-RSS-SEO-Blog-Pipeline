---
title: "Why Cursor Keeps Writing Prototype Pollution Into Your Merge Code"
slug: "why-cursor-keeps-writing-prototype-pollution-into-your-merge-code"
author: "Charles Kern"
source: "devto_webdev"
published: "Fri, 10 Jul 2026 09:36:02 +0000"
description: "TL;DR AI editors love writing recursive merge helpers, and most of them are open to prototype pollution. One crafted JSON payload with a proto key can flip a..."
keywords: "key, merge, source, target, prototype, object, you, pollution"
generated: "2026-07-10T09:45:24.782024"
---

# Why Cursor Keeps Writing Prototype Pollution Into Your Merge Code

## Overview

TL;DR AI editors love writing recursive merge helpers, and most of them are open to prototype pollution. One crafted JSON payload with a proto key can flip an isAdmin flag on every object in your app. Guard the keys or merge into a structure that has no prototype. It is a three-line fix. I asked Cursor for a "deep merge two config objects" helper last week. It gave me eight lines that worked perfectly on my test data. It also gave me a prototype pollution hole big enough to walk through. The function looked fine. That is the problem. Prototype pollution does not show up when you run the happy path. It shows up when someone sends you a key called proto . The code Cursor handed me (CWE-1321) function merge ( target , source ) { for ( const key in source ) { if ( source [ key ] && typeof source [ key ] === ' object ' ) { target [ key ] = merge ( target [ key ] || {}, source [ key ]); } else { target [ key ] = source [ key ]; } } return target ; } Now feed it something a user controls, like a parsed JSON request body: merge ({}, JSON . parse ( ' {"__proto__": {"isAdmin": true}} ' )); ({}). isAdmin ; // true You did not set isAdmin on anything. You set it on every object in the process. Any later check like if (user.isAdmin) now passes for objects that never had that field. Why this keeps happening The recursive merge pattern is all over old blog posts and StackOverflow answers, and almost none of them guard the special keys. The model learned merge from that corpus. It reproduces the shape of the answer, including the missing check, because the missing check never breaks a test. A for...in loop also walks keys like proto when they arrive as ordinary string properties from JSON.parse, which is exactly how the payload gets in. The fix Skip the dangerous keys, or merge into something that has no prototype to pollute. function merge ( target , source ) { for ( const key in source ) { if ( key === ' __proto__ ' || key === ' constructor ' || key === ' prototype ' ) continue ; if ( source [ key ] && typeof source [ key ] === ' object ' ) { target [ key ] = merge ( target [ key ] || {}, source [ key ]); } else { target [ key ] = source [ key ]; } } return target ; } If you can, do not hand-roll this at all. Storing user data in a Map instead of a plain object, or using Object.create(null) for the target, sidesteps the whole class of bug because there is no prototype chain to reach. I've been running SafeWeave for this. It hooks into Cursor and Claude Code as an MCP server and flags prototype pollution and the other patterns before I move on. That said, even a basic pre-commit hook with semgrep will catch most of what is in this post. The important thing is catching it early, whatever tool you use.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/c_k_fb750e731394/why-cursor-keeps-writing-prototype-pollution-into-your-merge-code-291a

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
