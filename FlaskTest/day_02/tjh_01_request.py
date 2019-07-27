from flask import Flask, request
from werkzeug.routing import BaseConverter


class MobileConverter(BaseConverter):
    regex = r"1[3-9]\d{9}"


app = Flask(__name__)
app.url_map.converters['mobile'] = MobileConverter


@app.route('/')
def index():
    return 'hello'


@app.route('/user/<string:user_id>')
def user(user_id):
    print(type(user_id))
    return 'hello:{}'.format(user_id)


@app.route('/mobile/<mobile:phone>')
def mobile(phone):
    return 'mobile:{}'.format(phone)


@app.route('/username')
def user_id():
    username = request.args.get('username')
    method = request.method
    return 'username:{}'.format(username) + '\n' + 'method:{}'.format(method)


@app.route('/image', methods=['POST'])
def download_img():
    img = request.files.get('pic')
    # print(img)
    # 文件对象
    with open('1.png', 'wb')as w:
        w.write(img.read())
    return 'Upload successful!'


@app.route('/test', methods=['POST'])
def test():
    return 'username:{}'.format(request.form.get('username'))


if __name__ == '__main__':
    app.run(debug=True)
