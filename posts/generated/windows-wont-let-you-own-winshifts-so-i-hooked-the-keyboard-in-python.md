---
title: "Windows won't let you own Win+Shift+S. So I hooked the keyboard in Python."
slug: "windows-wont-let-you-own-winshifts-so-i-hooked-the-keyboard-in-python"
author: "Akhouri Anmol Kumar"
source: "devto_python"
published: "Sat, 07 Nov 2026 04:51:12 +0000"
description: "I wanted one small thing: press Win+Shift+S and get my own screenshot tool instead of Snipping Tool. That turned into a 7,600-line Python project, and a pile..."
keywords: "ctypes, you, windows, win, can, python, one, key"
generated: "2026-11-07T05:28:40.830919"
---

# Windows won't let you own Win+Shift+S. So I hooked the keyboard in Python.

## Overview

I wanted one small thing: press Win+Shift+S and get my own screenshot tool instead of Snipping Tool. That turned into a 7,600-line Python project, and a pile of Windows internals that I couldn't find explained in one place. Here are the four that cost me the most hair. 1. RegisterHotKey can't claim Win+Shift+S Every tutorial says to use RegisterHotKey . It works for Ctrl+Alt+D . It silently fails for Win+Shift+S , because the shell reserves that combo. The way around it is a low-level keyboard hook ( WH_KEYBOARD_LL , id 13 ), which sees the key before the shell does: HOOKPROC = ctypes . WINFUNCTYPE ( ctypes . c_ssize_t , ctypes . c_int , ctypes . c_size_t , ctypes . c_ssize_t ) def cb ( nCode , wParam , lParam ): if nCode == 0 and wParam in ( 0x100 , 0x101 , 0x104 , 0x105 ): kb = ctypes . cast ( lParam , ctypes . POINTER ( KBDLLHOOKSTRUCT )). contents if kb . vkCode == 0x53 and win_down () and shift_down (): # S u . keybd_event ( 0xE8 , 0 , 0 , 0 ) # see below u . keybd_event ( 0xE8 , 0 , 2 , 0 ) QTimer . singleShot ( 0 , on_trigger ) # hop back to the Qt thread return 1 # swallow the key return u . CallNextHookEx ( None , nCode , wParam , lParam ) self . _proc = HOOKPROC ( cb ) # keep a reference! hook = u . SetWindowsHookExW ( 13 , self . _proc , k . GetModuleHandleW ( None ), 0 ) Three gotchas worth knowing: Keep a reference to the callback. If HOOKPROC(cb) gets garbage-collected, your app crashes on the next keypress. There's no traceback, it just dies. Swallowing S isn't enough. If you eat the keypress and the user then releases Win , Windows opens the Start menu. The fix is to inject an unassigned virtual key ( 0xE8 ) so Windows thinks Win was used in a combo. Track the key-up too. If you swallow the key-down, you have to swallow its matching key-up, or apps see an orphaned release. I pulled this into a pure function ( snip_hook_decision(...) ) with no ctypes in it, so it's unit-testable. The hook only looks at the specific keys it cares about while Win+Shift are held. Nothing is logged or stored. If you ship a keyboard hook, say that in your README. 2. Keeping your own UI out of your own recording My screen recorder has a floating control bar. Early on, every video started with the recorder recording itself, which looks amateur. Windows 10 (2004+) has a one-line fix: WDA_EXCLUDEFROMCAPTURE = 0x11 ctypes . windll . user32 . SetWindowDisplayAffinity ( int ( widget . winId ()), WDA_EXCLUDEFROMCAPTURE ) The window stays visible to the user but is invisible to capture APIs. It's best-effort on older builds, so wrap it in try/except and move on. 3. System audio in Python: sounddevice can't do it Recording the microphone is easy. Recording what the PC is playing is not. sounddevice can't do WASAPI loopback. What worked: Source Library Microphone sounddevice System audio (loopback) PyAudioWPatch Mixing + muxing into MP4 imageio-ffmpeg (bundles an ffmpeg binary) The part that matters: don't mix in real time. I record each source to its own WAV on disk, then mix once after the take with ffmpeg's amix . Real-time mixing means two clocks drifting against each other. Post-mixing means a dropped buffer in one stream can't corrupt the other. I also pad or trim each track to exactly the video duration before mixing, because mic and loopback streams never end at the same millisecond. 4. OCR with zero extra installs I wanted "select text from a screenshot" without telling users to install Tesseract. Windows 10/11 already ships an OCR engine: Windows.Media.Ocr . You can reach it from PowerShell, so Python just shells out: subprocess . run ( [ " powershell " , " -NoProfile " , " -ExecutionPolicy " , " Bypass " , " -File " , ps1 ], capture_output = True , timeout = 120 , creationflags = 0x08000000 , # CREATE_NO_WINDOW, no console flash ) The PowerShell script tries the user's language packs first and falls back to whatever recognizer is available. It runs in a QThread , so the UI never freezes. The result: no models to download, no 200 MB dependency, and it works offline. Small things that made it feel finished Recycle Bin, not delete. os.remove is permanent. SHFileOperationW with FOF_ALLOWUNDO sends files to the Recycle Bin, so "delete capture" is never scary. Atomic settings. Write to settings.json.tmp , then os.replace() . A crash mid-write can't corrupt your config. Single instance. A named mutex ( CreateMutexW + check for error 183 ) stops two copies fighting over the same global hotkeys. Autostart is one registry value under HKCU\...\Run . No installer needed. Where all this ended up All of the above lives in ASNIPP , a screenshot tool, screen recorder and editor that sits as a small "Dynamic Island" pill at the top of your screen. The parts I'm proudest of: Screenshots with pen, highlighter, arrows, shapes, text and pixelate (for hiding sensitive info) A color picker with a magnifier loupe, and a pixel ruler Pin-to-screen floating captures Screen recording with system audio and mic, plus live drawing that gets recorded into the video A built-in video editor: trim, speed, reverse, color looks, fades, rotate and GIF export OCR on any capture It's one 7600+ lines of python code packed into .exe, PyQt6, mss for capture and OpenCV for video. If you've ever wondered how far a python desktop app can go, it's a decent case study. 👉 [ https://github.com/Akhouri-Systems/ASNIPP/releases/download/v1.0.0/ASNIPP_v1.zip ] If you've built something with ctypes and Win32, I'd love to hear what bit you. Drop it in the comments.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/akhourianmolkumar/windows-wont-let-you-own-winshifts-so-i-hooked-the-keyboard-in-python-248c

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
