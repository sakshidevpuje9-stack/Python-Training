
import sqlite3
from flask import Flask, render_template, request, redirect, flash, url_for

app = Flask(__name__, template_folder='day_relationships_templates')
app.secret_key = 'demo_secret_key'

def get_db():
    conn = sqlite3.connect('day_relationships.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS subject (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    ''')
    
    conn.execute('''
        CREATE TABLE IF NOT EXISTS student (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            subject_id INTEGER,
            FOREIGN KEY (subject_id) REFERENCES subject(id)
        )
    ''')
    conn.commit()
    conn.close()
    
@app.route("/home")
def home():
    conn = get_db()
    students_raw = conn.execute('SELECT * FROM student').fetchall()
    
    students_joined = conn.execute('''
        SELECT student.name AS student_name,
               subject.name AS subject_name    
        FROM student
        JOIN subject ON student.subject_id = subject.id
    ''').fetchall()
    
    conn.close()
    return render_template("home.html", students_raw=students_raw, students_joined=students_joined)

@app.route("/add_subject", methods=["GET", "POST"])
def add_subject():
    if request.method == "POST":
        name = request.form['name'].strip()
        conn = get_db()
        conn.execute('INSERT INTO subject (name) VALUES (?)', (name,))
        conn.commit()
        conn.close()
        flash(f"Subject '{name}' added successfully!")
        return redirect(url_for('home'))  # Fixed: home not home.html
    return render_template("add_subject.html")

@app.route("/add_student", methods=["GET", "POST"])
def add_student():
    conn= get_db()
    subject = conn.execute('SELECT * FROM subject').fetchall()
    if request.method == "POST":
        name = request.form['name'].strip()
        subject_id = request.form['subject_id']
        conn.execute('INSERT INTO student (name, subject_id) VALUES (?, ?)', (name, subject_id))
        conn.commit()
        conn.close()
        flash(f"Student '{name}' added successfully!")
        return redirect(url_for('home'))  # Fixed: home not home.html
    conn.close()
    return render_template("add_student.html", subject=subject)

if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=5004)



import sqlite3


from flask import Flask, render_template, request, redirect, flash, url_for

app = Flask(__name__, template_folder='day_relationships_templates')
app.secret_key = 'demo_secret_key'

def get_db():
    conn = sqlite3.connect('day_relationships.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS subject (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    ''')
    
    # Table name changed: student -> students
    conn.execute('''
        CREATE TABLE IF NOT EXISTS student (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            subject_id INTEGER,
            FOREIGN KEY (subject_id) REFERENCES subject(id)
        )
    ''')
    conn.commit()
    conn.close()
    
@app.route("/home")
def home():
    conn = get_db()
    
    # Ab sagla 'students' aahe
    students_raw = conn.execute('SELECT * FROM student').fetchall()
    
    students_joined = conn.execute('''
        SELECT student.name AS student_name,
               subject.name AS subject_name    
        FROM student
        JOIN subject ON student.subject_id = subject.id
    ''').fetchall()
    
    conn.close()
    return render_template("hom.html", students_raw=students_raw, students_joined=students_joined)

@app.route("/add_subject", methods=["GET", "POST"])
def add_subject():
    if request.method == "POST":
        name = request.form['name'].strip()
        conn = get_db()
        conn.execute('INSERT INTO subject (name) VALUES (?)', (name,))
        conn.commit()
        conn.close()
        flash(f"Subject '{name}' added successfully!")
        return redirect(url_for('home'))
    return render_template("add_subject.html")

@app.route("/add_student", methods=["GET", "POST"])
def add_student():
    conn= get_db()
    subject = conn.execute('SELECT * FROM subject').fetchall()
    if request.method == "POST":
        name = request.form['name'].strip()
        subject_id = request.form['subject_id']
        conn.execute('INSERT INTO student (name, subject_id) VALUES (?, ?)', (name, subject_id))
        conn.commit()
        conn.close()
        flash(f"Student '{name}' added successfully!")
        return redirect(url_for('home.html'))
    conn.close()
    return render_template("add_student.html", subject=subject)

if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=5004)