![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


# Python and databases - homework - Day 1

Your task will be to create software to manage a library. Remember to save all your queries in a file. They will be useful to you later. Perform the following tasks:

1. prepare a database named **library_db**.
2. create the tables:
    * Author:
      * id: serial
      * name: string
    * Book:
      * id: serial
      * ISBN: string (max 13 characters)
      * name: string
      * description: string
      * is_loaned: bool, (default: False)
    * client:
      * id: serial
      * first_name: string
      * last_name: string
    * Category:
      * id: serial
      * name: string
3. add to the database:
    * 5 authors,
    * 10 books,
    * 3 customers.
4 Write queries to retrieve the following data from the database:
    * list of all authors,
    * author with id `2`,
    * list of all books,
    * book with id `2`,
    * list of all customers,
    * customer with id `1`.
5 Write a query to delete a book with id `5`.  

Remember to test SQL queries in the console or application first, only then write Python code.
