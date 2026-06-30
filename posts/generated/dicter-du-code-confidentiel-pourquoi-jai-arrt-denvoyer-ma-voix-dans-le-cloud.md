---
title: "Dicter du code confidentiel : pourquoi j'ai arrêté d'envoyer ma voix dans le cloud"
slug: "dicter-du-code-confidentiel-pourquoi-jai-arrt-denvoyer-ma-voix-dans-le-cloud"
author: "elboKazQC"
source: "devto_ai"
published: "Tue, 30 Jun 2026 14:22:35 +0000"
description: "Je suis consultant IA. La moitié de mes journées, je pilote des modèles de langage pour des clients. Je dicte beaucoup : des prompts à Claude Code, des notes..."
keywords: "est, pas, des, sur, que, pour, qui, une"
generated: "2026-06-30T14:30:32.342466"
---

# Dicter du code confidentiel : pourquoi j'ai arrêté d'envoyer ma voix dans le cloud

## Overview

Je suis consultant IA. La moitié de mes journées, je pilote des modèles de langage pour des clients. Je dicte beaucoup : des prompts à Claude Code, des notes de conception, des noms de variables, des bouts de logique métier qui ne sont pas encore publics. Pendant un bon moment, j'ai utilisé une solution de dictée cloud. Commode. Ça marche bien. Et puis un jour j'ai réalisé ce qui part réellement sur leurs serveurs quand j'appuie sur le bouton d'enregistrement. Ce que ta voix contient vraiment Quand tu dictes un prompt à un outil de code ou à un agent IA, t'as pas l'impression de transmettre quelque chose de sensible. T'es dans ta bulle, t'es chez toi, c'est juste toi qui parles à un micro. Mais dans ce flux audio, il y a le nom du produit client qui n'est pas encore annoncé. Il y a la logique d'un flux de données propriétaire. Il y a les noms des tables, des endpoints, des règles d'affaires. Il y a les acronymes internes qui permettent à n'importe qui de chercher sur Google et de comprendre dans quelle industrie tu travailles. Pour les outils de dictée cloud comme Wispr Flow, Otter ou les fonctions vocales intégrées à divers services, cet audio transite par des serveurs distants. Ce qui arrive ensuite, c'est leur affaire : rétention du contenu pour amélioration du modèle, accès interne potentiel, politiques qui changent silencieusement d'une mise à jour des CGU à l'autre. Sous NDA, t'es responsable de ça. Pas eux. Ce que "100 % local" veut dire en pratique La promesse d'une solution locale, c'est que l'audio ne quitte jamais ton disque. Point. Pas de requête réseau, pas de token envoyé quelque part, pas de métadonnée. Le modèle Whisper tourne directement sur ta machine. Il y a un test simple pour le vérifier : tu coupes ta connexion Wi-Fi, tu dictes, tu lâches le bouton. Si la transcription arrive, c'est 100 % local. Sinon, quelque chose part quelque part. Tu peux aussi ouvrir un moniteur réseau (Little Snitch, Glasswire, ou simplement Wireshark si t'as le goût de souffrir un peu) pendant une session de dictée, et regarder si des connexions sortantes s'ouvrent. Avec une solution vraiment locale, t'as rien. C'est le silence réseau qui prouve la confidentialité, pas la politique de vie privée du vendor. Le comment technique, sans faire semblant que c'est compliqué Le moteur sous le capot, c'est faster-whisper, une implémentation optimisée de Whisper par Systran. Plus rapide que l'originale d'OpenAI sur CPU, et elle tourne proprement sur Windows sans configuration ésotérique. La première fois que tu l'actives, le modèle (quelques centaines de mégaoctets selon la taille choisie) se télécharge une fois. Après ça, plus besoin de connexion. Si tu veux voir à quoi ressemble un appel de base : from faster_whisper import WhisperModel modele = WhisperModel ( " small " , device = " cpu " , compute_type = " int8 " ) segments , info = modele . transcribe ( " audio.wav " , language = " fr " , initial_prompt = " useState, Stripe, fa que, pis, API REST, webhook " ) for segment in segments : print ( segment . text ) Le paramètre initial_prompt est la pièce souvent oubliée. Il force le modèle à s'attendre à certains mots, ce qui améliore la transcription des termes techniques et des expressions québécoises. Tu peux y mettre des noms de variables, des mots de ton domaine, des expressions typiques de ton projet. La limite est d'environ 224 tokens, pis ça se remplit vite, fa que sois sélectif. Le compromis honnête Je vais pas te vendre ça comme une solution parfaite, parce que c'est pas le cas. L'accent québécois demeure plus difficile pour Whisper que le français de France standard. Sur un texte technique avec du vocabulaire précis, le glossaire dans initial_prompt aide vraiment. Sur une phrase purement conversationnelle avec des expressions régionales denses, attends-toi à plus de corrections manuelles qu'en FR standard. C'est la réalité. Je publie pas de chiffres de taux d'erreur parce que j'ai pas encore fait le benchmark formel, pis je vais pas inventer un nombre. C'est aussi Windows uniquement pour l'instant. Mac et Linux, c'est pas là. Et l'interface reste en phase alpha : fonctionnelle, mais elle a pas encore le polish d'un produit mature. Le setup de base demande quelques étapes techniques si tu pars de zéro. C'est précisément pourquoi j'ai fini par empaqueter tout ça. Pourquoi j'ai packagé ça J'avais déjà monté ce pipeline pour moi-même. Faster-whisper installé, un petit script Python, push-to-talk sur F6 (maintiens pour parler, relâche pour transcrire), intégration au presse-papier pour coller dans n'importe quelle app. Ça marchait. J'ai montré ça à quelques personnes. La réaction habituelle : "c'est cool, mais je vais pas m'asseoir pour installer tout ça." Fa que j'ai fait l'installeur. 63 MB. Tu lance, t'installes, t'appuies sur F6. Le code est ouvert sous licence MIT sur github.com/elboKazQC/tania-dictee si tu veux voir exactement ce qui tourne sur ta machine (pis c'est là que la transparence privacy commence vraiment : open source, pas juste une promesse dans une FAQ). La version packagée est disponible à 9 $ CAD, achat unique, sur Gumroad. Pas d'abonnement. Zéro utilisateur externe à date. Je suis en mode build-in-public, pis je te parle depuis le début du tunnel, pas depuis l'autre bout. Si le sujet t'intéresse, la waitlist est ici : elbokazqc.github.io/tania-dictee

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/elbokazqc/dicter-du-code-confidentiel-pourquoi-jai-arrete-denvoyer-ma-voix-dans-le-cloud-1e9d

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
