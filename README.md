# Mod 2 Review

## SQL and Relational Databases
 - Most people seem comfortable with this topic

## Object-Oriented Programming
 - A good number of people asked to hear more about this
 - Most important OOP concepts for data science:
    - Classes and instances
    - Class methods and instance methods
    - Class attributes and instance attributes
    - Inheritance
 - Check out the `oop_example.py` file, which has examples of all the most important stuff

## JSON and XML, APIs, Web Scraping
 - Mostly seems like you understand this.  Any questions?

## MongoDB and NoSQL
 - Some questions about the different kinds of NoSQL
 - Basic types of NoSQL:
    - Document store (e.g. MongoDB): basically like a giant dictionary, but each entry should have the same structure so you can query it in a structured way
    - Key-value store (e.g. Amazon S3 DynamoDB): truly just like a dictionary.  No guarantee that different values will have the same structure at all
    - Column store (e.g. HBase): instead of being arranged by rows, data is arranged by columns
    - Graph database: data is structured as nodes and edges (I drew an example of this on the board)

## Possibilities for Today's Lesson
 - Deeper dive into one-to-many vs. many-to-many relationships
 - SQL logic with JSON/APIs: using the [Star Wars API](https://swapi.co/documentation) to join two sets of JSON
 - SQL logic with classes and instances

...what we ended up doing was walking through the Star Wars API documentation and converting it into a domain model that uses SQL.  Then writing a couple `INSERT` and `SELECT` queries to show how a many-to-many relationship works.  **Key takeaway:** most real-world things have many-to-many relationships, but that means you need an extra table to represent each relationship, up to the overall number of tables - 1.  The reason you need a new table to represent the relationship is that SQL doesn't allow you to store lists of things in a single column, only individual things.  This is part of the advantage of NoSQL.