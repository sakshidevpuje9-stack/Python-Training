from flask import Flask

app = Flask(__name__)

Students=[
            
           {"Rollno": 1, "Name": "John", "Fees": 5000, "Attendance": 80, "Course": "Python", "Years_of_Study": 2},
           {"Rollno": 2, "Name": "Alice", "Fees": 4500, "Attendance": 70, "Course": "Java", "Years_of_Study": 1},
           {"Rollno": 3, "Name": "Bob", "Fees": 6000, "Attendance": 90, "Course": "C++", "Years_of_Study": 3},
]
    
@app.route('/')
def about():
    #create with html tags
    html ="<h1>Welcome to the Coaching Class </h1>" \
    
    for stud in Students:
        html += f'<li>{stud["Name"]}, ${stud["Fees"]}, {stud["Attendance"]}, {stud["Course"]}, {stud["Years_of_Study"]}</li>'
        html += '<tr><th>Rollno</th><th>Name</th><th>Fees</th><th>Attendance</th><th>Course</th><th>Years of Study</th></tr>'
        html += '</ul>'
    return html

@app.route('/about')
def home():
    return "<h1>Coaching Class Manager</h1>"


@app.route('/students')
def students():
    return "</h1><p>All students will be displayed here</p></h1>"

if __name__ == '__main__':
    app.run(debug=True)