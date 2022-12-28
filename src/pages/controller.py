import sqlite3

def connect():
    db = sqlite3.connect("src/db.sqlite3")
    db.isolation_level = None
    return db

def register(username, password):
    db = connect()
    try:
        db.execute("INSERT INTO users (username, password) VALUES (?, ?)", [username, password])
        db.commit()
    except:
        return False
    return True

def login(username, password):
    return True
