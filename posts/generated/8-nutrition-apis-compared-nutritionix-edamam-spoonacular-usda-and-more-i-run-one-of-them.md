---
title: "8 nutrition APIs compared: Nutritionix, Edamam, Spoonacular, USDA and more (I run one of them)"
slug: "8-nutrition-apis-compared-nutritionix-edamam-spoonacular-usda-and-more-i-run-one-of-them"
author: "Tosh Koevoets"
source: "devto_webdev"
published: "Wed, 11 Nov 2026 13:52:52 +0000"
description: "I run Your Move, which includes a nutrition API. Disclosure done. I spent a year wiring food databases into a trainer app before we built our own, so I have ..."
keywords: "yes, you, food, nutrition, your, api, data, foods"
generated: "2026-11-11T13:54:26.913240"
---

# 8 nutrition APIs compared: Nutritionix, Edamam, Spoonacular, USDA and more (I run one of them)

## Overview

I run Your Move, which includes a nutrition API. Disclosure done. I spent a year wiring food databases into a trainer app before we built our own, so I have been a paying customer of half this list. Our data is public and free: USDA FoodData Central and Open Food Facts. We structured it, removed the wrong entries and update it regularly, but we do not think it is fair to charge a lot for data that was free to begin with. So it is $19 a month with unlimited food searches and barcode scans. A large medical company that makes insulin pumps recently called us because fatsecret was raising its pricing a lot. They told us our data quality was on the same level, and we told them the $19 plan was enough. The three questions that matter: where does the food data come from, can you look up a barcode, and can you sign up without a sales call. Everything else is detail. The 8, side by side API Data sources Pricing Self-serve Barcode AI food logging Recipes included Your Move USDA FoodData Central + Open Food Facts, 3M+ products, 180+ countries $19/mo, 7-day trial Yes Yes Yes (text, photo, audio; Pro plan) Yes Edamam Own database, ~900k foods $9 to $58+/mo per product Yes Yes Yes Separate product USDA FoodData Central US government reference data Free Yes No No No fatsecret Own database, broad international coverage Contract (Premier tier) No Yes Yes No Nutritionix Own database, strong on US restaurant chains Custom (enterprise) No Yes Yes No Open Food Facts Community database, global barcodes Free (ODbL license) Yes Yes No No Spoonacular Own database, recipe-first From $5/mo, points-based Yes No No Yes API Ninjas (Nutrition) Not disclosed Subscription, full nutrients on premium Yes No No No Checked November 2026. Pricing pages move, verify before you commit. How I would pick You need to ship a food logger this quarter. Your Move or Edamam. Both are self-serve with barcode lookup and text-to-nutrition. Edamam bills per product, so nutrition analysis plus food database plus recipes is three subscriptions. Your Move is one key for all of it, including the exercise API if you ever need it. US restaurant menus are the core of your app. Nutritionix. Nobody else has that chain menu data. Budget for a sales conversation. International packaged foods. Your Move or fatsecret. Both have broad branded coverage across countries, and ours matches theirs. The difference is how you buy: fatsecret is contract only, Your Move is self-serve at $19. Budget is zero and you can build the product layer yourself. USDA FoodData Central for US generic foods, Open Food Facts for barcodes. Both are excellent raw data. Neither gives you serving sizes that just work, deduplication, or a search ranking a user would tolerate. That layer is what you pay the others for. Recipes first, nutrition second. Spoonacular. Its food ontology is genuinely good. Its nutrition data is a side dish. What a nutrition response looks like const headers = { 'X-API-Key' : process . env . YMOVE_KEY } ; const base = 'https://exercise-api.ymove.app/api/v2' ; // search, normalized per 100g so values are comparable const foods = await fetch ( `${base}/foods?query=chicken%20breast&per=100g` , { headers } ) . then ( r => r . json ( ) ) ; // barcode, with the country so you get the local label const product = await fetch ( `${base}/foods/barcode/041631000564?country=NL` , { headers } ) . then ( r => r . json ( ) ) ; // free text to logged meal (Pro plan) const meal = await fetch ( `${base}/foods/log/text` , { method : 'POST' , headers : { . . . headers , 'Content-Type' : 'application/json' } , body : JSON . stringify ( { text : 'grilled chicken with rice and broccoli' } ) , } ) . then ( r => r . json ( ) ) ; Three things I learned the hard way Ask where the calories come from. Several "nutrition APIs" are a thin wrapper over USDA with a markup. That is fine, but you should know, because then you also know what they cannot have: branded products and non-US foods. Barcode coverage is regional. A database that is great in the US can be empty in Brazil or India. Test with ten barcodes from your actual market before you sign anything. Serving sizes break more apps than missing foods do. Make sure every food comes with gram weights for its household units, or you will be writing a conversion table yourself at 2am. The full comparison with sources and a decision table is here: https://ymove.app/nutrition-api/top-nutrition-apis Wrong about your API? Comment and I will correct it.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/tosh_koevoets_c167a1efc0b/8-nutrition-apis-compared-nutritionix-edamam-spoonacular-usda-and-more-i-run-one-of-them-4c8p

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
