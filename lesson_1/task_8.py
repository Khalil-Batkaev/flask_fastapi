from flask import Flask, render_template


"""
Создать базовый шаблон для всего сайта, содержащий общие элементы дизайна (шапка, меню, подвал), и дочерние шаблоны 
для каждой отдельной страницы. Например, создать страницу "О нас" и "Контакты", используя базовый шаблон 

Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал), и дочерние 
шаблоны для страниц категорий товаров и отдельных товаров. Например, создать страницы "Одежда", "Обувь" и "Куртка", 
используя базовый шаблон.  
"""

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def index():
    context = {'title': 'Главная'}
    return render_template('index.html', **context)


@app.route('/women_goods/')
def women_goods():
    context = {'title': 'Товары для женщин'}
    return render_template('goods.html', **context)


@app.route('/men_goods/')
def men_goods():
    context = {'title': 'Товары для мужчин'}
    return render_template('goods.html', **context)


@app.route('/kids_goods/')
def kids_goods():
    context = {'title': 'Товары для детей'}
    return render_template('goods.html', **context)


@app.route('/accessories/')
def accessories():
    context = {'title': 'Аксессуары'}
    return render_template('goods.html', **context)


if __name__ == "__main__":
    app.run(debug=True)
