from flask import Flask, render_template

_news = [
    {
        'title': 'Главная',
        'description': 'Всё самое важное',
        'date': '2023-05-12'
    },
    {
        'title': 'Вторая',
        'description': 'Всё самое важное и ещё немного',
        'date': '2023-05-11'
    },
    {
        'title': 'Последняя',
        'description': 'Всё самое важное всё',
        'date': '2023-05-13'
    }
]


app = Flask(__name__)


@app.route('/news/')
def news():
    return render_template('news.html', news=_news)


if __name__ == "__main__":
    app.run()
