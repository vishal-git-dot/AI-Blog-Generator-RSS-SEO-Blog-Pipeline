---
title: "Check that an osu! skin's followpoint frames are numbered without gaps"
slug: "check-that-an-osu-skins-followpoint-frames-are-numbered-without-gaps"
author: "Frank"
source: "devto_python"
published: "Wed, 25 Nov 2026 21:18:29 +0000"
description: "An animated follow-point trail uses followpoint-{n}.png , starting at 0. A missing number in the middle usually stops the animation early, and it is easy to ..."
keywords: "followpoint, frames, png, missing, name, base, print, script"
generated: "2026-11-25T21:26:57.089103"
---

# Check that an osu! skin's followpoint frames are numbered without gaps

## Overview

An animated follow-point trail uses followpoint-{n}.png , starting at 0. A missing number in the middle usually stops the animation early, and it is easy to miss in a folder that already has followpoint.png . This note is a small Python script that lists the still frame and the numbered frames, then reports gaps before you pack the .osk . The script does not judge contrast or aim. It only checks names. You still need to play a jump map afterwards. Finished examples of follow-point density are easier to compare on osuskins.org . What the script looks for A base file followpoint.png , followpoint.jpg , or followpoint.jpeg (and the @2x partner if you ship one). Numbered frames followpoint-0.png , followpoint-1.png , and so on. A gap such as 0, 1, 3 (2 missing), or a sequence that starts at 1 instead of 0. The script Save this as check_followpoint_frames.py in the skin folder, or pass the folder as the first argument. #!/usr/bin/env python3 import sys from pathlib import Path STEM = "followpoint" EXTS = { ".png" , ".jpg" , ".jpeg" } def exists ( dirpath : Path , name : str ) -> Path | None : for ext in EXTS : for cand in ( dirpath / ( name + ext ) , dirpath / ( name + "@2x" + ext ) ) : if cand . is_file ( ) : return cand return None def main ( ) -> int : root = Path ( sys . argv [ 1 ] if len ( sys . argv ) > 1 else "." ) . resolve ( ) base = exists ( root , STEM ) frames = { } for p in root . iterdir ( ) : name = p . name for ext in list ( EXTS ) + [ e . replace ( "." , "@2x." ) for e in EXTS ] : pass low = name . lower ( ) if not low . startswith ( STEM + "-" ) : continue core = name for tail in ( "@2x.png" , "@2x.jpg" , "@2x.jpeg" , ".png" , ".jpg" , ".jpeg" ) : if core . lower ( ) . endswith ( tail ) : core = core [ : - len ( tail ) ] break else : continue suffix = core . split ( "-" , 1 ) [ - 1 ] if suffix . isdigit ( ) : frames . setdefault ( int ( suffix ) , [ ] ) . append ( p . name ) print ( "folder:" , root ) if base : print ( "base: " , base . name ) else : print ( "base: MISSING followpoint.png (or .jpg)" ) if not frames : print ( "frames: none (static follow point only)" ) return 0 if base else 1 nums = sorted ( frames ) print ( "frames:" , ", " . join ( str ( n ) for n in nums ) , "(%d files)" % sum ( len ( v ) for v in frames . values ( ) ) ) start = nums [ 0 ] end = nums [ - 1 ] missing = [ i for i in range ( 0 , end + 1 ) if i not in frames ] if start != 0 : print ( "warning: sequence starts at %d, not 0" % start ) if missing : print ( "MISSING frame numbers: " + ", " . join ( str ( i ) for i in missing ) ) return 1 print ( "ok: contiguous followpoint-0 .. followpoint-%d" % end ) return 0 if __name__ == "__main__" : raise SystemExit ( main ( ) ) What to do with the report A skin does not have to animate follow points. If you only ship followpoint.png , the script should report no frames and a present base file. If you meant to ship an animation, fix any missing number and run the script again, then play a map with clear jumps and confirm the trail still points right and fades in 1.2 seconds. The job of this check is only to catch a missing followpoint-2.png before you upload the .osk . If the names you intended to ship are present and numbered without gaps, the script is done.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/zentaolabs/check-that-an-osu-skins-followpoint-frames-are-numbered-without-gaps-5fai

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
