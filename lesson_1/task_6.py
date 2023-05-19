from flask import Flask, render_template

_students = [
    {"name": "Иван", "sname": "Иванов", "age": 20, "avg_score": 5},
    {"name": "Петр", "sname": "Петров", "age": 21, "avg_score": 4},
    {"name": "Сидор", "sname": "Сидоров", "age": 22, "avg_score": 3},
]


app = Flask(__name__)


@app.route('/students/')
def students():
    return render_template('students.html', students=_students)


if __name__ == "__main__":
    app.run()