from flask import Flask, render_template, request, escape
from pathlib import PurePath, Path
from werkzeug.utils import secure_filename


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello/')
def hello():
    name = 'Bob'
    return f"Hello {name}"


@app.get('/upload/')
def image_get():
    return render_template('upload.html')


@app.post('/upload/')
def image_post():
    file = request.files.get('file')
    file_name = secure_filename(file.filename)
    file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
    return f"Файл {file_name} загружен на сервер"


@app.route('/login',  methods=['GET', 'POST'])
def login():
    DATA = {
        'name': 'Ivan',
        'password': 'qwerty'
    }

    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        
        if name == DATA.get('name') and password == DATA.get('password'):
            return render_template('index.html')
        return render_template('404.html')

    return render_template('login.html')


@app.route('/text/', methods=['GET', 'POST'])
def text():
    if request.method == 'POST':
        data = escape(request.form.get('data'))
        return f'Длина строки: {len(data.split())}'
    return render_template('text.html')


@app.route('/num/', methods=['GET', 'POST'])
def num():
    if request.method == 'POST':
        num_1 = int(escape(request.form.get('num_1')))
        num_2 = int(escape(request.form.get('num_2')))
        operation = escape(request.form.get('operation'))

        if operation == '+':
            return f'Результат вычислений: {num_1 + num_2}'
        if operation == '-':
            return f'Результат вычислений: {num_1 - num_2}'
        if operation == '*':
            return f'Результат вычислений: {num_1 * num_2}'
        if operation == '/':
            return f'Результат вычислений: {num_1 / num_2}'
    return render_template('num.html')


if __name__ == '__main__':
    app.run()