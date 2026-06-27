
from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

HTML = """
<!doctype html>
<title>Add Reader</title>
<h2>Add Reader</h2>

{% if error %}
<p style="color:red;">{{ error }}</p>
{% endif %}

<form method="post">
    Name: <input type="text" name="name"><br><br>
    Email: <input type="text" name="email"><br><br>
    <input type="submit" value="Submit">
</form>
"""

def get_db_connection():
    return sqlite3.connect("library.db")

@app.route("/", methods=["GET", "POST"])
def add_reader():
    error = None

    if request.method == "POST":
        name = request.form.get("name", "")
        email = request.form.get("email", "")

        # validation
        if not name or "@" not in email:
            error = "Invalid data!"
        else:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "INSERT INTO Readers (name, email) VALUES (?, ?)",
                (name, email)
            )

            conn.commit()
            conn.close()

    return render_template_string(HTML, error=error)

if __name__ == "__main__":
    app.run(debug=True)