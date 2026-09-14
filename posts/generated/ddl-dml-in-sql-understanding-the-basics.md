---
title: "DDL & DML in SQL: Understanding the Basics."
slug: "ddl-dml-in-sql-understanding-the-basics"
author: "Feddy Mwanjumwa"
source: "devto_ai"
published: "Mon, 14 Sep 2026 12:17:32 +0000"
description: "When I started learning SQL, one of the first things I came across was DDL and DML. At first, the terms looked tough to learn and understand, but they are si..."
keywords: "table, students, ddl, dml, data, create, structure, database"
generated: "2026-09-14T12:21:57.415237"
---

# DDL & DML in SQL: Understanding the Basics.

## Overview

When I started learning SQL, one of the first things I came across was DDL and DML. At first, the terms looked tough to learn and understand, but they are simple once you understand what each one is responsible for. In this article, I'll explain: What DDL is What DML is Common DDL and DML commands Practical SQL examples The difference between DDL and DML What is DDL? DDL stands for Data Definition Language. DDL is used to define and modify the structure of a database. Think of DDL as building or changing the structure of a house. For example, DDL can be used to: 1.Create a table 2.Change a table 3.Delete a table 4.Add or remove columns DDL Commands CREATE- Creates a database object ALTER - Changes the structure of an object DROP - Deletes an object TRUNCATE - Removes all rows from a table 1. CREATE CREATE is used to create database objects such as tables. For example, let's create a students table: CREATE TABLE students ( student_id INT, student_name VARCHAR(100), age INT, grade VARCHAR(10) ); This creates a table called students with four columns. 2. ALTER ALTER is used to modify the structure of an existing table. For example, we can add an email column: ALTER TABLE students ADD COLUMN email VARCHAR(100); The table now has an additional email column. We could also rename a column: ALTER TABLE students RENAME COLUMN grade TO class_grade; 3. DROP DROP permanently removes a database object. For example: DROP TABLE students; This removes the entire students table. This should be used carefully because the table and its data are removed. 4. TRUNCATE TRUNCATE removes all rows from a table while keeping the table structure. TRUNCATE TABLE students; The table still exists, but the records inside it are removed. What is DML? DML stands for Data Manipulation Language. DML is used to work with the data stored inside database tables. If DDL builds the house, DML is what you use to work with the things inside the house. DML allows us to: Add data Change data Delete data Retrieve data Common DML Commands INSERT Adds new records UPDATE Modifies existing records DELETE Removes records SELECT Retrieves records ** 1. INSERT** INSERT adds new records to a table. For example: INSERT INTO students (student_id, student_name, age, class_grade) VALUES (1, 'Amos', 17, 'A'); We can insert multiple students at once: ` INSERT INTO students (student_id, student_name, age, class_grade) VALUES (2, 'Faith', 16, 'A'), (3, 'Brian', 18, 'B'); 2. SELECT SELECT is used to retrieve data from a table. To see everything in the table: SELECT * FROM students; We can also select specific columns: SELECT student_name, class_grade FROM students; Or filter the results: SELECT * FROM students WHERE age >= 17; 3. UPDATE UPDATE changes existing records. For example, suppose Brian's grade changes from B to A: UPDATE students SET class_grade = 'A' WHERE student_name = 'Brian'; The WHERE clause is extremely important. Without it: UPDATE students SET class_grade = 'A'; every student would be changed to grade A. 4. DELETE DELETE removes records from a table. For example: DELETE FROM students WHERE student_id = 3; This removes Brian's record. Again, be careful with the WHERE clause. Running: DELETE FROM students; would remove all records from the table. DDL vs DML The easiest way I remember the difference is: DDL = structure DML = data For example: CREATE TABLE students (...); This changes the structure of the database, so it is DDL. While: INSERT INTO students (...); adds data to the table, so it is DML. ** Quick Comparison ** DDL DML Defines database structure Manipulates stored data CREATE INSERT ALTER UPDATE DROP DELETE TRUNCATE SELECT A Practical Example Let's imagine we're building a small school database. First, we create the table: CREATE TABLE students ( student_id INT, student_name VARCHAR(100), age INT, class_grade VARCHAR(10) ); That's DDL because we're defining the table structure. Next, we add students: INSERT INTO students VALUES (1, 'Amos', 17, 'A'), (2, 'Faith', 16, 'A'), (3, 'Brian', 18, 'B'); That's DML because we're adding data. Now let's retrieve the students: SELECT * FROM students; We can update Brian's grade: UPDATE students SET class_grade = 'A' WHERE student_name = 'Brian'; And finally, we could remove a student: DELETE FROM students WHERE student_id = 3; Final Thoughts Understanding DDL and DML is one of the foundations of SQL. The main thing to remember is that: DDL deals with the structure. DML deals with the data. Once these concepts become familiar, working with databases becomes much easier because you can distinguish between changing the database itself and changing the information stored inside it. I'm continuing to learn SQL by building practical projects and working with real-world datasets, and these fundamentals have become an important part of that process.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/feddy_mwanjumwa_e4047cf0c/ddl-dml-in-sql-understanding-the-basics-4l7e

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
