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
    item_types = set(cur.execute("SELECT item_type FROM items;").fetchall())
    if "logged_in" in session:
        mod = bool(cur.execute("SELECT mod FROM users WHERE user_name=?", (session["username"],)))
        return render_template("main.html", username=session["username"], logged_in=session["logged_in"], mod=mod, types=item_types)
    else:
        return render_template("main.html", types=item_types)
    
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()

        username = request.form.get("user")
        password = request.form.get("pass")

        users = cur.execute("SELECT user_password FROM users WHERE user_name = ?;", (username,)).fetchall()

        username_found = False
        password_found = False

        if len(users) > 0:
            username_found = True
            if users[0][0] == password:
                password_found = True
        
        if (username_found and password_found):

            session["username"] = username
            session["logged_in"] = True

            return redirect(url_for("main"))
        else:
            return render_template("login.html")
    else:
        return render_template("login.html")


@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()

        username = request.form.get("user")
        password = request.form.get("pass")

        users = cur.execute("SELECT user_name FROM users WHERE user_name = ?;", (username,)).fetchone()
        print(users )

        username_found = False
        if users and len(users) > 0:
            username_found = True
        
        if not username_found:
            cur.execute("INSERT INTO users (user_name, user_password, mod) VALUES (?, ?, ?);", (username, password,False))
            conn.commit()

            session["username"] = username
            session["logged_in"] = True

            return redirect(url_for("main"))
        else:
            return render_template("signup.html")
    else:
        return render_template("signup.html")

@app.route("/logout")
def logout():
    if "logged_in" in session:
        session.pop("username")
        session.pop("logged_in")
    return redirect(url_for("main"))

@app.route("/content_add", methods=["POST", "GET"])
def content_add():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    if "logged_in" in session:
        mod = bool(cur.execute("SELECT mod FROM users WHERE user_name=?;", (session["username"],)).fetchone()[0])
        if mod:
            if request.method == "POST":
                title = request.form.get("title")
                type = request.form.get("type")
                content = request.form.get("content")
                cur.execute("INSERT INTO items (item_name, item_type, item_content) VALUES (?, ?, ?);", (title, type, content),)
                conn.commit()
                return redirect(url_for("main"))
            else:
                return render_template("content_add.html")
        else:
            return redirect(url_for("main"))
    else:
        return redirect(url_for("main"))
    

@app.route("/types/<type_chosen>")
def content_add(type_chosen):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    title = cur.execute("SELECT item_name FROM items WHERE item_type=?;", (type_chosen,)).fetchall()
    content = cur.execute("SELECT item_content FROM items WHERE item_type=?;", (type_chosen,)).fetchall()
    print(title, content, type_chosen)
    return render_template("content.html", type=type_chosen, title=title, content=content)

@app.route("/content_remove", methods=["POST", "GET"])
def content_remove():
    if request.method == "POST":
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
    else:
        return render_template("content_remove.html")


if __name__ == "__main__":
    app.run()