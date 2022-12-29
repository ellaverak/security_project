import sqlite3

def connect():
    db = sqlite3.connect("src/db.sqlite3")
    db.isolation_level = None
    return db

def register(username, password):
    #no hash
    #injection!
    #default account available
    db = connect()
    try:
        db.execute("INSERT INTO users (username, password) VALUES (?, ?)", [username, password])
        db.commit()
    except:
        return False
    return login(username, password)

def login(username, password):
    db = connect()
    try:
        global user_id
        user_id = db.execute("SELECT id FROM users WHERE username=? AND password=?", [username, password]).fetchall()[0]
        if user_id == None:
            raise
    except:
        return False
    return True

def logout():
    global user_id
    user_id = None

def return_user_id():
    return user_id

def save(author, name, publisher, year):
    db = connect()
    try:
        db.execute("INSERT INTO saved_references (author, name, publisher, year, user_id) VALUES (?, ?, ?, ?, ?)", [author, name, publisher, year, user_id[0]])
        db.commit()
    except:
        return False
    return True

def get_references():
    db = connect()
    try:
        references = db.execute("SELECT author, name, publisher, year FROM saved_references WHERE user_id = ?", [user_id[0]]).fetchall()
    except:
        return []
    return references