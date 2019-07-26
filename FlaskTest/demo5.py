from flask import Flask
from users import *


class MyConfig(object):
    SECRET_KEY = 'PYTHON 27'


class Development(MyConfig):
    DEBUG = True


class Production(MyConfig):
    DEBUG = False


def create_app():
    # register app
    app = Flask(__name__)
    # app.config.from_pyfile('settings.py')
    return app


app = create_app()
app.register_blueprint(user_bp)


# register route
@app.route('/', methods=['get', 'post'])
def hello_world():
    return 'hello world'


if __name__ == '__main__':
    print({rule.endpoint: rule.rule for rule in app.url_map.iter_rules()})
    # run
    app.run()
