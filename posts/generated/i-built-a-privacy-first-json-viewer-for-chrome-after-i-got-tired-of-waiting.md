---
title: "I built a privacy-first JSON viewer for Chrome after I got tired of waiting"
slug: "i-built-a-privacy-first-json-viewer-for-chrome-after-i-got-tired-of-waiting"
author: "Connor LeeBo"
source: "devto_webdev"
published: "Mon, 08 Jun 2026 04:24:41 +0000"
description: "A few months ago, like many devs, I noticed something off about the JSON viewer extension I'd been using for years. It had been quietly updated. The code wen..."
keywords: "json, you, viewer, extension, yaml, had, user, privacy"
generated: "2026-06-08T04:42:39.222474"
---

# I built a privacy-first JSON viewer for Chrome after I got tired of waiting

## Overview

A few months ago, like many devs, I noticed something off about the JSON viewer extension I'd been using for years. It had been quietly updated. The code went closed-source. Donation popups started appearing on unrelated pages including, in some reports, users' checkout pages. The maintainer had moved on, and the new owners had different priorities than "view JSON." I uninstalled it. Then I went looking for an alternative. The replacement options I found had their own problems. Some required <all_urls> permissions to do something that should only need access to the current tab. Some hadn't been updated in three years and choked on any JSON file over 5MB. Some quietly phoned home for "telemetry." So I built my own. It took longer than I expected. Here's what I learned. The trust pitch had to be the architecture I didn't want "trust me, bro" privacy. I wanted privacy you could verify by reading the manifest. The whole product reduces to three permissions: activeTab — only when the user explicitly clicks the toolbar icon scripting — to inject the viewer into the current tab storage — to remember the user's light/dark theme preference (and only that) That's it. No <all_urls> , no tabs , no cookies , no webRequest , no background page watching anything. The extension literally cannot read pages you don't gesture on, because Chrome's permission model won't let it. I also vendored every dependency. The only third-party code is js-yaml (MIT licensed, unmodified, copied into /vendor ). There are zero CDN imports, zero eval() , zero new Function() , zero remote scripts. What you install is exactly what runs. You can verify this with grep -r "fetch\|XMLHttpRequest" . and find nothing. Real-world files broke everything Most JSON viewer extensions render the tree with synchronous DOM manipulation. Drop a 10MB JSON file in and the tab freezes for 30+ seconds. The user thinks the browser crashed. I tested this with a synthetic 10MB file containing 17,000 records. The first version of my viewer froze the tab for 22 seconds. Unacceptable. The fix was lazy rendering. Top-level structure renders immediately with collapsed children. Subtrees only render when the user expands a node. A small progress bar shows the parsing/initial-render percentage so the user knows the extension is alive. This took two rewrites of the rendering code to get right. The trick was treating the JSON not as a tree to render, but as a tree to navigate . You don't need to draw 17,000 records up front — you need to be ready to draw any one of them on click. YAML and XML support, for real workflows If you've ever debugged a Kubernetes config, you know that scrolling through 400 lines of indented YAML is a special kind of pain. I added YAML support next, parsed with js-yaml. Now Kubernetes manifests, GitHub Actions workflows, Docker Compose files — anything served as text/yaml — renders as a collapsible tree. XML came after that, using the browser's native DOMParser. It works on local XML files via Chrome's built-in file viewer too — that was a fun rabbit hole I had to dive into. The do-no-harm rule One thing I hated about the old JSON viewers: if they couldn't parse a page, sometimes they'd still try to transform it, and you'd end up with a destroyed view of whatever was actually there. My rule: if the content isn't valid JSON, YAML, XML, or JSONP, the extension does nothing . A small toast tells the user why, and the original Chrome rendering of the page is preserved exactly. No blank screens. No destroyed content. Lessons for any indie extension developer Three things I'd tell my past self: 1. Permissions are your trust pitch. Users who care about privacy will read your manifest. Asking for less is worth more than any marketing copy. 2. Test with real-world data, not toy examples. A 50-line sample JSON file tells you nothing about whether your extension survives a real API response. 3. Open-source the whole thing, MIT licensed, with no build step. Auditability is a feature. Make it possible to verify your claims by reading the code, not by trusting a privacy policy. The extension It's called JSON Viewer · Open Source · No Tracking . Chrome Web Store: https://chromewebstore.google.com/detail/jljkcfhlbilhnhidghiepnbamhdjnpjf GitHub: https://github.com/connorleebo/json-viewer-extension MIT licensed, audit-able, no telemetry, no analytics If you've been waiting for a clean replacement, this is the one. If you've already found one, I'd love to hear which.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/connorleebo/i-built-a-privacy-first-json-viewer-for-chrome-after-i-got-tired-of-waiting-34jf

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
