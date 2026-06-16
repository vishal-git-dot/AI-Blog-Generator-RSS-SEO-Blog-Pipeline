---
title: "Deploying Label Studio Open-Source Data Labeling Platform on Ubuntu 24.04"
slug: "deploying-label-studio-open-source-data-labeling-platform-on-ubuntu-2404"
author: "Sanskriti Harmukh"
source: "devto_ai"
published: "Tue, 16 Jun 2026 20:57:20 +0000"
description: "Label Studio is an open-source data labeling platform that supports annotation across text, images, audio, video, and time series, with collaborative workflo..."
keywords: "docker, labelstudio, data, traefik, letsencrypt, label, studio, compose"
generated: "2026-06-16T21:09:41.017394"
---

# Deploying Label Studio Open-Source Data Labeling Platform on Ubuntu 24.04

## Overview

Label Studio is an open-source data labeling platform that supports annotation across text, images, audio, video, and time series, with collaborative workflows and ML-model integrations. This guide deploys Label Studio using Docker Compose with Traefik handling automatic HTTPS and persistent volumes for projects and labels. By the end, you'll have Label Studio serving an annotation workspace securely at your domain. Set Up the Directory Structure 1. Create the project directory: $ mkdir ~/labelstudio $ cd ~/labelstudio 2. Create the environment file: $ nano .env DOMAIN = labelstudio.example.com LETSENCRYPT_EMAIL = admin@example.com Deploy with Docker Compose 1. Create the Compose manifest: $ nano docker-compose.yaml services : traefik : image : traefik:v3.6 container_name : traefik command : - " --providers.docker=true" - " --providers.docker.exposedbydefault=false" - " --entrypoints.web.address=:80" - " --entrypoints.websecure.address=:443" - " --entrypoints.web.http.redirections.entrypoint.to=websecure" - " --entrypoints.web.http.redirections.entrypoint.scheme=https" - " --certificatesresolvers.letsencrypt.acme.httpchallenge=true" - " --certificatesresolvers.letsencrypt.acme.httpchallenge.entrypoint=web" - " --certificatesresolvers.letsencrypt.acme.email=${LETSENCRYPT_EMAIL}" - " --certificatesresolvers.letsencrypt.acme.storage=/letsencrypt/acme.json" ports : - " 80:80" - " 443:443" volumes : - " ./letsencrypt:/letsencrypt" - " /var/run/docker.sock:/var/run/docker.sock:ro" restart : unless-stopped labelstudio : image : heartexlabs/label-studio:1.23.0 container_name : labelstudio expose : - " 8080" environment : - DJANGO_ALLOWED_HOSTS=${DOMAIN} - CSRF_TRUSTED_ORIGINS=https://${DOMAIN} - USE_X_FORWARDED_HOST=true - SECURE_PROXY_SSL_HEADER=HTTP_X_FORWARDED_PROTO,https volumes : - ./data:/label-studio/data labels : - " traefik.enable=true" - " traefik.http.routers.labelstudio.rule=Host(`${DOMAIN}`)" - " traefik.http.routers.labelstudio.entrypoints=websecure" - " traefik.http.routers.labelstudio.tls.certresolver=letsencrypt" - " traefik.http.services.labelstudio.loadbalancer.server.port=8080" restart : unless-stopped 2. Create the data directory with group write access: $ mkdir data $ sudo chown :0 data 3. Start the services: $ docker compose up -d 4. Verify the services and view logs: $ docker compose ps $ docker compose logs Create the Admin and a Sample Project 1. Open https://labelstudio.example.com and click Sign Up to create the first administrator. 2. From the dashboard, click Create Project and set: Project Name: Sentiment Analysis Labeling Template: Text Classification 3. Click Save , then Import and paste the sample data: [ { "text" : "This product is amazing." }, { "text" : "Worst experience ever." } ] 4. Annotate each task, click Submit , and confirm the Data Manager shows them as Completed . Next Steps Label Studio is running and served securely over HTTPS. From here you can: Configure ML backends (PyTorch, scikit-learn) for active learning loops Invite collaborators with role-based permissions per project Export annotated datasets in COCO, YOLO, JSON, or CSV for downstream training For the full guide with additional tips, visit the original article on Vultr Docs .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/vultr/deploying-label-studio-open-source-data-labeling-platform-on-ubuntu-2404-5bd0

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
