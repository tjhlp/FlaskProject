from flask import Flask
from day_01.blueprints import user


class MyConfig(object):
    SECRET_KEY = 'PYTHON 27'


class Development(MyConfig):
    DEBUG = True


class Production(MyConfig):
    DEBUG = False


def create_app():
    # register app
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')
    return app


app = create_app()
app.register_blueprint(user)

# register route
@app.route('/', methods=['get','post'])
def hello_world():
    print(app.config.get('SECRET_KEY'))
    print(app.config.get('DEBUG'))
    return 'hello world'


if __name__ == '__main__':
    # search url
    url = {rule.endpoint: rule.rule for rule in app.url_map.iter_rules()}
    print(app.url_map)
    print(url)
    # run
    app.run()
