@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO Books (title) VALUES (%s)",
            (request.form["title"],)
        )
        conn.commit()
        conn.close()
        return redirect("/books")

    return render_template_string("""
        <form method="post">
            Title: <input name="title">
            <input type="submit">
        </form>
    """)