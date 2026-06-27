import psycopg2
from psycopg2.extras import RealDictCursor


USER = "zdenkocepan"
HOST = "localhost"
PASSWORD = ""
PORT = 5432


def create_db(db):
    """
    Create db with given name.

    :param str db: name of db
    """
    # Place exercise 1 solution here.
    pass


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
        conn.commit()
        if sql_code[0] == "S":
            data = cur.fetchall()

    conn.close()

    return data