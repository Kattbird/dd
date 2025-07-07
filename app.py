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
    if "logged_in" in session:
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        mod = cur.execute(f"SELECT mod FROM users WHERE user_name='{session["username"]}'")
        return render_template("main.html", username=session["username"], logged_in=session["logged_in"], mod=mod)
    else:
        return render_template("main.html")

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
        
        mod = cur.execute(f"SELECT mod FROM users WHERE user_name='{session["username"]}';").fetchone()
        if mod:
            title = request.form.get("title")
            type = request.form.get("type")
            content = request.form.get("content")
            cur.execute(f"INSERT INTO items (item_name, item_type, item_content) VALUES ('{title}', '{type}', '{content}');")
            conn.commit()
            return redirect(url_for("main"))
    
@app.route("/fightning_styles")
def fighting_style():
    return render_template("fightning_styles.html")


@app.route("/magic")
def fighting_style():
    return render_template("magic.html")


@app.route("/races")
def fighting_style():
    return render_template("races.html")


@app.route("/skills")
def fighting_style():
    return render_template("skills.html")

if __name__ == "__main__":
    app.run()
