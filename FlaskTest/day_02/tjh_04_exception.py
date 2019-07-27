from flask import Flask, abort, redirect

app = Flask(__name__)


@app.route('/')
def index():
    abort(401)
    return 'Hello'


@app.errorhandler(404)
def error(e):

    return redirect('https://www.baidu.com')


if __name__ == '__main__':
    app.run(debug=True)

