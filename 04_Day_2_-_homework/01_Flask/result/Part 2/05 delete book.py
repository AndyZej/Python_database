@app.route("/delete_book/<int:id>")
def delete_book(id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM Books WHERE id=%s", (id,))
    conn.commit()
    conn.close()
    return redirect("/books")