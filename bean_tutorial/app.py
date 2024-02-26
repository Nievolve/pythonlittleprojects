import database
import sqlite3

#connection = database.connect()

sqlite3.connect("tdatabase.db")

with connection:
    connection.execute("CREATE TABLE beans (id INTERGER PRIMARY KEY, name TEXT, method TEXT, rating INTERGER))")
