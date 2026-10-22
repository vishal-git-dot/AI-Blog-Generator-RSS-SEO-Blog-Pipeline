---
title: "Jev: what it's for and how to use it"
slug: "jev-what-its-for-and-how-to-use-it"
author: "Ilia"
source: "devto_python"
published: "Thu, 22 Oct 2026 10:54:38 +0000"
description: "A message arrives in a chat: “How can I enable notifications for new orders only?” The application needs to assign it a category: “question”, “advertising”, ..."
keywords: "message, question, can, advertising, your, choice, probability, answer"
generated: "2026-10-22T11:30:26.385299"
---

# Jev: what it's for and how to use it

## Overview

A message arrives in a chat: “How can I enable notifications for new orders only?” The application needs to assign it a category: “question”, “advertising”, or “other”. The category determines what happens next. Jev from TypeSafe AI takes data and typed questions, then returns values your code can use: a label, a score on a scale, or the probability of a “yes” answer. General LLMs also support structured outputs, so you can build a similar workflow with them. Jev is worth considering when you want an API contract built around decisions: probabilities across predefined options and independent questions about the same data in one call. Your application gets both a result and probability estimates it can use to choose its next action. This walkthrough follows the API documentation as of October 22, 2026. I haven't called the service or tested its probability calibration, accuracy, or speed for this article. A category, a scale, or a yes/no question Three question types are useful for text tasks. Choice selects one option from a set, such as “question”, “advertising”, or “other” for a chat message. You could also classify a support request by topic and route it to the right handler: billing, shipping, or returns. The categories have no inherent order. Score rates text against ordered levels. For a support queue, you could describe urgency as “can wait”, “disrupts work, but a workaround exists”, and “work has stopped”. Those three levels occupy positions 0 through 2. The resulting score can fall between levels, so it may be fractional. It represents a position on the scale you described. Noul returns the probability of a “yes” answer as a number from 0 to 1. For example, you could ask whether a comment contains personal data or whether a customer wants to speak to a person. This signal can help with moderation or a handoff to a human agent; your application sets the threshold for taking action. In one call, you could use Choice to classify a message and Noul to check whether it contains personal data. The application gets both a category and an additional signal for review. Each question is evaluated independently: the second does not receive the first one's answer. Your code needs to handle any dependencies between decisions. Your first request: classify a message We'll use Choice with the categories “question”, “advertising”, and “other”. The instructions will define a rule for mixed cases: if a promotional message contains a question, classify it as advertising. The quickstart requires Python 3.10 or later and the official typesafe-sdk package. Get an API key from the TypeSafe console and set the TYPESAFE_API_KEY environment variable. In a POSIX shell: python3 -m pip install typesafe-sdk export TYPESAFE_API_KEY = "your-api-key" Save the following code as classify_message.py . The client reads the key from the environment. Following the documentation's example, jev-latest selects the current model without pinning a version. from typesafe_sdk import Choice , TypeSafeClient message = " How can I enable notifications for new orders only? " with TypeSafeClient ( model = " jev-latest " ) as client : response = client . system_one ( state = message , questions = { " message_type " : Choice ( instructions = ( " Classify this chat message. " " If a promotional message contains a question, choose advertising. " ), criteria = { " question " : " A request for help or information without advertising " , " advertising " : " Promotion of a product, service, or external channel " , " other " : " Neither advertising nor a request for help or information " , }, ), }, ) answer = response . choices [ " message_type " ] print ( " Label: " , answer . choice ) print ( " Probabilities: " , answer . probabilities ) print ( " Confidence: " , answer . confidence ) Run python3 classify_message.py in the same shell session. state contains the text to evaluate. It can also hold structured data, such as a message together with the chat's rules. In questions , the message_type identifier links the question to its answer, instructions defines the task, and criteria describes the categories. The Python SDK makes Choice answers available through response.choices . The .choice field holds the label with the highest probability; .probabilities holds the distribution across the options. If “question” and “advertising” have similar probabilities, your application can send the message for review even though one label has technically won. The distribution lets your code account for that ambiguity when choosing an action. For Choice, confidence is calculated from the highest probability, adjusted for the number of options. A uniform distribution gives 0; assigning all probability to one option gives 1. It is a separate measure from the probability of the selected label. Even a high value does not guarantee that the model understood the message correctly. Jev fits application steps that turn text into a predefined decision: choosing a handler, setting priorities, or flagging a message for a moderator. After classification, a message labeled as a question can go to a bot that drafts a reply. Generating a detailed response or doing extended reasoning requires a separate step; Jev sits between the input data and your code's next action.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/aetseihe/jev-what-its-for-and-how-to-use-it-3iem

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
