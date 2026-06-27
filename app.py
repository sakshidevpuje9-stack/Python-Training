


from flask import Flask, render_template, request, redirect, url_for,flash,session
from werkzeug.security import check_password_hash,generate_password_hash

import sqlite3


app = Flask(__name__)
app.secret_key = "my secret key 123"

def get_db():
    conn = sqlite3.connect("student.db")
    conn.row_factory = sqlite3.Row
    return conn


# Home Page
@app.route('/')
def home():
    return render_template('home.html')


# About Page
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    students = []
    searched = False

    if request.method == 'POST':
        searched = True
        value = request.form['search']

        conn = get_db()

        students = conn.execute(
            """
            SELECT * FROM students
            WHERE CAST(Rollno AS TEXT) LIKE ?
               OR Name LIKE ?
            """,
            ('%' + value + '%', '%' + value + '%')
        ).fetchall()

        conn.close()

    return render_template(
        'search.html',
        students=students,
        searched=searched
    )

@app.route('/filter', methods=['GET', 'POST'])
def filter_students():
    students = []

    if request.method == 'POST':
        marks = request.form['marks']

        conn = get_db()
        students = conn.execute(
            "SELECT * FROM students WHERE Marks >= ?",
            (marks,)
        ).fetchall()
        conn.close()

    return render_template('filter.html', students=students)


# Add Student
@app.route('/add_student', methods=['GET', 'POST'])
def add_student():

    if 'username' not in session:
      flash("please login first",Warning)
      return redirect(url_for('login'))

    if request.method == 'POST':
        Rollno = request.form['Rollno']
        Name = request.form['Name']
        Subject = request.form['Subject']
        Marks = request.form['Marks']
        Grade = request.form['Grade']

        conn = get_db()
        conn.execute(
            "INSERT INTO students (Rollno, Name, Subject, Marks, Grade) VALUES (?, ?, ?, ?, ?)",
            (Rollno, Name, Subject, Marks, Grade)
        )
        conn.commit()
        conn.close()

        return redirect(url_for('students'))
        
        return render_template('add_student.html')


# View Students
@app.route('/students')
def students():
    conn = get_db()
    students = conn.execute(
        "SELECT * FROM students"
    ).fetchall()
    conn.close()

    return render_template('students.html', students=students)


# Edit Student
@app.route('/edit/<int:Rollno>', methods=['GET', 'POST'])
def edit_student(Rollno):

    conn = get_db()

    if request.method == 'POST':
        Name = request.form['Name']
        Subject = request.form['Subject']
        Marks = request.form['Marks']
        Grade = request.form['Grade']

        conn.execute("""
            UPDATE students
            SET Name=?, Subject=?, Marks=?, Grade=?
            WHERE Rollno=?
        """, (Name, Subject, Marks, Grade, Rollno))

        conn.commit()
        conn.close()

        return redirect(url_for('students'))

    student = conn.execute(
        "SELECT * FROM students WHERE Rollno=?",
        (Rollno,)
    ).fetchone()

    conn.close()

    return render_template(
        'edit_student.html',
        student=student
    )


# Delete Student
@app.route('/delete/<int:Rollno>')
def delete_student(Rollno):

    conn = get_db()
    conn.execute(
        "DELETE FROM students WHERE Rollno=?",
        (Rollno,)
    )
    conn.commit()
    conn.close()

    return redirect(url_for('students'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password']

        conn = sqlite3.connect('myproject.db')
        cur = conn.cursor()

        cur.execute("SELECT * FROM users WHERE username=?", (username,))
        user = cur.fetchone()

        if user:
            conn.close()
            return "Username already exists"

        cur.execute(
            "INSERT INTO users(username, password) VALUES (?, ?)",
            (username, password)
        )

        conn.commit()
        conn.close()

        return "Registration Successful"

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password']

        conn = sqlite3.connect('student.db')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        
        cur.execute(
            "SELECT * FROM users WHERE username=?",
            (username,)
        )
        user = cur.fetchone()

        conn.close()

        if user and user['password'] == password:
            session['username'] = username
            session ['role'] = user['role']
            flash(f'Welcome {username}!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'danger')

            session ['username'] = username

            #return "login successful"

    return render_template('login.html')
    

from flask import session, redirect, url_for

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('role',None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
