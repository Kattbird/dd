CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name TEXT NOT NULL,
    user_password TEXT NOT NULL,
    mod TEXT NOT NULL
);

CREATE TABLE items (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name TEXT NOT NULL,
    item_type TEXT NOT NULL,
    item_content TEXT NOT NULL
);

CREATE TABLE comments (
    comment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    comment_content TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)

);

CREATE TABLE posts (
    post_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    post_content TEXT NO NULL,  
    FOREIGN KEY(user_id) REFERENCES users(user_id)

);

CREATE TABLE item_comments (
    item_comment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    comment_id TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY(comment_id) REFERENCES comments(comment_id),
    FOREIGN KEY(user_id) REFERENCES users(user_id)
);


INSERT INTO users(user_name,user_password,mod) VALUES ('Dannyminer','Gribby','TRUE');
INSERT INTO users(user_name,user_password,mod) VALUES ('SabaEnjoyer','a','TRUE');
INSERT INTO users(user_name,user_password,mod) VALUES ('KaperDan','HWX','TRUE');