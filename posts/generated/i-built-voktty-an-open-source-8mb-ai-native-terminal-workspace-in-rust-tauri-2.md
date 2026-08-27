---
title: "I built Voktty: an open-source, ~8MB AI-native terminal workspace in Rust & Tauri 2"
slug: "i-built-voktty-an-open-source-8mb-ai-native-terminal-workspace-in-rust-tauri-2"
author: "Sergio Vargas"
source: "devto_ai"
published: "Thu, 27 Aug 2026 21:42:50 +0000"
description: "Like many developers, DevOps engineers, and sysadmins, my daily routine revolves around the terminal, remote servers, and containers. Over time, modern IDEs ..."
keywords: "terminal, voktty, native, your, rust, tauri, first, built"
generated: "2026-08-27T22:04:47.425121"
---

# I built Voktty: an open-source, ~8MB AI-native terminal workspace in Rust & Tauri 2

## Overview

Like many developers, DevOps engineers, and sysadmins, my daily routine revolves around the terminal, remote servers, and containers. Over time, modern IDEs have become increasingly resource-heavy, while standard terminals lack integrated AI context and modern workspace ergonomics. To solve this, I've been building Voktty : a lightweight (~7–8 MB), terminal-first development environment and AI-native workspace. It originated as an independent hard fork of Terax (originally created by Crynta) and has evolved into a dedicated, privacy-focused desktop application built with Tauri 2, Rust, React 19, and xterm.js WebGL . 🚀 Key Features GPU-Accelerated Terminal: High-performance WebGL rendering with split-pane multiplexing, command-aware blocks, and native shell integration (PowerShell, Bash, Zsh, Fish). Native MCP Client: First-class Model Context Protocol support. Connect local offline models via Ollama, LM Studio, or MLX , or use cloud APIs like Claude, OpenAI, and Gemini. Built-in Editor & Diagnostics: Lightweight CodeMirror 6 editor with opt-in LSP, DAP debugging, and AI-powered side-by-side diff reviews. Infrastructure Management: Native tabs and managers for SSH (with visual local/remote port tunnels), WSL , and Docker container lifecycles. Encrypted Live Sharing: Share host-controlled live terminal sessions with AES-256-GCM encryption without creating an account. 100% Privacy-First: Zero first-party telemetry, no mandatory accounts, and all API keys stored securely in your operating system keychain. 🛠️ The Tech Stack Core & Backend: Tauri 2, Rust, portable-pty Frontend: React 19, TypeScript, Vite, Tailwind CSS, shadcn/ui, Zustand Terminal & Editor: xterm.js (WebGL), CodeMirror 6 AI & Integration: Vercel AI SDK v6, native MCP client ⚠️ A Note on Platform Signing (Windows & macOS) Because Voktty is an independent, community-driven open-source project in its preview stage, builds do not yet carry paid Microsoft EV or Apple Developer certificates. As a result, Windows SmartScreen or macOS Gatekeeper may display an "Unverified Developer" warning upon installation. The entire source code is fully open and auditable on GitHub, and you can compile it locally with pnpm tauri build . Official certificates will be integrated as the project grows. 🤝 Looking for Contributors & Community Feedback Voktty is licensed under Apache-2.0 . I want to build this openly with the developer community and would love your help: Testers: Try it out in your daily terminal workflows and share your thoughts. Bug Reports & Feature Ideas: Let us know what shells, tools, or extensions you need. Contributors: PRs and collaborations in Rust, React 19, and TypeScript are warmly welcome! 🌐 Website: https://voktty.dev 💻 GitHub: https://github.com/voktty/voktty Drop a comment below with your feedback, suggestions, or terminal setup questions!

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/sergewinters/i-built-voktty-an-open-source-8mb-ai-native-terminal-workspace-in-rust-tauri-2-9p

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
