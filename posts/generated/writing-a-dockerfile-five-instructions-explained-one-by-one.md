---
title: "Writing a Dockerfile: five instructions, explained one by one"
slug: "writing-a-dockerfile-five-instructions-explained-one-by-one"
author: "Nduka NZEKA"
source: "devto_python"
published: "Wed, 25 Nov 2026 21:23:30 +0000"
description: "To run your Python app with Docker, you first need a Dockerfile. It is the recipe for your image: a text file, named Dockerfile , that lists the steps to bui..."
keywords: "image, app, one, run, docker, copy, you, build"
generated: "2026-11-25T21:26:57.088574"
---

# Writing a Dockerfile: five instructions, explained one by one

## Overview

To run your Python app with Docker, you first need a Dockerfile. It is the recipe for your image: a text file, named Dockerfile , that lists the steps to build it. We made a 28-second video that goes through the five instructions you need: tiktok.com You can also watch it on our site: Writing a Dockerfile . The rest of this post goes through each instruction of the video, with the code. The app A folder with two files: the code and the list of its dependencies. my-app/ ├── app.py └── requirements.txt The whole Dockerfile Here is the file from the video. It goes at the root of the folder: FROM ubuntu:22.04 WORKDIR /app COPY . . RUN apt-get update && apt-get install -y python3 python3-pip \ && pip3 install -r requirements.txt CMD [ "python3" , "app.py" ] Five instructions, read from top to bottom. FROM picks the starting image FROM ubuntu:22.04 An image almost always starts from an existing one. Here, Ubuntu 22.04, pulled from Docker Hub. It contains a minimal Ubuntu system and nothing else: no Python, no code of yours. The part after the colon is the tag, which is the version. Always write one. Without it, Docker takes latest , and your build may change the day a new version comes out. WORKDIR sets the working folder WORKDIR /app The instructions that follow ( COPY , RUN , CMD ) work from /app , inside the image. If the folder does not exist, Docker creates it. It is the cd of the Dockerfile, and it stays in effect when the container starts. COPY copies your code into it COPY . . Two paths: the first one is on your machine, the second one is in the image. The first dot is the build context, the folder you give to docker build . The second one is the working folder, so /app . After this line, app.py and requirements.txt are in the image, along with everything else in the folder. RUN installs your dependencies RUN apt-get update && apt-get install -y python3 python3-pip \ && pip3 install -r requirements.txt RUN executes a command while the image is being built, and keeps the result in the image. Here it installs Python, which the Ubuntu image does not have, then the packages listed in requirements.txt . The -y matters: nobody is there to answer "yes" during a build. CMD tells Docker which command to run at startup CMD [ "python3" , "app.py" ] CMD does nothing during the build. It records the default command, the one that runs when a container starts from the image. You can replace it for one run by adding a command after the image name: docker run my-app python3 other.py . The form with brackets starts the program directly, without a shell in between, so it receives the stop signal when you stop the container. RUN and CMD are easy to mix up: When How many RUN While the image is built As many as you need CMD When a container starts One: if you write several, only the last one counts Every instruction adds a layer An image is not one block. Each instruction adds a step on top of the previous ones, and Docker keeps the result of each step in its build cache. You can see them, once the image is built: docker history my-app To be precise, the instructions that change files ( COPY , RUN ) add a layer of files, and that is where the size of the image comes from. CMD only records a setting: it shows up in the history with a size of 0B. This is why the order of the lines matters. When you build again, Docker reuses the cache until it reaches a line that changed, or a COPY whose files changed. From that line on, everything is rebuilt. In the file above, COPY . . comes before RUN . Change one character in app.py and Docker installs Python and all the packages again. Going one step further The file above is the simplest one to read, not the one to ship. Once the five instructions are clear, two changes make the image faster to build and much lighter: FROM python:3.13-slim WORKDIR /app COPY requirements.txt . RUN pip install --no-cache-dir -r requirements.txt COPY . . CMD [ "python" , "app.py" ] Start from an image that already has Python. python:3.13-slim saves the apt-get step, and the image is much smaller than the one built on Ubuntu. --no-cache-dir keeps pip's download cache out of it. Copy requirements.txt first, the code after. The packages are reinstalled only when the list of dependencies changes. A change in app.py rebuilds the last COPY alone. COPY . . takes everything in the folder, including a .env file with your passwords if there is one. Add a .dockerignore file next to the Dockerfile to leave out what has no place in the image: .git .env __pycache__ venv There is more to a production image, starting with not running the app as root. That is for another post. Next The Dockerfile is only the recipe. Building the image and running a container takes two commands: docker build -t my-app . docker run my-app That is part 2 of the series: Building and running a container . This video is part of a short series on Docker by Ilaria Digital School , an online tech school with live, instructor-led classes. Docker is taught in our Full-Stack Software Developer Pathway .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ilariadigitalschool/writing-a-dockerfile-five-instructions-explained-one-by-one-3kgc

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
