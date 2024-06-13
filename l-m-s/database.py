import sqlite3

def create_connection():
    conn = sqlite3.connect('library.db')
    return conn

def create_tables():
    conn = create_connection()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS books (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 title TEXT NOT NULL,
                 author TEXT NOT NULL,
                 available INTEGER DEFAULT 1)''')
    c.execute('''CREATE TABLE IF NOT EXISTS borrows (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 book_id INTEGER,
                 borrower TEXT NOT NULL,
                 borrow_date TEXT,
                 return_date TEXT,
                 FOREIGN KEY(book_id) REFERENCES books(id))''')
    conn.commit()
    conn.close()

create_tables()

