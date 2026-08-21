---
title: "Model Context Protocol: Setup MCP Server on Bare Metal"
slug: "model-context-protocol-setup-mcp-server-on-bare-metal"
author: "Jakson Tate"
source: "devto_python"
published: "Fri, 21 Aug 2026 06:30:05 +0000"
description: "Integrating Large Language Models (LLMs) with enterprise databases using custom REST APIs requires constant glue-code maintenance. The Model Context Protocol..."
keywords: "mcp, server, fastmcp, path, json, directory, data, ssh"
generated: "2026-08-21T06:55:13.097350"
---

# Model Context Protocol: Setup MCP Server on Bare Metal

## Overview

Integrating Large Language Models (LLMs) with enterprise databases using custom REST APIs requires constant glue-code maintenance. The Model Context Protocol (MCP) provides a universal, standardized interface for dynamic tool discovery via JSON-RPC. Here is how to deploy a secure FastMCP server on Bare Metal infrastructure. Phase 1: Environment Setup with uv Bypass standard pip bloat and use uv —the Rust-based Python package manager—for ultra-fast dependency isolation. ⚠️ SRE WARNING: The FastMCP Import Anomaly Do not install mcp[cli] when writing custom Python code using from fastmcp import FastMCP . Namespace collisions cause an immediate ModuleNotFoundError . Install fastmcp directly. # 1. Install 'uv' globally curl -LsSf [ https://astral.sh/uv/install.sh] ( https://astral.sh/uv/install.sh ) | sh source $HOME /.local/bin/env # 2. Setup project directory mkdir ~/enterprise-mcp && cd ~/enterprise-mcp uv init uv venv source .venv/bin/activate # 3. SRE FIX: Install FastMCP package explicitly uv add fastmcp Phase 2: Architecting the Secure FastMCP Server MCP uses Standard I/O ( stdio ) to stream JSON-RPC messages to AI clients. 🚨 SECURITY ALERT: The print() Crash Trap Never use standard print() statements in your MCP server code. Outputting text to stdout injects raw string data into the JSON stream, corrupting the protocol and instantly crashing Claude Desktop. Force all logging exclusively to sys.stderr . Create server.py : import sys import logging from fastmcp import FastMCP # SRE FIX: Force all logging to stderr to protect the JSON-RPC stdio stream logging . basicConfig ( level = logging . INFO , stream = sys . stderr , format = ' %(levelname)s: %(message)s ' ) logger = logging . getLogger ( __name__ ) mcp = FastMCP ( " Enterprise-Data-Gateway " ) @mcp.tool () def get_server_status () -> str : """ Returns operational status of the Bare Metal server. """ logger . info ( " Tool called: get_server_status " ) return " ServerMO Bare Metal Node 01: All systems operational. 0% Packet Loss. " if __name__ == " __main__ " : logger . info ( " Starting MCP Server on stdio transport... " ) mcp . run ( transport = " stdio " ) Phase 3: Hardening Against Path Traversal Granting AI agents file system tools requires strict sandboxing to prevent prompt injections from exfiltrating system secrets like /etc/passwd . 🚨 SECURITY ALERT: The Sibling Directory Bypass String checks like requested_path.startswith(str(ALLOWED_DIR)) create critical vulnerabilities! If your allowed directory is /home/data , requesting /home/data-secret/pass.txt passes string matching. Use Path.is_relative_to() instead. Add file sandboxing to server.py : from pathlib import Path ALLOWED_DIR = Path ( " /home/ubuntu/enterprise-mcp/data " ). resolve () @mcp.tool () def read_secure_file ( filename : str ) -> str : """ Reads a text file strictly from the allowed data sandbox. """ requested_path = ( ALLOWED_DIR / filename ). resolve () # SRE FIX: Prevent Sibling Directory Path Traversal Bypass if not requested_path . is_relative_to ( ALLOWED_DIR ): logger . error ( f " Security Violation: Attempted path traversal to { requested_path } " ) return " ERROR: Access Denied. Path traversal detected. " if not requested_path . is_file (): return f " ERROR: File ' { filename } ' not found in sandbox. " try : with open ( requested_path , ' r ' , encoding = ' utf-8 ' ) as f : return f . read () except Exception as e : logger . error ( f " Read error: { str ( e ) } " ) return " ERROR: Could not read file due to permissions or locking. " Phase 4: Remote Stdio over SSH (Claude Desktop Integration) To connect local Claude Desktop to this remote MCP server without exposing public ports: ⚠️ SRE WARNING: The MOTD & Working Directory Trap Running standard SSH commands causes two critical failures: Ubuntu MOTD banners ("Welcome to Ubuntu") corrupt the JSON-RPC stream. SSH defaults to /home/ubuntu , completely blinding uv to your virtual environment. Pass -q -T to SSH to kill login banners, and pass --directory and --quiet to uv . Edit claude_desktop_config.json on your local laptop: { "mcpServers" : { "enterprise-bare-metal" : { "command" : "ssh" , "args" : [ "-q" , "-T" , "-i" , "/path/to/private_key.pem" , "ubuntu@YOUR_REMOTE_SERVER_IP" , "/home/ubuntu/.local/bin/uv" , "--directory" , "/home/ubuntu/enterprise-mcp" , "run" , "--quiet" , "server.py" ] } } } Restart Claude Desktop to connect your local AI agent directly over an encrypted SSH pipe. FastMCP & Model Context Protocol FAQ MCP Protocol vs REST API: Which is better for AI Agents? REST APIs require custom integration code and static endpoint management for every tool. MCP standardizes client-server interactions, allowing AI agents to dynamically discover and execute tools via JSON-RPC. Why did my MCP Server crash Claude Desktop? Standard print() statements or SSH MOTD banners write raw text to stdout , corrupting the JSON-RPC stream. Route Python logs to sys.stderr and use ssh -q -T . Why is .startswith() dangerous for directory path checks? string.startswith("/data") matches /data-secret/file.txt . Always use path.is_relative_to(ALLOWED_DIR) for filesystem sandboxing. 👉 Read the full guide on ServerMO: Setup MCP Server on Bare Metal | ServerMO

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/jaksontate/model-context-protocol-setup-mcp-server-on-bare-metal-1hdj

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
