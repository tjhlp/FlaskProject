from flask import Flask
from flask_restful import Resource, Api
# from flask_restful.representations import json

app = Flask(__name__)
api = Api(app)

from flask import make_response, current_app
from flask_restful.utils import PY3
from json import dumps


@api.representation('application/json')
def output_json(data, code, headers=None):
    """Makes a Flask response with a JSON encoded body"""

    settings = current_app.config.get('RESTFUL_JSON', {})

    if 'message' not in data:
        data = {
            'message': 'tjh',
            'data': data
        }

    # If we're in debug mode, and the indent is not set, we set it to a
    # reasonable value here.  Note that this won't override any existing value
    # that was set.  We also set the "sort_keys" value.
    if current_app.debug:
        settings.setdefault('indent', 4)
        settings.setdefault('sort_keys', not PY3)

    # always end the json dumps with a new line
    # see https://github.com/mitsuhiko/flask/pull/1262
    dumped = dumps(data, **settings) + "\n"

    resp = make_response(dumped, code)
    resp.headers.extend(headers or {})
    return resp


@api.resource('/')
class Index(Resource):
    def get(self):
        my_dict = {
            'username': 'xiaoming',
            'age': 12
        }
        return my_dict


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
