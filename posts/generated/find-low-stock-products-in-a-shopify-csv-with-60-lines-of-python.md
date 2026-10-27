---
title: "Find low-stock products in a Shopify CSV with 60 lines of Python"
slug: "find-low-stock-products-in-a-shopify-csv-with-60-lines-of-python"
author: "BotHot"
source: "devto_python"
published: "Tue, 27 Oct 2026 17:31:18 +0000"
description: "If you run a small shop, you probably export your products from Shopify now and then. Somewhere in that file are the variants that are almost sold out, and s..."
keywords: "row, qty, handle, threshold, variant, mug, rows, low"
generated: "2026-10-27T17:47:38.997973"
---

# Find low-stock products in a Shopify CSV with 60 lines of Python

## Overview

If you run a small shop, you probably export your products from Shopify now and then. Somewhere in that file are the variants that are almost sold out, and scrolling through a spreadsheet to find them is boring and easy to get wrong. This small script reads a Shopify product export and lists every variant at or below a stock threshold. It only reads the file and never changes it. It uses nothing but Python's standard library. What the export looks like Shopify's product CSV has one row per variant. Products with several images get extra rows that only contain an image URL, so the quantity cell is empty there. The columns we need are: Handle (the product ID in the URL) Title (only filled on the first row of a product) Variant SKU Variant Inventory Qty The script #!/usr/bin/env python3 import argparse import csv import sys QTY_COLUMN = " Variant Inventory Qty " SKU_COLUMN = " Variant SKU " HANDLE_COLUMN = " Handle " TITLE_COLUMN = " Title " def read_rows ( path ): with open ( path , newline = "" , encoding = " utf-8-sig " ) as f : reader = csv . DictReader ( f ) missing = [ c for c in ( HANDLE_COLUMN , QTY_COLUMN ) if c not in ( reader . fieldnames or [])] if missing : sys . exit ( f " Missing column(s): { ' , ' . join ( missing ) } " ) return list ( reader ) def find_low_stock ( rows , threshold ): low , unreadable = [], [] last_title = {} for number , row in enumerate ( rows , start = 2 ): # row 1 is the header handle = row [ HANDLE_COLUMN ] if row . get ( TITLE_COLUMN ): last_title [ handle ] = row [ TITLE_COLUMN ] raw = ( row . get ( QTY_COLUMN ) or "" ). strip () if raw == "" : continue # extra image rows have no quantity try : qty = int ( float ( raw )) except ValueError : unreadable . append (( number , handle , raw )) continue if qty <= threshold : low . append ({ " row " : number , " handle " : handle , " title " : last_title . get ( handle , "" ), " sku " : row . get ( SKU_COLUMN , "" ), " qty " : qty , }) return low , unreadable def main (): parser = argparse . ArgumentParser () parser . add_argument ( " csv_file " ) parser . add_argument ( " --threshold " , type = int , default = 5 ) parser . add_argument ( " --out " , default = " low_stock.csv " ) args = parser . parse_args () rows = read_rows ( args . csv_file ) low , unreadable = find_low_stock ( rows , args . threshold ) with open ( args . out , " w " , newline = "" , encoding = " utf-8 " ) as f : writer = csv . DictWriter ( f , fieldnames = [ " row " , " handle " , " title " , " sku " , " qty " ]) writer . writeheader () writer . writerows ( sorted ( low , key = lambda r : r [ " qty " ])) print ( f " { len ( rows ) } rows read, { len ( low ) } at or below { args . threshold } " ) for r in sorted ( low , key = lambda r : r [ " qty " ]): print ( f " qty { r [ ' qty ' ] : > 3 } { r [ ' sku ' ] or ' - ' : < 10 } { r [ ' title ' ] or r [ ' handle ' ] } " ) for number , handle , raw in unreadable : print ( f " row { number } : cannot read quantity { raw !r} ( { handle } ) " ) if __name__ == " __main__ " : main () Trying it I tested it on a small made-up file (not real shop data): Handle,Title,Variant SKU,Variant Inventory Qty,Image Src blue-mug,Blue Mug,MUG-B,12,https://example.com/a.jpg blue-mug,,,,https://example.com/b.jpg red-mug,Red Mug,MUG-R,3,https://example.com/c.jpg tote-bag,Tote Bag,BAG-1,0,https://example.com/d.jpg sticker-pack,Sticker Pack,STK-1,five,https://example.com/e.jpg poster-a3,Poster A3,POS-A3,5,https://example.com/f.jpg notebook,Notebook,NB-1,40,https://example.com/g.jpg $ python3 low_stock.py sample.csv --threshold 5 7 rows read, 3 at or below 5 qty 0 BAG-1 Tote Bag qty 3 MUG-R Red Mug qty 5 POS-A3 Poster A3 row 6: cannot read quantity 'five' (sticker-pack) The sticker pack has a typo ( five instead of 5 ). The script does not guess; it reports the row number so you can fix it. The empty image row of the blue mug is skipped on purpose. With --threshold 2 only the tote bag is listed. The file low_stock.csv contains the same list, sorted from lowest to highest stock, ready to open in Excel. Notes and limits It checks the quantity column only. If a variant does not track inventory, Shopify leaves that cell empty and the variant is skipped. The threshold is a plain number. A product that sells ten a day needs a different threshold than one that sells one a month, so adjust it per shop. Check the column names in your own export. Shopify has changed its export format before, and the script stops with a clear message if a column is missing. If you want to extend it, an easy next step is a second threshold per product type, or sending the result by e-mail once a week. I write these drafts with the help of AI tools and check the code and the results myself before publishing.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/steven_keil_cb87a560f87f0/find-low-stock-products-in-a-shopify-csv-with-60-lines-of-python-3g2m

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
