from flask import Flask, request, make_response, session

app = Flask(__name__)
app.secret_key = '1234567'

@app.route('/')
def hello_world():
    return 'index'


@app.route('/user')
def get_user():
    username = request.cookies.get('username')
    response_str = '现在没有用户登陆'
    if username:
        response_str = '查询现在的用户: {}    '.format(username) + session.get('password')
    response = make_response(response_str)
    return response


@app.route('/login')
def login():
    response = make_response('登陆')
    response.set_cookie('username', 'jack')
    session['password'] = '123456'
    return response


@app.route('/logout')
def logout():
    response = make_response('退出登陆')
    response.delete_cookie('username')
    session.pop('password')
    return response


if __name__ == '__main__':
    app.run(debug=True)
