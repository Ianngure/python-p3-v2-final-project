import sqlite3
from datetime import datetime
from models import Book, Borrow
from database import create_connection

def add_book(title, author):
    conn = create_connection()
    c = conn.cursor()
    c.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
    conn.commit()
    conn.close()

def view_books():
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM books")
    books = c.fetchall()
    conn.close()
    return [Book(*book) for book in books]

def delete_book(book_id):
    conn = create_connection()
    c = conn.cursor()
    c.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()

def find_book(title):
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM books WHERE title LIKE ?", ('%' + title + '%',))
    books = c.fetchall()
    conn.close()
    return [Book(*book) for book in books]

def borrow_book(book_id, borrower):
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT available FROM books WHERE id = ?", (book_id,))
    available = c.fetchone()[0]
    if available:
        borrow_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        c.execute("INSERT INTO borrows (book_id, borrower, borrow_date) VALUES (?, ?, ?)", (book_id, borrower, borrow_date))
        c.execute("UPDATE books SET available = 0 WHERE id = ?", (book_id,))
        conn.commit()
    conn.close()

def return_book(book_id):
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT available FROM books WHERE id = ?", (book_id,))
    available = c.fetchone()[0]
    if not available:
        return_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        c.execute("UPDATE borrows SET return_date = ? WHERE book_id = ? AND return_date IS NULL", (return_date, book_id))
        c.execute("UPDATE books SET available = 1 WHERE id = ?", (book_id,))
        conn.commit()
    conn.close()
