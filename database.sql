import sqlite3


def create_database():
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL
        )
    """)

    cursor.execute(
        "INSERT INTO users (username) VALUES (?)",
        ("alice",)
    )

    connection.commit()
    connection.close()
