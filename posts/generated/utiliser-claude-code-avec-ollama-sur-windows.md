---
title: "Utiliser Claude Code avec Ollama sur Windows"
slug: "utiliser-claude-code-avec-ollama-sur-windows"
author: "CHAYMAE HANIDA"
source: "devto_ai"
published: "Wed, 21 Oct 2026 11:27:34 +0000"
description: "Introduction Claude Code est un agent de programmation qui s'utilise dans le terminal. Ollama permet de lui fournir un modèle open source, y compris des modè..."
keywords: "claude, code, ollama, avec, sur, dans, cloud, les"
generated: "2026-10-21T11:30:28.806327"
---

# Utiliser Claude Code avec Ollama sur Windows

## Overview

Introduction Claude Code est un agent de programmation qui s'utilise dans le terminal. Ollama permet de lui fournir un modèle open source, y compris des modèles cloud gratuits. Dans cet article, je décris comment j'ai configuré les deux sur Windows et les problèmes rencontrés. Prérequis Windows 10 ou 11 PowerShell Un compte Ollama (gratuit) Une connexion internet Étape 1 : installer Claude Code Dans PowerShell : irm https://claude.ai/install.ps1 | iex Étape 2 : corriger le PATH Après l'installation, la commande claude n'était pas reconnue. Il faut ajouter le dossier d'installation au PATH : [ Environment ]:: SetEnvironmentVariable ( "Path" , [ Environment ]:: GetEnvironmentVariable ( "Path" , "User" ) + "; $ env : USERPROFILE \.local\bin" , "User" ) Fermer PowerShell, le rouvrir, puis vérifier : claude --version Étape 3 : installer Ollama Télécharger l'installateur sur ollama.com. Pour l'installer sur un autre disque : . \OllamaSetup.exe /DIR = "D:\Ollama" Pour stocker les modèles sur ce disque : [ Environment ]:: SetEnvironmentVariable ( "OLLAMA_MODELS" , "D:\OllamaModels" , "User" ) Se connecter ensuite à son compte Ollama depuis l'application. Étape 4 : lancer Claude Code avec Ollama mkdir D:\test-claude cd D:\test-claude ollama launch claude --model gemma4:31b-cloud Au premier lancement, Claude Code demande si on fait confiance au dossier. Il faut choisir Yes, I trust this folder (le choix par défaut est « No, exit »). Test J'ai demandé à Claude Code de créer un fichier : crée un fichier hello.py qui affiche Bonjour Résultat : le fichier hello.py a été créé avec le contenu suivant : print ( " Bonjour " ) Problème rencontré : modèle retiré Avec glm-5:cloud , j'ai obtenu l'erreur suivante : API Error: 410 glm-5 was retired on July 15, 2026 Les modèles cloud changent souvent. Pour voir la liste actuelle : ollama launch claude Utilisation dans VS Code En ouvrant le dossier du projet dans VS Code puis en lançant la commande depuis le terminal intégré, l'extension Claude Code pour VS Code s'installe automatiquement. Précautions Ne lancez pas Claude Code depuis C:\Users\<nom> : il aurait accès à tout votre dossier utilisateur. Utilisez toujours le dossier du projet. Le mode « auto » exécute des actions sans demander. Avec Shift + Tab , on peut choisir un mode qui demande une confirmation. Le modèle utilisé (ici Gemma 4) n'est pas Claude : la qualité des réponses diffère. Conclusion La configuration est rapide avec ollama launch claude . Les principales difficultés sont le PATH sous Windows et le choix d'un modèle cloud encore disponible.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/chaymae_hanida_a8e6c66e29/utiliser-claude-code-avec-ollama-sur-windows-2eeh

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
