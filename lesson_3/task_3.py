from flask import Flask, render_template, request, url_for, redirect
from flask_wtf.csrf import CSRFProtect
from forms import SignupForm

"""
Создать форму регистрации для пользователя.  Форма должна содержать поля: имя, электронная почта, пароль (с
подтверждением), дата рождения, согласие на обработку персональных данных.  Валидация должна проверять, что все поля
заполнены корректно (например, дата рождения должна быть в формате дд.мм.гггг).  При успешной регистрации
пользователь должен быть перенаправлен на страницу подтверждения регистрации
"""

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
csrf = CSRFProtect(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)


@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        return redirect(url_for('hello', name=name))
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run()
