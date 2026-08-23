---
title: "My first GitHub Project; from a local folder to GitHub using Git and SSH"
slug: "my-first-github-project-from-a-local-folder-to-github-using-git-and-ssh"
author: "Yop Gony Dak"
source: "devto_webdev"
published: "Sun, 23 Aug 2026 00:57:59 +0000"
description: "when i first heard about Git and GitHub ,I was really confused by the two terms .more words and concepts such as repository ,commit ,SSH key ,push ,pull, wer..."
keywords: "git, your, github, project, ssh, bash, first, commit"
generated: "2026-08-23T01:43:25.007582"
---

# My first GitHub Project; from a local folder to GitHub using Git and SSH

## Overview

when i first heard about Git and GitHub ,I was really confused by the two terms .more words and concepts such as repository ,commit ,SSH key ,push ,pull, were even more confusing .Knowing the definition alone did not make me understand better .instead of just going through the document provided by my institution i decided to do it practically so that i could learn more on these concepts .this article will cover how i carried out the practical exercise on my computer ,the process ,steps and the commands i used ,and my personal understanding from each step. Step 1: Setting Up Git Locally Before anything else, ensure Git is installed on your computer. You can check by running: bash git --version If it’s not installed, download it from a secure link. Next, configure your identity so Git knows who you are: bash git config --global user.name "Your Name" git config --global user .email " your.email@example.com " This information will appear in your commit history. Step 2: Initialize Your Local Project Navigate to your project folder and initialize Git: bash cd my-first-project git init This command creates a hidden .git directory that tracks changes in your project. Add your files to the staging area: bash git add . Then commit them with a message: bash git commit -m "Initial commit" Now your project is officially version-controlled! Step 3: Connect to GitHub Using SSH SSH (Secure Shell) allows you to connect to GitHub securely without typing your password every time. Generate an SSH key: bash ssh-keygen -t ed25519 -C " your.email@example.com " Copy your public key: bash cat ~/.ssh/id_ed25519.pub Then go to GitHub → Settings → SSH and GPG keys → New SSH key, paste it, and save. Test the connection: bash ssh-T git@github.com If you see a welcome message, you’re good to go! 4: Create a Remote Repository On GitHub, click New Repository, give it a name (e.g., my-first-project ), and choose whether it’s public or private. Copy the SSH URL—it should look like this: git@github.com :username/my-first-project.git Link your local folder to this remote repository: bash git remote add origin git@github.com :username/my-first-project.git 5: Push Your Code to GitHub Finally, send your local commits to GitHub: bash git push -u origin main After this, your project will appear online. You can now collaborate, track changes, and share your work with others. my Key Takeaways Git tracks your project history locally. GitHub hosts your code online for collaboration. SSH provides secure, password-free access. The basic workflow is: init → add → commit → push. my Final Thoughts Setting up my first GitHub project is a milestone in my developer journey. Once i,ve done it, i realize how powerful version control can be—not just for saving my work, but for learning, collaborating, and growing.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dakgony2022arch/my-first-github-project-from-a-local-folder-to-github-using-git-and-ssh-k1e

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
