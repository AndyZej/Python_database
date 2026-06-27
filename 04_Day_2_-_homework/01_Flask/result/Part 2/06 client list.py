@app.route("/clients")
def clients():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM Customers")
    data = cur.fetchall()
    conn.close()
    return str(data)