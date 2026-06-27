from psycopg2 import connect


CREATE_DB = "CREATE DATABASE exam2"
DB_USER = "postgres"
DB_PASSWORD = "coderslab"
DB_HOST = "127.0.0.1"

cnx = connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
cnx.autocommit = True
cursor = cnx.cursor()
cursor.execute(CREATE_DB)
print("Database created")
cnx.close()