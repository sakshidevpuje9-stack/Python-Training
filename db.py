
import sqlite3

conn = sqlite3.connect("student.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    Rollno INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Subject TEXT NOT NULL,
    Marks INTEGER NOT NULL,
    Grade TEXT,
    Action TEXT
)
""")

conn.commit()
conn.close()

print("Students table created successfully!")