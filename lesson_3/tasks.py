from flask import Flask, render_template
from random import choice, randint

from sqlalchemy import select

from my_models import db, Students, Faculty, Books, Authors

QTY = 5
ID_DATA = [i for i in range(1, QTY + 1)]
FIRST_YEAR = 1800
LAST_YEAR = 2022
QTY_BOOKS = [i for i in range(QTY**3)]

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.cli.command("db-init")
def init_db():
    db.create_all()
    print('OK')


"""
Создать базу данных для хранения информации о студентах университета.
База данных должна содержать две таблицы: "Студенты" и "Факультеты".
В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, возраст, пол, группа и id факультета.
В таблице "Факультеты" должны быть следующие поля: id и название факультета.
Необходимо создать связь между таблицами "Студенты" и "Факультеты".
Написать функцию-обработчик, которая будет выводить список всех студентов с указанием их факультета.
"""


@app.cli.command('db-add-students')
def add_test_data():

    for i in range(1, QTY + 1):
        faculty = Faculty(name=f'faculty{i}')
        db.session.add(faculty)
    db.session.commit()
    print('faculty_ok')

    for i in range(1, (QTY + 1)**2):
        student = Students(first_name=f'name{i}', last_name=f'surname{i}', age=20, gender='m' if not i % 2 else 'w',
                           group=2, faculty_id=choice(ID_DATA))
        db.session.add(student)
    db.session.commit()
    print('students_ok')


"""
Создать базу данных для хранения информации о книгах в библиотеке.  База данных должна содержать две таблицы: "Книги" 
и "Авторы". В таблице "Книги" должны быть следующие поля: id, название, год издания, количество экземпляров и id 
автора. В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.  Необходимо создать связь между таблицами 
"Книги" и "Авторы".  Написать функцию-обработчик, которая будет выводить список всех книг с указанием их авторов.
"""


@app.cli.command('db-add-books')
def add_test_data():
    for i in range(1, QTY + 1):
        author = Authors(first_name=f'name_{i}', last_name=f'surname_{i}')
        db.session.add(author)
    db.session.commit()
    print('authors_ok')

    for i in range(1, (QTY + 1)**2):
        book = Books(name=f'title_{i}', publishing_year=randint(FIRST_YEAR, LAST_YEAR), qty=choice(QTY_BOOKS),
                     author_id=choice(ID_DATA))
        db.session.add(book)
    db.session.commit()
    print('books_ok')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/students/')
def get_students():
    students = Students.query.all()
    context = {'students': students}
    return render_template('students.html', **context)


@app.route('/books/')
def get_books():
    books = Books.query.all()
    context = {'books': books}
    return render_template('books.html', **context)


if __name__ == '__main__':
    app.run()
