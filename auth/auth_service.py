from passlib.hash import argon2
import sqlite3
from config.settings import DB_PATH

class AuthService:
    def __init__(self):
        self.db_path = DB_PATH

    def create_user(self, email, password):
        hashed = argon2.hash(password)

        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO users (email, password) VALUES (?, ?)",
            (email, hashed)
        )

        conn.commit()
        conn.close()

    def authenticate(self, email, password):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()

        cur.execute("SELECT password FROM users WHERE email = ?", (email,))
        row = cur.fetchone()

        conn.close()

        if not row:
            return False

        stored_hash = row[0]
        return argon2.verify(password, stored_hash)
