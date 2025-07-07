import os
import sqlite3
from dotenv import load_dotenv
from flask import Flask, url_for, redirect, render_template, request, session

load_dotenv("key.env")

app = Flask(__name__)
app.secret_key = os.getenv("key")

@app.route("/")
@app.route("/main")
def main():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
<<<<<<< HEAD
    item_types = cur.execute("SELECT item_type FROM items;").fetchall()
    if "logged_in" in session:
        mod = cur.execute(f"SELECT mod FROM users WHERE user_name='{session["username"]}'")
=======

    item_types = cur.execute("SELECT item_type FROM items;").fetchall()
    if "logged_in" in session:
        mod = bool(cur.execute(f"SELECT mod FROM users WHERE user_name='{session["username"]}'"))
>>>>>>> b98b9bafa151c830d7a69df6f919523b640236a4
        return render_template("main.html", username=session["username"], logged_in=session["logged_in"], mod=mod, types=item_types)
    else:
        return render_template("main.html", types=item_types)
    
@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/login_check", methods=["POST", "GET"])
def login_check():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    username = request.form.get("user")
    password = request.form.get("pass")

    users = cur.execute("SELECT user_name, user_password FROM users;")

    username_found = False
    password_found = False

    for i in users:
        if i[0] == username:
            username_found = True
            if i[1] == password:
                password_found = True
            break
    
    if (username_found and password_found):

        session["username"] = username
        session["logged_in"] = True

        return redirect(url_for("main"))
    else:
        return redirect(url_for("login"))

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/signup_check", methods=["POST", "GET"])
def signup_check():
    
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    username = request.form.get("user")
    password = request.form.get("pass")

    users = cur.execute("SELECT user_name FROM users;")

    username_found = False

    for i in users:
        if i[0] == username:
            username_found = True
            break
    
    if not username_found:
        cur.execute(f"INSERT INTO users (user_name, user_password, mod) VALUES ('{username}', '{password}', FALSE);")
        conn.commit()

        session["username"] = username
        session["logged_in"] = True

        return redirect(url_for("main"))
    else:
        return redirect(url_for("signup"))

@app.route("/logout")
def logout():
    if "logged_in" in session:
        session.pop("username")
        session.pop("logged_in")
    return redirect(url_for("main"))

@app.route("/content_add")
def content_add():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    if "logged_in" in session:
        mod = bool(cur.execute(f"SELECT mod FROM users WHERE user_name='{session["username"]}';").fetchone()[0])
        if mod:
            return render_template("content_add.html")
        else:
            return redirect(url_for("main"))
    else:
        return redirect(url_for("main"))

@app.route("/content_add_db", methods=["POST", "GET"])
def content_add_db():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    if "logged_in" in session:
        mod = bool(cur.execute(f"SELECT mod FROM users WHERE user_name='{session["username"]}';").fetchone())
        if mod:
            title = request.form.get("title")
            type = request.form.get("type")
            content = request.form.get("content")
            cur.execute(f"INSERT INTO items (item_name, item_type, item_content) VALUES ('{title}', '{type}', '{content}');")
            conn.commit()
            return redirect(url_for("main"))
    

@app.route("/types/<type_chosen>")
def content(type_chosen):
    type_chosen = type_chosen[0]
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    title = cur.execute(f"SELECT item_name FROM items WHERE item_type=('{type_chosen}');")
    content = cur.execute(f"SELECT item_content FROM items WHERE item_type=('{type_chosen}');")
<<<<<<< HEAD
=======
    print()
>>>>>>> b98b9bafa151c830d7a69df6f919523b640236a4
    return render_template("content.html", type=type_chosen, title=title, content=content)

if __name__ == "__main__":
    app.run()
