---
title: "The SSRF guard your MCP fetch_url tool is missing"
slug: "the-ssrf-guard-your-mcp-fetchurl-tool-is-missing"
author: "MCP Security Notes"
source: "devto_python"
published: "Wed, 12 Aug 2026 02:08:36 +0000"
description: "If your MCP server has any tool that takes a URL and fetches it — fetch_url , read_web , summarize_page , a webhook caller — an attacker who controls the mod..."
keywords: "http, url, hostname, none, your, not, host, return"
generated: "2026-08-12T02:22:46.156494"
---

# The SSRF guard your MCP fetch_url tool is missing

## Overview

If your MCP server has any tool that takes a URL and fetches it — fetch_url , read_web , summarize_page , a webhook caller — an attacker who controls the model's input can point it at http://169.254.169.254/latest/meta-data/ and read your cloud credentials, or at http://localhost:6379 to poke an internal service. That's SSRF, and a scheme check alone does not stop it. Here's a resolver-based guard that does, plus the DNS-rebinding and redirect gaps most guides miss. Why the common fixes fail # BROKEN 1: block "localhost" by string if " localhost " in url or " 127.0.0.1 " in url : # 0x7f.1, 127.1, [::1], 2130706433 all bypass reject () # BROKEN 2: check the hostname, then fetch by hostname host = urlparse ( url ). hostname if is_private ( host ): # host is a NAME, not an IP — DNS can point it anywhere reject () requests . get ( url ) # re-resolves; attacker's DNS returns 169.254.169.254 the 2nd time Two real gaps: Blocklists lose. There are dozens of ways to spell a private IP (decimal, octal, IPv6-mapped). You cannot enumerate the bad ones — allowlist the scheme and reject by resolved IP class instead. TOCTOU / DNS rebinding. If you validate a hostname and then let the HTTP client resolve it again, the attacker's DNS can answer "public" on the first lookup and "internal" on the second. The guard: resolve once, validate the IP, connect to that IP import ipaddress , socket from urllib.parse import urlparse def safe_target ( url : str ): u = urlparse ( url ) if u . scheme not in ( " http " , " https " ): # no file://, gopher://, ftp:// return None if not u . hostname : return None # resolve ONCE, ourselves try : infos = socket . getaddrinfo ( u . hostname , u . port or ( 443 if u . scheme == " https " else 80 ), proto = socket . IPPROTO_TCP ) except socket . gaierror : return None ip = ipaddress . ip_address ( infos [ 0 ][ 4 ][ 0 ]) if ( ip . is_private or ip . is_loopback or ip . is_link_local or ip . is_reserved or ip . is_multicast or ip . is_unspecified ): return None # 169.254/16, 127/8, 10/8, ::1, etc. all covered return str ( ip ) # connect to THIS ip, not the hostname Then pin the connection to the IP you validated so the client can't re-resolve: import requests def fetch ( url : str , max_bytes = 2_000_000 ): ip = safe_target ( url ) if ip is None : raise ValueError ( " blocked target " ) u = urlparse ( url ) # connect to the validated IP, keep Host header + SNI for TLS pinned = url . replace ( u . hostname , ip , 1 ) r = requests . get ( pinned , headers = { " Host " : u . hostname }, stream = True , timeout = 5 , allow_redirects = False ) # <-- handle redirects yourself body = r . raw . read ( max_bytes + 1 , decode_content = True ) if len ( body ) > max_bytes : raise ValueError ( " response too large " ) return body Three things that guide-grade snippets skip: allow_redirects=False . A 302 to http://169.254.169.254/ bypasses every up-front check. Follow redirects manually, re-running safe_target on each Location . Cap the body. Unbounded reads let an attacker DoS you with a multi-GB response. Stream and stop. Set a timeout. No timeout means a hostile host holds your worker open forever. The test that proves it import pytest from mymcp.net import safe_target @pytest.mark.parametrize ( " evil " , [ " http://169.254.169.254/latest/meta-data/ " , " http://127.0.0.1:6379/ " , " http://localhost/ " , " http://[::1]/ " , " http://0177.0.0.1/ " , # octal 127.0.0.1 " http://2130706433/ " , # decimal 127.0.0.1 " http://10.0.0.5/ " , " file:///etc/passwd " , " gopher://internal/_x " , ]) def test_ssrf_blocked ( evil ): assert safe_target ( evil ) is None def test_public_allowed (): assert safe_target ( " https://example.com/ " ) is not None If test_ssrf_blocked is green on all of those, you've closed the class — including the numeric-encoding tricks that beat every string blocklist. This is one of six guards I keep in a hardening kit for MCP servers — SSRF, symlink-safe path containment, argv-only exec, safe deserialization, input bounds, and a pre-deploy grep + payload checklist with tests. Want to check your own server first? Paste it into the free MCP Server Security Scanner — instant findings, 100% in your browser. The full copy-paste guards + tests are the MCP Server Security Hardening Kit ($19) . The resolver and tests above are yours free — ship them today.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/mcpsecnotes/the-ssrf-guard-your-mcp-fetchurl-tool-is-missing-19mk

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
