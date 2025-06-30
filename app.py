import os
import sqlite3
from dotenv import load_dotenv
from flask import Flask, url_for, redirect, render_template, request, session

load_dotenv("key.env")

app = Flask(__name__)
app.secret_key = os.getenv("secret")

@app.route("/")
@app.route("/main")
def main():
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

    users = cur.execute("SELECT user_name, user_password FROM users")

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

    users = cur.execute("SELECT user_name FROM users")

    username_found = False

    for i in users:
        if i[0] == username:
            username_found = True
            break
    
    if not username_found:
        cur.execute(f"INSERT INTO users (user_name, user_password) VALUES ('{username}', '{password}')")
        conn.commit()

        session["username"] = username
        session["logged_in"] = True

        return redirect(url_for("main"))
    else:
        return redirect(url_for("signup"))

if __name__ == "__main__":
    app.run()