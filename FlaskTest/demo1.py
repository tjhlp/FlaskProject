from flask import Flask

# register app
app = Flask(__name__)


class MyConfig(object):
    SECRET_KEY = 'PYTHON 27'


class Development(MyConfig):
    DEBUG = True


class Production(MyConfig):
    DEBUG = False


# three methods of configuration
# app.config.from_object(Development)
app.config.from_pyfile('settings.py')


# app.config.from_envvar('PROJECT', silent=True)

# register route
@app.route('/')
def hello_world():
    print(app.config.get('SECRET_KEY'))
    print(app.config.get('DEBUG'))
    return 'hello world'


if __name__ == '__main__':
    # run
    app.run()
