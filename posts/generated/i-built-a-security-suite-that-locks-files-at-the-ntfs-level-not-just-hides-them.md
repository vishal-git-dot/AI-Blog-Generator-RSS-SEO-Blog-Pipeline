---
title: "I Built a Security Suite That Locks Files at the NTFS Level (Not Just Hides Them)"
slug: "i-built-a-security-suite-that-locks-files-at-the-ntfs-level-not-just-hides-them"
author: "Akhouri Anmol Kumar"
source: "devto_python"
published: "Tue, 08 Sep 2026 10:54:03 +0000"
description: "Your files aren't actually protected. They're just hidden. Right-click → Properties → Hidden. That's what most "file lockers" do. Rename a folder, mark it hi..."
keywords: "your, atlock, password, akhouri, security, files, ntfs, level"
generated: "2026-09-08T10:58:23.960856"
---

# I Built a Security Suite That Locks Files at the NTFS Level (Not Just Hides Them)

## Overview

Your files aren't actually protected. They're just hidden. Right-click → Properties → Hidden. That's what most "file lockers" do. Rename a folder, mark it hidden, call it a day. Anyone with five minutes and a Google search opens it anyway. I got tired of that lie, so I built ATLOCK v4 — a Windows security suite that locks files at the NTFS ACL level, meaning the OS itself refuses to open them without your key. Not obfuscation. Actual permission-level denial. What it actually does 🔒 File Guard — Locks files using Windows' own NTFS access control lists. No password stored in a text file to steal. No "hidden" flag to toggle off. The filesystem says no. 🗝️ Password Vault — Fernet (AES-128-CBC + HMAC) encrypted storage for emails, UPI IDs, PINs, whatever you don't want floating around in plaintext. Master password runs through PBKDF2-HMAC-SHA256 at 200,000 iterations with a random salt — the same class of KDF hardening you'd expect from a password manager, not a side project. ⚡ System Lockdown — One click, full OS-level lock with a countdown. Walk away from your desk without walking away from your data. 📸 Intruder Ops — Get a wrong password once, ATLOCK silently snaps a photo. Get it wrong three or four times, it records a 10-second video and sounds an alarm. Everything drops straight into your own Pictures/Videos folder — nothing phones home. The stack Python · customtkinter · OpenCV · cryptography (Fernet/PBKDF2) pywin32 (NTFS ACL manipulation) · PyInstaller A gold-on-black UI because security software doesn't have to look like it was designed in 2004. Why this version matters v4 is a full security hardening pass over earlier builds. The vault used to run on XOR — which, let's be honest, isn't cryptography, it's a suggestion. Now it's real Fernet AES with HMAC integrity checks. Intruder attempts are masked before they ever touch a log file. Alert credentials are encrypted with a machine-bound key instead of sitting in plaintext config. The difference between "looks secure" and "is secure" is usually about 200,000 PBKDF2 iterations and a healthy distrust of your own past decisions. Try it ATLOCK v4 is live now — https://akhouri-anmol-kumar.github.io/Akhouri-systems/ ATLOCK v4 Repo Link 🔗 : https://github.com/Akhouri-Anmol-Kumar/ATLOCK If you're the kind of developer who reads cryptography docs for fun, I'd genuinely love feedback on the vault implementation. Break it, tell me how, I'll fix it. Built solo by Akhouri Anmol Kumar under Akhouri Systems. ATLOCK "We Build What Others Forgot To Fix"

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/akhourianmolkumar/i-built-a-security-suite-that-locks-files-at-the-ntfs-level-not-just-hides-them-bid

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
