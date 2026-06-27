@app.route("/book_details/<int:id>")
def book_details(id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Books WHERE id=%s", (id,))
    book = cur.fetchone()
    conn.close()
    return str(book)