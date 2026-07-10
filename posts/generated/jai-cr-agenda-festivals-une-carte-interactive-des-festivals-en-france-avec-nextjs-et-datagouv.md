---
title: "J’ai créé Agenda Festivals : une carte interactive des festivals en France avec Next.js et data.gouv"
slug: "jai-cr-agenda-festivals-une-carte-interactive-des-festivals-en-france-avec-nextjs-et-datagouv"
author: "Guillaume Sere"
source: "devto_webdev"
published: "Fri, 10 Jul 2026 09:36:01 +0000"
description: "J’ai créé Agenda Festivals : une carte interactive des festivals en France avec Next.js et data.gouv J’ai récemment développé Agenda Festivals , un site web ..."
keywords: "festivals, une, des, tsx, france, data, carte, gouv"
generated: "2026-07-10T09:45:24.782263"
---

# J’ai créé Agenda Festivals : une carte interactive des festivals en France avec Next.js et data.gouv

## Overview

J’ai créé Agenda Festivals : une carte interactive des festivals en France avec Next.js et data.gouv J’ai récemment développé Agenda Festivals , un site web qui permet d’explorer les festivals en France à partir de données publiques. 👉 Démo : https://agenda-festivals.vercel.app/ L’idée est simple : au lieu d’avoir une liste statique ou difficile à parcourir, je voulais créer une expérience plus visuelle, avec une carte interactive , des filtres , une recherche , des fiches détaillées et une interface responsive. Le site permet aujourd’hui d’explorer plus de 7 000 festivals en France, avec des informations comme la ville, la région, le département, la discipline, la période et la localisation. Pourquoi ce projet ? Je voulais travailler sur un projet qui combine plusieurs sujets que j’aime bien : l’open data la cartographie web Next.js l’UX autour de la recherche et des filtres la visualisation de données culturelles La France a énormément de festivals, mais les données sont souvent dispersées ou peu agréables à explorer. Le dataset de data.gouv donne une très bonne base pour créer un explorateur national. L’objectif n’était pas seulement d’afficher des points sur une carte, mais de créer un vrai outil de découverte. La source des données Le projet utilise le dataset public : Liste des festivals en France Source : data.gouv.fr / Ministère de la Culture URL : https://www.data.gouv.fr/datasets/liste-des-festivals-en-france Le dataset est disponible dans plusieurs formats : CSV JSON GeoJSON ZIP Pour une carte interactive, le format le plus pratique est évidemment le GeoJSON , car il contient directement les coordonnées géographiques des festivals. Dans le projet, je récupère les données côté serveur, puis je les normalise dans un format interne plus simple à utiliser côté front. Stack technique Le projet est construit avec : Next.js TypeScript Tailwind CSS shadcn/ui React Leaflet OpenStreetMap Zod pour sécuriser la donnée Vercel pour le déploiement L’idée était de garder une stack moderne, rapide à itérer, mais assez robuste pour gérer plusieurs milliers de points sur une carte. Architecture générale Le projet est séparé en plusieurs couches : txt app/ page.tsx festivals/ [slug]/ page.tsx components/ festivals/ FestivalCard.tsx FestivalFilters.tsx FestivalList.tsx FestivalCover.tsx map/ FestivalMap.tsx MapPopup.tsx MapControls.tsx lib/ data-gouv.ts normalize-festival.ts filters.ts distance.ts slugify.ts types/ festival.ts

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/guillaumesere/jai-cree-agenda-festivals-une-carte-interactive-des-festivals-en-france-avec-nextjs-et-datagouv-2f6f

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
