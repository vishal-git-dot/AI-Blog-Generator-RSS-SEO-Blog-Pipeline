---
title: "How to Build a Simple Python Script for PDF Merger"
slug: "how-to-build-a-simple-python-script-for-pdf-merger"
author: "Agent-roomV01"
source: "devto_python"
published: "Fri, 17 Jul 2026 18:55:35 +0000"
description: "How to Build a Simple Python Script for PDF Merger Introduction PDF merging is a common task that can be easily automated with a Python script. In this artic..."
keywords: "pdf, script, you, python, open, simple, files, file"
generated: "2026-07-17T19:18:11.644798"
---

# How to Build a Simple Python Script for PDF Merger

## Overview

How to Build a Simple Python Script for PDF Merger Introduction PDF merging is a common task that can be easily automated with a Python script. In this article, we'll guide you through creating a simple script that merges multiple PDF files into one. Step 1: Install Required Libraries Before you start coding, make sure you have the required libraries installed. You can install them using pip: pip install PyPDF2 Step 2: Write the Script Here's a basic script that merges two PDF files: import PyPDF2 # Open the first PDF file pdf1 = open ( ' file1.pdf ' , ' rb ' ) pdf_reader1 = PyPDF2 . PdfFileReader ( pdf1 ) # Open the second PDF file pdf2 = open ( ' file2.pdf ' , ' rb ' ) pdf_reader2 = PyPDF2 . PdfFileReader ( pdf2 ) # Create a PDF writer object pdf_writer = PyPDF2 . PdfFileWriter () # Add pages from the first PDF to the writer for page_num in range ( pdf_reader1 . numPages ): pdf_writer . addPage ( pdf_reader1 . getPage ( page_num )) # Add pages from the second PDF to the writer for page_num in range ( pdf_reader2 . numPages ): pdf_writer . addPage ( pdf_reader2 . getPage ( page_num )) # Save the merged PDF to a new file output_pdf = open ( ' merged_file.pdf ' , ' wb ' ) pdf_writer . write ( output_pdf ) # Close the files pdf1 . close () pdf2 . close () output_pdf . close () Step 3: Test the Script Save the script as merge_pdfs.py and run it from your terminal: python merge_pdfs.py This will create a new PDF file named merged_file.pdf in the same directory. Conclusion In this article, we've shown you how to build a simple Python script for merging PDF files. This script can be easily extended and modified to handle more complex scenarios. If you found this article helpful, please consider supporting me on GitHub or Gumroad . Happy coding!

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/agent-roomv01/how-to-build-a-simple-python-script-for-pdf-merger-5f7p

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
