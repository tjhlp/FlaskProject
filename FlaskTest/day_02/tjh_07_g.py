from flask import Flask, g, abort

app = Flask(__name__)


def login_required(func):
    def inner(*args, **kwargs):
        if g.username is not None:
            return func(*args, **kwargs)
        abort(401)

    return inner


@app.before_request
def add_username():
    g.username = 'tjh'


@app.route('/')
def index():
    return 'Hello'


@app.route('/user')
@login_required
def username():
    get_username = g.username
    return 'username:{}'.format(get_username)


@app.route('/login')
def login():
    g.username = 'tjh'
    return '登陆：{}'.format(g.username)


@app.route('/logout')
def logout():
    g.username = None
    return '登出'


if __name__ == '__main__':
    app.run(debug=True)
