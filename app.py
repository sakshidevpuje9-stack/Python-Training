
from flask import Flask, render_template, request,flash,url_for


app = Flask(__name__)
import sqlite3
def get_db():
    conn=sqlite3.connect('student.db')
    conn.row_factory=sqlite3.Row
    return conn
    

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/stud')
def stud():
 return render_template('stud.html', )


@app.route('/add_student')
def add_student():
    return render_template('add_student.html')

@app.route('/insert', methods=["GET","POST"])
def insert():
    if request.method == "POST":

     Rollno = request.form['Rollno']
    name = request.form['Name']
    marks = request.form['Marks']
    performance = request.form['Performance']
    progress = request.form['Progress']

    conn = sqlite3.connect("student.db")
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO stud
    (Rollno, Name, Marks, Performance, Progress)
    VALUES (?, ?, ?, ?, ?)
    """, (Rollno, name, marks, performance, progress))

    conn.commit()
    conn.close()

    return "Student Added Successfully"



if __name__ == '__main__':
    app.run(debug=True)

