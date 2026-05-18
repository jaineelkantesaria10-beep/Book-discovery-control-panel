from flask import Flask, render_template, request, redirect, url_for
import sqlite3
# Bhavnesh ki file se uska function import kiya
from api_handler import search_books_from_api

app = Flask(__name__)
DB_NAME = "books_repository.db"

# 1. Main Home Page Route
@app.route('/')
def index():
    # Shuruat mein jab page khulega, toh koi books nahi dikhayenge (empty list)
    return render_template('index.html', books=[])

# 2. Search Route (Yeh tera main kaam hai - Connecting frontend to Bhavnesh's API)
@app.route('/search', methods=['POST'])
def search_books():
    # Frontend ke input field se user ka keyword uthaya
    search_query = request.form.get('search_query')
    
    # Bhavnesh ka function chalaya aur usme query daal di
    # Yeh function ab internet se real books lekar aayega
    real_books = search_books_from_api(search_query)
    
    # Wapas index.html par bhej rahe hain, par is baar real data ke saath
    return render_template('index.html', books=real_books, query=search_query)

# 3. Control Panel Route (Purana database wala code, isko touch nahi kiya)
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