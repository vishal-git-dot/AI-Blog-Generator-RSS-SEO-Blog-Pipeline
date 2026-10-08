---
title: "Your Offline Banner Fires on a Guess, and a VPN Can Flip It"
slug: "your-offline-banner-fires-on-a-guess-and-a-vpn-can-flip-it"
author: "Vladimir Elchinov"
source: "devto_webdev"
published: "Thu, 08 Oct 2026 12:59:50 +0000"
description: "Somewhere in most front ends there is a line like this: if ( ! navigator . onLine ) showOfflineBanner (); MDN's page for that property contains a sentence th..."
keywords: "not, your, you, online, status, whether, mdn, when"
generated: "2026-10-08T13:09:09.869779"
---

# Your Offline Banner Fires on a Guess, and a VPN Can Flip It

## Overview

Somewhere in most front ends there is a line like this: if ( ! navigator . onLine ) showOfflineBanner (); MDN's page for that property contains a sentence that should probably be in a larger font: Therefore, this property is inherently unreliable, and you should not disable features based on the online status, only provide hints when the user may seem offline. Not "be careful with". Do not disable features based on it. The reason is what it actually measures, which is not reachability. It fails in both directions, for documented reasons MDN names the mechanisms, and they are worth reading as two separate bugs rather than one caveat. It says true when nothing works. In MDN's words, "connection to LAN is considered online, even though the LAN may not have Internet access", and "the computer may be running a virtualization software that has virtual ethernet adapters that are always 'connected'". So a developer with Docker running, or anybody on a hotel wifi that has not been paid for yet, is online as far as the property is concerned. It says false when everything works. This is the one that will reach your inbox. Again from MDN: "On Windows, the online status is determined by whether it can reach a Microsoft home server, which may be blocked by firewalls or VPNs, even if the computer has Internet access." Read that again with your user base in mind. The browser decides whether your app is online by whether it can reach Microsoft . On a corporate network, behind a VPN that routes split-tunnel or a firewall that drops unrecognised destinations, that probe fails and the flag goes false while your API is perfectly reachable. If you disabled the save button on that flag, you disabled it for exactly the users who are on a managed laptop. The second thing people reach for is also a hint When onLine disappoints, the next stop is usually navigator.connection . It is worth knowing what that returns before building on it. Read from the machine I am writing this on, a desktop on wifi: { "onLine" : true , "effectiveType" : "4g" , "rtt" : 50 , "downlink" : 10 } effectiveType is "4g" on a wired-speed connection with no radio involved, because the label is a bucket for "fast", not a statement about the network type. The rtt and downlink figures are rounded into coarse steps on purpose, to make them less useful for fingerprinting. They are a hint about conditions, and nothing in them tells you whether your own API answers. The only honest check is a request you control There is exactly one way to know whether your app can reach your server, which is to ask your server: async function reachable ( timeoutMs = 3000 ) { const ctrl = new AbortController (); const timer = setTimeout (() => ctrl . abort (), timeoutMs ); const started = performance . now (); try { const res = await fetch ( " /health " , { method : " HEAD " , cache : " no-store " , signal : ctrl . signal }); return { ok : res . ok , status : res . status , ms : Math . round ( performance . now () - started ) }; } catch ( e ) { return { ok : false , status : e . name , ms : Math . round ( performance . now () - started ) }; } finally { clearTimeout ( timer ); } } cache: "no-store" is not decoration: without it a cached 200 will tell you the network is fine while it is down. The timeout matters because the interesting failure is not refusal, it is silence. Use navigator.onLine as MDN suggests, to decide whether it is worth asking at all, and never as the answer. And why this ends up in a ticket you cannot close Here is the shape of the report. "Your app kept telling me I had no internet. My internet was fine." That is unfalsifiable, and the reason is that the flag leaves no trace. It is a boolean with no provenance: nothing records which heuristic produced it, what the browser probed, whether it was a virtual adapter or a blocked reachability check. You cannot reproduce it either, because you are not behind their VPN and your machine is not running their endpoint protection. The fix for the ticket is the same as the fix for the code. If something is going to tell a user they are offline, record the evidence it decided on: the status and timing of a request you control, not the boolean. {"ok": false, "status": "AbortError", "ms": 3000} is a bug report. navigator.onLine === false is an opinion. Everything above is one instance of a thing worth generalising: when a browser API gives you a single boolean for a condition that has ten causes, the boolean is not evidence about any of them.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/session_replay/your-offline-banner-fires-on-a-guess-and-a-vpn-can-flip-it-5aaj

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
