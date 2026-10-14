---
title: "The Second Browser Tab Is Where Good Tests Go to Die"
slug: "the-second-browser-tab-is-where-good-tests-go-to-die"
author: "Simon Gerber"
source: "devto_webdev"
published: "Wed, 14 Oct 2026 21:11:57 +0000"
description: "The sign-in test passes locally. Then you run it in CI and the browser sits on a blank tab until the job times out. The application is fine. The identity pro..."
keywords: "test, window, browser, you, can, provider, login, when"
generated: "2026-10-14T21:28:09.488452"
---

# The Second Browser Tab Is Where Good Tests Go to Die

## Overview

The sign-in test passes locally. Then you run it in CI and the browser sits on a blank tab until the job times out. The application is fine. The identity provider is fine. The browser opened another window, and the automation is still trying to click a button in the first one. Welcome to one of the less glamorous parts of browser automation: keeping track of which browser context you're actually controlling. OAuth is easy until the provider changes the route Consider a typical third-party login: Click "Continue with Google". A popup opens on another origin. Enter credentials in the provider's window. The provider redirects or closes the popup. The original application receives the result and renders the signed-in state. It's tempting to automate that as a series of clicks. But the test really has two responsibilities: interact with the correct window during authentication, and prove that control returned to the app afterward. That distinction matters when the popup sometimes redirects inside itself and sometimes closes. A hardcoded assumption about the "second tab" can break as soon as a browser, account state, or provider configuration changes. The discussion in this guide to cross-origin popups, OAuth returns, and window-handle swaps is a useful reminder to follow window lifecycle events, not only tab positions. The wrong assertion can make a broken login look successful Here's a suspiciously common test: Click Sign in. Enter username and password. Click Continue. Assert that the login popup disappeared. Congratulations. You've verified that a popup disappeared. It might have closed because login succeeded. It might have crashed. It might have been blocked. The user might still be signed out. The assertion should live in the application: a signed-in session exists, the right account is shown, and a protected page behaves as expected. If the purpose of the test is specifically to inspect OAuth errors, that's a different scenario. This sounds obvious until you browse a test suite with 300 steps and discover that half of the "success" checks only verify that a modal closed. Tool choice matters, but not in the usual way Framework comparisons often start with syntax and speed. I care more about how visible the browser state is when something goes wrong. Can the test identify the new page or handle without guessing? Can it work across origins? Can it show you what happened in each window? Can the person debugging it understand the sequence without replaying the failure on their laptop? The Cypress vs WebdriverIO comparison explores some of the tradeoffs around browser control and debugging. The right choice depends on the flows you actually need to support, especially if your app relies on popups, multiple tabs, or external authentication. Don't decide based solely on the prettiest demo. Give both candidates the same annoying real-world login flow. Repeatable tests start with boring session hygiene A second issue often gets mixed up with window handling: test state leaks. The test opens with an already-authenticated cookie. Or the provider remembers the previous account. Or the registration email is already in use. Now the flow takes a different path from yesterday, and somebody labels it flaky. Before each run, define the desired starting state. Is this a first-time login or a returning user? Are cookies preserved intentionally? What happens to the user record afterward? If the test creates data, who deletes it? This evaluation guide to disposable test data and session resets asks a surprisingly valuable question: does the testing platform survive a rerun without someone manually cleaning up? A great first run followed by a broken second run is not a great test. Capture the handoff, not just the ending If a multi-window test fails, a screenshot of the last visible page is often insufficient. You want the sequence: Which window was active before the click? Which new window appeared, and when? What URL did each context reach? When was the original context restored? What did the application show after return? That's also why I find this multi-window testing benchmark plan more useful than a generic pass-rate comparison. It's interested in handoffs and the evidence left behind when they fail. You don't need a giant framework to think this way. Even a simple test can explicitly record the active context, verify the return, and reset its session. The irony is that a one-line login assertion can depend on five systems: your frontend, your backend, a browser, an identity provider, and the test runner's context management. When it fails, "add a sleep" is rarely the best investigative strategy.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/orbitpickle307/the-second-browser-tab-is-where-good-tests-go-to-die-13h2

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
