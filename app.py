from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DB_NAME = "books_repository.db"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/control-panel')
def control_panel():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM saved_books")
    books = cursor.fetchall()
    conn.close()
    return render_template('control_panel.html', books=books)

if __name__ == '__main__':
    from database import init_db
    init_db()
    app.run(debug=True)