CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT;
    user_name TEXT NOT NULL;
    user_password TEXT NO NULL;
);

CREATE TABLE items (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT;
    item_name TEXT NOT NULL;
    item_type TEXT NOT NULL;
    content TEXT NO NULL;
);

CREATE TABLE comment (
    comment_id INTEGER PRIMARY KEY AUTOINCREMENT;
    user_name TEXT NO NULL;
    content TEXT NO NULL;

);

