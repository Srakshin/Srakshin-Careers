from flask import Flask, render_template,jsonify

app = Flask(__name__)
Jobs = [
    {
      'Id':1,
      'Title':'Frontend Engineering',
      'Location':'Hyderabad',
      'Salary': 100000
    },
    {
      'Id':2,
      'Title':'Backend Engineering',
      'Location':'Maharastra',
      'Salary': 200000
    },
    {
      'Id':3,
      'Title':'Editor',
      'Location':'Gachibowli',
      'Salary': 300000
    }
]

@app.route("/")
def hello_world():
    return render_template('Home.html',jobs=Jobs)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(Jobs)

if __name__ == "__main__":
    app.run(debug=True)

