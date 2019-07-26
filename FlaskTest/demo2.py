from flask import Flask


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


# register route
@app.route('/')
def hello_world():
    print(app.config.get('SECRET_KEY'))
    print(app.config.get('DEBUG'))
    return 'hello world'


# if __name__ == '__main__':
    # run
    # app.run()
    # app.run(host='0.0.0.0', port=5001, debug=True)
