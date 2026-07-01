
import sqlite3
from flask import Flask, render_template, request, flash


app = Flask(__name__)
app.secret_key = "Sakshi123"

def get_db():
   """Database connection""" 
   conn = sqlite3.connect('myproject.db')
   conn.row_factory = sqlite3.Row  # To access columns by name
   return conn

def init_db():
    
    
    conn = get_db()

conn = sqlite3.connect("students.db")
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

conn = sqlite3.connect('myproject.db')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
''')

try:
     cur.execute("Alter table users ADD column role text default 'student' ")
except Exception:
     pass

conn.commit()
conn.close()

print("Students table created successfully!")

conn = sqlite3.connect('table.db')
cur = conn.cursor()

cur.execute('''
                  CREATE TABLE IF NOT EXISTS subjects (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     name TEXT NOT NULL UNIQUE
                     )
                     '''
                  )
default_subjects = ['Java', 'C++', 'Python', 'Operating Systems', 'Data Structures', 'Database Management Systems', 'Computer Networks']

for subject in default_subjects:
         try:
               conn.execute("INSERT INTO subjects (name) VALUES (?)", (subject,))
         except sqlite3.IntegrityError:
               # Subject already exists, ignore the error
               pass
                 
conn.commit()
conn.close()
    
    
init_db()  # Initialize the database
if __name__ == "__main__":
   app.run(debug=True)

