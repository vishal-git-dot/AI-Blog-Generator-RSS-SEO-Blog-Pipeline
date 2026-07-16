---
title: "Phone Not Vibrating? A 10-Second Browser Check Tells You If the Motor Is Dead"
slug: "phone-not-vibrating-a-10-second-browser-check-tells-you-if-the-motor-is-dead"
author: "keyboardTester.Click"
source: "devto_webdev"
published: "Thu, 16 Jul 2026 13:44:19 +0000"
description: "This is a cross-post of a guide I originally published on KeyboardTester.click: Phone Not Vibrating? Test Your Vibration Motor and Fix It . When a phone stop..."
keywords: "vibration, motor, test, repair, vibrate, not, you, one"
generated: "2026-07-16T14:05:41.530198"
---

# Phone Not Vibrating? A 10-Second Browser Check Tells You If the Motor Is Dead

## Overview

This is a cross-post of a guide I originally published on KeyboardTester.click: Phone Not Vibrating? Test Your Vibration Motor and Fix It . When a phone stops vibrating, almost everyone guesses. Is it a setting? Is the motor dead? Do I need a repair? You can stop guessing in about ten seconds — and the trick is a browser API most web developers already know. The fork: settings vs a dead motor The Web Vibration API exposes a single function: // A 200 ms buzz navigator . vibrate ( 200 ); // A pattern: vibrate 100 ms, pause 50 ms, vibrate 100 ms navigator . vibrate ([ 100 , 50 , 100 ]); // Cancel any ongoing vibration navigator . vibrate ( 0 ); That call asks the operating system to fire the vibration motor directly , skipping your ringtone, Do Not Disturb, and per-app notification layers. So the result is clean evidence about the hardware itself: It buzzes → the motor physically works. Your problem is a setting (sound mode, Do Not Disturb, battery saver, or one app's notification config). Total silence → you are probably on the hardware path: case off, sliders up, retest, then price a repair. I put a free, no-install tester at vibration-test.php that plays tap-to-run patterns (short pulse, one-second buzz, triple tap, SOS, heartbeat, and a custom millisecond pattern). Important honesty note: it triggers vibration; it cannot measure vibration strength — the browser has no API for that. The platform catch every dev should know navigator.vibrate() is Android-only in practice . Two gotchas: iOS Safari has never shipped it. Apple cites fingerprinting risk; MDN lists it as unsupported. So on iPhone the browser check simply cannot run — you go to Settings > Sounds & Haptics instead. Firefox dropped it. Firefox removed the Vibration API in 2024, so on Android use Chrome or Samsung Internet . Worldwide that is still most phones: Android holds 69.14% of mobile OS share vs 30.79% for iOS (StatCounter, June 2026). The Android settings ladder (when the motor works) If the test buzzes, walk these in order: ring/vibrate mode → Do Not Disturb → "Vibrate on ring/notifications" toggles → battery saver (it throttles haptics) → per-app notification settings → the system haptic-strength slider. One of them is the culprit. The Samsung "Never Play" haptics trap is a common one: a single toggle can silence feedback while everything else looks correct. When it is hardware: what it actually costs If it stays silent everywhere — no keyboard taps, no call buzz — price a fix with real numbers instead of dread: Software-level shop fix: $39–59 (Owl Repair, 2026) Android vibration motor replacement: $69–129 depending on model (Owl Repair, 2026) iPhone 13 Taptic Engine, Apple self-repair: $43.64 part + $49 tool rental = $92.64 ; $99 with AppleCare+; $449 out-of-warranty "other damage" (AppleInsider, 2022) A vibration motor is one of the cheaper board-level repairs. Under warranty/AppleCare+/carrier protection, a short video of the silent test is unambiguous claim evidence — Owl Repair attributes roughly 60% of no-vibration phones to hardware faults. And the "factory reset first" advice you see everywhere? Skip it. If the browser test buzzes, the hardware is fine and a reset is a waste; if it is silent, a reset will not repair a motor. Try it Run the check: vibration motor test Full walkthrough (Android ladder + iPhone checklist + costs): Phone Not Vibrating? Test Your Vibration Motor and Fix It If your phone's touchscreen also started misbehaving after a drop, a quick ghost touch test is worth running before you pay for anything, so one repair quote covers everything at once.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/keyboard-testerclick/phone-not-vibrating-a-10-second-browser-check-tells-you-if-the-motor-is-dead-5bfb

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
