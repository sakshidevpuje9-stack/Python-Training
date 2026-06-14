
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/welcome')
def home():
    return render_template('my_project/welcome.html')

@app.route('/login')
def login():
    return render_template('my_project/index.html')

@app.route('/stu')
def stu():
    return render_template('my_project/stu.html')

@app.route('/rec')
def rec():
    return render_template('my_project/rec.html')

if __name__ == '__main__':
    app.run(debug=True)

    