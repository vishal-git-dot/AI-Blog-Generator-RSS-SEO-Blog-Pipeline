---
title: "How to Connect Azure SQL Database in Azure Databricks with PySpark"
slug: "how-to-connect-azure-sql-database-in-azure-databricks-with-pyspark"
author: "Jin"
source: "devto_python"
published: "Wed, 12 Aug 2026 06:59:55 +0000"
description: "In this article, I will show how to connect Azure SQL Database from Azure Databricks , read a SQL table or query result, and write a Spark DataFrame back to ..."
keywords: "sql, azure, data, database, spark, databricks, read, connect"
generated: "2026-08-12T07:40:00.501742"
---

# How to Connect Azure SQL Database in Azure Databricks with PySpark

## Overview

In this article, I will show how to connect Azure SQL Database from Azure Databricks , read a SQL table or query result, and write a Spark DataFrame back to Azure SQL Database. We will use PySpark because Azure Databricks is built for distributed data processing. PySpark can read data from external databases into Spark DataFrames, transform the data at scale, and write the result back to Azure SQL Database. Microsoft also provides Spark connector support for SQL Server and Azure SQL as input data sources and output sinks for Spark jobs. Connect the Azure SQK Database define the Azure SQL Database connection settings. Read data from Azure SQL Database Read a full table and Read a SQL query To read a full table, use the dbtable option. To run a SQL query against Azure SQL Database and load the result into Databricks, use the query option. Databricks also supports JDBC-style reads and writes with Spark Data Source APIs, including reading from a table or pushing down a source SQL query. Write Data to Azure SQL Database In this example, we first create a small pandas DataFrame and convert it to a Spark DataFrame. import pandas as pd data = { " Product " : [ " Laptop " , " Mouse " , " Keyboard " , " Monitor " , " Headset " , " Webcam " , " USB Hub " , " Laptop " , " Mouse " , " Monitor " ], " Region " : [ " North " , " South " , " East " , " West " , " North " , " East " , " South " , " West " , " North " , " East " ], " Units_Sold " : [ 15 , 42 , 30 , 8 , 25 , 17 , 60 , 22 , 38 , 10 ], " Revenue " : [ 22500 , 1260 , 2400 , 3200 , 1875 , 850 , 1800 , 33000 , 1140 , 4000 ] } pdf = pd . DataFrame ( data ) df = spark . createDataFrame ( pdf ) display ( df ) In Azure Databricks notebooks, spark is usually available automatically. If you run the code outside Databricks, you may need to create a SparkSession manually. Use .write.format("sqlserver") and provide the connection options. df . write . format ( " sqlserver " ) . options ( ** SQL_OPTIONS ) . option ( " dbtable " , " dbo.test_table " ) . mode ( " overwrite " ) #or "append" . save () Explore more Jin Follow Hello there! 👋 I'm Jin, a Business Intelligence Developer with a passion for all things data. Proficient in Python, SQL, Power BI, Tableau Thank you for taking the time to explore data-related insights with me. I appreciate your engagement. Connect with me on LinkedIn Connect with me on X

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/luca1iu/how-to-connect-azure-sql-database-in-azure-databricks-with-pyspark-557f

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
