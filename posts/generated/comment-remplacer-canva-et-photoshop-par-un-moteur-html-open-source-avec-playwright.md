---
title: "Comment remplacer Canva et Photoshop par un moteur HTML open source avec Playwright"
slug: "comment-remplacer-canva-et-photoshop-par-un-moteur-html-open-source-avec-playwright"
author: "Mohamed Amine Ben Mallessa"
source: "devto_python"
published: "Sat, 04 Jul 2026 03:32:18 +0000"
description: "📖 Article original : GitHub Gist Par Mohamed Amine Ben Mallessa — Lead Dev Sollea AI Le produit qu'on a construit Avec mon équipe chez Sollea AI, nous avons ..."
keywords: "par, sollea, dans, backend, lignes, canva, html, playwright"
generated: "2026-07-04T03:39:49.956644"
---

# Comment remplacer Canva et Photoshop par un moteur HTML open source avec Playwright

## Overview

📖 Article original : GitHub Gist Par Mohamed Amine Ben Mallessa — Lead Dev Sollea AI Le produit qu'on a construit Avec mon équipe chez Sollea AI, nous avons développé une plateforme SaaS de génération d'affiches événementielles. L'application complète — développée en Next.js 15 (frontend par Nassim Tarkhani) et FastAPI (backend par Nassim Tarkhani) — permet à des utilisateurs non techniques de remplir un formulaire et d'obtenir instantanément une affiche professionnelle prête à imprimer. Le mur qu'on a rencontré Le pipeline de rendu original reposait sur deux briques externes : Canva Connect / Autofill : nécessitait un plan Enterprise à plusieurs milliers d'euros par an. Bloqué administrativement. Photopea (alternative gratuite à Photoshop dans le navigateur) : fonctionnait en théorie, mais en pratique c'était un cauchemar technique : Chargement d'un PSD public dans un iframe — contraintes CORS impossibles à contourner proprement Ré-upload des exports vers le backend — fragilité réseau Artefacts bizarres dans le payload des tickets Aucun rendu côté serveur possible Pas d'injection de photos dans les mockups Bref : deux impasses techniques , une équipe bloquée, un client qui attend. La solution que j'ai développée J'ai remplacé l'ensemble du pipeline par un moteur de « render templates » HTML qui tient dans 3 concepts : Un template = un dossier backend/templates/<slug>/ avec un template.html + un manifest.json L'aperçu live = le frontend charge le template dans une iframe et lui envoie les données du formulaire par postMessage Le rendu final = Playwright (Chromium headless) ouvre le même template, injecte les données et exporte en PDF A4 vectoriel + PNG 300 dpi (~3,5 secondes) Ajouter un nouveau format d'affiche ? Il suffit de déposer un dossier. Zéro code backend, zéro code frontend. Ce qu'on a supprimé 132 lignes de code Canva OAuth 243 lignes de renderer Photopea 87 lignes de compositeur canvas 33 lignes de route d'export Photopea Résultat : ~500 lignes de code supprimées, 0 dépendance externe de design, des affiches générées 10× plus vite. Pourquoi c'est important Pas besoin de Canva Enterprise. Pas besoin de Photoshop. Pas besoin de SaaS payant. Un fichier HTML, un manifeste JSON, et Playwright. L'open source a encore gagné. Article original publié sur GitHub Gist. Mohamed Amine Ben Mallessa — Lead Dev chez Sollea AI 🔗 GitHub | LinkedIn Merci à **Nassim Tarkhani * pour le développement frontend et backend FastAPI.* opensource #playwright #htmltemplates #fastapi #nextjs #devops #solutions Techniques #innovation 💻 Vous avez un projet similaire ? Sollea AI — Développement full-stack, automatisation IA, solutions sur mesure. 🔗 Sollea AI · GitHub · LinkedIn Équipe dirigée par **Mohamed Amine Ben Mallessa * — Lead Dev Sollea AI*

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/benmallessamohamedamine/comment-remplacer-canva-et-photoshop-par-un-moteur-html-open-source-avec-playwright-4h2f

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
