---
title: "Serverless Python: Deploying FastAPI to Google Cloud Run with Docker"
slug: "serverless-python-deploying-fastapi-to-google-cloud-run-with-docker"
author: "Ayush Kumar"
source: "devto_python"
published: "Tue, 14 Jul 2026 13:53:09 +0000"
description: "Introduction In my previous article , we built a high-performance Async API using FastAPI and SQLAlchemy 2.0. But code that only lives on localhost provides ..."
keywords: "run, docker, cloud, you, your, api, container, logicloop"
generated: "2026-07-14T13:57:07.326993"
---

# Serverless Python: Deploying FastAPI to Google Cloud Run with Docker

## Overview

Introduction In my previous article , we built a high-performance Async API using FastAPI and SQLAlchemy 2.0. But code that only lives on localhost provides zero value. Today, we are moving that API to production. We will containerize our application using Docker and deploy it to Google Cloud Run - a fully managed serverless platform that scales automatically. Why Cloud Run? Scale to Zero: You don't pay for servers when no one is using your API. Concurrency: Unlike AWS Lambda (which handles 1 request per instance), Cloud Run can handle 80+ requests per container concurrently. Portability: Since it's just a Docker container, you can move it to AWS or Azure later if you want. Step 1: The Dockerfile The first step is packaging our Python environment. Create a file named Dockerfile (no extension) in your project root. We will use a multi-stage build or a slim image to keep our container lightweight. Dockerfile # 1. Use an official lightweight Python image FROM python : 3.11 - slim # 2. Set environment variables # PYTHONDONTWRITEBYTECODE: Prevents Python from writing .pyc files # PYTHONUNBUFFERED: Ensures logs are flushed directly to terminal (critical for Cloud Logging) ENV PYTHONDONTWRITEBYTECODE = 1 ENV PYTHONUNBUFFERED = 1 # 3. Set the working directory WORKDIR / app # 4. Install dependencies # We copy requirements.txt first to leverage Docker cache COPY requirements . txt . RUN pip install -- no - cache - dir - r requirements . txt # 5. Copy the application code COPY . . # 6. Expose the port (Cloud Run defaults to 8080) EXPOSE 8080 # 7. Run the application # Host 0.0.0.0 is required for the container to be accessible from outside CMD [ " uvicorn " , " main:app " , " --host " , " 0.0.0.0 " , " --port " , " 8080 " ] Pro Tip: Make sure you have a requirements.txt file. You can generate one with pip freeze > requirements.txt . Step 2: Build & Test Locally Before pushing to the cloud, always test the container locally. Bash # Build the image docker build - t logicloop - api . # Run the container docker run - p 8080 : 8080 logicloop - api Go to http://localhost:8080/docs . If you see your Swagger UI, your container is valid. Step 3: Push to Google Artifact Registry Cloud Run pulls images from a registry. We will use Google's Artifact Registry (the successor to Container Registry). 1. Create a Repository (One time setup): Bash gcloud artifacts repositories create my - repo \ -- repository - format = docker \ -- location = us - central1 \ -- description = " Docker repository " 2. Tag your image: Replace PROJECT_ID with your actual Google Cloud Project ID. Bash docker tag logicloop - api us - central1 - docker . pkg . dev / PROJECT_ID / my - repo / logicloop - api : v1 3. Push the image: Bash docker push us - central1 - docker . pkg . dev / PROJECT_ID / my - repo / logicloop - api : v1 Step 4: Deploy to Cloud Run Now for the magic command. This tells Google to take that image and turn it into a live HTTPS endpoint. Bash gcloud run deploy logicloop - backend \ -- image us - central1 - docker . pkg . dev / PROJECT_ID / my - repo / logicloop - api : v1 \ -- platform managed \ -- region us - central1 \ -- allow - unauthenticated --allow-unauthenticated : Makes the API public (great for testing). For internal APIs, you would remove this. The Result: Google will spit out a URL that looks like: https://logicloop-backend-ue542.a.run.app Click it, add /docs , and congratulations - your API is live on the internet, secured with HTTPS automatically. Important Architecture Note: The Database If you followed my previous guide using SQLite , you need to know a critical Cloud Run limitation: The filesystem is ephemeral. If Cloud Run scales down or restarts your container (which happens often), your SQLite file is deleted and your data resets. For Production: You must connect this service to a managed database like Google Cloud SQL (Postgres) . You would pass the connection string as an Environment Variable: Bash gcloud run deploy logicloop - backend \ -- set - env - vars DATABASE_URL = " postgresql+asyncpg://user:pass@IP:5432/dbname " ... This keeps your application "stateless" (the code) while your data lives safely in a persistent "stateful" layer (the database). What's Next? We have Code and Deployment. But running docker build manually every time you change a line of code is painful. In the next article, we will automate this pipeline using GitHub Actions for a full CI/CD workflow.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ayush_kumar_085a0f2c54e3f/serverless-python-deploying-fastapi-to-google-cloud-run-with-docker-22g9

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
