# Overview

This software is a python program that uses SQLite to create and populate a database. The program starts with multiple tables being created, then data is inserted into each table, one table is manipulated, some aggregate functions are used, and it finishes with an inner join. The data is displayed along the way so the changes can be seem.

This was written with the goal of becoming more familiar with SQlite. Previusly, I had only used MySQL in MySQL workbench and not in python, but I discovered that SQLite was even more user friendly than workbench. I look forward to using SQLite more in the future.

[Software Demo Video](https://youtu.be/e4v4Xvb-drE)

# Relational Database

This database uses SQLite, which is a C-language library that impements a SQL database engine. It is currently the most used database worldwide.

The inventory2 database is made up of four tables: brands, products, stock, and sales. The products table utilizes the brand_id found in the brands table, and the stock and sales tables use the product_id from the products table.

# Development Environment

This program was written using Python and SQLite in a VS code editor.

Python first came about in the early 1990's in the Netherlands. It was designed by Guido van Rossum, and the name Python came from his favorite TV show, Monty Python's Flying Circus. Python is a language that can be used daily in a variety of projects and industries. SQLite3 is a built-in library within Python.

# Useful Websites

- [Geeks for Geeks](https://www.geeksforgeeks.org/python-sqlite-join-clause/)
- [YouTube](https://www.youtube.com/watch?v=byHcYRpMgI4&t=3785s)

# Future Work

- Organize the program by using classes
- Expand the database
- Use more complex joins and functions