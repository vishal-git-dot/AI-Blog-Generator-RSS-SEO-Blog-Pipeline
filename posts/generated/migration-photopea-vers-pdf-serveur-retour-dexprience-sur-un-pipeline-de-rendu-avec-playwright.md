---
title: "Migration Photopea vers PDF serveur : retour d'expérience sur un pipeline de rendu avec Playwright"
slug: "migration-photopea-vers-pdf-serveur-retour-dexprience-sur-un-pipeline-de-rendu-avec-playwright"
author: "Mohamed Amine Ben Mallessa"
source: "devto_python"
published: "Sat, 04 Jul 2026 03:32:20 +0000"
description: "📖 Article original : GitHub Gist Par Mohamed Amine Ben Mallessa — Lead Dev Sollea AI Le contexte technique L'application qu'on a livrée permet de générer des..."
keywords: "rendu, par, html, serveur, playwright, sollea, est, les"
generated: "2026-07-04T03:39:49.956358"
---

# Migration Photopea vers PDF serveur : retour d'expérience sur un pipeline de rendu avec Playwright

## Overview

📖 Article original : GitHub Gist Par Mohamed Amine Ben Mallessa — Lead Dev Sollea AI Le contexte technique L'application qu'on a livrée permet de générer des affiches personnalisées à partir d'un simple formulaire web. L'utilisateur remplit ses informations, et l'application produit un document prêt à imprimer. Architecture : Next.js 15 (frontend par Nassim Tarkhani) + FastAPI (backend par Nassim Tarkhani). Une stack moderne, mais le maillon faible était le rendu des documents — c'est là que je suis intervenu. Le piège des solutions « gratuites » Quand on a commencé, Photopea semblait être la solution idéale. En pratique, le maintenir en production s'est révélé très coûteux : Problème n°1 : L'iframe introuvable Le PSD était hébergé sur un serveur public. Les en-têtes CORS nécessaires n'étaient pas supportés par l'infrastructure du client. Problème n°2 : Les exports fantômes Les exports transitaient par un appel API. En cas de latence réseau, les fichiers étaient tronqués sans alerte. Problème n°3 : Aucun rendu serveur Le rendu passait obligatoirement par le navigateur du client. Pas de génération automatisée possible. Problème n°4 : L'effet « boîte noire » Impossible de diagnostiquer la source des bugs de rendu. La solution que j'ai développée Décision 1 : Un template HTML = une affiche Au lieu d'un PSD fermé, chaque format d'affiche est un fichier HTML ouvert, versionné dans le dépôt. Décision 2 : Playwright pour le rendu serveur Chromium headless via Playwright produit un PDF vectoriel parfait et un PNG haute résolution. ~3,5 secondes par affiche. Décision 3 : La même source de vérité Le template HTML sert à la fois pour l'aperçu live et le rendu final. Garantie que l'aperçu est identique au document imprimé. Le résultat Métrique Avant (Photopea) Après (Moteur HTML) Dépendances externes 2 (Canva, Photopea) 1 (Playwright) Coût licence $$$ (Canva Enterprise) $0 Temps de rendu 30-60s ~3,5s Rendu serveur Impossible PDF + PNG Fiabilité Fragile Robuste Ce que cette expérience m'a appris Les solutions « gratuites » qui nécessitent une infrastructure complexe reviennent souvent plus chères qu'une solution simple qu'on maîtrise de bout en bout. Un template HTML n'a pas la puissance d'un PSD, mais il est lisible, versionnable et reproductible — trois avantages décisifs pour la production. Mohamed Amine Ben Mallessa — Lead Dev chez Sollea AI 🔗 GitHub | LinkedIn Merci à **Nassim Tarkhani * pour le développement frontend et backend FastAPI.* playwright #html #pdfgeneration #fastapi #nextjs #retourdexperience #solleaai #opensource 💻 Vous avez un projet similaire ? Sollea AI — Développement full-stack, automatisation IA, solutions sur mesure. 🔗 Sollea AI · GitHub · LinkedIn Équipe dirigée par **Mohamed Amine Ben Mallessa * — Lead Dev Sollea AI*

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/benmallessamohamedamine/migration-photopea-vers-pdf-serveur-retour-dexperience-sur-un-pipeline-de-rendu-avec-playwright-2dj8

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
