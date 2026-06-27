@app.route("/add_client", methods=["GET", "POST"])
def add_client():
    if request.method == "POST":
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO Customers (name) VALUES (%s)",
            (request.form["name"],)
        )
        conn.commit()
        conn.close()
        return redirect("/clients")

    return '''
        <form method="post">
            Name: <input name="name">
            <input type="submit">
        </form>
    '''