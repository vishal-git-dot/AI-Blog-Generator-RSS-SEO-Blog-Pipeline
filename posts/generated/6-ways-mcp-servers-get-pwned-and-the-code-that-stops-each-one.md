---
title: "6 ways MCP servers get pwned — and the code that stops each one"
slug: "6-ways-mcp-servers-get-pwned-and-the-code-that-stops-each-one"
author: "MCP Security Notes"
source: "devto_python"
published: "Tue, 11 Aug 2026 06:47:02 +0000"
description: "MCP (Model Context Protocol) servers hand an LLM real tools: read a file, run a command, fetch a URL. The problem: the arguments to those tools are driven by..."
keywords: "load, path, mcp, not, true, yaml, servers, code"
generated: "2026-08-11T07:15:40.513958"
---

# 6 ways MCP servers get pwned — and the code that stops each one

## Overview

MCP (Model Context Protocol) servers hand an LLM real tools: read a file, run a command, fetch a URL. The problem: the arguments to those tools are driven by untrusted content — a web page, a document, another model. That is a textbook injection surface, and MCP servers are shipping with the same six holes over and over. Here is each one with a copy-paste fix. 1. Path traversal → arbitrary file read A read_file tool that does open(base + user_path) leaks /etc/passwd the moment the model is told to read ../../../../etc/passwd . Symlinks and absolute paths bypass naive prefix checks. from pathlib import Path def resolve_within ( base : str , user_path : str ) -> Path | None : base_p = Path ( base ). resolve () target = ( base_p / user_path ). resolve () # resolves .. and symlinks if base_p not in target . parents and target != base_p : return None # refuse, don't clamp return target Refuse on None . Never "clean" the path and continue — that is how the regression re-opens. 2. Command execution → RCE subprocess.run(f"convert {name}", shell=True) is game over. Any tool arg the model influences is attacker-controlled. subprocess . run ([ " convert " , name ], shell = False , timeout = 10 ) # argv list, never a string Whitelist the args the user actually controls; reject anything not on the list. 3. Unsafe deserialization → RCE pickle.load , torch.load (pre-2.6 default), yaml.load without a safe loader, and numpy.load(allow_pickle=True) all execute code on load. This is huntr's most-paid MCP/AI bug class. import yaml yaml . safe_load ( data ) # not yaml.load torch . load ( f , weights_only = True ) # not the default on old versions # for models: prefer safetensors over pickle entirely 4. SSRF in URL-fetching tools A fetch_url tool will happily hit http://169.254.169.254/ (cloud metadata) or http://localhost:6379 . Resolve the host and block private ranges before connecting. import ipaddress , socket def is_public ( host : str ) -> bool : ip = ipaddress . ip_address ( socket . gethostbyname ( host )) return not ( ip . is_private or ip . is_loopback or ip . is_link_local or ip . is_reserved ) Also disable redirects and cap the response size. 5. Secret leakage Don't put keys in tool code or echo request data back unsanitized. Bound every input's length and type; a 50MB "filename" is an attack, not a filename. 6. No pre-deploy check Run this every release: grep -rn "shell=True \| os.system \| subprocess.call(" src/ grep -rn "pickle.load \| yaml.load( \| torch.load( \| allow_pickle=True" src/ grep -rn "open( \| Path( \| send_file \| extractall" src/ Then fire the attacker payloads ( ../ , 169.254.169.254 , a pickle with a __reduce__ ) at a local instance and confirm every one is refused. I audit MCP servers and AI/ML packages for a living. If you want the full thing — a symlink/absolute-proof path guard with its call-site regression test, the SSRF resolver, the safe-deserialization swaps, and the exact attacker payloads to fire at your own server — I packaged it as a MCP Server Security Hardening Kit ($19) . The pre-deploy checklist above is free; the kit is the code that makes every box pass. Ship it secure.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/mcpsecnotes/6-ways-mcp-servers-get-pwned-and-the-code-that-stops-each-one-3nk1

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
