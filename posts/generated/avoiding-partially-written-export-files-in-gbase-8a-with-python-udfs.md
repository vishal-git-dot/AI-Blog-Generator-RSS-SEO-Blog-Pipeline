---
title: "Avoiding Partially Written Export Files in GBase 8a with Python UDFs"
slug: "avoiding-partially-written-export-files-in-gbase-8a-with-python-udfs"
author: "Michael"
source: "devto_python"
published: "Fri, 27 Nov 2026 07:24:00 +0000"
description: "GBase 8a, the China-domestically developed MPP database from GBASE, can export over ftp and sftp . When the export is large — tens of GB — the target file ta..."
keywords: "gbase, csv, tmp, home, varchar, ftp, export, sftp"
generated: "2026-11-27T07:44:07.269333"
---

# Avoiding Partially Written Export Files in GBase 8a with Python UDFs

## Overview

GBase 8a, the China-domestically developed MPP database from GBASE, can export over ftp and sftp . When the export is large — tens of GB — the target file takes time to finish writing. If a downstream job picks it up mid-export, it reads an incomplete file , which shows up as inconsistent data or parse errors. This post uses Python UDFs to add ftp / sftp rename support so the file only becomes visible when it is complete. The idea Downstream consumers usually scan for files matching a rule, for example *.csv under a load directory. Making an unfinished file fail that rule can be done two ways, and they can be combined: Name does not match — target is .csv , temporary file is .csv.tmp Path does not match — write to a temporary directory first Two steps Export to a temporary file (different suffix, or a temporary directory). Once the export finishes, use the protocol's rename to switch the temporary name to the final one — changing the suffix or moving across directories. FTP rename UDF Stored under gclusterdb , taking host, username, password, source name, target name . Port customisation is not implemented; extend it if you are not on the default ftp port: use gclusterdb ; drop function if exists ftpRename ; create function ftpRename ( server varchar ( 100 ) , username varchar ( 100 ) , password varchar ( 100 ) , sourceFilename varchar ( 1000 ) , targetFilename varchar ( 1000 ) ) returns varchar $$ from ftplib import FTP ftp = FTP ( server ) ftp . login ( username , password ) ftp . rename ( sourceFilename , targetFilename ) ftp . close ( ) return 'OK' $$ language plpythonu ; Calling it: gbase > select ftprename ( '10.0.2.201' , 'gbase' , 'gbase1234' , '/home/gbase/t1.csv.tmp' , '/home/gbase/t1.csv' ) ; +------------------------------------------------------------------------------------------------+ | ftprename ( '10.0.2.201' , 'gbase' , 'gbase1234' , '/home/gbase/t1.csv.tmp' , '/home/gbase/t1.csv' ) | +------------------------------------------------------------------------------------------------+ | OK | +------------------------------------------------------------------------------------------------+ 1 row in set ( Elapsed : 00 : 00 : 00.08 ) SFTP rename UDF The standard Python library does not speak sftp, so this example uses pysftp ( pip install pysftp ). Everything else matches the FTP version: use gclusterdb ; drop function if exists sftpRename ; create function sftpRename ( server varchar ( 100 ) , v_username varchar ( 100 ) , v_password varchar ( 100 ) , sourceFilename varchar ( 1000 ) , targetFilename varchar ( 1000 ) ) returns varchar $$ import pysftp with pysftp . Connection ( server , username = v_username , password = v_password ) as sftp : sftp . rename ( sourceFilename , targetFilename ) sftp . close ( ) return 'OK' $$ language plpythonu ; gbase > select sftprename ( '10.0.2.201' , 'gbase' , 'gbase1234' , '/home/gbase/t1.csv.tmp' , '/home/gbase/t1.csv' ) ; +------------------------------------------------------------------------------------------------+ | sftprename ( '10.0.2.201' , 'gbase' , 'gbase1234' , '/home/gbase/t1.csv.tmp' , '/home/gbase/t1.csv' ) | +------------------------------------------------------------------------------------------------+ | OK | +------------------------------------------------------------------------------------------------+ 1 row in set ( Elapsed : 00 : 00 : 00.08 ) The full flow gbase > select * from t1 into outfile 'sftp://gbase:gbase1234@10.0.2.201/home/gbase/t1.csv.tmp' fields terminated by ',' ; Query OK , 3 rows affected ( Elapsed : 00 : 00 : 00.32 ) gbase > select gclusterdb . sftprename ( '10.0.2.201' , 'gbase' , 'gbase1234' , '/home/gbase/t1.csv.tmp' , '/home/gbase/tmp/t1.csv' ) ; +-----------------------------------------------------------------------------------------------------------+ | gclusterdb . sftprename ( '10.0.2.201' , 'gbase' , 'gbase1234' , '/home/gbase/t1.csv.tmp' , '/home/gbase/tmp/t1.csv' ) | +-----------------------------------------------------------------------------------------------------------+ | OK | +-----------------------------------------------------------------------------------------------------------+ 1 row in set ( Elapsed : 00 : 00 : 00.43 ) The temporary file can live in a different directory , provided the account has write permission there. This example uses both a temporary tmp directory and a .tmp suffix: gbase > select * from t1 into outfile 'sftp://gbase:gbase1234@10.0.2.201/home/gbase/tmp/t1_2.csv.tmp' fields terminated by ',' ; Query OK , 3 rows affected ( Elapsed : 00 : 00 : 00.44 ) gbase > select gclusterdb . sftprename ( '10.0.2.201' , 'gbase' , 'gbase1234' , '/home/gbase/tmp/t1_2.csv.tmp' , '/home/gbase/t1_2.csv' ) ; +---------------------------------------------------------------------------------------------------------------+ | gclusterdb . sftprename ( '10.0.2.201' , 'gbase' , 'gbase1234' , '/home/gbase/tmp/t1_2.csv.tmp' , '/home/gbase/t1_2.csv' ) | +---------------------------------------------------------------------------------------------------------------+ | OK | +---------------------------------------------------------------------------------------------------------------+ 1 row in set ( Elapsed : 00 : 00 : 00.44 ) Both the export and the rename run inside the gbase client, and the consumer's scan rule never matches a .tmp file. Handing atomic visibility to rename means even a tens-of-GB export no longer needs a sleep timer or a human "is it done yet" check — a small UDF turns the database's own export into a safe handoff.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/michaelfv/avoiding-partially-written-export-files-in-gbase-8a-with-python-udfs-3moa

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
