# SQL Heroes
## Description
Create an interactive shell script with the help of python that helps superheroes stay in touch with their friends and keep track of supervillains through the terminal.
For this project, we will be using Python 3 and PostgreSQL and the PyPi package psycopg3.
This project does not focus on the front end; you are creating a connection to a database with PostgresQL and an interactive shell script that helps navigate the database. You will demo your CRUD operations with an interactive python shell script.

## MVP
By default, the app should perform full CRUD operations (at least one of each Create, Read, Update, Delete) on the supplied SQL Database file and prompt the user for input in the terminal to show a list of heroes and their friends.

## CRUD principals
### CREATE New Hero AND/OR New Trait
1. CREATE TABLE table_name (
        id
    ); 

2. INSERT INTO
    heroes (name, about_me, biography)
VALUES
    (
        name, 
        about_me,
        biography
    );

### READ
SELECT * FROM table_name

### UPDATE
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;

### DELETE


## Python functions
### CREATE 
- def create_hero():

- def create_trait():


### READ



### UPDATE
- def update():


### DELETE
- def delete():