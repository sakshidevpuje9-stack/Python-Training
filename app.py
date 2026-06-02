from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Coaching Class Manager</h1>"

@app.route('/about')
def about():
    return "</h1><p>This is Student Management System for Coaching Class</p>"

@app.route('/students')
def students():
    return "</h1><p>All students will be displayed here</p></h1>"

if __name__ == '__main__':
    app.run(debug=True)