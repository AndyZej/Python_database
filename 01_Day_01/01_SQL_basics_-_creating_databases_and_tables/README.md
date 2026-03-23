![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


## Exercise 1 &ndash; done with the lecturer

Create a new database named `exercises_db`. Save the command to a variable in the file **exercise1.py**.


## Exercise 2 &ndash; done with the lecturer

Create the following tables in a database named ```exercises_db```:

* products:
  * id: serial
  * name: string
  * description: string
  * price: float(5,2)
* Orders:
  * id: serial
  * description: string
* Customers:
  * id: serial
  * name: string
  * surname: string


Save the command to a variable in **task2.py** file.


## Exercise 3

Create a new database named ```cinemas_db```. Save the SQL code to a variable in the **exercise3.py** file.


## Exercise 4

In a database named ```cinemas_db``` create the following tables (remember that all names should be in English):

* cinemas:
  * id: serial
  * name: string
  * address: string
* Movies:
  * id: serial
  * name: string
  * description: string
  * rating: int
* Tickets:
  * id: serial
  * quantity: int
  * price: float
* Payments:
  * id: serial
  * type: string
  * date: date

1. Add appropriate attributes to the fields (e.g. each **id** should be a primary key, autonumbered).
2. Write appropriate SQL queries.
3. Write the SQL statement to a variable in the **exercise4.py** file.
4. Remember that if a database with the given name already exists, it cannot be created again. You must delete it first.
5. Carefully read the error codes returned by the database.

**Hint:** For string type, use varchar or text type, as appropriate.
