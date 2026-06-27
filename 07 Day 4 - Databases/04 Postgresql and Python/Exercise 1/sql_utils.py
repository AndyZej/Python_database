import psycopg2
from psycopg2.extras import RealDictCursor

USER = "zdenkocepan"
HOST = "localhost"
PASSWORD = ""
PORT = 5432


def execute_sql(sql_code, db):
    """
    Run given sql code with psycopg2.

    :param str sql_code: sql code to run
    :param str db: name of db,

    :rtype: list
    :return: data from psycobg2 cursor as a list (can be None) if nothing to fetch.
    """
    conn = psycopg2.connect(
        database=db,
        user=USER,
        host=HOST,
        port=PORT
    )

    data = None
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(sql_code)
        data = cur.fetchall()

    conn.close()

    return data


data = execute_sql("SELECT * FROM customers", "exercises_db")

for row in data:
    for k, v in row.items():
        print(f"{k}:  {v}")

    print()