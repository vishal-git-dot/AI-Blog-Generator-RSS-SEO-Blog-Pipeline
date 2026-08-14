---
title: "Readability in the age of AI-assisted programming"
slug: "readability-in-the-age-of-ai-assisted-programming"
author: "Alex Netkachov"
source: "devto_ai"
published: "Fri, 14 Aug 2026 13:05:31 +0000"
description: "With the recent shift toward AI-assisted programming, the readability of code has become even more important. AI agents can read and modify code much faster ..."
keywords: "code, rules, can, formatting, typescript, when, not, being"
generated: "2026-08-14T13:17:35.139852"
---

# Readability in the age of AI-assisted programming

## Overview

With the recent shift toward AI-assisted programming, the readability of code has become even more important. AI agents can read and modify code much faster than humans, but they are not as good at understanding the intent of the code. Adding human reviewers to the process can help, but given the volume of code being written, it is crucial to have code that is easy to read and understand. I'm working on a project that aims to improve the readability of TypeScript code. These are some of the problems that I have identified as making code less readable. Code does not fit in the editor Modern IDEs have a lot of features that are controlled from the IDE window. These controls occupy a lot of screen space, leaving less space for the code itself. This becomes worse when the IDE is used on a laptop or when source code control operations are performed, such as viewing diffs or resolving merge conflicts. A typical IDE window now has a file tree, a code editor, and an AI agent or chat panel. Additional tasks such as viewing diffs or resolving merge conflicts can result in the code editor being split into multiple panes, leaving very little space for the code itself. Diffs have unnecessary noise When code is modified, the diff shows all the changes made to the code. However, sometimes the changes are not directly related to the change being made, but are triggered by formatting rules. A method rename can change the line length, triggering formatting rules that alter code unrelated to the change being made. This can even change the indentation of large code blocks, making it difficult to understand the actual change being made. Code is too dense An important factor in readability is code density. Long lines with many statements and expressions are hard to read. When code is not spaced properly, it becomes difficult to identify control structures and understand the flow of the code. Formatting rules are too complex Developers writing or modifying code for others to read are generally willing to follow formatting rules. However, when the rules are too complex, they can be difficult to follow, resulting in inconsistent formatting, frustration, and lost productivity. Formatting is inconsistent When code structures are formatted in different styles, it becomes difficult to identify control structures and understand the flow of the code. This can be caused either by a lack of formatting rules or by rules that are not deterministic (i.e., the same code structure can be formatted in different ways). Solutions There are common solutions and mitigation actions that can be taken to address these problems: Use an automatic code formatter that is deterministic, consistent, and has simple formatting rules. There are plenty of these tools, so automation itself is not a problem. However, designing a set of rules that is simple, deterministic, and consistent is a challenge. Use a code linter that can detect and report code that is too complex, such as long statements, too many nested structures, or too many parameters. Again, there are plenty of these tools, but designing a set of rules for a particular project or team is still a challenge. Review the code manually, especially when the code is being modified. This can be done by peers or by AI agents, but it is important to have an experienced human in the loop to ensure that the code is readable and understandable. I've started with the first step, which is to design a set of formatting rules for TypeScript and implement them in a code formatter: sfmt . I'm building it by studying popular formatting tools and linters for TypeScript and adding custom rules on top of them. Some of the tools that I have learned from are: Oxfmt - performant formatter for TypeScript and JavaScript. Oxlint - a linter for TypeScript and JavaScript. Prettier - an opinionated code formatter for many languages, including TypeScript and JavaScript. dprint - a pluggable and configurable code formatting platform for many languages, including TypeScript and JavaScript. Biome - a code formatter and linter for many languages, including TypeScript and JavaScript. ESLint - a pluggable and configurable linter tool. If you are interested in this project, please check it out and provide feedback or subscribe for updates. If you prefer to follow along and want to support the project, I would appreciate a star on GitHub .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/alex_netkachov_5306c2df5d/readability-in-the-age-of-ai-assisted-programming-4b35

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
