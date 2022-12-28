CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);

CREATE TABLE references (
    id INTEGER PRIMARY KEY,
    author TEXT,
    name TEXT,
    publisher TEXT,
    year INTEGER,
    user_id INTEGER REFERENCES users
);

