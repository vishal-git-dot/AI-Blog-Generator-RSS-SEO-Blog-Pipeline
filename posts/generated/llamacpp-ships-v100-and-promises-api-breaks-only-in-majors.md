---
title: "llama.cpp ships v1.0.0 and promises API breaks only in majors"
slug: "llamacpp-ships-v100-and-promises-api-breaks-only-in-majors"
author: "Mikhail Savchenko"
source: "devto_ai"
published: "Sat, 14 Nov 2026 05:44:58 +0000"
description: "The ggml-org team announced llama.cpp v1.0.0 on Hugging Face, releasing the llama.cpp library (libllama) and the underlying ggml tensor library (libggml) as ..."
keywords: "team, api, llama, cpp, change, major, linux, macos"
generated: "2026-11-14T05:48:05.831806"
---

# llama.cpp ships v1.0.0 and promises API breaks only in majors

## Overview

The ggml-org team announced llama.cpp v1.0.0 on Hugging Face, releasing the llama.cpp library (libllama) and the underlying ggml tensor library (libggml) as 1.0.0 at the same time. The project is about three and a half years old, and the team says many downstream applications now depend on it. What the version number now means The headline change is a commitment about compatibility. Both projects will signal API and ABI incompatibilities through a major-version bump. The team lays out the rules for all its projects that use semantic versioning: Major: a breaking change to the public C API in the include directory. Minor: a backward-compatible feature, backend update, model support or API addition. Patch: a bug fix with no API change. The team says it will be stricter about making these boundaries visible as adoption grows. Distribution The post lists the channels through which the software is distributed: Pre-release artifacts for Linux, macOS, Windows, Android and iOS. Docker images for Linux. Debian packages. Homebrew for macOS and Linux. conda-forge for Windows, macOS and Linux. MacPorts and Winget. An XCFramework for iOS and macOS. The team also points packagers to a discussion thread on how to add the projects to their own release pipelines. Development and coverage The team says it uses LLMs in its own development in a measured way, while keeping control of the architecture. It is investing in CI infrastructure, using Hugging Face's HF Buckets and HF Jobs for capacity, and adding self-hosted runners across major hardware platforms with support from NVIDIA, AMD, Qualcomm, Arm, IBM and Intel. On models, llama.cpp currently supports more than 150 architecture variants and all mainstream speculative decoding methods. Hardware support comes through ggml backends, each of which can be compiled as a dynamic library and loaded at runtime. What is not in the announcement The post does not describe new model capabilities or performance figures, and it gives no timeline for a future major release. The change is about predictability for the people who build on the libraries.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/mikefluff/llamacpp-ships-v100-and-promises-api-breaks-only-in-majors-2k99

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
