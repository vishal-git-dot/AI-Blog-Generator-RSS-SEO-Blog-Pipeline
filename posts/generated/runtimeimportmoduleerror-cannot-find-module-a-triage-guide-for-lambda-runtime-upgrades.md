---
title: ""Runtime.ImportModuleError: Cannot find module — a triage guide for Lambda runtime upgrades""
slug: "runtimeimportmoduleerror-cannot-find-module-a-triage-guide-for-lambda-runtime-upgrades"
author: "ntoledo319"
source: "devto_python"
published: "Fri, 24 Jul 2026 07:17:03 +0000"
description: "You bumped a Lambda function to a newer runtime, redeployed, and the first invocation dies at cold start: Runtime.ImportModuleError: Error: Cannot find modul..."
keywords: "runtime, module, you, package, lambda, python, your, aws"
generated: "2026-07-24T08:34:24.201809"
---

# "Runtime.ImportModuleError: Cannot find module — a triage guide for Lambda runtime upgrades"

## Overview

You bumped a Lambda function to a newer runtime, redeployed, and the first invocation dies at cold start: Runtime.ImportModuleError: Error: Cannot find module 'some-package' (Python's version reads Unable to import module 'handler': No module named 'some_package' — same underlying category of failure.) The unhelpful part: this exact message is the symptom of at least four different root causes, and none of them are code bugs — your handler didn't change. Here's how to tell them apart before you start guessing. The triage 1. Is the missing module aws-sdk (lowercase, no @ ) and did you move to nodejs18.x or later? That's not a bundling problem — AWS stopped preinstalling AWS SDK v2 in the runtime starting with nodejs18.x . Only @aws-sdk/* v3 modular clients ship now. This has a dedicated fix with the full v2→v3 migration: eolkits.com/fix/node-cannot-find-module-aws-sdk . 2. Is the module genuinely in package.json / requirements.txt , and did you switch bundlers or bump esbuild recently? esbuild 0.22+ changed its default to treat node_modules as external — meaning a real dependency can still get silently excluded from the deployment ZIP. If you use SAM, CDK, or Serverless Framework with the esbuild build method, force it back to inline: # SAM template.yaml Metadata : BuildMethod : esbuild BuildProperties : Packages : bundle or esbuild --packages=bundle directly. Confirm by unzipping your build artifact and checking whether the module directory is actually present under node_modules/ — don't trust the build log alone. 3. Does the error only happen through a Lambda Layer, and did you build that layer on your laptop or a generic CI image? A layer built on the wrong base image is a structure/path problem, not a missing-package problem: Node expects nodejs/node_modules/<package> inside the layer zip, Python expects python/<package> . If the layer was zipped with a different top-level folder, or built for the wrong architecture ( x86_64 vs arm64 ), the runtime won't find it even though the package is technically "in" the layer. Rebuild inside the actual Lambda base image for your target runtime and architecture: docker run --rm -v " $PWD " :/opt public.ecr.aws/lambda/nodejs:22 \ npm install --prefix /opt/nodejs 4. Does the module load fine on your machine but fail only on Lambda, and does it involve a native binary ( .node file, or a Python package like psycopg2 , numpy , pydantic-core , grpcio )? That's usually not a "cannot find" problem at the module-resolution level at all — it's the loader finding the file and then failing to link it, which Node/Python often still surfaces as an import error. This is a glibc/architecture mismatch between where the binary was compiled and the runtime's base OS. Full diagnosis and fix: eolkits.com/fix/lambda-glibc-version-not-found . If none of the four fit Check the boring things first, in order: does the Handler setting ( file.export for Node, file.function for Python) still match where the file actually lives in the deployment package after the runtime change moved your build output layout? Did the runtime change also change the working directory the bundler assumes ( /var/task vs /opt )? A surprising fraction of "phantom" ImportModuleErrors are a handler path pointing at a file that no longer exists at that path post-rebuild, not a missing dependency at all. Catching this before a cold start in production does All four causes above are detectable from the deployment artifact itself, before you ever invoke the function — which matters because ImportModuleError only surfaces at cold start, so a broken deploy can sit "successful" for minutes or hours before anyone notices. If you're tracking deprecated-runtime exposure across an account already, the same scan pass is a natural place to also flag native-dependency ABI mismatches and stale bundler configs before a redeploy trips one of these: the free EOLkits scanner checks an account in about 30 seconds, nothing uploaded — I maintain it.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ntoledo319/runtimeimportmoduleerror-cannot-find-module-a-triage-guide-for-lambda-runtime-upgrades-1jj1

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
