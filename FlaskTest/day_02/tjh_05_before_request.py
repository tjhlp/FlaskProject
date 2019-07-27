from flask import Flask

app = Flask(__name__)


@app.before_first_request
def before_first():
    print('1')


@app.before_request
def before_request():
    print('2')


@app.after_request
def after_request(response):
    print('3')
    return response


@app.teardown_request
def teardown(response):
    print('4')


@app.route('/')
def index():
    return 'Hello'


if __name__ == '__main__':
    app.run(debug=True)
