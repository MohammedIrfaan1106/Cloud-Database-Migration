
import sqlite3

def migrate_data():
    source = sqlite3.connect("source.db")
    target = sqlite3.connect("target.db")

    s_cur = source.cursor()
    t_cur = target.cursor()

    t_cur.execute('''
        CREATE TABLE IF NOT EXISTS employees(
            id INTEGER,
            name TEXT,
            department TEXT
        )
    ''')

    try:
        rows = s_cur.execute("SELECT * FROM employees").fetchall()

        for row in rows:
            t_cur.execute(
                "INSERT INTO employees VALUES (?,?,?)",
                row
            )

        target.commit()
        print(f"{len(rows)} records migrated successfully.")

    except Exception as e:
        print("Migration Error:", e)

    source.close()
    target.close()
