@app.route("/loan", methods=["GET", "POST"])
def loan():
    if request.method == "POST":
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO Loans (customer_id, book_id, loan_date)
            VALUES (%s, %s, CURRENT_DATE)
        """, (request.form["customer"], request.form["book"]))
        conn.commit()
        conn.close()
        return redirect("/books")

    return "Loan form here"