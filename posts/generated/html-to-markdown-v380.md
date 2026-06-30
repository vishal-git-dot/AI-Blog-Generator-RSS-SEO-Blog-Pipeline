---
title: "html-to-markdown v3.8.0"
slug: "html-to-markdown-v380"
author: "Khalid Hussein"
source: "devto_webdev"
published: "Tue, 30 Jun 2026 03:58:34 +0000"
description: "TL;DR Package rebrand. Every published identifier moves from kreuzberg -namespaced to xberg -namespaced — npm, Maven, NuGet, Homebrew tap, GitHub org. See th..."
keywords: "html, markdown, xberg, kreuzberg, install, package, node, tap"
generated: "2026-06-30T04:06:54.983862"
---

# html-to-markdown v3.8.0

## Overview

TL;DR Package rebrand. Every published identifier moves from kreuzberg -namespaced to xberg -namespaced — npm, Maven, NuGet, Homebrew tap, GitHub org. See the migration table. Node binding consolidated. The separate -node package and TypeScript wrapper under packages/typescript/ are removed; the NAPI-RS crate now ships directly as @xberg-io/html-to-markdown . PHP install path changed. Use pie install xberg-io/html-to-markdown — composer require cannot load a native ext-php-rs extension. What Is html-to-markdown? html-to-markdown is a CommonMark-compliant HTML→Markdown converter with a Rust core, maintained by the Xberg team. It exposes a single consistent API across 14 language bindings and ships as a CLI, a library, and an MCP server. What Changed in v3.8.0 v3.8.0 promotes v3.8.0-rc.2 and is a rebrand + package consolidation release. The converter's behavior, output format, and core API are unchanged. Package identity rebrand: Kreuzberg → Xberg Every published artifact identifier has moved: Artifact Old New npm (Node) @kreuzberg/html-to-markdown-node @xberg-io/html-to-markdown npm (WASM) @kreuzberg/html-to-markdown-wasm @xberg-io/html-to-markdown-wasm npm (CLI) @kreuzberg/html-to-markdown-cli @xberg-io/html-to-markdown-cli Maven groupId dev.kreuzberg io.xberg Maven artifactId html-to-markdown html-to-markdown (groupId only changes) JNI symbols Java_dev_kreuzberg_android_… Java_io_xberg_android_… NuGet KreuzbergDev.HtmlToMarkdown XbergIo.HtmlToMarkdown Homebrew tap kreuzberg-dev/homebrew-tap xberg-io/homebrew-tap GitHub org github.com/kreuzberg-dev github.com/xberg-io Node binding consolidation The separate -node wrapper package and the TypeScript layer under packages/typescript/ are removed. The NAPI-RS crate now ships directly as @xberg-io/html-to-markdown , with platform packages named @xberg-io/html-to-markdown-<platform> . If you were importing from the old wrapper, update to the direct package — the API surface is the same. Swift publish branch fix The same fix applied to Crawlberg v1.0.0 lands here: the publish workflow now creates the release/swift/3.8.0 branch carrying the substituted XCFramework checksum. SwiftPM packages that pin via .package(url: …, branch: "release/swift/<version>") will now resolve correctly. Migration Guide 1. Update package declarations # Node.js — was @kreuzberg/html-to-markdown-node npm install @xberg-io/html-to-markdown # WASM — was @kreuzberg/html-to-markdown-wasm npm install @xberg-io/html-to-markdown-wasm # PHP — was composer require kreuzberg/html-to-markdown pie install xberg-io/html-to-markdown <!-- Java/Kotlin — groupId changes --> <dependency> <groupId> io.xberg </groupId> <artifactId> html-to-markdown </artifactId> <version> 3.8.0 </version> </dependency> # C# — was KreuzbergDev.HtmlToMarkdown dotnet add package XbergIo.HtmlToMarkdown 2. PHP: switch from composer require to pie install composer require cannot install a native ext-php-rs extension. Any existing install instructions using composer require kreuzberg/html-to-markdown will silently fail to load the extension. Use PIE: pie install xberg-io/html-to-markdown 3. Update Homebrew tap brew untap kreuzberg-dev/homebrew-tap brew tap xberg-io/homebrew-tap brew install html-to-markdown Verification checklist [ ] html-to-markdown --version prints 3.8.0 [ ] Node import from @xberg-io/html-to-markdown resolves [ ] PHP extension loads ( php -m | grep html_to_markdown ) [ ] Swift package resolves via SPM What Else Is in Recent Releases v3.8.0 carries no new conversion features. The last substantive feature release was v3.7.0 , which expanded the MCP server to full API parity: a typed ConvertConfig object covering every ConversionOptions field, a new extract_metadata tool returning structured Open Graph / JSON-LD / Twitter Card metadata as JSON, and MCP prompts, resources, and completions capabilities. If you are integrating html-to-markdown into an AI agent pipeline, the MCP server is production-ready as of 3.7.0. Learn more Release : github.com/xberg-io/html-to-markdown/releases/tag/v3.8.0 Repository : github.com/xberg-io/html-to-markdown Documentation : docs.html-to-markdown.xberg.io Getting started : pip install html-to-markdown · npm install @xberg-io/html-to-markdown · cargo add html-to-markdown

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/xberg-io/html-to-markdown-v380-4k83

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
