![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


## Exercise 1 &ndash; done with the lecturer

Write a function `execute_sql` that runs any sql code. The function should take two parameters:
* database name,
* SQL query.

The function should take the sql code given in the parameter and  execute it on the given database.
The function should return a list of results (for queries of the **SELECT** type), or `None`.

Put the solution in the **sql_utils.py** file.


## Exercise 2 &ndash; done with the lecturer

Using Flask, write a program that will display on a page all the products contained in a database named  `exercises_db`.

**Hint:** The program should run an SQL query that retrieves all entries from an appropriate table, and then display them on the screen. You can use the code written in the previous exercise.

Put the solution in the file **sql_utils.py**.


## Exercise 3

1. In the file **form.html** there is a form for creating new entries in arrays.
Analyze the HTML and use this code in the rest of the exercise.
2. Using Flask, write a program that:
  * when entering using the **GET** method, will display a form containing the following fields:
    * `name` - movie name,
    * `description` - movie description,
    * `rating` - movie rating,
  * when entering using the **POST** method, will check if the form was filled in correctly:
    * if yes, it will save the movie to the database,
    * if not, it will return an appropriate message.

Share the program at `add_movie`.  
You can use the functions created in the previous exercises.


## Exercise 4

Using Flask, write a page that:
* will be available at `movies`,
* retrieves all the movies from the database,
* displays them on the page as a list.    


## Exercise 5 (*)

Using Flask, write a page that:
* will be available at `movie/<movie_id>`, the `movie_id`, being the number that specifies the **id** of the movie,
* retrieves information about the movie with the given ID from the database,
* displays it on the page.    


## Exercise 6 (*)

Using Flask, write a page that will delete the selected movie with the given **id**. The id should be passed in the page address.
The page should display information about the deletion of the table entry.


## Exercise 7 (*)

Using Flask, write a page to which you pass the id of a movie using the GET method. The page should:

- retrieve the movie data from the database; if you pass an invalid movie id, it should display the message "there is no such movie."
- display a form with the following fields:
  - movie id (hidden field, impossible to edit),
  - movie title,
  - movie description.

Each of these fields should be filled with data extracted from the database.

After submitting the form (using the POST method), the program should:

- retrieve the movie data from the database,
- generate an appropriate query, which will **change** the movie data in the database,
- execute this query,
- when everything is finished correctly, display the message "changed movie data",
- in case of an error, display the message "oops... something went wrong!".


First test your SQL queries in the console or admin panel, then write Python code.

**Note: If you see "write page" in the command prompt, it means that you need to write a Python program using Flask that will communicate with the
user via WWW pages and HTTP protocol.**
