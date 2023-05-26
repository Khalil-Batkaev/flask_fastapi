from flask import Flask, render_template
from random import choice
from my_models import Students, Faculty, db

"""
Создать базу данных для хранения информации о студентах университета.
База данных должна содержать две таблицы: "Студенты" и "Факультеты".
В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, возраст, пол, группа и id факультета.
В таблице "Факультеты" должны быть следующие поля: id и название факультета.
Необходимо создать связь между таблицами "Студенты" и "Факультеты".
Написать функцию-обработчик, которая будет выводить список всех студентов с указанием их факультета.
"""

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.cli.command("db-init")
def init_db():
    db.create_all()
    print('OK')


@app.cli.command('db-add-data')
def add_test_data():
    qty = 5

    for i in range(1, qty + 1):
        faculty = Faculty(name=f'faculty{i}')
        db.session.add(faculty)
    db.session.commit()
    print('faculty_ok')

    for i in range(1, (qty + 1)**2):
        student = Students(first_name=f'name{i}', last_name=f'surname{i}', age=20, gender='m' if not i % 2 else 'w',
                           group=2, faculty_id=choice([1, 2, 3, 4, 5]))
        db.session.add(student)
    db.session.commit()
    print('students_ok')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/students/')
def get_students():
    students = Students.query.all()
    context = {'students': students}
    return render_template('students.html', **context)


if __name__ == '__main__':
    app.run()
