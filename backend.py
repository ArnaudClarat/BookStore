import sqlite3

def connect():
    conn = sqlite3.connect("bookstore.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER")
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn = sqlite3.connect("bookstore.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book (title, author, year, isbn) VALUES (?,?,?,?)", (title, author, year, isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("bookstore.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    row = cur.fetchall()
    conn.close()
    return row

def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("bookstore.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title, author, year, isbn))
    row = cur.fetchall()
    conn.close()
    return row

def view_one(id):
    conn = sqlite3.connect("bookstore.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE id = ?", (id,))
    conn.close()

def update(id, title, author, year, isbn):
    conn = sqlite3.connect("bookstore.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title = ?, SET author = ?, SET year = ?, SET isbn = ? WHERE id = ?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()

def delete(id):
    conn = sqlite3.connect("bookstore.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id = ?", (id,))
    conn.commit()
    conn.close()