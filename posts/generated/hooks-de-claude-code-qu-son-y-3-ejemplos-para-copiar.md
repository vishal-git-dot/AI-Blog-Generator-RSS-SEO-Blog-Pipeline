---
title: "Hooks de Claude Code: qué son y 3 ejemplos para copiar"
slug: "hooks-de-claude-code-qu-son-y-3-ejemplos-para-copiar"
author: "El Telar"
source: "devto_ai"
published: "Fri, 23 Oct 2026 21:01:06 +0000"
description: "Un hook es un comando que Claude Code ejecuta automáticamente en un momento concreto : después de editar un archivo, antes de ejecutar una orden o cuando te ..."
keywords: "claude, hooks, code, que, command, matcher, write, con"
generated: "2026-10-23T21:14:15.045090"
---

# Hooks de Claude Code: qué son y 3 ejemplos para copiar

## Overview

Un hook es un comando que Claude Code ejecuta automáticamente en un momento concreto : después de editar un archivo, antes de ejecutar una orden o cuando te espera. Según la documentación oficial, dan un control determinista: la acción ocurre siempre, sin depender de que el modelo se acuerde. 1. Notificación cuando Claude te espera (macOS) En ~/.claude/settings.json : { "hooks" : { "Notification" : [ { "matcher" : "" , "hooks" : [ { "type" : "command" , "command" : "osascript -e 'display notification \" Claude Code needs your attention \" with title \" Claude Code \" '" } ] } ] } } Escribe /hooks para comprobar que aparece. Si no suena, activa las notificaciones de Script Editor en Ajustes del Sistema. 2. Prettier tras cada edición { "hooks" : { "PostToolUse" : [ { "matcher" : "Edit|Write" , "hooks" : [{ "type" : "command" , "command" : "jq -r '.tool_input.file_path' | xargs npx prettier --write" }] } ] } } 3. Bloquear archivos protegidos Un script que termina con código 2 bloquea la acción y Claude recibe el mensaje: #!/bin/bash INPUT = $( cat ) FILE_PATH = $( echo " $INPUT " | jq -r '.tool_input.file_path // empty' ) for pattern in ".env" "package-lock.json" ".git/" ; do if [[ " $FILE_PATH " == * " $pattern " * ]] ; then echo "Blocked: $FILE_PATH matches ' $pattern '" > &2 exit 2 fi done exit 0 Regístralo como hook PreToolUse con matcher: "Edit|Write" . Guía completa, con diagrama, dónde se guardan y preguntas frecuentes: eltelar.es .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/eltelar_es/hooks-de-claude-code-que-son-y-3-ejemplos-para-copiar-3j2d

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
