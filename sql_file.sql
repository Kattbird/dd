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

-- help for frontend
INSERT INTO users(user_name,user_password,mod) VALUES ('Dannyminer','Gribby','TRUE');
INSERT INTO users(user_name,user_password,mod) VALUES ('SabaEnjoyer','a','TRUE');
INSERT INTO users(user_name,user_password,mod) VALUES ('KaperDan','HWX','TRUE');
INSERT INTO items(item_name,item_type,item_content) VALUES (title,type,content);
SELECT item_name,item_content FROM items WHERE item_type='{}';
SELECT item_type FROM items;

-- Race
INSERT INTO items(item_name,item_type,item_content) VALUES ('Giant','Race','Eigheen percent chance');
INSERT INTO items(item_name,item_type,item_content) VALUES ('Human','Race','Eigheen percent chance');
INSERT INTO items(item_name,item_type,item_content) VALUES ('Fairy','Race','Eigheen percent chance');
INSERT INTO items(item_name,item_type,item_content) VALUES ('Beastman','Race','fifteen percent chance');
INSERT INTO items(item_name,item_type,item_content) VALUES ('Vampite','Race','fifteen percent chance - human sized - have ears - gray skin - cant fly - will burn in sun - slower healt regen during day - normal food is poison');
INSERT INTO items(item_name,item_type,item_content) VALUES ('Pig','Race','zero point tree tree percent chance');
INSERT INTO items(item_name,item_type,item_content) VALUES ('Goddes','Race','five percent chance - has two wings - human sized');
INSERT INTO items(item_name,item_type,item_content) VALUES ('Demon','Race','five percent chance - runs on all fours - have horns - skin tone red or other - only allowed first stage - demon combat style');

-- Magic
INSERT INTO items(item_name,item_type,item_content) VALUES ('Sunshine','Magic','Escanors magic');
INSERT INTO items(item_name,item_type,item_content) VALUES ('Drole Dance','Magic','Doles magic');
INSERT INTO items(item_name,item_type,item_content) VALUES ('Spirit Spear Chaestifol','Magic','King magic');
INSERT INTO items(item_name,item_type,item_content) VALUES ('Take-over','Magic','Random magic');
INSERT INTO items(item_name,item_type,item_content) VALUES ('Time','Magic','Dio magic');
INSERT INTO items(item_name,item_type,item_content) VALUES ('Transpork','Magic','Hawks magic');
INSERT INTO items(item_name,item_type,item_content) VALUES ('Light','Magic','Goddeses magic');
INSERT INTO items(item_name,item_type,item_content) VALUES ('Full counter','Magic','Maliodas magic');

-- Fighting Styles
INSERT INTO items(item_name,item_type,item_content) VALUES ('Brawler','Fighting Styles','Common - based on yuji intadori');
INSERT INTO items(item_name,item_type,item_content) VALUES ('Karate','Fighting Styles','?');
INSERT INTO items(item_name,item_type,item_content) VALUES ('Ashiin','Fighting Styles','legendary - Based on Rogue Lineages Ashiin race combat');
INSERT INTO items(item_name,item_type,item_content) VALUES ('Meliodas','Fighting Styles','mythical - only with voicelines');
INSERT INTO items(item_name,item_type,item_content) VALUES ('Giant','Fighting Styles','100%');
INSERT INTO items(item_name,item_type,item_content) VALUES ('Fairy','Fighting Styles','100%');
INSERT INTO items(item_name,item_type,item_content) VALUES ('Demon','Fighting Styles','100%');