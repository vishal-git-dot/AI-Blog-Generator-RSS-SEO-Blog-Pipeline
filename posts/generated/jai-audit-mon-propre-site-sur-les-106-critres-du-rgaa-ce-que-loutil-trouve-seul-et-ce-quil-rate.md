---
title: "J'ai audité mon propre site sur les 106 critères du RGAA : ce que l'outil trouve seul, et ce qu'il rate"
slug: "jai-audit-mon-propre-site-sur-les-106-critres-du-rgaa-ce-que-loutil-trouve-seul-et-ce-quil-rate"
author: "Charly Duguey"
source: "devto_ai"
published: "Fri, 02 Oct 2026 12:07:38 +0000"
description: "En bref : j'ai audité mon site sur les 106 critères du RGAA. 71 applicables, 71 conformes. Mais un script ne juge que 24 critères sur 106, et le chiffre ne v..."
keywords: "sur, les, site, pas, des, par, audit, une"
generated: "2026-10-02T12:13:45.784421"
---

# J'ai audité mon propre site sur les 106 critères du RGAA : ce que l'outil trouve seul, et ce qu'il rate

## Overview

En bref : j'ai audité mon site sur les 106 critères du RGAA. 71 applicables, 71 conformes. Mais un script ne juge que 24 critères sur 106, et le chiffre ne vaut rien sans sa méthode. Le 14 septembre 2026, j'ai audité mon propre site WordPress (thème enfant Blocksy) sur les 106 critères du RGAA 4.1, le référentiel français construit sur WCAG 2.1. Résultat : 71 critères applicables, 71 conformes, 35 non applicables, soit 100 %. Le détail est dans ma déclaration d'accessibilité , avec ses limites. Ce que ce 100 % ne dit pas Aucun test avec un lecteur d'écran réel. Je me suis appuyé sur l'arbre d'accessibilité du navigateur, pas sur l'interprétation d'un lecteur. C'est un audit interne. Je suis l'auteur du site et de l'audit. 35 critères sont non applicables : le site n'a ni vidéo, ni son, ni cadre, ni CAPTCHA, ni document à télécharger. Un site client en aura, son taux sera plus dur à tenir. La méthode 20 pages : les 5 pages obligatoires, 12 pages représentatives, et 3 tirées au hasard parmi les 55 du plan du site (tirage reproductible). Outils : Chromium piloté par Playwright (1366 par 900 pixels, puis 320 pixels de large avec un zoom à 200 %), le validateur du W3C et deux scripts maison. Répartition : un script juge seul 24 critères, je tranche les 82 autres à la main à partir des preuves relevées. Le script mesure Il ne sait pas juger présence d'un texte alternatif si ce texte décrit vraiment l'image contraste, focus visible l'ordre de lecture intitulés de liens, titres, repères le comportement au lecteur d'écran zoom à 200 %, lecture à 320 px les messages de correction de saisie étiquettes de champs, lien d'évitement l'espacement du texte Un rapport à 100 % sur les 24 critères mesurés ne veut donc jamais dire « conforme ». C'est la logique de l' audit d'accessibilité RGAA que je propose : les critères mesurés par l'outil, puis la vérification à la main, avec un rapport priorisé. Quatre pièges de mesure focus() en boucle ment. Le style natif dépend de :focus-visible , inactif sur un focus programmatique. J'ai testé à la vraie touche Tab, sur 45 arrêts par page. La cascade CSS ne se déduit pas du fichier. Blocksy repose la couleur de bordure des champs par une variable après mes règles. Seuls les outils de développement disent quelle règle gagne. Le contraste se calcule sur des couches composées. Une pellicule blanche à 5 % sur du bleu nuit n'est pas du blanc : sans composition, mon outil annonçait 1:1 sur du texte lisible. Le cache sert des copies différentes. Deux visites d'affilée ne renvoyaient pas la même feuille de style. Je demande chaque page sous une adresse jamais mise en cache. Ce que l'audit a trouvé sur mon site Contraste (3.2, 3.3) : bordure des champs à 1,24:1, passée à 3,47:1 ; numéro des cartes de 3,81:1 à 5,34:1. Lien d'évitement (12.7) : il pointait vers une ancre inexistante. Menu (10.13) : le panneau s'ouvrait au survol et ne se refermait pas. La touche Échap le masque maintenant. Langue (8.7) : les messages d'erreur du formulaire s'affichaient en anglais. Structure (8.9, 9.3) : une fausse liste faite de sauts de ligne est devenue une vraie liste de description. Code (8.2) : zéro erreur au validateur du W3C, contre sept par page le matin même. À retenir Un script ne remplace pas l'audit : il en couvre moins d'un quart. Un taux ne se cite jamais sans les critères non applicables ni la réserve du lecteur d'écran. La collecte se rejoue à volonté, mais la grille porte des jugements humains. Si l'audit trouve des défauts comme ceux-ci sur un site, la mise en conformité RGAA consiste à les corriger un par un, puis à re-mesurer.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/cduguey/jai-audite-mon-propre-site-sur-les-106-criteres-du-rgaa-ce-que-loutil-trouve-seul-et-ce-quil-3ami

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
