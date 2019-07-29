from flask import Flask
from flask_restful import Resource, Api


def decoration_1(func):
    print('decoration_1')

    def inner(*args, **kwargs):
        print('decoration1')
        return func(*args, **kwargs)

    return inner


def decoration_2(func):
    print('decoration_2')

    def inner(*args, **kwargs):
        print('decoration2')
        return func(*args, **kwargs)

    return inner


app = Flask(__name__)

api = Api(app)


@api.resource('/')
class index(Resource):
    # method_decorators = [decoration_1, decoration_2]
    method_decorators = {
        'get': [decoration_1, decoration_2],
        'post': [decoration_1]
    }

    def get(self):
        return 'hello get'

    def post(self):
        return 'hello post'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
