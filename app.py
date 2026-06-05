

from pprint import pp

from flask import Flask, render_template

app = Flask(__name__)

Student_data = [
                 {"name": "Sakshi", "score": 80,"Attempt": 1,"Status": "Pass"},
                 {"name": "Arti", "score": 90,"Attempt": 2,"Status": "Pass"},
                {"name": "Satyarth", "score": 70,"Attempt": 1,"Status": "Pass"},
                {"name": "Shivam", "score": 60,"Attempt": 3,"Status": "Pass"},
                 
]

@app.route('/')
def Home():
    return render_template('Home.html')

@app.route('/About')
def About():
    return render_template('About.html')

@app.route('/Students')
def Students():
    return render_template('Stud.html', students=Student_data)

if __name__ == '__main__':
    app.run(debug=True)

