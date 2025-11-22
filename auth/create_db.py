import sqlite3
from config.settings import DB_PATH

def main():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    );
    """)

    conn.commit()
    conn.close()
    print(f"Banco de dados criado com sucesso em: {DB_PATH}")

if __name__ == "__main__":
    main()
