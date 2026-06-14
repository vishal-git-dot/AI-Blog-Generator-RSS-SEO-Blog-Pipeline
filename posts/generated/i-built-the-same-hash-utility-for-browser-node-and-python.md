---
title: "I Built the Same Hash Utility for Browser, Node, and Python"
slug: "i-built-the-same-hash-utility-for-browser-node-and-python"
author: "AltRepo"
source: "devto_python"
published: "Sun, 14 Jun 2026 08:51:03 +0000"
description: "Hashing text is easy until you try to make the same workflow feel clean across different environments. In the browser, you usually reach for the Web Crypto A..."
keywords: "hash, browser, node, altrepo, python, same, hashing, file"
generated: "2026-06-14T09:45:48.684410"
---

# I Built the Same Hash Utility for Browser, Node, and Python

## Overview

Hashing text is easy until you try to make the same workflow feel clean across different environments. In the browser, you usually reach for the Web Crypto API. For files, that means working with File or Blob objects and reading them as ArrayBuffer. In Node, file hashing usually means streams and the built-in crypto module. In Python, the same job usually goes through hashlib. None of that is complicated on its own. The annoying part is that the APIs are different enough that you end up rewriting the same small helpers over and over. That is why I made a small set of AltRepo hash utilities. For the browser, I have a local-first hash tool: AltRepo Text Hash Generator For JavaScript projects, I published: @altrepo /hash on npm For Python scripts, I published: altrepo-hash on PyPI The goal is simple: hash text, bytes, browser files, Node files, and Python files with a small predictable API. The browser version is useful when you just want to paste text and get a checksum without installing anything. The npm package is useful when you want the same kind of helper inside a JavaScript or TypeScript project. The Python package is useful for scripts, automation, and checksum verification. I also kept the packages small. The Python package uses the standard library. The JavaScript package separates browser and Node behavior so browser code does not pull in Node-only file APIs. That part matters because browser hashing and Node hashing are similar in purpose, but they are not the same implementation. Browser example: import { hashText } from " @altrepo /hash"; const digest = await hashText("hello", "SHA-256"); console.log(digest); Node file hashing uses the Node entry point: import { hashFile } from " @altrepo /hash/node"; const digest = await hashFile("archive.zip", "sha256"); console.log(digest); Python example: from altrepo_hash import hash_text print(hash_text("hello", algorithm="sha256")) I also made a couple of small examples here: GitHub hash repo JavaScript hash repo Browser file hash Gist The bigger idea behind AltRepo is to keep small utilities practical. Some tasks need a server. Hashing text or checking a local file usually does not. More AltRepo developer packages and demos: AltRepo Developer Packages

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/altrepo/i-built-the-same-hash-utility-for-browser-node-and-python-1546

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
