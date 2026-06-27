from flask import Flask, request, redirect
import psycopg2

app = Flask(__name__)

def get_conn():
    return psycopg2.connect(
        database="library",
        user="postgres",
        password="coderslab",
        host="127.0.0.1"
    )

# ---------------- BOOKS ----------------

@app.route("/books")
def books():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, title FROM Books")
    data = cur.fetchall()
    conn.close()
    return str(data)


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

    return '''
        <form method="post">
            Title: <input name="title">
            <input type="submit">
        </form>
    '''


@app.route("/book_details/<int:id>")
def book_details(id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Books WHERE id=%s", (id,))
    book = cur.fetchone()
    conn.close()
    return str(book)


@app.route("/delete_book/<int:id>")
def delete_book(id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM Books WHERE id=%s", (id,))
    conn.commit()
    conn.close()
    return redirect("/books")

# ---------------- CLIENTS ----------------

@app.route("/clients")
def clients():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM Customers")
    data = cur.fetchall()
    conn.close()
    return str(data)


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


@app.route("/delete_client/<int:id>")
def delete_client(id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM Customers WHERE id=%s", (id,))
    conn.commit()
    conn.close()
    return redirect("/clients")


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

# ---------------- LOAN ----------------

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

    return "Loan form"

if __name__ == "__main__":
    app.run(debug=True)