---
title: "The cp932 crash in the build gate that only happened on Windows — static detection, behavioral testing, and a negative check"
slug: "the-cp932-crash-in-the-build-gate-that-only-happened-on-windows-static-detection-behavioral-testing-and-a-negative-check"
author: "Susumu Takahashi"
source: "devto_python"
published: "Wed, 19 Aug 2026 01:26:25 +0000"
description: "The symptom During the Windows build for v1.6.11, the build gate reported "version number consistency check failed." But the version numbers were correct eve..."
keywords: "build, windows, utf, check, gate, tools, subprocess, emoji"
generated: "2026-08-19T01:37:09.903487"
---

# The cp932 crash in the build gate that only happened on Windows — static detection, behavioral testing, and a negative check

## Overview

The symptom During the Windows build for v1.6.11, the build gate reported "version number consistency check failed." But the version numbers were correct everywhere. The real cause was not a version mismatch. The build gate in build_app.py calls tools/bump_version.py via subprocess and checks its exit code. The success messages in bump_version.py contained emoji (✅ and similar). On Japanese Windows, the default code page is cp932, which cannot encode those characters. Python raised a UnicodeEncodeError on the very first write to stdout, the process exited non-zero, and the build gate misread that as a version inconsistency. UnicodeEncodeError: 'cp932' codec can't encode character '✅' in position 0 Why it didn't show up on Mac macOS terminals use UTF-8 by default. Running bump_version.py directly or via subprocess on Mac produces no encoding errors — emoji flows through cleanly. On Japanese Windows, the process inherits the cp932 code page. U+2705 (✅) has no cp932 representation, so the write fails immediately. Because the build was always done on Mac first, this failure had no chance to appear in local testing. It only surfaced when the Windows build ran. Fix 1 — replace emoji with ASCII All emoji in tools/bump_version.py output were replaced with ASCII equivalents. # Before print ( f " ✅ { file } : { old } → { new } " ) print ( f " ❌ NG: { file } " ) # After print ( f " [OK] { file } : { old } → { new } " ) print ( f " [NG] { file } " ) Emoji in terminal output can be helpful, but when output is consumed by another process over a pipe, encoding compatibility cannot be assumed. Tools invoked from build scripts should limit their output to ASCII. Fix 2 — force UTF-8 in the subprocess call The build gate was also updated to enforce UTF-8 on its end. result = subprocess . run ( [ sys . executable , " tools/bump_version.py " , " --check " ], capture_output = True , encoding = " utf-8 " , errors = " replace " , env = { ** os . environ , " PYTHONUTF8 " : " 1 " , " PYTHONIOENCODING " : " utf-8 " }, ) PYTHONUTF8=1 forces UTF-8 for stdin/stdout/stderr in Python 3.7+. PYTHONIOENCODING=utf-8 covers older-style enforcement. errors="replace" prevents a crash if any unencodable character slips through — defense in depth. Fix 3 — three-layer regression guard in test_windows_cp932_safety.py Fixing the bug is not enough if the same failure can re-emerge. Three test layers were added to catch it before it reaches Windows. Layer 1 — static detection : read the source file and verify that no cp932-incompatible character is present. def test_bump_version_no_cp932_unsafe_chars (): src = pathlib . Path ( " tools/bump_version.py " ). read_text ( encoding = " utf-8 " ) for i , ch in enumerate ( src ): try : ch . encode ( " cp932 " ) except ( UnicodeEncodeError , UnicodeDecodeError ): raise AssertionError ( f " cp932-unsafe char U+ { ord ( ch ) : 04 X } at pos { i } : { ch !r} " ) Layer 2 — behavioral verification : run bump_version.py --check in a subprocess with PYTHONIOENCODING=cp932 set and assert that it exits 0. def test_bump_version_check_runs_under_cp932 (): result = subprocess . run ( [ sys . executable , " tools/bump_version.py " , " --check " ], capture_output = True , env = { ** os . environ , " PYTHONIOENCODING " : " cp932 " }, ) assert result . returncode == 0 , result . stderr Layer 3 — negative check : inject an emoji intentionally and confirm that layer 1 raises AssertionError . This ensures the detector cannot become a test that always passes. def test_cp932_detector_catches_emoji (): with pytest . raises ( AssertionError ): src = " print( ' ✅ ok ' ) " for ch in src : ch . encode ( " cp932 " ) What to take away When development and builds both happen on Mac, Windows-specific encoding failures have nowhere to appear until the Windows build runs. The failure mode here — correct Mac behavior, crash on Windows, misread error message pointing at the wrong cause — is easy to miss and easy to misdiagnose. Designing tests that simulate Windows encoding constraints on Mac, before the Windows build, catches this category of failure at the CI level rather than at the point of release. Related: Version bump oversights — a single-source script with a --check gate

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/susumun/the-cp932-crash-in-the-build-gate-that-only-happened-on-windows-static-detection-behavioral-mpd

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
