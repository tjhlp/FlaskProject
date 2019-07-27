from flask import Flask, redirect, jsonify, render_template
from flask import make_response

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello'


@app.route('/baidu')
def baidu():
    return redirect('https://www.baidu.com')


@app.route('/json')
def re_json():
    dict_a = {'a': 'b', 'c': 'd'}
    return jsonify(dict_a)


@app.route('/render')
def render_test():
    con_list = [1, 2, 3]
    con_str = 'tjh'
    return render_template('index.html', my_list=con_list, my_str=con_str)


@app.route('/myresponse')
def my_response():
    response = make_response('123456')
    response.status_code = 666
    response.headers['python'] = 'chuanzhi'
    return response
    # return '123456', 666, {'python': 'chuanzhi'}


if __name__ == '__main__':
    app.run(debug=True)
