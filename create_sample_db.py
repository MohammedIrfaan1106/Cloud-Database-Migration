
import sqlite3

conn = sqlite3.connect("source.db")
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS employees(
 id INTEGER PRIMARY KEY,
 name TEXT,
 department TEXT
)
''')

cur.execute(
    "INSERT INTO employees(name, department) VALUES (?, ?)",
    ("John", "IT")
)

conn.commit()
conn.close()

print("Sample source database created.")
