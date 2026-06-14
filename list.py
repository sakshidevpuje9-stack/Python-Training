''' write a python program to display the name marks and grade of the students using list ,function and for loop'''

from tokenize import Name


student =["maithili","ashwini","sangita","priya","sneha"]
marks =[85,90,78,92,88]

def calculate_grade(marks):

    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    else:
        grade= "F"  
    
    print("Name:",student[i])
    print("Marks:",marks)
    print("Grade:",grade)
    print("-----------------------------")

for i in range(len(student)):
    calculate_grade(marks[i])

    @app.route('/add_student')
def add_student():
    return render_template('add_student.html')

@app.route('/insert', methods=['POST'])
def insert():
    Rollno = request.form['Rollno']
    name = request.form['Name']
    marks = request.form['Marks']
    performance = request.form['Performance']
    progress = request.form['Progress']

    conn = sqlite3.connect("student.db")
    cur = conn.cursor()

    conn.execute("""
    INSERT INTO stud
    (Rollno,Name, Marks, Performance, Progress)
    VALUES (?, ?, ?, ?, ?)
    """, (Rollno,name, marks, performance, progress))


    @app.route('/stud')
def stud():
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM stud")
    data = cur.fetchall()

    conn.close()

    return render_template('stud.html', stud=data)


    

    
      
      