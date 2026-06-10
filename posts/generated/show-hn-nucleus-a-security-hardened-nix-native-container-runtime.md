---
title: "Show HN: Nucleus – A security-hardened, Nix-native container runtime"
slug: "show-hn-nucleus-a-security-hardened-nix-native-container-runtime"
author: "0kenx"
source: "hackernews"
published: "Tue, 09 Jun 2026 23:03:40 +0000"
description: "Hi HN, I've been building Nucleus, a lightweight Linux container runtime focused on two workloads: ephemeral AI-agent sandboxes and declarative NixOS service..."
keywords: "mode, nucleus, native, runtime, ephemeral, agent, not, docker"
generated: "2026-06-10T04:15:10.535910"
---

# Show HN: Nucleus – A security-hardened, Nix-native container runtime

## Overview

Hi HN, I've been building Nucleus, a lightweight Linux container runtime focused on two workloads: ephemeral AI-agent sandboxes and declarative NixOS services. It's a single Rust binary, no daemon. It is not a Docker replacement and not a strict subset of Docker either. I dropped the entire image-and-distribution half (no Dockerfile, no layers, no registry, no pull/push, no persistent storage layer) in exchange for going deeper on isolation and reproducibility. The rootfs is either a directory copied into tmpfs (agent mode) or a Nix-built closure mounted read-only (production mode). If your mental model is "run my image instead of docker run," this won't fit. If it's "run untrusted or ephemeral workloads with stronger, auditable isolation on a single host," that's the target. Things that I think are interesting: - Defense-in-depth defaults. All capabilities dropped, ~100-syscall seccomp allowlist (vs Docker's ~300), up to 8 namespaces including time/cgroup, Landlock LSM path ACLs per service. - Deny-by-default egress. Outbound traffic is denied unless you allow specific CIDRs or DNS-resolved domains. Enforced with namespace-local iptables rules. - Externalized, hash-pinned security policies. seccomp (JSON), capabilities (TOML), and Landlock (TOML) live as separate SHA-256-verified files, decoupled from the rootfs build. There's a nucleus seccomp generate that records syscalls in trace mode and emits a minimal profile. - gVisor as a first-class integrated runtime, not an add-on. Explicit network modes including a gvisor-host mode that's intentionally separate from native host networking. - Nix-native production path. nucleus.lib.mkRootfs builds locked-down closures; rootfs attestation verifies a per-file SHA-256 manifest at startup; first-class NixOS module. - Formal verification. TLA+ specs for the isolation/resource/filesystem/security/gVisor subsystems, checked with Apalache, plus property-based tests that drive the Rust implementation against the specs. Honest tradeoffs: - Linux x86_64 only. No macOS/Windows/BSD, no plans. - No CNI, no overlay networks, no cluster orchestration. nucleus compose is a single-host TOML DAG over systemd, not Swarm/K8s. - Ephemeral-by-default storage. Persistence is opt-in via explicit --volume binds. - Agent mode applies several mechanisms best-effort by design (warn-and-continue on seccomp/Landlock failure). For fail-closed isolation on ephemeral workloads use --service-mode strict-agent; for long-running services use production mode. Cold-start is ~12ms in the native runtime. Postgres 18 pgbench numbers under Nucleus are within noise of bare metal in our harness (full results in benches/). Comments URL: https://news.ycombinator.com/item?id=48469039 Points: 23 # Comments: 2

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://github.com/sig-id/nucleus

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
