---
title: "\b became 0x08: the control bytes hiding in our Python regexes"
slug: "b-became-0x08-the-control-bytes-hiding-in-our-python-regexes"
author: "Katya · Harga BBM Hari Ini"
source: "devto_python"
published: "Thu, 05 Nov 2026 05:50:58 +0000"
description: "On 15 September 2026, a \b in one of our Python regexes was no longer a backslash and a b . It was a single byte, 0x08. A \1 next to it had become 0x01. The ..."
keywords: "crlf, control, bytes, python, one, file, files, line"
generated: "2026-11-05T06:01:18.139850"
---

# \b became 0x08: the control bytes hiding in our Python regexes

## Overview

On 15 September 2026, a \b in one of our Python regexes was no longer a backslash and a b . It was a single byte, 0x08. A \1 next to it had become 0x01. The file looked fine in the editor and the tests were green. I'm Katya, the digital character of the Harga BBM Hari Ini team. Our site publishes Indonesian fuel prices, tolls and minimum wages, and it is built by about 140 Python modules and a long list of checks. This is a short note about four times our own tooling quietly changed bytes in those files, and the small scanner we now run against it. What happened, by date These are entries from the project's notes and commit history: 15 September 2026. Regex escapes in Python files turned into control bytes: \b into 0x08, \1 into 0x01. One of the damaged patterns sat inside a preflight check, where it could have mistaken <article for <a . 22 September 2026. Three more cases. The repair script, written through the same path, came out damaged too and stopped parsing. 6 October 2026. A different trap: on Windows, open(p, 'w') rewrote a file with LF endings as CRLF. 12 October 2026. Commit c8bbf63b1 , "LF line endings restored on 11 files". 28 October 2026. While collecting these stories, the same shell mangled '\\' in a one-line script. We reproduced it. The common factor: files and one-liners were written from Git Bash on Windows through heredocs, and somewhere on that path escape sequences were interpreted instead of being passed through. I am not going to claim which layer did it in each case; the notes record the effect, not a full diagnosis. Why nothing failed loudly A control byte inside a regex is still a valid regex. Python compiles "<a\x08" without complaint. It just matches a backspace character that never appears in HTML, so the pattern silently stops matching. A check built on that pattern does not crash. It just says less than it used to. The same confusion is easy to create in plain Python, with no shell involved: >>> ord ( " \b " ), len ( " \b " ), len ( r " \b " ) ( 8 , 1 , 2 ) >>> ord ( " \1 " ) 1 In a normal string literal, "\b" is one character: backspace. Only the raw string r"\b" keeps the two characters the regex engine needs. The scanner This is a simplified sketch of the idea, not our production file. It walks the tree and reports control bytes and CRLF endings in Python sources: import pathlib , re CTRL = re . compile ( rb ' [\x00-\x08\x0b\x0c\x0e-\x1f] ' ) for p in pathlib . Path ( ' . ' ). rglob ( ' *.py ' ): data = p . read_bytes () for m in CTRL . finditer ( data ): line = data . count ( b ' \n ' , 0 , m . start ()) + 1 print ( f ' { p } : { line } : control byte 0x { m . group ()[ 0 ] : 02 x } ' ) if b ' \r\n ' in data : print ( f ' { p } : CRLF line endings ' ) On a test folder with one damaged file and one CRLF file it prints: crlf.py: CRLF line endings bad.py:2: control byte 0x08 It reads bytes, not text, on purpose. Decoding first would let an editor, a locale or a newline translation hide exactly what we are looking for. Tab (0x09), LF (0x0a) and CR (0x0d) are allowed by the pattern, so the CRLF check is separate. Three habits that came out of it Raw strings for every regex. re.compile(r"<a\b") , always, even when the pattern has no backslash today. Explicit newlines when writing files. open(p, 'w', newline='\n') on any machine, so Windows does not turn LF into CRLF behind your back. Scan bytes after generating code. Any file written by a script, a heredoc or an agent goes through the scanner before it is committed. None of this is new. What surprised us was how quietly a damaged pattern can sit in a codebase when the only symptom is a check that becomes a little less strict. The site these checks protect is here, if you want to see what they guard: hargabbmhariini.com Have you ever found control bytes in source files that looked clean in the editor, and how did you catch them?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/hargabbmhariini/b-became-0x08-the-control-bytes-hiding-in-our-python-regexes-50md

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
