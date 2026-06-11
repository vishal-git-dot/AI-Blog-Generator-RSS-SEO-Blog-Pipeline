---
title: "Kostenloser DSGVO-Scanner für eure Website — 73% der getesteten .de-Domains hatten Verstöße"
slug: "kostenloser-dsgvo-scanner-fr-eure-website-73-der-getesteten-de-domains-hatten-verste"
author: "Nevik Schmidt"
source: "devto_webdev"
published: "Thu, 11 Jun 2026 10:39:44 +0000"
description: "Originally written for r/de on Reddit — sharing here for the dev.to community. Moin zusammen, als Entwickler aus Deutschland habe ich in den letzten Monaten ..."
keywords: "fonts, der, ich, und, google, dsgvo, die, habe"
generated: "2026-06-11T10:47:52.348859"
---

# Kostenloser DSGVO-Scanner für eure Website — 73% der getesteten .de-Domains hatten Verstöße

## Overview

Originally written for r/de on Reddit — sharing here for the dev.to community. Moin zusammen, als Entwickler aus Deutschland habe ich in den letzten Monaten über 200 deutsche Websites auf DSGVO-Konformität gescannt. Das Ergebnis: 73% hatten mindestens einen Verstoß , der zu einer Abmahnung führen könnte. Deshalb habe ich einen kostenlosen Scanner gebaut, den jeder nutzen kann: nevik.de/guard/ Kein Account, keine Anmeldung, einfach URL eingeben und Ergebnis sehen. Was der Scanner prüft Google Fonts: Werden noch externe Fonts von Google geladen? (LG München Urteil — Abmahnrisiko €500-2000) Cookie Consent: Ist ein Cookie-Banner vorhanden und DSGVO-konform? Externe Tracker: Facebook Pixel, Google Analytics, Hotjar etc. SSL/TLS: Ist die Seite sicher erreichbar? Impressum: Vorhanden und vollständig? Datenschutzerklärung: Vorhanden? Server-Standort: Wo liegen die Daten? (EU oder DritLand) Die häufigsten Verstöße (Top 5) 1. Google Fonts nachladen (52% der Sites) ❌ <link href= "https://fonts.googleapis.com/css2?family=..." rel= "stylesheet" > ✅ Fonts lokal hosten — so geht's: Kurzer Fix: # Fonts herunterladen npx google-font-download "Inter:wght@400;700" --output ./fonts # In CSS referenzieren @font-face { font-family: 'Inter' ; src: url ( '/fonts/inter-regular.woff2' ) format ( 'woff2' ) ; } 2. Kein Cookie-Banner (38% der Sites) Trotz Tracking-Pixels oder Analytics kein Consent-Tool installiert. 3. Google Analytics ohne Anpassung (31%) Standard-GA4 ohne Server-Side Tagging oder IP-Anonymisierung. 4. Fehlendes Impressum (19%) Besonders bei kleineren Projekten und Blogs oft vergessen. 5. Kontaktformular ohne Datenschutzhinweis (15%) "Mit dem Absenden stimmen Sie der Datenverarbeitung zu" fehlt. Warum ich das kostenlos anbiete Ich bin selbst als Freelancer tätig und habe erlebt, wie eine Abmahnung wegen Google Fonts €900 gekostet hat. Das muss nicht sein. Der Basis-Scan ist und bleibt kostenlos. Für Agenturen oder Unternehmen, die mehrere Domains überwachen wollen, gibt es eine Pro-Version mit: Wiederkehrende Scans (täglich/wöchentlich) E-Mail-Benachrichtigungen bei neuen Verstößen PDF-Reports für Mandanten White-Label-Option Was ihr tun könnt Eigene Website scannen: nevik.de/guard/ — 30 Sekunden, kostenlos Ergebnisse prüfen und die obigen Fixes anwenden Regelmäßig checken — nach jedem Website-Update können neue Verstöße auftreten Ich habe auch einen ausführlichen DSGVO-Leitfaden für Entwickler geschrieben, der alle technischen Details enthält (Code-Beispiele, Checklisten, Vorlagen). Bei Interesse schreibt mir eine DM. Falls ihr Fragen zu konkreten DSGVO-Problemen habt, fragt gerne hier — ich helfe wo ich kann.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/nevik_schmidt_3635afa2b85/kostenloser-dsgvo-scanner-fur-eure-website-73-der-getesteten-de-domains-hatten-verstosse-54e4

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
