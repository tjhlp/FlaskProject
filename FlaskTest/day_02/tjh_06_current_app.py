from flask import Flask, current_app

app1 = Flask(__name__)
app2 = Flask(__name__)
app1.redis_cli = 'app1_redis'
app2.redis_cli = 'app2_redis'


@app1.route('/')
def index():
    return 'Hello: {}'.format(current_app.redis_cli)


@app2.route('/')
def index():
    return 'Hello: {}'.format(current_app.redis_cli)


if __name__ == '__main__':
    app1.run(debug=True, port=5001)
    app2.run(debug=True, port=5002)
