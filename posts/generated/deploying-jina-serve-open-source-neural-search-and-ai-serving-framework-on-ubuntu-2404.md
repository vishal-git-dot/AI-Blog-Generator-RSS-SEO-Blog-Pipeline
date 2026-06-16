---
title: "Deploying Jina Serve Open-Source Neural Search and AI Serving Framework on Ubuntu 24.04"
slug: "deploying-jina-serve-open-source-neural-search-and-ai-serving-framework-on-ubuntu-2404"
author: "Sanskriti Harmukh"
source: "devto_ai"
published: "Tue, 16 Jun 2026 20:55:00 +0000"
description: "Jina Serve is an open-source framework for building neural search and multimodal AI applications, with a cloud-native runtime that handles dynamic batching, ..."
keywords: "jina, executor, flow, text, docker, traefik, letsencrypt, search"
generated: "2026-06-16T21:09:41.017682"
---

# Deploying Jina Serve Open-Source Neural Search and AI Serving Framework on Ubuntu 24.04

## Overview

Jina Serve is an open-source framework for building neural search and multimodal AI applications, with a cloud-native runtime that handles dynamic batching, async streaming, and microservice orchestration. This guide deploys a Jina Flow with a custom text executor using Docker Compose, with Traefik handling automatic HTTPS in front of the gateway. By the end, you'll have a Jina Flow serving an /index and /search API securely at your domain. Set Up the Directory Structure 1. Create the project directory structure: $ mkdir -p ~/jina-serve/executor $ cd ~/jina-serve 2. Create the executor module: $ nano executor/executor.py from jina import Executor , requests from docarray import BaseDoc , DocList class TextDoc ( BaseDoc ): text : str = "" class TextProcessor ( Executor ): @requests ( on = " /index " ) def index ( self , docs : DocList [ TextDoc ], ** kwargs ) -> DocList [ TextDoc ]: for doc in docs : if doc . text : doc . text = doc . text . upper () return docs @requests ( on = " /search " ) def search ( self , docs : DocList [ TextDoc ], ** kwargs ) -> DocList [ TextDoc ]: return docs 3. Pin the executor's Python dependencies: $ nano executor/requirements.txt jina==3.34.0 docarray>=0.40.0 4. Wire the executor into Jina's loader: $ nano executor/config.yml jtype : TextProcessor py_modules : - executor.py 5. Define the Flow: $ nano flow.yml jtype : Flow with : protocol : http port : 8080 executors : - name : textprocessor uses : executor/config.yml 6. Build the container image with the Flow baked in: $ nano Dockerfile FROM jinaai/jina:3.34.0-py39-standard WORKDIR /app COPY executor/requirements.txt /app/executor/requirements.txt RUN pip install --no-cache-dir -r /app/executor/requirements.txt COPY executor /app/executor COPY flow.yml /app/flow.yml ENTRYPOINT ["jina", "flow", "--uses", "flow.yml"] 7. Create the environment file: $ nano .env DOMAIN = jina.example.com LETSENCRYPT_EMAIL = admin@example.com JINA_LOG_LEVEL = INFO Deploy with Docker Compose 1. Create the Compose manifest: $ nano docker-compose.yml services : traefik : image : traefik:v3.6 container_name : traefik command : - " --providers.docker=true" - " --providers.docker.exposedbydefault=false" - " --entrypoints.web.address=:80" - " --entrypoints.websecure.address=:443" - " --entrypoints.web.http.redirections.entrypoint.to=websecure" - " --entrypoints.web.http.redirections.entrypoint.scheme=https" - " --certificatesresolvers.letsencrypt.acme.httpchallenge=true" - " --certificatesresolvers.letsencrypt.acme.httpchallenge.entrypoint=web" - " --certificatesresolvers.letsencrypt.acme.email=${LETSENCRYPT_EMAIL}" - " --certificatesresolvers.letsencrypt.acme.storage=/letsencrypt/acme.json" ports : - " 80:80" - " 443:443" volumes : - " /var/run/docker.sock:/var/run/docker.sock:ro" - " ./letsencrypt:/letsencrypt" restart : unless-stopped jina : build : context : . dockerfile : Dockerfile container_name : jina-flow environment : - JINA_LOG_LEVEL=${JINA_LOG_LEVEL} expose : - " 8080" labels : - " traefik.enable=true" - " traefik.http.routers.jina.rule=Host(`${DOMAIN}`)" - " traefik.http.routers.jina.entrypoints=websecure" - " traefik.http.routers.jina.tls.certresolver=letsencrypt" - " traefik.http.services.jina.loadbalancer.server.port=8080" restart : unless-stopped 2. Build and start the stack: $ docker compose up -d --build 3. Verify the services and tail logs: $ docker compose ps $ docker compose logs Verify the Gateway 1. Check the status endpoint: $ curl https://jina.example.com/status { "jina" :{ "jina" : "3.34.0" , "docarray" : "0.40.1" ... 2. POST a document to /index : $ curl -X POST https://jina.example.com/index \ -H "Content-Type: application/json" \ -d '{"data": [{"text": "hello world"}]}' { "data" :[{ "id" : null , "text" : "HELLO WORLD" }], ... } 3. POST to /search to see the passthrough endpoint: $ curl -X POST https://jina.example.com/search \ -H "Content-Type: application/json" \ -d '{"data": [{"text": "test message"}]}' 4. Submit a batch of documents: $ curl -X POST https://jina.example.com/index \ -H "Content-Type: application/json" \ -d '{"data": [{"text": "first"}, {"text": "second"}, {"text": "third"}]}' Next Steps Jina Serve is running and serving requests over HTTPS. From here you can: Add more executors to the Flow for pre-processing, embedding, and ranking Switch the runtime to GPU images for accelerated inference Persist embeddings in Qdrant, Weaviate, or other vector stores For the full guide with additional tips, visit the original article on Vultr Docs .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/vultr/deploying-jina-serve-open-source-neural-search-and-ai-serving-framework-on-ubuntu-2404-1m8g

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
