import re

from flask import Flask
from flask_restful.reqparse import RequestParser
from flask_restful import Resource, Api, inputs

app = Flask(__name__)
api = Api(app)
parse = RequestParser()


def re_mobile(value):
    if re.match('1[3-9]\d{9}', value):
        return value
    else:
        raise ValueError('Valid mobile')


@api.resource('/')
class Index(Resource):
    def get(self):
        parse.add_argument('name', required=True, help='missing name')
        parse.add_argument('like', action='append')
        parse.add_argument('height', type=inputs.int_range(180, 230))
        parse.add_argument('mobile', type=re_mobile)

        parse.add_argument('json_str', required=True, location='json')

        name = parse.parse_args().get('name')
        like = parse.parse_args().get('like')
        height = parse.parse_args().get('height')
        mobile = parse.parse_args().get('mobile')

        json_str = parse.parse_args().get('json_str')
        return 'name:{} like:{} height:{} mobile:{} json_str:{}'.format(name, like, height, mobile, json_str)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
