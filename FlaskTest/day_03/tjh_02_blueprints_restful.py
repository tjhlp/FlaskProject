from flask import Flask, Blueprint
from flask_restful import Resource, Api

app = Flask(__name__)

blue_print = Blueprint('user', __name__)
blue_api = Api(blue_print)


@blue_api.resource('/')
class Index(Resource):
    def get(self):
        return 'Hello'


app.register_blueprint(blue_print)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
