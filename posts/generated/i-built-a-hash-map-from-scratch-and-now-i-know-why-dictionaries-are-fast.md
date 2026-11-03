---
title: "I built a hash map from scratch (and now I know why dictionaries are fast)"
slug: "i-built-a-hash-map-from-scratch-and-now-i-know-why-dictionaries-are-fast"
author: "Leandros Georgiou"
source: "devto_python"
published: "Tue, 03 Nov 2026 13:31:10 +0000"
description: "In Python, if you have a dictionary with a million things in it, my_dict["apple"] still comes back instantly. I'd use dictionaries for ages without knowing h..."
keywords: "bucket, key, buckets, hash, map, self, pair, list"
generated: "2026-11-03T13:55:05.591550"
---

# I built a hash map from scratch (and now I know why dictionaries are fast)

## Overview

In Python, if you have a dictionary with a million things in it, my_dict["apple"] still comes back instantly. I'd use dictionaries for ages without knowing how that's possible, so as part of my data structures project I built my own version from scratch, called a hash map. Here's how it works. The problem with a list Let's imagine we stored our pairs in a normal list: fruit = [[ " apple " , 1 ], [ " pear " , 7 ], [ " fig " , 2 ]] To find the value for "fig", we have to check "apple", then "pear", then "fig". With three items that's fine, but with a million items we might have to check a million. This is O(n): the more items there are, the longer it takes. A hash map gets around this by not searching at all. It works out exactly where the key should be and goes straight there. Hashing: turning a key into a position Python has a built-in function called hash() that turns a value into a big number. The important thing is that the same key always gives the same number while the program is running. That number is far too big to use as a position in a list, so we use % (the remainder) to squash it down to fit. If we have 8 slots: index = hash ( key ) % 8 This always gives a number from 0 to 7. So "apple" might always go to slot 3. When we want "apple" back later, we do the same calculation, get 3 again, and look straight in slot 3. No searching through everything. One thing that surprised me: if you print hash("apple") , you get a different number every time you restart Python. That's done on purpose, for security. But it stays the same while your program is running, which is all a hash map needs. Buckets Each slot is called a bucket, and each bucket is just a list. So the whole hash map is a list of lists: self . buckets = [[] for _ in range ( capacity )] There's a trap here. You might think you could write [[]] * capacity instead, but that makes one empty list and puts it in every slot, so all 8 "buckets" are actually the same list. Put something in bucket 3 and it shows up in every bucket. The version above makes 8 separate empty lists. Collisions There's a catch. There are loads of possible keys but only 8 buckets, so sometimes two different keys land in the same bucket. This is called a collision. For example, whole numbers hash to themselves in Python, so with 8 buckets: hash(0) % 8 = 0 hash(8) % 8 = 0 0 and 8 both go in bucket 0. That's why each bucket is a list, so it can hold more than one pair. Bucket 0 would look like this: [[ 0 , "zero" ], [ 8 , "eight" ]] So when we look for 8, we go straight to bucket 0, then check the few pairs inside it. That's still really fast, because a bucket only has a handful of pairs in it, not the whole map. The code Here's the main part of my hash map. _index works out the bucket, set stores a pair, and get finds one: def _index ( self , key ): return hash ( key ) % self . capacity def set ( self , key , value ): bucket = self . buckets [ self . _index ( key )] for pair in bucket : if pair [ 0 ] == key : # key already here, so update it pair [ 1 ] = value return bucket . append ([ key , value ]) # new key, so add the pair self . size += 1 if self . size / self . capacity > 0.75 : self . _resize () def get ( self , key ): bucket = self . buckets [ self . _index ( key )] for pair in bucket : if pair [ 0 ] == key : return pair [ 1 ] raise KeyError ( key ) Notice, get only ever loops through one bucket, never the whole map. If the key isn't there, it raises a KeyError , just like a real dictionary does. Resizing Collisions are fine when the buckets are short. But if we kept adding pairs to 8 buckets, say 1,000 pairs, every bucket would have about 125 pairs in it, and we'd be back to slow searching. So the hash map keeps track of how full it is. This is called the load factor: load factor = number of pairs / number of buckets When the load factor goes over 0.75, the map doubles its number of buckets and puts every pair back in again. Why put them all back in? Because the bucket a key goes in depends on how many buckets there are. Remember, 8 went in bucket 0 when there were 8 buckets. With 16 buckets: hash ( 8 ) % 16 = 8 Now it belongs in bucket 8. Therefore, every pair has to be worked out again and moved to its new bucket. Resizing takes a while, because it touches every pair, which is O(n). But it only happens now and again, and because the map doubles each time, it happens less and less often. Spread out over all the set calls, adding a pair is still O(1) on average. So why are dictionaries fast? Putting it all together: Hashing means you jump straight to the right bucket instead of searching. Buckets handle collisions, so two keys can share a slot. Resizing keeps the buckets short, so checking a bucket stays quick. That's why getting, setting and deleting are O(1) on average, no matter how big the map gets. Python's real dictionary is cleverer than mine about collisions (it doesn't keep a list in each slot), but the big idea is the same: hash the key to go straight to the right place, and grow before it gets too full. Testing it I wrote pytest tests for it, including putting 1,000 keys into a map that started with only 8 buckets, to make sure it resized properly and could still find every key. I also tested a collision on purpose (0 and 8), and that asking for a missing key raises a KeyError . The full code and tests are in my repo: data-structures-from-scratch

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ljgeorgiou/i-built-a-hash-map-from-scratch-and-now-i-know-why-dictionaries-are-fast-3185

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
