@app.route("/books")
def books():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, title FROM Books")
    books = cur.fetchall()
    conn.close()
    return render_template_string("""
        <ul>
        {% for b in books %}
            <li><a href="/book_details/{{ b[0] }}">{{ b[1] }}</a></li>
        {% endfor %}
        </ul>
    """, books=books)