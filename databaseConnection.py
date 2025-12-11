import sqlite3

def db_connection():
    conection =  sqlite3.connect("userDatabase.db")
    return conection