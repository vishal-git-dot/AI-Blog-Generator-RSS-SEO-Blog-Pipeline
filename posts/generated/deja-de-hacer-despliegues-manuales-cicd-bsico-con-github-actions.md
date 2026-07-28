---
title: "Deja de hacer despliegues manuales: CI/CD básico con GitHub Actions"
slug: "deja-de-hacer-despliegues-manuales-cicd-bsico-con-github-actions"
author: "Asier Caballero"
source: "devto_python"
published: "Tue, 28 Jul 2026 08:21:02 +0000"
description: "Deja de hacer despliegues manuales: CI/CD básico con GitHub Actions Si todavía copias archivos por SCP o subes carpetas por FTP en julio de 2026, por favor, ..."
keywords: "que, github, actions, node, pipeline, una, push, test"
generated: "2026-07-28T08:43:31.568648"
---

# Deja de hacer despliegues manuales: CI/CD básico con GitHub Actions

## Overview

Deja de hacer despliegues manuales: CI/CD básico con GitHub Actions Si todavía copias archivos por SCP o subes carpetas por FTP en julio de 2026, por favor, para. No tiene sentido. GitHub Actions es el estándar de facto y si no lo usas, estás perdiendo el tiempo que podrías dedicar a cosas más interesantes. Vamos al grano. Un pipeline no es magia. Es solo un script que se ejecuta en una máquina virtual de GitHub cada vez que haces un git push . El concepto clave: Eventos y Runners Todo se basa en eventos. Puedes disparar tu pipeline cuando haces un push a main , cuando abres un Pull Request, o incluso a una hora específica. GitHub te presta una máquina (el "Runner"). Tú le dices qué hacer en un archivo YAML dentro de .github/workflows/ . Tu primer workflow Crea el archivo .github/workflows/ci.yml en tu repositorio. Este es un ejemplo para una app sencilla de Node.js que deberías tener funcional hoy: name : CI Pipeline on : push : branches : [ " main" ] pull_request : branches : [ " main" ] jobs : test : runs-on : ubuntu-latest steps : - uses : actions/checkout@v4 - name : Setup Node uses : actions/setup-node@v4 with : node-version : ' 22' - run : npm ci - run : npm test ¿Qué hace esto? on : Escucha cambios en main . runs-on : Pide una máquina con Ubuntu actualizada a la fecha. actions/checkout : Descarga tu código en la máquina. setup-node : Prepara el entorno. run : Ejecuta los comandos que escribirías en tu terminal. Si el npm test falla, el pipeline se detiene y te manda un correo. Así es como mantienes el código roto lejos de producción. No pongas secretos en el repo Esto es un error de novato nivel junior: subir contraseñas o tokens de API al repo. GitHub tiene "Secrets" para esto. Ve a Settings > Secrets and variables > Actions . Ahí guardas tu DB_PASSWORD o tu AWS_ACCESS_KEY . En el YAML, los llamas así: env : DB_PASSWORD : ${{ secrets.DB_PASSWORD }} Nunca, bajo ninguna circunstancia, escribas el valor real en el archivo. Si lo haces, revócalo inmediatamente. Despliegue automático (CD) Aquí es donde ahorras horas. Una vez que los tests pasan, puedes desplegar automáticamente a tu nube de preferencia. Si usas Docker, el flujo lógico es: Build de la imagen. Login en tu registry (GHCR, AWS ECR, lo que sea). Push de la imagen. SSH al servidor o comando de actualización en Kubernetes. Ejemplo para subir una imagen a GitHub Container Registry: build-and-push : needs : test runs-on : ubuntu-latest steps : - uses : actions/checkout@v4 - name : Login a GHCR uses : docker/login-action@v3 with : registry : ghcr.io username : ${{ github.actor }} password : ${{ secrets.GITHUB_TOKEN }} - name : Build y Push uses : docker/build-push-action@v6 with : push : true tags : ghcr.io/${{ github.repository }}/app:latest Fíjate en el needs: test . Si los tests fallan, la parte de despliegue ni siquiera arranca. Eso es seguridad. Lo que veo que falla siempre He revisado muchos repos de clientes a mediados de este 2026 y estos son los tres problemas más comunes: Dependencias no cacheadas : Si cada vez que corres un test bajas todo node_modules o pip desde cero, el pipeline tarda 5 minutos en vez de 30 segundos. Usa actions/cache o, mejor aún, las capacidades integradas de setup-node y setup-python . Workflows gigantes : No intentes meter todo en un solo YAML de 500 líneas. Si tu pipeline crece, usa Reusable Workflows . Si tienes un proceso de test que usas en 10 proyectos diferentes, sepáralo. Ignorar las matrices (Matrix Builds) : Si tu app debe funcionar en Node 20, 22 y 24, no hagas tres pipelines. Usa la estrategia de matriz: strategy : matrix : node-version : [ 20 , 22 , 24 ] steps : - uses : actions/setup-node@v4 with : node-version : ${{ matrix.node-version }} GitHub ejecutará tres trabajos en paralelo. Es mucho más eficiente que hacerlo uno tras otro. Un consejo final sobre seguridad En 2026, los ataques a cadenas de suministro están a la orden del día. Si vas a usar acciones de terceros (no creadas por GitHub o por la organización oficial de tu lenguaje), usa el hash del commit en lugar de la versión (ej: @v4 ). Ejemplo: uses: actions/checkout@b4ffde65f46336abfa881881184668721206f353 Sí, es un poco más pesado de mantener, pero si alguien hackea el repositorio de esa acción y publica una versión maliciosa, tú estás protegido porque tu pipeline sigue apuntando al commit seguro. ¿Y ahora qué? No intentes automatizar todo el primer día. Empieza con el npm test en el pipeline. Cuando eso esté sólido, añade el despliegue automático. Luego añade análisis estático de código (como SonarQube o ESLint) en el mismo flujo. El objetivo del DevOps no es llenar el repo de YAMLs, es que tú no tengas que estar pendiente de si el deploy salió bien o si el código que subió el compañero rompió la base de datos. Que la máquina trabaje por ti. Si tienes dudas, mira la documentación oficial. GitHub Actions ha cambiado mucho desde hace un par de años; ya es mucho más rápido y estable. Deja de pelearte con scripts de bash locales y centraliza esto en la plataforma donde vive tu código. ¿Tienes algún problema con un error específico de runner ? Déjame un comentario y lo miramos.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/acrdev/deja-de-hacer-despliegues-manuales-cicd-basico-con-github-actions-40j9

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
