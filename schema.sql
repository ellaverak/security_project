CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT
);

CREATE TABLE saved_references (
    id INTEGER PRIMARY KEY,
    author TEXT,
    name TEXT,
    publisher TEXT,
    year INTEGER,
    user_id INTEGER REFERENCES users
);

