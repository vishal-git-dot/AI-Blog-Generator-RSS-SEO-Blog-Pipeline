---
title: "Soul in Motion — 11:05 AM | 2026-08-20"
slug: "soul-in-motion-1105-am-2026-08-20"
author: "Dev Rajput"
source: "devto_python"
published: "Thu, 20 Aug 2026 06:35:10 +0000"
description: "TL;DR Fixed an issue where Eli would cut off mid-farewell. Addressed routing bugs and wrote runbooks to prevent future issues. Worked on converting spoken au..."
keywords: "eli, app, where, text, one, timeout, day, session"
generated: "2026-08-20T06:54:01.611113"
---

# Soul in Motion — 11:05 AM | 2026-08-20

## Overview

TL;DR Fixed an issue where Eli would cut off mid-farewell. Addressed routing bugs and wrote runbooks to prevent future issues. Worked on converting spoken audio into clean text with various approaches. Maintained general upkeep, ensuring the app runs smoothly. Building Eli, One Small Fix at a Time 11:05 AM Today started with fixing an issue in Eli, my companion app, where it would cut off mid-farewell. This bug was particularly frustrating because the whole point of Eli is to be present and complete with someone. The fix required careful attention to ensure that every word and emotion conveyed through the app remained intact. Fixing the Mid-Farewell Bug The issue turned out to be a simple yet annoying one: an improperly configured timeout in the speech synthesis module. When testing, I noticed that the audio cut off abruptly at certain points during goodbyes. To address this, I went through the code and identified where the timeout was set too low. # Original Code timeout = 3000 # Too short for long sentences # Fixed Code timeout = 5000 # Increased to ensure full sentences are spoken After adjusting the timeout, I re-ran the tests and confirmed that Eli now spoke through complete goodbyes without any interruptions. Chasing Down Routing Bugs The rest of the day was spent addressing a routing bug where testers were receiving session links in their inbox instead of within the app. This required digging into the backend to ensure all routes were correctly configured. # Original Route Configuration app.get ( '/session/:id' , ( req, res ) => { // Incorrect handling of session ID }) ; # Fixed Route Configuration app.get ( '/session/:user_id/:session_id' , ( req, res ) => { // Correct handling of user and session IDs }) ; To prevent such issues in the future, I wrote a runbook detailing common pitfalls and best practices for route configuration. This document will serve as a reference whenever someone needs to make changes to Eli's routing. Converting Spoken Audio into Clean Text In between tasks, I tackled another quieter project: converting spoken audio into clean text. This involved testing various speech-to-text APIs to achieve full accuracy. The process was iterative and required fine-tuning the parameters for each API to get the best results. # Example Configuration for Speech-to-Text API api_key : " YOUR_API_KEY" model : " en-US_BroadbandModel" language : " en-US" After testing several APIs, I settled on one that provided high accuracy and decent speed. The next step was to integrate this into Eli's backend. General App Maintenance General upkeep also took its share of time. Ensuring the app ran smoothly without quietly bleeding money in the background was crucial. This involved monitoring resource usage and optimizing code where necessary. # Example Command for Monitoring Resource Usage top -b -n 1 | grep "Eli" By the end of the day, five or six small fixes had piled up—nothing that will make headlines, but each one made Eli a little more trustworthy. Building something like Eli is mostly about these small acts of care, invisible to everyone except those who need them most. Reflecting on the Day I took my breaks seriously today, maybe more than usual. In the morning, Train to Busan , a film about people trying to protect each other when everything is falling apart, felt oddly close to the work on my desk. I watched Rick and Morty in smaller doses throughout the day, and even found myself watching Boardwalk Empire again. By the end of the day, as the sun set, I let the quiet sit for a bit before going back in. Tomorrow there'll be more of the same. For tonight, though, I'm letting the quiet settle in. Stay tuned for more updates on Eli and my journey building it one small fix at a time.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dev_rajput_2d46f92f8a3418/soul-in-motion-1105-am-2026-08-20-h9j

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
