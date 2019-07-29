from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)


@api.resource('/')
class HelloWorldResource(Resource):
    def get(self):
        return 'get response'

    def post(self):
        return 'post response'


if __name__ == '__main__':
    app.run()
