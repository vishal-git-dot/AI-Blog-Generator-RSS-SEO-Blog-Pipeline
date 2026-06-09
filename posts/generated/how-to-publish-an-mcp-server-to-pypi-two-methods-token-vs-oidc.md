---
title: "How to Publish an MCP Server to PyPI — Two Methods (Token vs OIDC)"
slug: "how-to-publish-an-mcp-server-to-pypi-two-methods-token-vs-oidc"
author: "Gabriel Mahia"
source: "devto_python"
published: "Tue, 09 Jun 2026 14:40:08 +0000"
description: "Publishing your first MCP server to PyPI unlocks distribution to any AI system in the world. Here's the exact workflow used for the East Africa AI Stack, cov..."
keywords: "pypi, mcp, your, token, publish, build, python, pip"
generated: "2026-06-09T15:18:05.198695"
---

# How to Publish an MCP Server to PyPI — Two Methods (Token vs OIDC)

## Overview

Publishing your first MCP server to PyPI unlocks distribution to any AI system in the world. Here's the exact workflow used for the East Africa AI Stack, covering both publishing methods. What You're Publishing An MCP (Model Context Protocol) server is a Python package that exposes tools to AI assistants like Claude. When installed via pip , any MCP-compatible AI can call your tools. pip install bima-mcp # Kenya insurance intelligence pip install mkopo-mcp # Alternative credit scoring pip install soko-mcp # Commodity price intelligence pip install sifa-mcp # Portable reputation system Method 1: API Token (Faster Setup) Use this when you want to publish immediately with minimal configuration. Step 1: Get a PyPI token Go to pypi.org/manage/account/#api-tokens → Add API token. Either create a token scoped to a specific project, or use the account-wide token for new projects. Step 2: Add the token as a GitHub secret In your repo: Settings → Secrets and variables → Actions → New secret. Name: PYPI_API_TOKEN , Value: your token string starting with pypi- . Or via API (using PyNaCl to encrypt): from nacl import encoding , public import base64 def encrypt_secret ( public_key_b64 : str , secret_value : str ) -> str : pk = public . PublicKey ( public_key_b64 . encode (), encoding . Base64Encoder ()) box = public . SealedBox ( pk ) return base64 . b64encode ( box . encrypt ( secret_value . encode ())). decode () Step 3: Create .github/workflows/publish.yml name : Publish to PyPI on : push : tags : [ " v*" ] jobs : publish : runs-on : ubuntu-latest steps : - uses : actions/checkout@v4 - uses : actions/setup-python@v5 with : python-version : " 3.11" - run : pip install build - run : python -m build - uses : pypa/gh-action-pypi-publish@release/v1 with : password : ${{ secrets.PYPI_API_TOKEN }} Step 4: Fix your pyproject.toml The most common CI failure is a wrong build-backend . Use exactly: [build-system] requires = ["setuptools> = 61.0 "] build-backend = "setuptools.build_meta" # ← NOT "setuptools.backends.legacy:build" [project] name = "your-package" version = "0.1.0" # ... [tool.setuptools.packages.find] where = [ "src" ] Step 5: Release git tag v0.1.0 && git push origin v0.1.0 GitHub Actions runs, builds your package, uploads to PyPI. Done. Method 2: OIDC Trusted Publisher (More Secure, Recommended) No token stored anywhere. GitHub authenticates directly with PyPI via OpenID Connect. Step 1: Register on PyPI Go to pypi.org/manage/project/{your-package}/settings/publishing/ → Add a new publisher. Fill in: Owner: your-github-username Repository: your-repo-name Workflow filename: publish.yml Environment: pypi (optional but recommended) Step 2: Update your workflow name : Publish to PyPI on : push : tags : [ " v*" ] jobs : publish : runs-on : ubuntu-latest environment : pypi # ← matches the environment in PyPI settings permissions : id-token : write # ← OIDC requires this permission steps : - uses : actions/checkout@v4 - uses : actions/setup-python@v5 with : python-version : " 3.11" - run : pip install build - run : python -m build - uses : pypa/gh-action-pypi-publish@release/v1 # No password needed — OIDC handles auth No password: line. No token stored in GitHub secrets. The id-token: write permission is what authenticates with PyPI. Step 3: Release the same way git tag v0.1.0 && git push origin v0.1.0 Common Failure Modes Error Cause Fix python -m build fails Wrong build-backend Use setuptools.build_meta exactly python -m build fails Missing src/ directory Create src/{package_name}/__init__.py 403 from PyPI Token invalid or insufficient scope Re-generate token with project scope 400 from PyPI Package version already exists Bump version in pyproject.toml OIDC 403 Publisher not registered on PyPI Complete the Trusted Publisher setup at pypi.org ModuleNotFoundError at runtime [tool.setuptools.packages.find] missing Add where = ["src"] section Src Layout (Recommended) your-mcp-server/ ├── src/ │ └── your_package/ │ ├── __init__.py │ └── main.py ← entry point ├── pyproject.toml ├── README.md └── .github/ └── workflows/ └── publish.yml The main.py entry point: from fastmcp import FastMCP mcp = FastMCP ( name = " your-mcp-server " ) @mcp.tool () def your_tool ( param : str ) -> dict : return { " result " : f " processed { param } " } def main (): mcp . run () if __name__ == " __main__ " : main () The pyproject.toml script entry: [project.scripts] your-mcp-server = "your_package.main:main" After pip install your-mcp-server , users run it as a CLI command that Claude connects to. All 12 packages in the East Africa AI Stack use this pattern. Full source at gabrielmahia.github.io .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/gabrielmahia/how-to-publish-an-mcp-server-to-pypi-two-methods-token-vs-oidc-2ne8

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
