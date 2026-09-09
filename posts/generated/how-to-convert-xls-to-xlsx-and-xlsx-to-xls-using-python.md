---
title: "How to Convert XLS to XLSX and XLSX to XLS Using Python"
slug: "how-to-convert-xls-to-xlsx-and-xlsx-to-xls-using-python"
author: "Leon Davis"
source: "devto_python"
published: "Wed, 09 Sep 2026 10:28:09 +0000"
description: "Excel files can be saved in different formats depending on the version of Microsoft Excel and the application that generates them. Among these formats, .xls ..."
keywords: "xls, xlsx, excel, workbook, files, format, file, python"
generated: "2026-09-09T11:03:04.611373"
---

# How to Convert XLS to XLSX and XLSX to XLS Using Python

## Overview

Excel files can be saved in different formats depending on the version of Microsoft Excel and the application that generates them. Among these formats, .xls and .xlsx are the two most commonly used. The .xls format was used by older versions of Excel, while .xlsx became the default format after Excel 2007. Although .xlsx is now widely used, .xls files can still be found in many existing systems and applications. When working with Excel files in Python, converting between these two formats is sometimes necessary, especially when dealing with legacy files or applications with specific format requirements. This article shows how to convert .xls files to .xlsx and .xlsx files to .xls using Python. Why Convert between XLS and XLSX? The .xlsx format provides several improvements over the older .xls format: Higher capacity : .xlsx supports more rows and columns than .xls . Better compatibility : It works better with newer versions of Excel and other spreadsheet applications. Smaller file sizes : .xlsx uses ZIP compression, which can reduce file size. More features : Newer Excel functions, formulas, and formatting options are better supported. However, .xls files are still required in some cases, especially when working with older software or systems. For these scenarios, converting .xlsx files back to .xls can also be useful. Tools for Converting Excel Files in Python There are several Python libraries available for working with Excel files. For example, pandas is commonly used for processing spreadsheet data, while openpyxl is mainly used for reading and writing .xlsx files. xlrd and xlwt can also be used when working with older .xls files. In this article, we will use Spire.XLS for Python to perform the conversion. It provides APIs for loading Excel workbooks and saving them in different Excel formats. Install the Required Library Install the library with pip before starting: pip install spire.xls After installation, import the required classes in your Python project. Convert XLS to XLSX Using Python To convert an .xls file to .xlsx , load the workbook and save it with the target Excel format. Example: from spire.xls import * # Create a workbook object workbook = Workbook () # Load the XLS file workbook . LoadFromFile ( " input.xls " ) # Save as XLSX format workbook . SaveToFile ( " output.xlsx " , ExcelVersion . Version2013 ) # Release resources workbook . Dispose () The LoadFromFile() method loads the existing Excel file, and SaveToFile() saves the workbook in the specified format. The ExcelVersion.Version2013 parameter indicates that the output file should be saved as an .xlsx file. After running the code, the converted file will be saved as output.xlsx . Convert XLSX to XLS Using Python The conversion from .xlsx to .xls follows the same process. The only difference is the Excel version used when saving the file. Example: from spire.xls import * # Create a workbook object workbook = Workbook () # Load the XLSX file workbook . LoadFromFile ( " input.xlsx " ) # Save as XLS format workbook . SaveToFile ( " output.xls " , ExcelVersion . Version97To2003 ) # Release resources workbook . Dispose () Here, ExcelVersion.Version97To2003 specifies the older .xls format. The workbook is loaded from input.xlsx and saved as output.xls . Important Notes XLS format limitations : The .xls format has several restrictions compared with .xlsx : Maximum of 65,536 rows. Maximum of 256 columns. Limited support for newer Excel features. Because of these limitations, converting a large .xlsx file into .xls should be done carefully. Some data or features may not be preserved after conversion. Formatting compatibility : When converting between .xls and .xlsx, some Excel features may not be fully supported by both formats. After conversion, check the workbook to ensure that formulas, formatting, and other features are preserved as expected. Conclusion Converting between .xls and .xlsx formats is a common task when processing Excel files in Python. By loading an existing workbook and saving it with the required Excel version, developers can convert files between the two formats with a small amount of code.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/leondavis1991/how-to-convert-xls-to-xlsx-and-xlsx-to-xls-using-python-32gb

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
