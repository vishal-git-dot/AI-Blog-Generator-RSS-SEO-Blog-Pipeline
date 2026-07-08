---
title: "I Built a React Error Boundary Lab (and Showed What They Can't Catch)"
slug: "i-built-a-react-error-boundary-lab-and-showed-what-they-cant-catch"
author: "Devanshu Biswas"
source: "devto_webdev"
published: "Wed, 08 Jul 2026 19:20:27 +0000"
description: "Without an error boundary, one component that throws during render unmounts your entire React tree — the dreaded blank white screen. Boundaries turn that int..."
keywords: "boundary, error, lab, catch, react, fallback, err, one"
generated: "2026-07-08T19:41:38.375732"
---

# I Built a React Error Boundary Lab (and Showed What They Can't Catch)

## Overview

Without an error boundary, one component that throws during render unmounts your entire React tree — the dreaded blank white screen. Boundaries turn that into a contained, recoverable fallback. So I built a lab where you crash things on purpose and watch how far the damage spreads (and doesn't). ▶ Live demo: https://error-boundary-lab.vercel.app/ Source (React 19): https://github.com/dev48v/error-boundary-lab The whole thing is a class component Error boundaries are the one corner of modern React that still must be a class — there's no hook equivalent for componentDidCatch : class ErrorBoundary extends Component { state = { err : null }; static getDerivedStateFromError ( err ) { return { err }; } // → switch to fallback UI componentDidCatch ( err , info ) { logToSentry ( err , info ); } // → report it render () { return this . state . err ? < Fallback /> : this . props . children ; } } getDerivedStateFromError flips the state that renders the fallback; componentDidCatch is your logging hook. Isolation is the point Crash one widget wrapped in its own boundary and it shows a fallback while its siblings keep working . Wrap independent regions — a sidebar, each route, a risky third-party widget — and one failure degrades gracefully instead of white-screening the app. The lab shows three isolated widgets; kill one, the other two are fine. Errors bubble to the nearest boundary, so nesting works how you'd hope: crash an inner widget and only the inner fallback appears — the outer content around it stays intact. The part that trips everyone up: what boundaries DON'T catch Boundaries only catch errors in render, lifecycle methods, and constructors of the tree below them. They do not catch: Event handlers — an onClick that throws. The boundary is never involved; use try/catch in the handler. Async code — setTimeout , promises, fetch().then() . The throw happens outside React's render pass. Server-side rendering. Errors thrown in the boundary itself (a parent boundary handles those). The lab has a live "throw in an onClick" button proving the boundary stays out of it — only the handler's own try/catch catches it. For async/handler errors you want surfaced in a boundary, the react-error-boundary library's useErrorBoundary() forwards them for you. Recovering To recover after a catch, change the boundary's resetKey (or remount it) so it re-renders its children — the lab's "reset" buttons do exactly that. If this made error boundaries click, a star helps others find it: https://github.com/dev48v/error-boundary-lab

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dev48v/i-built-a-react-error-boundary-lab-and-showed-what-they-cant-catch-84p

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
