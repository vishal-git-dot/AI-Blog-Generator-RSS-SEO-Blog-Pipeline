---
title: "I built a Telegram bot that counts calories from food photos. It confidently called soup "berry compote""
slug: "i-built-a-telegram-bot-that-counts-calories-from-food-photos-it-confidently-called-soup-berry-compote"
author: "alexdv124"
source: "devto_python"
published: "Sat, 04 Jul 2026 03:27:34 +0000"
description: "My wife tracks her meals, and I watched her type "buckwheat, boiled, 100 g" into a calorie app for the hundredth time. Search, scroll, pick the wrong entry, ..."
keywords: "model, telegram, bot, calories, food, soup, berry, her"
generated: "2026-07-04T03:39:49.956915"
---

# I built a Telegram bot that counts calories from food photos. It confidently called soup "berry compote"

## Overview

My wife tracks her meals, and I watched her type "buckwheat, boiled, 100 g" into a calorie app for the hundredth time. Search, scroll, pick the wrong entry, fix the grams. Every meal, every day. At some point it's easier to teach a vision model to look at the plate. So I built a Telegram bot. You send a photo of your food, it identifies the dishes, estimates portion weights, and replies with a card: calories, protein, fat, carbs. Text and voice work too ("2 eggs and a toast"). The borscht incident The first version was hilariously confident about wrong answers. Borscht — a red beet soup, if you've never met one — came back as "berry compote" (a sweet berry drink). Red liquid in a bowl, what else could it be? Adding more example dishes to the prompt made it worse : the model just got magnetized to whatever was on the list. A cod fillet became "syrniki" (cottage cheese pancakes) because syrniki were mentioned and both are pale and pan-fried. What actually fixed it was making the model read the serving context before naming anything: liquid served in a deep bowl with a spoon and sour cream is soup, not a drink. Flaky texture that separates in layers is fish, not pancakes. Fried items are never served floating in liquid. A short list of physical rules beat a long list of dishes. Portion estimation works the same way — the model reasons from plate size, cutlery, how full the bowl is. My wife has been checking its gram estimates against her kitchen scale for a week and it lands closer than either of us expected. Stack, briefly Python + aiogram, a vision LLM with structured JSON output (with a fallback parser for the days the model decides to wrap JSON in prose), Pillow for rendering the result cards. Photos are analyzed on the fly and never stored. Payments are Telegram Stars, so there's no app store, no signup, no card form — the whole onboarding is "send a photo". Yesterday I also wired up inline mode: type @SnapPlateBot in any chat, describe the food, and it counts right there — like @gif, but for calories. Try to break it The bot is free to try (5 analyses + 1 daily): https://t.me/SnapPlateBot?start=devto I'd genuinely love reports on non-Russian cuisines — it grew up on borscht, so ramen, mole and biryani are its final exam.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/alexdv124/i-built-a-telegram-bot-that-counts-calories-from-food-photos-it-confidently-called-soup-berry-5bah

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
