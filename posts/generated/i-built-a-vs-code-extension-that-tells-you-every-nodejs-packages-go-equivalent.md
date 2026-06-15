---
title: "I Built a VS Code Extension That Tells You Every Node.js Package's Go Equivalent"
slug: "i-built-a-vs-code-extension-that-tells-you-every-nodejs-packages-go-equivalent"
author: "Sagar Kashyap"
source: "devto_webdev"
published: "Mon, 15 Jun 2026 04:53:38 +0000"
description: "We've all been there. You're migrating a Node.js project to Go (or Rust, or Python — pick your poison), and you hit the first import : import express from ' ..."
keywords: "you, your, import, code, package, packagepal, express, what"
generated: "2026-06-15T05:01:58.096389"
---

# I Built a VS Code Extension That Tells You Every Node.js Package's Go Equivalent

## Overview

We've all been there. You're migrating a Node.js project to Go (or Rust, or Python — pick your poison), and you hit the first import : import express from ' express ' ; import axios from ' axios ' ; import jsonwebtoken from ' jsonwebtoken ' ; import bcrypt from ' bcrypt ' ; import sequelize from ' sequelize ' ; And now the real work begins: Googling every single package to find its equivalent in Go. "What's the Go equivalent of Express?" → Gin? Echo? Fiber? Chi? "What replaces Axios in Go?" → net/http? resty? req? "What's the Go bcrypt?" → golang.org/x/crypto/bcrypt? But wait, how do I import that? Multiply this by 30–50 packages in a real codebase and you've just burned an entire afternoon on Stack Overflow tabs. I got tired of it, so I built something PackagePal is a free VS Code extension that does one thing really well: Hover over any import → instantly see the top 3 equivalent packages in your target language. No browser tabs. No Googling. No context switching. Just hover. How it works (30-second version) Open any source file (JavaScript, Python, Go, Rust, Java, C++, Ruby, PHP, Swift, Kotlin — 13 languages supported) Set your target language (e.g., "Go") via the status bar Hover over any import statement PackagePal uses Gemini AI to find the top 3 equivalents with: 📦 Package name and description 💻 Ready-to-paste code snippet 📘 Direct link to official documentation That's it. No configuration files, no setup ceremony. A real example: migrating Express to Go Let's say you're converting a Node.js REST API to Go. Here's what happens when you hover over express : PackagePal shows you: # Go Equivalent Why 1 gin-gonic/gin Most popular, great middleware ecosystem, fast 2 labstack/echo Clean API, built-in middleware, good docs 3 gofiber/fiber Express-inspired syntax (easiest transition from Node) Each suggestion includes a code snippet showing how to set up a basic server — so you can immediately start coding instead of reading "Getting Started" guides. The sidebar: your migration dashboard Beyond hover, PackagePal has a sidebar explorer (click the 🚀 icon in your Activity Bar) that: Auto-scans every import in your current file Shows a tree view of every package and its equivalents Click to expand code snippets and documentation links It's like having a migration cheat sheet that updates itself as you work through your codebase. Why I built this I was migrating a personal project from Node.js/Express to Go last year. The actual code translation wasn't hard — Go's syntax is straightforward if you know any C-family language. The painful part was the dependency mapping . My package.json had 47 packages. For each one, I had to: Google "[package name] equivalent in Go" Compare 3–4 options on Reddit/GitHub Read the README to understand the API Write the import statement This took me two full days just to map dependencies — before writing a single line of Go. I figured: this should be one hover away, not a research project. The tech behind it PackagePal uses Google's Gemini AI (you bring your own free API key from Google AI Studio ) to generate context-aware suggestions. It's not a static lookup table — it understands: What the source package does (not just name matching) The ecosystem conventions of the target language Which alternatives are actively maintained in 2026 This means it works for niche packages too, not just the big ones. Your key, your control PackagePal uses a Bring Your Own Key (BYOK) model: Get a free Gemini API key (takes 30 seconds) The key is stored securely in VS Code's native Secret Storage Only package names are sent to the API — zero source code leaves your machine No accounts, no telemetry, no tracking. What languages are supported? Source / Target Languages JavaScript, TypeScript, Python, Go, Rust, Java, Kotlin, C#, C++, Ruby, PHP, Swift You can migrate in any direction — Python → Rust, Java → Go, Ruby → Python, whatever your project needs. Try it in 60 seconds Install PackagePal from the VS Code Marketplace Run Set Gemini API Key from the command palette (get a free key at aistudio.google.com ) Set your target language in the status bar Open any file with imports and hover That's it. If it saves you even one Google search, I'd love to hear about it in the comments 👇 What's next I'm actively working on: Workspace batch scan — scan all files in your project at once Migration reports — export a complete dependency mapping as a document Multi-model support — choice of AI models beyond Gemini If you have ideas or feedback, open an issue on GitHub or drop a comment below. Links: 🔗 VS Code Marketplace 🐙 GitHub 🌐 Website If PackagePal helps you, I'd really appreciate a ⭐ on the Marketplace — it helps other developers discover it!

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/sagar_kashyap_d20f1d5fa65/i-built-a-vs-code-extension-that-tells-you-every-nodejs-packages-go-equivalent-48o0

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
