![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


# Python and databases &ndash; homework &ndash; Day 2

Link the tables with relationships:
1. authors and books (one-to-many relationship); for the sake of simplicity, assume that a book can only have one author; 
   it is enough if you edit appropriate tables,
2. books and categories (many-to-many relationship); one book can have many categories, one category can belong to many books; 
   add an appropriate intermediate table,
3. customers and books (many-to-many relationship); 
   in the intermediate table, add fields:
    * loan_date: date.
    * return_date: date (Null by default)


Using **Flask**, write an application for managing the library. The application should have the following pages:
1. `books` - list of all books,
2. `add_book` - a page that:
    * after entering by **GET** method, will display a form for adding a book,
    * after entering by **POST** method, will add the book to the database,
3. `book_details/<id>` - a page displaying detailed data of a book,
4. `delete_book/<id>` - a page for deleting a book with a given id
5. `clients` - a list of all customers,
6. `add_client` - a page that:
    * after entering by **GET** method, will display a form for adding a customer,
    * after entering by **POST** method. will add the customer to the database,
7. `delete_client/<id>` - a page for deleting a customer with given id
8. `client_details/<id>` - page displaying customer's detailed data, including all books borrowed by the customer
9. loan - a page for borrowing a book:
  * after entering by **GET** method, it should display a form with a list of customers and books,
  * after entering using **POST** method, it should add the loan to the database.


(*) You can develop the application at your own discretion, adding other useful functionalities. e.g.:
    * category management,
    * book return page,
    * loan blockade (mechanism which allows one customer to borrow only one book at a time)
    * possibility of rating books,
    * possibility of commenting books.
    
----

### Task: Practice SQL (*)

In the homework repository you will find a dump of the **football_en.sql** database.
This is the database with the results of a Football League.

Create a database on the server and import the SQL file. If you don't know how to do this, search on Google, using the keywords: *PostgreSQL, import, dump*.

Take a look at the structure and data. You will find there two tables: **Teams** and **Games**.
The first is a list of football clubs and points scored up to the date of the database export.
The second table is the results of the games. Fields `team_home` and `team_away` are foreign keys to the **Teams** table.

Write queries that:

1. extract the club that is the table leader,
2. extract the table, sorted by number of points scored,
3. extract all the matches that The Fiery Dragons played at home,
4. extract all the matches that The Fiery Dragons played away,
5. extract all the matches (home and away) of The Fiery Dragons.
6. add up all the goals scored by The Fiery Dragons at home and away
(make two queries: one home, and one away).

In subsections 3 - 5 the result should include in turn:

* name of the home team,
* name of the away team,
* number of goals scored by home team,
* number of goals scored by visitors.  
