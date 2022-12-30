import sqlite3

cursor = sqlite3.connect("src/db.sqlite3")
cursor.isolation_level = None

cursor.execute("DROP TABLE IF EXISTS users")
cursor.execute("DROP TABLE IF EXISTS saved_references")
cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT)")
cursor.execute("CREATE TABLE saved_references (id INTEGER PRIMARY KEY, author TEXT, name TEXT, publisher TEXT, year INTEGER, user_id INTEGER REFERENCES users)")
