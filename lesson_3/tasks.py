from flask import Flask, render_template, request, redirect, url_for
from random import choice, randint
from my_models import db, Students, Faculty, Books, Authors, Users
from flask_wtf.csrf import CSRFProtect
from forms import SignupForm

QTY = 5
ID_DATA = [i for i in range(1, QTY + 1)]
FIRST_YEAR = 1800
LAST_YEAR = 2022
QTY_BOOKS = [i for i in range(QTY**3)]

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
csrf = CSRFProtect(app)

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


"""
Создать форму регистрации для пользователя.  Форма должна содержать поля: имя, электронная почта, пароль (с
подтверждением), дата рождения, согласие на обработку персональных данных.  Валидация должна проверять, что все поля
заполнены корректно (например, дата рождения должна быть в формате дд.мм.гггг).  При успешной регистрации
пользователь должен быть перенаправлен на страницу подтверждения регистрации
"""


@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)


@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if request.method == 'POST' and form.validate():

        user = Users(name=form.name.data, email=form.email.data, password=hash(form.password.data),
                     birth_date=form.birth_date.data)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('hello', name=form.name.data))
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run()
