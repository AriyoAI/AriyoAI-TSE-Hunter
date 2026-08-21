import sqlite3


DB_NAME = "ariyoai.db"



def get_connection():

    return sqlite3.connect(DB_NAME)



def create_database():

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS signals (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        symbol TEXT,

        score INTEGER,

        reasons TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)


    conn.commit()

    conn.close()



def save_signal(symbol, score, reasons):

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        INSERT INTO signals
        (symbol, score, reasons)

        VALUES (?, ?, ?)
        """,

        (
            symbol,
            score,
            str(reasons)
        )

    )


    conn.commit()

    conn.close()



def get_signals():

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT *
        FROM signals
        ORDER BY id DESC
        """
    )


    data = cursor.fetchall()


    conn.close()


    return data
