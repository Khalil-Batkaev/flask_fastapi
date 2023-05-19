from flask import Flask

app = Flask(__name__)


@app.route("/string/<line>")
def string(line):
    return f'{len(line)}'


html_templ = """
<h1>Моя первая HTML страница</h1>
<p>Привет, мир!</p>
"""


@app.route("/html/")
def return_html():
    return html_templ


if __name__ == '__main__':
    app.run()
