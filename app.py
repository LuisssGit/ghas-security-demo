from flask import Flask, request
import sqlite3
import subprocess

app = Flask(__name__)


@app.route("/user")
def get_user():
    username = request.args.get("username", "")

    # INTENCIONALMENTE VULNERABLE:
    # SQL Injection
    query = f"SELECT id, username FROM users WHERE username = '{username}'"

    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute(query)

    users = cursor.fetchall()
    connection.close()

    return {"users": users}


@app.route("/ping")
def ping():
    host = request.args.get("host", "localhost")

    # INTENCIONALMENTE VULNERABLE:
    # Command Injection
    result = subprocess.check_output(
        f"ping -c 1 {host}",
        shell=True
    )

    return result.decode()


@app.route("/")
def home():
    return "GHAS Security Demo"


if __name__ == "__main__":
    app.run(debug=True)
