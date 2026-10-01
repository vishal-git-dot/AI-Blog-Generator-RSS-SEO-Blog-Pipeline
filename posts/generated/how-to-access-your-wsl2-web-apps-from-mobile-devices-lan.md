---
title: "How to Access Your WSL2 Web Apps from Mobile Devices & LAN"
slug: "how-to-access-your-wsl2-web-apps-from-mobile-devices-lan"
author: "Logifire"
source: "devto_webdev"
published: "Thu, 01 Oct 2026 22:10:47 +0000"
description: "If you use WSL2 (Windows Subsystem for Linux) for web development, you've likely hit this wall: you start a development server (Vite, Next.js, Node, Django, ..."
keywords: "firewall, your, you, wsl, hyperv, windows, rules, hyper"
generated: "2026-10-01T22:31:42.469027"
---

# How to Access Your WSL2 Web Apps from Mobile Devices & LAN

## Overview

If you use WSL2 (Windows Subsystem for Linux) for web development, you've likely hit this wall: you start a development server (Vite, Next.js, Node, Django, Docker), open http://localhost:3000 on your Windows host, and everything works seamlessly. Then you grab your mobile phone or another device on the same Wi-Fi network to test responsive design or mobile-specific behavior... Connection Refused or Request Timed Out . I spent hours struggling with this exact issue before discovering why standard Windows Firewall solutions don't work for WSL2. Here is a clear explanation of the root cause and a simple, automated fix. The Root Cause: Why Standard Firewall Rules Fail WSL2 does not run as a native Windows process. It operates inside a lightweight Hyper-V Virtual Machine behind a virtual network adapter. Because of this architecture: Classic Windows Defender Firewall rules ( wf.msc or New-NetFirewallRule ) apply to the host OS, not to traffic passing into the Hyper-V virtual network. Even if you allow port 3000 in wf.msc or configure port forwarding, the Hyper-V Firewall isolation layer blocks incoming traffic originating from your LAN. To allow external network traffic into WSL2, Windows requires specific Hyper-V firewall rules created via New-NetFirewallHyperVRule using WSL's specific VMCreatorId . These rules live in a separate firewall store and do not show up in the classic wf.msc GUI . The Solution: A Simple 1-Command Fix To streamline this process, I created an open-source utility script that automatically resolves the WSL Hyper-V container ID, creates persistent Hyper-V firewall rules, and manages port exposure effortlessly. 📦 Download Ready-to-Use Package: Release 0.1 ( wsl-hyperv-firewall.zip ) 🔗 GitHub Repository: Logifire/wsl-hyperv-firewall Step-by-Step Guide: Accessing WSL2 from Mobile Step 1: Bind Your Dev Server to 0.0.0.0 By default, most development servers only listen on 127.0.0.1 (localhost). You must instruct your server to listen on all network interfaces: Vite / Vue / Svelte: npm run dev -- --host 0.0.0.0 Next.js: npm run dev -- -H 0.0.0.0 -p 3000 (or npx next dev -H 0.0.0.0 ) Python HTTP Server: python -m http.server 8000 --bind 0.0.0.0 Node.js / Express: Ensure your app uses app.listen(3000, '0.0.0.0') Step 2: Open the Port in Hyper-V Firewall Download wsl-hyperv-firewall.zip from the latest release and extract it (or clone the repository). Right-click wsl-hyperv-firewall.bat and select Run as administrator . You can run commands directly from PowerShell/CMD: # Syntax: .\wsl-hyperv-firewall.bat add <port> . \wsl-hyperv-firewall.bat add 5173 (Alternatively, running wsl-hyperv-firewall.bat without arguments launches an interactive prompt where you can simply type add 5173 ). Step 3: Find Your Windows Local IP Address In PowerShell or CMD on Windows, check your LAN IP address: ipconfig Look for IPv4 Address under your active Wi-Fi or Ethernet adapter (e.g., 192.168.1.150 ). Step 4: Connect from Your Mobile Device Ensure your mobile device is connected to the same Wi-Fi network. Open your browser on the phone and navigate to: http://192.168.1.150:5173 Your dev server running inside WSL2 will now load immediately! Managing Your Rules You can list all active Hyper-V rules created by the script or remove them when you finish testing: # List active WSL Hyper-V rules . \wsl-hyperv-firewall.bat list # Remove rule when testing is complete . \wsl-hyperv-firewall.bat remove 5173 Note: Rules created with New-NetFirewallHyperVRule are persistent across reboots, so you don't need to re-add them every time you restart your machine. Summary If you are developing inside WSL2 and need mobile or cross-device network testing on your LAN, traditional firewall tweaks won't cut it. Opening ports via New-NetFirewallHyperVRule is the clean, native Windows solution. Download the zip archive or check out the full source code on GitHub: 👉 github.com/Logifire/wsl-hyperv-firewall Feel free to star the repo or drop a comment if this solved your WSL2 networking headaches! Written with AI assistance.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/logifire/how-to-access-your-wsl2-web-apps-from-mobile-devices-lan-37lf

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
