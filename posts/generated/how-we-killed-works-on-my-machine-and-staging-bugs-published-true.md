---
title: "How we killed "works on my machine" and staging bugs published: true"
slug: "how-we-killed-works-on-my-machine-and-staging-bugs-published-true"
author: "Proxyceptor"
source: "devto_webdev"
published: "Sun, 27 Sep 2026 11:36:48 +0000"
description: "TL;DR We replaced Charles Proxy + manual SSL cert installs with an in-app JS interceptor (Proxyceptor / SuperDebug SDK) for mocking API responses, simulating..."
keywords: "you, request, proxy, app, response, staging, rewrite, cdn"
generated: "2026-09-27T11:46:32.762002"
---

# How we killed "works on my machine" and staging bugs published: true

## Overview

TL;DR We replaced Charles Proxy + manual SSL cert installs with an in-app JS interceptor (Proxyceptor / SuperDebug SDK) for mocking API responses, simulating latency, and rewriting URLs on Smart TVs, staging builds, and browsers — without touching certificates or proxy configs. Rules live in a shared cloud workspace instead of local rewrite files. The problem If you've built anything that ships to Smart TVs (Android TV, Fire TV, Tizen, webOS), you know this loop: QA finds a bug on a TV in the office You ask "can you send me the network logs?" There are no network logs, because getting a proxy cert onto a TV means digging through developer settings, sideloading a cert, and praying the manufacturer didn't lock it down Two hours later you still don't have a repro Even on web, the standard fix — Charles Proxy or mitmproxy — has friction: every teammate installs their own root cert, exports their own rewrite rules, and nobody's config matches anyone else's. What we switched to Instead of a system-level MITM proxy, we're now using an SDK that patches fetch , XHR , and sendBeacon directly inside the app's JS runtime (or Chrome's declarativeNetRequest API for the browser extension). No certificate, no OS trust store, no VPN profile. Setup is one script tag: <script src= "https://proxytea.com/superdebug.min.js" ></script> <script> window . superDebugObj = SuperDebug . init ({ apiKey : ' sdm_live_qa_team_key ' , enableProxy : true , showUI : true }); </script> Zero build step. Works the same whether it's dropped into a React/Vue/Next.js web app or a Smart TV app's index.html. What you can actually do with it Rules fall into three buckets: Request modify URL rewrite (e.g. point a video player's .m3u8 manifest request from prod CDN to a staging CDN, no rebuild) JSON body deep-merge Header injection Response modify Full mock response body Deep-merge a partial mock into a real response Run an arbitrary JS transform on the response Header rewrite (CORS, cache-control) Performance modify Inject artificial latency Drop the request entirely Flip the HTTP status code Example: rerouting a live stream request without touching the TV app build — // original request { "stream_origin" : "https://cdn.streampulse.io" , "manifest" : "/live/match-hd-1080p.m3u8" , "drm_profile" : "widevine_prod_v4" , "environment" : "production" } // intercepted + rewritten via URL rule: *.m 3 u 8 -> staging-cdn.internal { "stream_origin" : "https://staging-cdn.internal" , "manifest" : "/test-match-drm.m3u8" , "drm_profile" : "widevine_staging_test_keys" , "environment" : "staging_qa" } The rewrite happens before the request leaves the device — no cert needed on the TV at all. The part that actually changed our workflow Individually, request/response mocking isn't new Charles Proxy does all of this too. What's different is that rules are defined once, in a cloud workspace dashboard, and every device with the SDK installed picks them up automatically. No exporting .chlsj files around Slack. Practical effect: our QA lead can toggle "return 500 on checkout" once, and it's live for every tester on every device in the same second. Nobody's debugging why their local rule set is stale. It also means non-engineers can drive it. The dashboard is form-based pick a URL pattern, choose "return 500" or paste a mock body, toggle it on. No CLI required. Things worth checking before you adopt something like this Any tool intercepting live traffic deserves scrutiny, so a couple of things we verified: Where does the data go? Interception/modification happens client-side. Only rule definitions (URL patterns, mock JSON) sync to the cloud — not actual request/response bodies. What happens when a rule is broken? A malformed mock or a rule that throws is caught, logged as a warning, and the SDK falls back to the original unmodified request. It doesn't take the page down. When this isn't the right tool If you need packet-level inspection, need to intercept traffic outside a browser/app JS context (e.g. a native binary making raw socket calls), or need to see genuinely at the network layer rather than the application layer, you still want a real proxy — Charles, mitmproxy, or similar. This is a complement to that stack for the specific case of app-level request/response manipulation across a team, not a wholesale replacement. Result For our specific pain QA needing to simulate API failures and CDN swaps on Smart TVs and staging without engineering hand-holding — this cut the certificate setup step to zero and turned "can you fake this scenario for me" into something QA does themselves in under a minute. If your team is still exporting Charles rewrite files over Slack, it's worth fifteen minutes to try the alternative.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/proxyceptor/how-we-killed-works-on-my-machine-and-staging-bugspublished-true-hjp

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
