---
title: "Zmanin-WP: Common Codes, part 1"
slug: "zmanin-wp-common-codes-part-1"
author: "Leon Adato"
source: "devto_webdev"
published: "Mon, 05 Oct 2026 14:00:00 +0000"
description: "If you’ve been following this blog, you’ll know that I’ve been working on my Zmanim-WP plugin for WordPress for a while now. This blog series is designed to ..."
keywords: "you, blog, shortcodes, sof, zman, each, time, can"
generated: "2026-10-05T14:10:16.265771"
---

# Zmanin-WP: Common Codes, part 1

## Overview

If you’ve been following this blog, you’ll know that I’ve been working on my Zmanim-WP plugin for WordPress for a while now. This blog series is designed to help you dig deeper into the plugin and understand what it does, how it works, and whether it’s right for your needs. “…And There Was Morning…” There are a four shortcodes that help calculate times related to the start of the day. Sunrise Alot hashachar Sof Zman Kria Shema Sof Zman Tefilah I’ve discussed some of these times in other parts of this series and I want to keep the focus of these blogs on HOW to use each shortcode. Feel free to let me know in the comments if you want a more explicit tutorial on each of these (and upcoming) times and when they are used. Sunrise ([zman_sunrise])- this is, as the name implies, the time the sun rises. I covered the shortcode extensively in the previous blog post . Alot hashachar ([zman_alot]) – before “sunrise” (when the disk of the sun appears over the horizon) is “dawn”. This is a somewhat murky concept, but it basically relates to the time the first light of the sun can be seen coming over the horizon. Sof Zman Kria Shema ([zman_shema]) – the latest time one can say the Shema prayer. Sof Zman Tefilah ([[zman_tefilah]]) – the latest time one can say morning (shacharit) prayers. To these I’m going to add one more: The date itself ([zman_zmandate]). Each of those shortcodes can be used as-is, or with the options I described in the previous blog post . Examples: [zman_sunrise date="saturday"] [zman_shema date="saturday" dateformat="g:i:s a"] [zman_alot offset=-20] [[zman_tefilah dateformat=”g:i a”]] [zman_zmandate] But, of course, there’s more. Special Options In addition to the standard options, there are special options that only apply to certan shortcodes. Today, I’m going to look at just one: lang This let’s you control whether information displays in English (the default) or Hebrew. It works for the following shortcodes: Rosh Chodesh ([zman_chodesh]) the Molad ([zman_molad]) the Parsha ([zman_parsha]). Shabbat Mevorchim ([zman_mevorchim]) the date ([zman_zmandate]) For the date ([zman_zmandate]) you can also specify “transliterated” (or “translit” or even “trans”) to give an English-ified version of the Hebrew date. So, while [[zman_date lang="hebrew"]] would give you: י״ד טבת תשפ״ו [ [zman_date lang="transliterated"]] would render as: 14 Tevet, 5786 A Matter of Opinion Unlike my last blog on the plugin , where I dug into the options, in this case the complexity comes from the initial setup: Most of the standard time options give you the chance to select the Rabbinic opinion (“shitah”) used for it’s calculations. For example, Alot hashachar could use any one of the following opinions: alos72 alos60 alos72Zmanis alos96 alos90Zmanis alos96Zmanis alos90 alos120 alos120Zmanis alos26Degrees alos18Degrees alos19Degrees alos19Point8Degrees alos16Point1Degrees alosBaalHatanya What each of these items mean, and what circumstances they should be used in, is the topic for another day (and probably another 5 blog posts). Until then, you can get some details on the KosherJava documentation site: https://kosherjava.com/zmanim/docs/api/com/kosherjava/zmanim/ComplexZmanimCalendar.html#getAlos60() Here are the shitot for each of the shortcodes we’re covering today: Alot hashachar ([zman_alot]) alos72 alos60 alos72Zmanis alos96 alos90Zmanis alos96Zmanis alos90 alos120 alos120Zmanis alos26Degrees alos18Degrees alos19Degrees alos19Point8Degrees alos16Point1Degrees alosBaalHatanya Sof Zman Kria Shema ([zman_shema]) “sofZmanShmaMGA sofZmanShmaGra sofZmanShmaMGA19Point8Degrees sofZmanShmaMGA16Point1Degrees sofZmanShmaMGA18Degrees sofZmanShmaMGA72Minutes sofZmanShmaMGA72MinutesZmanis sofZmanShmaMGA90Minutes sofZmanShmaMGA90MinutesZmanis sofZmanShmaMGA96Minutes sofZmanShmaMGA96MinutesZmanis sofZmanShma3HoursBeforeChatzos sofZmanShmaMGA120Minutes sofZmanShmaAlos16Point1ToSunset sofZmanShmaAlos16Point1ToTzaisGeonim7Point083Degrees sofZmanShmaKolEliyahu sofZmanShmaAteretTorah sofZmanShmaFixedLocal sofZmanShmaBaalHatanya sofZmanShmaMGA18DegreesToFixedLocalChatzos sofZmanShmaMGA16Point1DegreesToFixedLocalChatzos sofZmanShmaMGA90MinutesToFixedLocalChatzos sofZmanShmaMGA72MinutesToFixedLocalChatzos sofZmanShmaGRASunriseToFixedLocalChatzos Sof Zman Tefilah ([[zman_tefilah]]) sofZmanTfilaMGA sofZmanTfilaGra sofZmanTfilaMGA19Point8Degrees sofZmanTfilaMGA16Point1Degrees sofZmanTfilaMGA18Degrees sofZmanTfilaMGA72Minutes sofZmanTfilaMGA72MinutesZmanis sofZmanTfilaMGA90Minutes sofZmanTfilaMGA90MinutesZmanis sofZmanTfilaMGA96Minutes sofZmanTfilaMGA96MinutesZmanis sofZmanTfilaMGA120Minutes sofZmanTfila2HoursBeforeChatzos sofZmanTfilahAteretTorah sofZmanTfilaFixedLocal sofZmanTfilaBaalHatanya sofZmanTfilaGRASunriseToFixedLocalChatzos My goal here is not to overwhelm you. Rather, I want to emphasize that, for each of the different shortcodes, you should look over, consider, and select the opinion that best fits your needs. Until next time!

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/leonadato/-zmanin-wp-common-codes-part-1-2nb4

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
