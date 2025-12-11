import sqlite3

conn = sqlite3.connect("userDatabase.db")
cursor = conn.cursor()
cursor.execute(""" CREATE TABLE IF NOT EXISTS users(
               id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
               name TEXT,
               email TEXT UNIQUE,
               password TEXT)
""")
conn.commit()
conn.close()