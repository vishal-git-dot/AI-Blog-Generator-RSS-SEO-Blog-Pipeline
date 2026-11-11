---
title: "Three filters, cheap to expensive: how a duplicate finder avoids hashing your whole disk"
slug: "three-filters-cheap-to-expensive-how-a-duplicate-finder-avoids-hashing-your-whole-disk"
author: "alice kelly"
source: "devto_python"
published: "Wed, 11 Nov 2026 13:41:48 +0000"
description: "Every duplicate file finder starts with the same obvious plan: hash every file, group by digest. It is correct, it is simple, and on a real drive it is unusa..."
keywords: "not, files, size, file, one, only, duplicate, read"
generated: "2026-11-11T13:54:26.912106"
---

# Three filters, cheap to expensive: how a duplicate finder avoids hashing your whole disk

## Overview

Every duplicate file finder starts with the same obvious plan: hash every file, group by digest. It is correct, it is simple, and on a real drive it is unusable. Here is the naive baseline, measured on a 1.09 GB working folder with 877 files: naive: 877 files, 1.09 GB, 21.2 s (SHA-256 over every byte) 21 seconds for one gigabyte. A 500 GB drive is three hours, and that is before you count the USB drive that spins down every 30 seconds. The fix is not a faster hash. SHA-256 is already fast enough — the CPU is not the bottleneck, the disk is. The fix is not reading the bytes at all for the files that cannot possibly be duplicates. Filter 1 — size (free) os.stat gives you the size without opening the file. Two files with different sizes are not duplicates, full stop. This filter costs one syscall per file and eliminates the majority of a normal folder. def _by_size ( self , entries ) : buckets = defaultdict ( list ) for e in entries : buckets [ e . size ] . append ( e ) return { s : v for s , v in buckets . items ( ) if len ( v ) > 1 } Only buckets with more than one member survive. On a typical disk that is a small fraction of the file count — photos, videos, and documents almost all have unique sizes. Filter 2 — the first 4 KB Files that share a size are the only candidates left. For those, read 4 KB and hash that. HEAD_BYTES = 4096 def _hash_file ( path , limit = None ) : h = hashlib . sha256 ( ) remaining = limit with open ( _long_path ( path ) , "rb" ) as f : while True : want = CHUNK if remaining is None else min ( CHUNK , remaining ) if want <= 0 : break chunk = f . read ( want ) if not chunk : break h . update ( chunk ) if remaining is not None : remaining -= len ( chunk ) return h . hexdigest ( ) 4 KB is not a magic number. It is the point where the cost of the read is negligible compared to opening the file at all, and where formats diverge: JPEG headers, ZIP local headers, MP4 ftyp boxes, and Office files all differ within the first few hundred bytes. Two files that agree on both size and first 4 KB are either duplicates or deliberately constructed to look like them. Filter 3 — full SHA-256, only for survivors Whatever is still standing gets read end to end and hashed properly. groups = defaultdict ( list ) for e in candidates : d = _hash_file ( e . path ) # full read groups [ d ] . append ( e ) The point of this stage is not speed. It is that this is the only stage allowed to decide a file gets deleted , and it uses a cryptographic digest, not CRC32, not a size match, not a filename pattern. Duplicate cleaners get one-star reviews for exactly one reason: they deleted something that was not a duplicate. What it actually measures Same folder, same machine, three filters instead of one: three-layer: 872 files seen, 279 hashed (32.0%), 42 groups, 107 duplicate files, 184.6 MB reclaimable, 9.9 s naive: 877 files, 21.2 s 2.1x on 1.09 GB. That number is unimpressive, and it is worth being honest about why: this folder is small and it is full of build artefacts that genuinely collide on size. The ratio is not a constant — it is a function of how much of your disk is unique. On a photo library where every file is a different size, filter 1 alone removes almost everything and the speedup is an order of magnitude. On a folder of copied installers it approaches 1x, because most of the data really is duplicate and really does have to be read. The metric that matters is not files hashed. It is bytes read , and filters 1 and 2 exist to make that number small. Two Windows traps that break the naive version Hard links. st_nlink > 1 means several names point at one inode. They are not duplicates — deleting either name frees nothing, because the data is still referenced. A finder that reports them as duplicates and "cleans" them gives the user a fake number and zero reclaimed space. key = ( st . st_dev , st . st_ino ) if st . st_nlink > 1 : if key in seen_inodes : continue seen_inodes . add ( key ) Long paths. MAX_PATH is 260 characters and open() fails past it. Prefixing with \\?\ bypasses the limit, but only for absolute paths, and only on Windows: if len ( s ) >= 240 and not s . startswith ( "\\\\" ) : return "\\\\?\\" + s The 240 threshold, not 260, leaves room for the prefix itself and for the path separator that gets appended. The shape of the whole thing walk → os.walk, prune excluded dirs in place, collect (path, size, inode) by size → keep only buckets with >1 member by head → 4 KB SHA-256 inside those buckets, keep only >1 full hash → SHA-256 end to end, that digest decides Four stages, about 40 lines of logic, and the expensive one runs on a third of the files or fewer. The same shape works for photo libraries, backups, and the Downloads folder everyone has been meaning to clean since 2019. FileDedupe is a Windows duplicate file finder that uses this pipeline. Free on the Microsoft Store . Code excerpts above are from the shipping scanner.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/alice_kelly_68226d164218e/three-filters-cheap-to-expensive-how-a-duplicate-finder-avoids-hashing-your-whole-disk-3h3i

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
