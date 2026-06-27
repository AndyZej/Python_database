from psycopg2 import connect
...
cnx = connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
cnx.autocommit = True
cursor = cnx.cursor()