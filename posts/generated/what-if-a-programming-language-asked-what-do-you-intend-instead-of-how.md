---
title: "What if a programming language asked 'What do you intend?' instead of 'How?'"
slug: "what-if-a-programming-language-asked-what-do-you-intend-instead-of-how"
author: "Art"
source: "devto_ai"
published: "Tue, 27 Oct 2026 17:30:05 +0000"
description: "Most programming languages ask you a question before you've even started: How? How do I allocate this window? How do I register this callback? How do I keep ..."
keywords: "you, what, how, sml, sms, language, button, small"
generated: "2026-10-27T17:47:39.002983"
---

# What if a programming language asked 'What do you intend?' instead of 'How?'

## Overview

Most programming languages ask you a question before you've even started: How? How do I allocate this window? How do I register this callback? How do I keep the button and the label in sync? How do I build, package, sign and ship it? I've been building a language that asks something else first: What do you intend? It's called ForgeIL , short for Intention Language. It's part of Forge4D , an open-source project I've been working on, and it's very much early-stage. Let me show you what I mean, and then I'd really like to hear where you think it's wrong. Describing instead of instructing Say you want a small app: a window, a greeting, a button. When the button is pressed, the greeting changes. That sentence is already the whole program. Everything else is translation. In ForgeIL you write down what is there: Window { id : mainWindow title : " Hello " size : 480 , 320 VBoxContainer { anchors : left | top | right | bottom Label { id : greeting text : " Hello, Forge! " } Button { id : btnHello text : " Say hello " } } } And you write down what should happen: on btnHello . clicked () { greeting . text = " Hello again! " } No framework imports, no subclassing, no lifecycle methods, no listener wiring. You describe the structure and the reaction; a runtime handles the how. Two halves, on purpose ForgeIL consists of two deliberately different languages: Half Answers File Example SML (Simple Markup Language) What is there? .sml Button { id: save text: "Save" } SMS (Simple Multiplatform Script) What should happen? .sms on save.clicked() { … } SML has no logic at all: no loops, no conditions, no variables. Only things and their properties. SMS handles behaviour: variables, functions, decisions, and above all events. Its syntax is small and borrows from Kotlin. A screen is usually a pair of files with the same name, main.sml and main.sms , and the runtime wires them together by id. Why not one language? Structure changes slowly, behaviour changes often. A designer can rearrange the whole layout without touching a line of script, as long as the ids stay. Structure can be checked before anything runs. An unknown property is a warning, not a crash. Regular structure is easy for machines to write. SML is so uniform that an AI model can generate it reliably. That's by design, and it's the part I'm most curious about (more below). Behaviour stays small. The script doesn't build the UI, so it only contains actual logic. A typical screen is a few dozen lines. What the runtime does You don't compile, link or package by hand while developing. The Forge Runner builds the native UI from SML (macOS, Linux, Android) and compiles SMS straight to native machine code via LLVM. No VM, no garbage collector. When the app is ready, the same project builds into a .app or .apk with the runner inside. Honest status This is an early edition. Part I of the accompanying book is complete and every example in it runs in the current runner. While writing Part III, I found parts of SMS that the native compiler doesn't handle correctly yet, so I'm fixing the compiler first and the chapters on SML and SMS will follow. I'd rather tell you that now than have you find out. It's all GPL 3.0 or later, with a commercial license for companies that only want to take, close and sell. Prior art, and what's different "Intention" as a programming concept isn't new. Charles Simonyi's Intentional Programming at Microsoft Research in the 90s stored programs as trees of intentions, independent of syntax. The difference I'm betting on is that today an AI can do the translation from intent to implementation, and that a strict, small, regular language gives that AI (and the human) something precise to target, instead of free-form prompts. Where I'd love your opinion Is a hard split between structure (no logic) and behaviour a feature or a limitation? Where did similar splits hurt you (think XAML, QML, HTML and JS)? If AI writes more and more code, should we design languages for being reliably generated (small, regular, checkable) rather than for human cleverness? Is "native, no GC" the right call for UI scripting, or an unnecessary constraint? What would make you try something like this? What would make you close the tab? Code and docs: Forge4D on Codeberg · The book https://crowdbooks.crowdware.info/books/forge4d-c2c815

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/artanidos/what-if-a-programming-language-asked-what-do-you-intend-instead-of-how-22j2

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
