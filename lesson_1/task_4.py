from flask import Flask

app = Flask(__name__)


@app.route("/numbers/<nums>")
def numbers(nums):
    num_1, num_2 = map(int, nums.split('_'))
    return f'{num_1 + num_2}'


if __name__ == '__main__':
    app.run()