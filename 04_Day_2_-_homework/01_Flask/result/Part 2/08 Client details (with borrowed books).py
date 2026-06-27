@app.route("/client_details/<int:id>")
def client_details(id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        SELECT b.title
        FROM Loans l
        JOIN Books b ON l.book_id = b.id
        WHERE l.customer_id = %s
    """, (id,))
    books = cur.fetchall()
    conn.close()
    return str(books)