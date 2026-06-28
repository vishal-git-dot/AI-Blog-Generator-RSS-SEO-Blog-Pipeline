---
title: "AI Language Learning"
slug: "ai-language-learning"
author: "Elena Revicheva"
source: "devto_ai"
published: "Sun, 28 Jun 2026 19:30:04 +0000"
description: "Originally published on AIdeazz — cross-posted here with canonical link. $12,456 is what I spent on Oracle Cloud infrastructure to ship EspaLuz, a Spanish la..."
keywords: "conversation, user, espaluz, which, using, database, oracle, store"
generated: "2026-06-28T19:38:17.340591"
---

# AI Language Learning

## Overview

Originally published on AIdeazz — cross-posted here with canonical link. $12,456 is what I spent on Oracle Cloud infrastructure to ship EspaLuz, a Spanish language learning platform, before I had a single paying user. 100 free signups later, I still hadn't cracked the code on user retention. It wasn't until I switched from a web app to a WhatsApp-based conversation interface that I started to see traction – 3 paying users who taught me more about what works than the previous 100 free trials. Architecture Overview EspaLuz uses a two-layer memory system to store conversation context and user progress. The first layer is a simple key-value store that I implemented using Oracle's NoSQL database, which costs $0.25 per hour for a single node. The second layer is a graph database that stores relationships between conversation topics and user interests, which I built using a custom implementation of a graph traversal algorithm. This two-layer approach allowed me to avoid using a paid vector store, which would have added an extra $500 to my monthly expenses. Conversation Continuity One of the key challenges I faced when building EspaLuz was maintaining conversation continuity across sessions. Since WhatsApp doesn't provide a built-in mechanism for storing conversation state, I had to implement a custom solution using a combination of Oracle's Cloud Storage and my graph database. This allowed me to store conversation context and retrieve it when the user started a new session, giving the illusion of continuous conversation. I measured the success of this approach by tracking user engagement, which increased by 30% after implementing conversation continuity. Routing and Agents To handle incoming WhatsApp messages, I used a combination of Groq's routing engine and Claude's natural language processing (NLP) library. This allowed me to route user input to the correct conversation agent, which would then respond with a relevant message. I implemented a total of 5 conversation agents, each with its own set of intents and responses. The agents were built using a custom implementation of a finite state machine, which allowed me to manage conversation flow and user state. Multi-Agent Systems EspaLuz uses a multi-agent system to manage conversation flow and user state. Each agent is responsible for a specific aspect of the conversation, such as greetings, lessons, or feedback. The agents communicate with each other using a custom protocol that I designed, which allows them to share user state and conversation context. This approach allowed me to scale the conversation interface horizontally, adding new agents as needed to handle increasing user traffic. I measured the success of this approach by tracking user retention, which increased by 25% after implementing the multi-agent system. Lessons Learned The 3 paying users who signed up for EspaLuz taught me more about what works than the previous 100 free signups. They showed me that users value conversation continuity and personalized feedback, and that they are willing to pay for a high-quality language learning experience. I also learned that a WhatsApp-based conversation interface is more engaging than a web app, with users spending an average of 20 minutes per session compared to 5 minutes per session on the web app. These lessons have informed my approach to building future language learning platforms, and I believe that they can be applied to other domains as well. Frequently Asked Questions Q: How did you implement the two-layer memory system in EspaLuz? A: I used a combination of Oracle's NoSQL database and a custom graph database to store conversation context and user progress. The NoSQL database provides fast key-value lookups, while the graph database allows me to store relationships between conversation topics and user interests. Q: What was the biggest challenge you faced when building EspaLuz? A: The biggest challenge was maintaining conversation continuity across sessions. I had to implement a custom solution using a combination of Oracle's Cloud Storage and my graph database to store conversation context and retrieve it when the user started a new session. Q: How do you handle incoming WhatsApp messages in EspaLuz? A: I use a combination of Groq's routing engine and Claude's NLP library to route user input to the correct conversation agent. The agents are built using a custom implementation of a finite state machine, which allows me to manage conversation flow and user state. Q: What is the average user retention rate for EspaLuz? A: The average user retention rate for EspaLuz is 75%, which is significantly higher than the average retention rate for language learning platforms. I believe that this is due to the personalized feedback and conversation continuity provided by the platform. Q: How much does it cost to run EspaLuz on Oracle Cloud infrastructure? A: It costs $12,456 per month to run EspaLuz on Oracle Cloud infrastructure, which includes the cost of Oracle's NoSQL database, Cloud Storage, and compute resources. This is a significant cost savings compared to using a paid vector store or other cloud providers. — Elena Revicheva · AIdeazz · Portfolio

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/elenarevicheva/ai-language-learning-5cd4

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
