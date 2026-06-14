import sqlite3

def get_db():
    conn = sqlite3.connect("student.db")
    return conn

def create_table():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS stud(
        Rollno INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        Marks INTEGER,
        Performance TEXT,
        Progress TEXT
    )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()
    print("Database and Table Created Successfully")