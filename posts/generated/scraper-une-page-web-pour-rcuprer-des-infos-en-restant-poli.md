---
title: "Scraper une page web pour récupérer des infos en restant poli"
slug: "scraper-une-page-web-pour-rcuprer-des-infos-en-restant-poli"
author: "Dev du Sud"
source: "devto_python"
published: "Wed, 21 Oct 2026 21:18:58 +0000"
description: "Scraper, ça veut dire quoi ? Scraper une page web, c'est demander à Python de lire une page internet et d'en extraire une information. Par exemple : le titre..."
keywords: "une, est, page, les, pas, self, dans, script"
generated: "2026-10-21T21:27:30.861988"
---

# Scraper une page web pour récupérer des infos en restant poli

## Overview

Scraper, ça veut dire quoi ? Scraper une page web, c'est demander à Python de lire une page internet et d'en extraire une information. Par exemple : le titre d'un article, le prix affiché sur une page produit, une liste d'horaires, ou les liens présents dans une page. C'est pratique, mais ce n'est pas une excuse pour aspirer tout un site comme un sauvage. Derrière un site, il y a un serveur, une personne, une entreprise, parfois un petit commerçant. Un script mal réglé peut envoyer trop de requêtes et gêner le site. Dans ce tuto, on va faire un exemple simple et poli : télécharger une seule page, annoncer qui on est avec un User-Agent , attendre entre les demandes si on en fait plusieurs, et ne pas contourner les protections. Les règles de base Avant de scraper, regardez si le site propose une API ou un fichier export. C'est souvent plus propre. Lisez aussi les conditions d'utilisation si les données sont sensibles ou commerciales. Ne récupérez pas de données personnelles sans raison claire. Ne contournez pas un login, un paywall, un captcha ou une interdiction technique. Et si un site dit non dans son fichier robots.txt , respectez ce signal, surtout pour un projet automatisé. Le scraping doit rester raisonnable : peu de pages, peu souvent, et avec un vrai besoin. Le script Python from html.parser import HTMLParser from urllib.request import Request , urlopen from time import sleep class ExtracteurTitres ( HTMLParser ): def __init__ ( self ): super (). __init__ () self . dans_h2 = False self . titres = [] def handle_starttag ( self , tag , attrs ): if tag == " h2 " : self . dans_h2 = True def handle_endtag ( self , tag ): if tag == " h2 " : self . dans_h2 = False def handle_data ( self , data ): texte = data . strip () if self . dans_h2 and texte : self . titres . append ( texte ) url = " https://example.com " requete = Request ( url , headers = { " User-Agent " : " DevDuSudBot/1.0 contact: contact@example.com " }) with urlopen ( requete , timeout = 10 ) as reponse : html = reponse . read (). decode ( " utf-8 " , errors = " ignore " ) extracteur = ExtracteurTitres () extracteur . feed ( html ) for titre in extracteur . titres : print ( titre ) sleep ( 2 ) Ce que fait le script Le script télécharge une page, lit son HTML, puis récupère le texte placé dans les balises h2 . Sur certains sites, les titres sont dans des h1 , h2 , h3 , ou dans des blocs plus complexes. Il faudra donc adapter selon la page. Le User-Agent est une phrase d'identité. Au lieu de se cacher, votre script explique qui il est. Pour un vrai projet, mettez une adresse de contact valable. Cela montre que vous n'essayez pas de vous faire passer pour un navigateur humain. Le sleep(2) marque une pause. Ici, on ne fait qu'une page, donc il ne sert pas beaucoup. Mais si vous parcourez plusieurs pages, cette pause évite de taper trop vite sur le serveur. Un exemple utile et raisonnable Imaginez un commerçant qui veut vérifier une fois par jour si ses horaires apparaissent correctement sur une page partenaire. Le script peut lire la page, chercher un texte, et alerter si l'information change. C'est un usage raisonnable. À l'inverse, aspirer tout un catalogue concurrent toutes les dix secondes serait agressif. Même si c'est techniquement possible, ce n'est pas une bonne idée. Les limites du scraping Beaucoup de sites modernes chargent les informations avec JavaScript. Dans ce cas, le HTML reçu par Python peut être presque vide. Il faut alors utiliser d'autres outils, parfois plus lourds, ou chercher une API officielle. Autre limite : la structure d'une page peut changer. Si le site remplace ses h2 par autre chose, votre script ne trouvera plus rien. Un scraper doit donc être surveillé et corrigé de temps en temps. À retenir Scraper, ce n'est pas voler ni spammer. C'est lire automatiquement une page publique, avec mesure et respect. La bonne attitude est simple : peu de requêtes, une identité claire, pas de contournement, pas de données sensibles inutiles. Python donne le pouvoir de récupérer de l'information. La partie importante, c'est de l'utiliser proprement.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/devdusud/scraper-une-page-web-pour-recuperer-des-infos-en-restant-poli-4akp

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
