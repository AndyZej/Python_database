rom psycopg2 import connect, OperationalError
from psycopg2.errors import DuplicateDatabase

CREATE_DB = "CREATE DATABASE exam2"

DB_USER = "postgres"
DB_PASSWORD = "coderslab"
DB_HOST = "127.0.0.1"

try:
    connection = connect(
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST
    )
    connection.autocommit = True
    cursor = connection.cursor()

    try:
        cursor.execute(CREATE_DB)
        print("Database created")
    except DuplicateDatabase:
        print("Database already exists")

    connection.close()

except OperationalError as error:
    print("Connection error:", error)