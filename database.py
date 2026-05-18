import sqlite3

DB_NAME = "books_repository.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS saved_books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT,
            isbn TEXT,
            status TEXT DEFAULT 'To Read'
        )
    ''')
    conn.commit()
    conn.close()
    print("Database initialized successfully!")

if __name__ == "__main__":
    init_db()
    # Yeh function hum bana rahe hain taaki API ka data isme daal kar DB me save kar sakein
def insert_book(title, author, isbn, status='To Read'):
    conn = sqlite3.connect(DB_NAME) # Database file se connection joda
    cursor = conn.cursor() # Ek pointer banaya jo SQL chalayega
    
    # SQL Command: Table me Data Insert karne ke liye
    cursor.execute('''
        INSERT INTO saved_books (title, author, isbn, status)
        VALUES (?, ?, ?, ?)
    ''', (title, author, isbn, status))
    
    conn.commit() # Is line se data computer ki hard-disk me pakka save ho jata hai
    conn.close()  # Connection band kiya taaki file lock na ho
    print(f"Bhai, successfully save ho gayi: {title}")