---
title: "Playwright 1.64 adds WebMCP. What changes for your tests?"
slug: "playwright-164-adds-webmcp-what-changes-for-your-tests"
author: "Anton Gulin"
source: "devto_webdev"
published: "Sat, 17 Oct 2026 15:01:14 +0000"
description: "Originally published on anton.qa . This release matters when your website offers actions for AI agents to call. WebMCP lets a page offer those actions. Playw..."
keywords: "page, tool, your, webmcp, check, frame, browser, application"
generated: "2026-10-17T15:18:37.848972"
---

# Playwright 1.64 adds WebMCP. What changes for your tests?

## Overview

Originally published on anton.qa . This release matters when your website offers actions for AI agents to call. WebMCP lets a page offer those actions. Playwright 1.64 adds experimental support for listing and calling them. If your website offers no WebMCP actions, there are none to test yet. If your team is adding them, you can check them alongside the normal page journey. Keep your normal browser tests. The extra checks concern what these website actions return and change. A delivery-date example Imagine your website offers AI an action to find an order's delivery date. A tool is the callable action your website provides. Suppose test order 1043 has a saved delivery date of October 16. Call the lookup with that order number. Compare the reply with the saved date, and confirm the records stayed unchanged. This is an illustrative example, not a recorded test run. Your website must register the action, and your browser needs WebMCP enabled. Start with a supported page and browser Your application must register tools through the browser's experimental WebMCP interface. The browser also needs WebMCP enabled. Chromium needs --enable-features=WebMCP when the browser starts. Firefox needs both dom.modelcontext.enabled and dom.modelcontext.testing.enabled preferences. WebKit does not implement the feature. The Playwright API calls the main frame's instance page.webmcp . A frame is one page area with its own content. A tool inside a child frame belongs to that frame's frame.webmcp instance. Choose the frame that actually registers the tool. These prerequisites matter before you diagnose a missing tool. A page without registered tools does not establish that your test setup failed. An empty list can be correct for a page without tools. List what the page offers tools() returns tools currently registered in the chosen frame. Compare the names with the actions your application intended to offer. Check the description and input shape too. An input schema describes the values a tool expects. The page supplies names, descriptions, input rules, and annotations, which are hints about behavior. Treat those page-provided details as untrusted input. An annotation saying an action is read-only is a page-provided hint. It does not prove the action cannot change data. If a tool is missing, first check the chosen frame and registration timing. Then check whether your application registered it. tools() can also throw when the browser lacks WebMCP support. Call one tool and check its effect callTool() invokes a named tool in the chosen frame. Select an action with a known expected result in your own application. Supply the input that matches its schema. The call returns the result supplied by the page's tool. Check both the returned content and the application result. For our order lookup, compare the reply with the known delivery date. For an update, read the saved record after the call. Check the intended change and confirm other records stayed unchanged. Follow the app's documented save timing. A returned value only tells you that the tool answered. It does not prove the answer is correct or the update persisted. Use a controlled record for actions that change data. Keep purchases and customer notifications outside this check. A callback is the code that runs the tool. Situation to exercise What Playwright exposes What the tester should check Valid tool and input The page's returned result Expected content and the relevant application state Tool returns isError: true A returned error result The reported failure and whether state stayed as expected Name is not registered An exception, a reported execution failure The intended registration and the reported failure Tool's callback throws An exception, a reported execution failure The reported failure and resulting application state The last two cases both fail through an exception. That failure alone does not identify its cause. Inspect the registered names and the controlled failure you exercised. Keep the normal page journey A page-tool check tells you what an AI-facing action reports and changes. It does not replace a person's normal browser journey. Keep tests for visible controls, messages, and the complete user task. Those checks answer a different question: can a person finish the task through the page? A short review list For your own tool-enabled page, ask: Which frame registers the tool, and is WebMCP enabled in this browser? Does tools() show the expected action and input shape? Does callTool() return the expected content for a known input? Does the application state match that result? What happens for a returned error, an unknown name, and a callback failure? Do normal page controls still support the user's task? That list gives you a practical starting point for Playwright 1.64. Adapt each expected result to your application's actual contract. I'm Anton. I build AI tools and measure how fast they really run. Former Apple engineer. I make ollamatps.com and write about building and measuring AI at anton.qa .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/aiwithanton/playwright-164-adds-webmcp-what-changes-for-your-tests-35gl

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
