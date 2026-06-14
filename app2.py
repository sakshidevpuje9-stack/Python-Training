from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'sakshi123'  # Replace with a secure secret key

@app.route('/')
def home():
    return render_template('my_project1/Welcome.html')


@app.route('/studentform')
def studentform():
    return render_template('my_project1/studentForm.html')


@app.route('/about')
def about():
    return render_template('my_project1/About.html')

@app.route('/records')
def records():

    students_data = [
        {"name":"Rahul","course":"Python","attendance":90,"fees":"Paid"},
        {"name":"Priya","course":"Java","attendance":85,"fees":"Pending"},
        {"name":"Amit","course":"Web Design","attendance":95,"fees":"Paid"},
        {"name":"Sneha","course":"C Programming","attendance":88,"fees":"Paid"}
    ]
    return render_template('my_project1/records.html', students=students_data)

if __name__ == '__main__':
    app.run(debug=True)

    

    





