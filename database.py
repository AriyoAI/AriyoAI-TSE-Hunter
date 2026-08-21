import sqlite3
from datetime import datetime


DB_NAME = "hunter.db"


def create_database():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS signals (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        symbol TEXT,

        score INTEGER,

        reasons TEXT,

        created_at TEXT

    )
    """)

    conn.commit()
    conn.close()



def save_signal(symbol, score, reasons):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO signals
        (symbol, score, reasons, created_at)

        VALUES (?, ?, ?, ?)
        """,
        (
            symbol,
            score,
            ",".join(reasons),
            datetime.now().isoformat()
        )
    )

    conn.commit()
    conn.close()



def signal_exists(symbol):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT symbol
        FROM signals
        WHERE symbol=?
        """,
        (symbol,)
    )

    result = cursor.fetchone()

    conn.close()

    return result is not None



if __name__ == "__main__":

    create_database()

    print(
        "Database ready 🟢"
    )
