---
title: "We Built a RAG Chatbot for Customer Support That Cut Tickets by 73%"
slug: "we-built-a-rag-chatbot-for-customer-support-that-cut-tickets-by-73"
author: "Vinish Bhaskar"
source: "devto_ai"
published: "Wed, 30 Sep 2026 04:43:45 +0000"
description: "Our team at Pimjo runs more than a dozen products. Support tickets kept asking the same things: how refunds work, how an integration connects, where to find ..."
keywords: "chatbot, answer, what, agent, your, support, rag, bot"
generated: "2026-09-30T04:59:51.114636"
---

# We Built a RAG Chatbot for Customer Support That Cut Tickets by 73%

## Overview

Our team at Pimjo runs more than a dozen products. Support tickets kept asking the same things: how refunds work, how an integration connects, where to find an API key. Every answer already existed in our documentation. Customers still waited hours for someone to send them a link. We tried a chatbot first. It answered confidently and often wrongly. A wrong answer with no source is worse than no answer, because the customer acts on it and then writes in again. What worked was a RAG chatbot or AI support agent chatbot that answers only from our own content and hands off when it can't. This post explains how that pattern works, what a support bot needs beyond basic retrieval, and the numbers we saw over 45 days. What a RAG chatbot is RAG stands for retrieval-augmented generation. It splits answering into two steps: Retrieve: When a question arrives, the system searches your content (docs, FAQs, past tickets) for the passages most related to it. Generate: The language model receives those passages along with the question and writes an answer based on them. A plain chatbot built on a language model answers from whatever it learned during training. It knows nothing about the pricing change you made last week. A RAG chatbot answers from a set of documents you control. Update the documents, and the answers change with them. Why the other options failed us Scripted bots work inside their decision trees. Ask something slightly different, and they produce a fluent answer with nothing behind it. They also can't pass a hard question to a person. Static help centers are correct on the day you write them. Change your pricing, and the old article keeps showing last quarter's numbers until someone remembers to edit it. Hiring raises cost in a straight line, but repeat questions keep arriving at the same rate. You buy capacity, not resolution. Retrieval is not enough for support Retrieval puts the right passage in front of the model. A customer-facing bot needs a few more rules around it: Refuse when the content has no answer. If retrieval finds nothing relevant, the bot should say it can't confirm the answer instead of guessing. Hand off with the full thread. When the bot stops, a person should receive a ticket containing the whole conversation, so the customer doesn't repeat the problem. Read the whole conversation. A follow-up like "what about the annual plan?" only makes sense with the earlier messages. Set an explicit scope. Define what the bot handles, what it refuses, what it never shares, and when it escalates. Keep internal content separate. Run a different agent with its own knowledge base for staff, so internal policy never reaches a customer. Restrict where the bot runs. Allowed-domain rules keep each agent on the sites you assign it to. Treat handoffs as a to-do list. Each escalation points to a gap in your docs. Add the missing answer, and the bot handles that question next time. What we measured over 45 days We built these rules into Nivon.AI and ran it in production on two of our products, Aymo AI and Meku.dev, for 45 days before offering it to anyone else. Across both products: Tickets reaching a person dropped by 73% . Time to first response went from 15 minutes to 6 minutes . The agent resolved 80% of chat widget conversations without a person. These numbers measure different things. Most of the ticket drop came from customers using the chat widget instead of filing a ticket. The 80% figure covers only the conversations that happened in the widget. They are our own numbers, not an industry benchmark. Your results depend on how complete your documentation is and what your customers ask. Try it with Nivon.AI Nivon is the support agent that came out of this work. Setup takes minutes and doesn't require a developer. Knowledge sources: Crawl a website or sitemap, upload documents, import from Google Drive or OneDrive, add FAQs, paste text, or import past support tickets. Model choice: Pick from 20+ models from OpenAI, Anthropic, Google, and xAI for each agent. Switch at any time. Languages: The agent replies in the language the customer writes in, across 95+ languages. Chat First or Lead First: Choose whether the agent answers questions right away or qualifies the visitor first. Workspaces: Separate agents, conversations, and knowledge by team or product, with admin and member roles. Analytics: Track conversation volume, resolution rate, response time, and where customers write from. Nivon runs alongside your existing helpdesk. Anything the agent can't resolve becomes a ticket with the conversation attached, so there is nothing to migrate. Data handling Content and conversations are encrypted in transit and at rest, and each workspace is isolated. Nothing you send is used to train any AI model. Nivon meets GDPR, CCPA, and ISO 27001-level requirements. SOC 2 Type II compliance is in progress. Pricing Plans are priced by support volume, not per seat. Plan Price Credits per month Team members Free $0 150 1 Starter $9/mo 3,000 3 Growth $29/mo 12,000 5 Business $59/mo 30,000 15 Each plan also caps the number of agents, workspaces, and training pages. The free plan does not expire and needs no card. Integrations Google Drive and OneDrive are live. Slack, GitHub, and Telegram are in progress, and Notion is in review. Current status is on the roadmap . Before you add any RAG chatbot Check your docs first. List the ten questions your team answers most often and confirm each answer exists in writing. A RAG chatbot can only be as accurate as the content it retrieves. To set one up, start with the quickstart guide or create a free account .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/vinishbhaskar/we-built-a-rag-chatbot-for-customer-support-that-cut-tickets-by-73-2cpo

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
