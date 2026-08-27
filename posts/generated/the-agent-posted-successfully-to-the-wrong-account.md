---
title: "The agent posted successfully. To the wrong account."
slug: "the-agent-posted-successfully-to-the-wrong-account"
author: "Eugeniya Ivanova"
source: "devto_webdev"
published: "Thu, 27 Aug 2026 08:31:54 +0000"
description: "Back in July I wrote about what it takes to wire an AI agent into social platforms : six OAuth flows, three-step media uploads, tokens expiring on their own ..."
keywords: "wrong, one, what, you, agent, tool, call, server"
generated: "2026-08-27T08:36:24.648156"
---

# The agent posted successfully. To the wrong account.

## Overview

Back in July I wrote about what it takes to wire an AI agent into social platforms : six OAuth flows, three-step media uploads, tokens expiring on their own private schedules. The conclusion was to hide all of it behind a single tool call and stop looking at it. Two months on, that part is done. Our MCP server answers over OAuth now, with proper metadata at /.well-known/oauth-authorization-server , PKCE, and dynamic client registration, so connecting an editor no longer involves typing a key into a config file. Sixteen tools, one endpoint. The plumbing works. What I got wrong was assuming the plumbing was the risky part. My job is getting our product into people's hands, which means I use it the way I hope other people will: I ask an agent to publish and go back to what I was doing. Living with that for a couple of months taught me that once an agent has write access, failures stop announcing themselves. An identifier that looks exactly like an identifier A language model produces plausible-looking strings. That is the entire skill. Ask it to post to LinkedIn and it can hand the API a value with the right prefix, the right length, the right shape, and the wrong account. Nothing about that request is malformed. There is no error to catch. The API was asked to do something specific and it did it. So the first instruction our server gives any client is not a description of what it does. It's a rule: call list_connections first, copy each platformId verbatim, never invent one. Before the tool list, before the examples, before anything explaining what the product is for. Writing documentation for a reader who will confidently improvise is a genuinely different job from writing it for a human who will get bored and skim. "Tomorrow at 9am" is a timezone question The API takes ISO 8601 in UTC and nothing else. So when you say "tomorrow at 9am," something has to decide which 9am you meant, and that something is the model. It's right most of the time. When it isn't, nothing surfaces at the call. The response is a normal success, the post sits in the queue with a perfectly valid timestamp, and you find out at 4am from the post itself. I now read the scheduled time back in the confirmation. Not because the model is bad at arithmetic, but because a wrong answer here is indistinguishable from a right one until it's too late to matter. Accepted now, dead later Instagram, TikTok and YouTube won't publish without media. Nothing stops an agent from scheduling a text-only Instagram post: it validates, it enters the queue, it sits there looking healthy for a day, and it dies at publish time. Queue membership is not a promise. It's the kind of distinction you only learn by getting burned, because until then the failure is completely invisible. The annotations nobody looks at MCP lets a server tag each tool with hints about what it does: readOnlyHint , destructiveHint . Ours are filled in. Sixteen tools, six of them flagged destructive: deleting posts, deleting media, removing a LinkedIn comment or reaction. { "name" : "delete_post" , "annotations" : { "readOnlyHint" : false , "destructiveHint" : true } } They're advisory. A client can ignore them entirely, and plenty do. But they cost almost nothing to add, and they're the only way a server can tell a client "this one deserves a confirmation dialog" without inventing a private protocol. If you run an MCP server and haven't filled them in, that's twenty minutes of work that lets every well-behaved client protect your users for you. A fake platform to post into The fix I like most is the least clever one: { "content" : "test" , "platforms" : [ "publora-playground" ] } It accepts the post, validates it against the real rules, returns a normal response, and throws it away. Nothing reaches a real network. It exists because there was previously no honest way to answer "is this connected and working?" Every genuine end-to-end test involved putting something real on someone's real timeline, which is a fine way to test at 2am and an awful one at any other hour. Now the whole round trip is testable without an audience. Every integration that writes somewhere public should have one of these, and most don't. What I'd tell July I'm biased about the product, so here's the part that isn't about it. When you give an agent write access to anything outward-facing, the failure worth designing against is not the 500. Exceptions land in logs and somebody eventually reads them. The dangerous one is the call that succeeds and quietly does the wrong thing: right shape, wrong target, no error anywhere in the chain. The July version of this was "hide the complexity behind one tool call." I still think that's right. I'd just add the second half now: and make the tool call hard to get subtly wrong, because subtly wrong is the only kind of wrong that gets published. Posting from the terminal saved me a context switch. The guardrails are what made me willing to leave it running while I did something else. I drafted this with Claude and then checked every claim against the live server before publishing. The playground response, the tool annotations, and the OAuth metadata are all things I re-ran rather than remembered. If you run an agent with write access to production, where's your line: a dry-run target, tool annotations, or a human confirming every call?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/eugeniya_ivanova_4a58eadc/the-agent-posted-successfully-to-the-wrong-account-3kf3

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
