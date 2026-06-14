
from flask import Flask, render_template

app = Flask(__name__)

# Home Page - class.html
@app.route('/')
def home():
    return render_template('my_project/class.html')

# Students Dashboard - students.html
@app.route('/students')
def students():
    data = {
        'total_students': 120,
        'attendance_percent': 95,
        'fees_status': 'Pending'
    }
    return render_template('my_project/students.html')

# Records Table - records.html
@app.route('/records')
def records():
    students_data = [
        {'no': 1, 'name': 'Rahul', 'course': 'Python', 'attendance': 90, 'fees': 'Paid'},
        {'no': 2, 'name': 'Priya', 'course': 'Java', 'attendance': 85, 'fees': 'Pending'},
        {'no': 3, 'name': 'Amit', 'course': 'Web Design', 'attendance': 95, 'fees': 'Paid'},
        {'no': 4, 'name': 'Sneha', 'course': 'C Programming', 'attendance': 88, 'fees': 'Paid'}
    ]
    return render_template('my_project/records.html', students=students_data)



if __name__ == '__main__':
    app.run(debug=True)

    
