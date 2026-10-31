---
title: "I asked an AI Builder to build a forecasting app in one pass."
slug: "i-asked-an-ai-builder-to-build-a-forecasting-app-in-one-pass"
author: "Chinonyerem"
source: "devto_ai"
published: "Sat, 31 Oct 2026 17:02:24 +0000"
description: "I wanted a forecasting app. Not a dashboard, not a chart with a line on it. An app that takes positions on prediction markets and keeps a record of those pos..."
keywords: "one, not, you, builder, app, markets, then, what"
generated: "2026-10-31T17:12:26.639829"
---

# I asked an AI Builder to build a forecasting app in one pass.

## Overview

I wanted a forecasting app. Not a dashboard, not a chart with a line on it. An app that takes positions on prediction markets and keeps a record of those positions, so that when someone claims they called it, you can check when they actually said it. I wrote a specification. It was long. It named the fonts, the sizes, the spacing scale, the radius rules, and the exact hex values. Then I pressed generate. The app came back in about five minutes, working, with a server proxy and three screens. It had also read every one of those colour instructions and applied them backwards. Here is what happened. The design system has a token called primary . In that system primary is the colour of text. The generated components used it as a background. So bg-primary painted the page white, and the accent came out blue, which is the colour the design system uses before you tell it anything. The colours were not missing. They were defined exactly as I asked, sitting in the config, unused, while the page rendered in the default palette. It is a specific kind of failure: the instructions were followed, and then ignored. I fixed it by overriding five custom properties and setting one attribute on the html element. That is the whole fix. It took twenty minutes to find and two minutes to apply. What the app actually does Prediction markets are markets where people trade on whether something will happen. The price of a position is roughly what the market thinks the chance is. If a position costs six cents, the market is saying six percent. Reckon reads those markets, lets you take a position, and writes that position to Walrus Memory before the outcome is known. Walrus Memory stores the data as objects on the Sui blockchain, which means the write carries a timestamp that nobody can backdate. Then it grades every position against the current price. Not against how the market resolved, because these markets resolve in 2027 and a grading system that waits for resolution shows you an empty table for a year. The second customer is software. An AI agent working on someone's behalf needs to decide whether a forecast is worth trusting. It cannot make an account. It has no email address, it cannot accept terms, and it has no way to read a reputation. So Reckon answers its request with a price. The agent pays one cent of USDC on Sui testnet, and the payment is gasless, so the agent does not need any SUI for fees. Reckon reads that transaction on chain, and returns the forecast. One payment, one call. Send the same payment twice and it is refused. The bit that was genuinely hard Walrus Memory writes are asynchronous. You ask it to remember something, it hands you a job, and about twelve seconds later a blob exists. So the record cannot be read from your own file, because a serverless function does not keep one between requests. It has to be read back from the memory service. That means the memory service is the database, and the local file is a cache. Which is fine, until recall fails and you serve a cache and the page shows four positions where there are seven, with nothing on screen to say so. We added a line that names the reason. A short list that looks complete is worse than an error. The other thing worth knowing: recall needs a seal session. Without one, the service returns a successful response with an empty list and a field called dropped_count with a number greater than zero. It looks exactly like an empty namespace. We spent time looking for a bug in our own write path before working out that the data was there and simply would not decrypt. About the builder The generated code was readable, and extending it was not painful. The workflow around it was the problem. There is no way to edit code in the builder itself. The interface says coming soon. So every small change is another prompt, and a prompt that changes one line regenerates a lot more than one line. The sync also only runs one way. The builder pushes to GitHub. There is no way to pull hand written changes back into the builder's copy. Once I had edited the project outside the builder, those two copies could never meet again. Which is a strange limitation for a tool whose whole purpose is to generate a project you then own. What I would tell someone starting Write the specification. It is worth it, even when the tool gets parts of it wrong. Then expect to finish the work by hand. The generated shell is a real head start, and the part that takes the time is never the shell. Also: check what it did with your colours. Not whether it used them. Whether it used them the right way round.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/chnnyrm/i-asked-an-ai-builder-to-build-a-forecasting-app-in-one-pass-3dke

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
