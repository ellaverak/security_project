import sqlite3
#from werkzeug.security import generate_password_hash, check_password_hash

def connect():
    db = sqlite3.connect("src/db.sqlite3")
    db.isolation_level = None
    return db

def register(username, password):
    db = connect()
    #hash_value = generate_password_hash(password)
    try:
        #INJECTION
        #IDENTIFICATION AND AUTHENTICATION FAILURES
        db.execute("INSERT INTO users (username, password) VALUES ('"+username +"', '"+password+"')")
        #db.execute("INSERT INTO users (username, password) VALUES (?, ?)", [username, hash_value])
        db.commit()
    except:
        return False
    return login(username, password)

def login(username, password):
    db = connect()
    try:
        #INJECTION
        #IDENTIFICATION AND AUTHENTICATION FAILURES
        global user_id
        user_id = db.execute("SELECT id FROM users WHERE username='"+username+"' AND password='"+password+"'").fetchall()[0]
        user_id = user_id[0]
        #user = db.execute("SELECT id, password FROM users WHERE username=?", [username]).fetchall()[0]
        #user_id = user[0]
        if user_id == None:
            raise
        #if user_id == None or not check_password_hash(user[1], password):
        #    raise
    except:
        return False
    return True

def logout():
    global user_id
    user_id = None

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

def return_user_id():
    return user_id
