from flask import Flask, render_template, request, redirect, url_for, make_response

"""
Создать страницу, на которой будет форма для ввода имени и электронной почты, при отправке которой будет создан 
cookie-файл с данными пользователя, а также будет произведено перенаправление на страницу приветствия, 
где будет отображаться имя пользователя.

На странице приветствия должна быть кнопка «Выйти», при нажатии на которую будет удалён cookie-файл с данными 
пользователя и произведено перенаправление на страницу ввода имени и электронной почты. 
"""


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)


@app.route('/signin/',  methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        name, email = request.form.get('name'), request.form.get('email')
        uid = hash(name + email)  # использую самую простую хэш функцию для примера
        response = make_response(render_template('hello.html', name=name))
        response.set_cookie('user', f'{uid}')
        return response
    return render_template('signin.html')


@app.route('/signout/')
def signout():
    response = make_response(render_template('signin.html'))
    response.delete_cookie('user')
    return response


if __name__ == '__main__':
    app.run()
