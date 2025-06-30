CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name TEXT NOT NULL,
    user_password TEXT NOT NULL
);

CREATE TABLE items (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name TEXT NOT NULL,
    item_type TEXT NOT NULL,
    item_content TEXT NOT NULL
);

CREATE TABLE comments (
    comment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name TEXT NOT NULL,
    comment_content TEXT NOT NULL

);

CREATE TABLE posts (
    post_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    user_name TEXT NOT NULL,
    post_content TEXT NO NULL
);

CREATE TABLE item_comments (
    item_comment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_comment_content TEXT NOT NULL
    comment_id TEXT NOT NULL,
    user_name TEXT NOT NULL,
);