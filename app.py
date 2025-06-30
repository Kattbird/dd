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
    return render_template("main.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

if __name__ == "__main__":
    app.run()