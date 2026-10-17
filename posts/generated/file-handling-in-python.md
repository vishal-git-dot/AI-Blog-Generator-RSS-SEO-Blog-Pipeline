---
title: "File Handling in Python"
slug: "file-handling-in-python"
author: "Lameck Odhiambo"
source: "devto_python"
published: "Sat, 17 Oct 2026 03:32:08 +0000"
description: "File handling in Python is important as it allows you to create, read, update, and delete files directly from your code. Python manages these operations usin..."
keywords: "file, open, data, line, json, csv, python, txt"
generated: "2026-10-17T03:51:06.689380"
---

# File Handling in Python

## Overview

File handling in Python is important as it allows you to create, read, update, and delete files directly from your code. Python manages these operations using a built-in open() function, which creates a file object to interact with the file system. with Statement This is best practice and recommended method for opening files in Python is using the with keyword. It automatically closes the file once the block of code finishes, even if errors occur. This prevents memory leaks and file corruption. # The file closes automatically outside this block with open ( " example.txt " , " r " ) as file : content = file . read () print ( content ) File Open Modes The second argument of open() specifies the "mode" (how you want to interact with the file) • "r" ( Read ): Default mode. Opens a file for reading. Throws a FileNotFoundError if the file doesn't exist. • "w" ( Write ): Opens a file for writing. Overwrites existing content. Creates a new file if it doesn't exist. • "a" ( Append ): Opens a file to add data to the end. It does not erase existing content. Creates a new file if it doesn't exist. • "x" ( Create ): Creates a specific file. Returns an error if the file already exists. Reading Files .txt Python provides several methods to extract text from an open file: • read(size) : Reads the entire file as a single string. You can pass an optional integer size to read only a specific number of characters. • readline() : Reads just one line at a time. Helpful for reading large files line by line. • readlines() : Reads all lines at once and returns them as a list of strings. • Line Loop (Efficient) : You can iterate directly over the file object using a loop, which is memory-efficient for large files. # Reading line-by-line efficiently with open ( " large_file.txt " , " r " ) as file : for line in file : print ( line . strip ()) # strip() removes extra newlines # Reading entire content at once with open ( " example.txt " , " r " , encoding = " utf-8 " ) as file : content = file . read () print ( content ) .json Python converts JSON data directly into dictionaries and lists import json with open ( ' data.json ' , ' r ' ) as file : data = json . load ( file ) print ( data ) .csv import csv with open ( ' data.csv ' , mode = ' r ' , encoding = ' utf-8 ' ) as file : # Create the reader object reader = csv . reader ( file ) # Optional: Skip the header row if your file has one header = next ( reader ) for row in reader : # Each row is a list. Access columns by index (e.g., row[0]) print ( row ) Writing Files .txt To add content, open the file in write ("w") or append ("a") mode: • write(string) : Inserts a string into the file. • writelines(list) : Inserts a list of strings into the file all at once lines_to_write = [ " First line \n " , " Second line \n " ] with open ( " output.txt " , " w " ) as file : file . writelines ( lines_to_write ) .json import json # Your data structure (Python dictionary) user_data = { " name " : " Alice Smith " , " age " : 30 , " active " : True , " roles " : [ " admin " , " user " ] } # Writing to a file with open ( " user.json " , " w " ) as file : json . dump ( user_data , file ) .csv import csv # Data structured as a list of lists (rows) data = [ [ " Name " , " Age " , " City " ], [ " Alice " , 30 , " New York " ], [ " Bob " , 25 , " Los Angeles " ], [ " Charlie " , 35 , " Chicago " ] ] # Open the file in write mode ('w') with open ( ' output.csv ' , mode = ' w ' , newline = '' , encoding = ' utf-8 ' ) as file : writer = csv . writer ( file ) # Write all rows at once writer . writerows ( data ) Deleting and Deleting Files For file system operations like deleting or renaming, you need to import Python's built-in os module import os # Delete a file safely if os . path . exists ( " old_file.txt " ): os . remove ( " old_file.txt " ) Conclusion File handling is critical because it enables data persistence, allowing programs to save information permanently to a storage disk so it isn't lost when the application closes or the system powers down. It serves as a universal bridge for software interoperability, letting different systems exchange data using standardized formats like CSV or JSON, and allows programs to efficiently stream massive datasets that are too large to fit into a computer's temporary memory (RAM). Additionally, it is essential for maintaining application configuration settings and generating long-term audit logs, making it a foundational tool for building functional, scalable, and secure software.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/lameck_odhiambo_748e9ef18/file-handling-in-python-3jhc

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
