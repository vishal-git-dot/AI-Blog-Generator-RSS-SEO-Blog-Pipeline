---
title: "1 porcja, 2 porcje, 5 porcji: Scaling Recipes and Handling Polish Plurals With Intl.PluralRules"
slug: "1-porcja-2-porcje-5-porcji-scaling-recipes-and-handling-polish-plurals-with-intlpluralrules"
author: "Akbo Ichou"
source: "devto_webdev"
published: "Fri, 25 Sep 2026 20:56:16 +0000"
description: "A "servings" slider looks like the easiest feature on a recipe site: multiply every quantity by a factor. Then you ship it in Polish and discover two things ..."
keywords: "porcje, round, porcji, polish, number, const, porcja, intl"
generated: "2026-09-25T21:21:27.487275"
---

# 1 porcja, 2 porcje, 5 porcji: Scaling Recipes and Handling Polish Plurals With Intl.PluralRules

## Overview

A "servings" slider looks like the easiest feature on a recipe site: multiply every quantity by a factor. Then you ship it in Polish and discover two things — scaling has real-world edge cases, and Polish has three plural forms for counted nouns (plus one for fractions). Kuchnia Przepisy is a Polish recipe site covering dinners, cakes (serniki, szarlotki, no-bake cakes), soups, and modern categories like air fryer, Thermomix/Lidlomix and high-protein recipes. Here's how to scale recipes properly and label them correctly in Polish. Store quantities as numbers, not strings "2 szklanki mąki" can't be scaled. Store structure, render text: interface Ingredient { qty : number | null ; // null for "sól do smaku" (salt to taste) unit : " g " | " ml " | " szt " | " łyżka " | " łyżeczka " | " szklanka " | null ; name : string ; // "mąka pszenna" scalable ?: boolean ; // false for e.g. "1 blacha" or a pinch } Scale — then round to something a person can measure Multiplying 3 eggs by 1.5 gives 4.5 eggs. Nobody measures 4.5 eggs, or 187.5 g of flour to the gram. Round by unit: function roundFor ( unit : Ingredient [ " unit " ], x : number ) { switch ( unit ) { case " szt " : return Math . max ( 1 , Math . round ( x )); // whole items (eggs) case " g " : case " ml " : return x < 50 ? Math . round ( x ) : Math . round ( x / 5 ) * 5 ; case " łyżka " : case " łyżeczka " : case " szklanka " : return Math . round ( x * 4 ) / 4 ; // quarters default : return x ; } } export function scale ( list : Ingredient [], from : number , to : number ) { const f = to / from ; return list . map (( i ) => i . qty == null || i . scalable === false ? i : { ... i , qty : roundFor ( i . unit , i . qty * f ) } ); } Baking scales by pan area, not servings Many cakes are written for a baking tray ("12 porcji z blachy") or a round tin. Doubling servings doesn't mean doubling the tin — scale by area: const rectArea = ( w : number , h : number ) => w * h ; const roundArea = ( d : number ) => Math . PI * ( d / 2 ) ** 2 ; // 24 cm round tin -> 26 cm round tin const factor = roundArea ( 26 ) / roundArea ( 24 ); // ≈ 1.17 Baking time doesn't scale linearly, so the UI suggests checking earlier or later instead of recalculating it. Polish plurals: one, few, many — and other English has "1 serving / 2 servings". Polish uses different forms depending on the number: 1 → porcja 2–4, 22–24, 32–34… → porcje 0, 5–21, 25–31… → porcji fractions (1,5) → porcji Don't hand-code the rules — Intl.PluralRules already knows them: const pr = new Intl . PluralRules ( " pl-PL " ); const PORCJA : Record < Intl . LDMLPluralRule , string > = { one : " porcja " , few : " porcje " , many : " porcji " , other : " porcji " , zero : " porcji " , two : " porcje " , }; export const porcje = ( n : number ) => ` ${ new Intl . NumberFormat ( " pl-PL " ). format ( n )} ${ PORCJA [ pr . select ( n )]} ` ; porcje ( 1 ); // "1 porcja" porcje ( 3 ); // "3 porcje" porcje ( 12 ); // "12 porcji" porcje ( 22 ); // "22 porcje" porcje ( 1.5 ); // "1,5 porcji" The same approach works for minutes ("1 minuta", "2 minuty", "5 minut") and pieces ("1 jajko", "2 jajka", "5 jajek"). Categories as a tree The navigation mirrors how Polish home cooks search: top-level groups like Obiad, Ciasta, Zupy and Nowoczesna, with focused subcategories (quick dinners, chicken dishes, one-pot meals, cream soups, air fryer). A recipe can live in several subcategories, so it's a tag set with a primary category for breadcrumbs and URLs — not a strict tree. Takeaways Store quantities as structured data so they can be scaled. Round scaled amounts to measurable units; keep eggs whole. Scale baking by pan area. Use Intl.PluralRules for languages with complex plurals. Browse the recipes at kuchnia-przepisy.pl (in Polish). Which language gave you the most trouble with pluralization?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/akbo_ichou_c41c249cc2783d/1-porcja-2-porcje-5-porcji-scaling-recipes-and-handling-polish-plurals-with-intlpluralrules-4mfa

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
