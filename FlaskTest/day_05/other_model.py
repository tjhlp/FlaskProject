from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class MyConfig(object):
    # mysql数据库配置

    # mysql数据库的连接信息
    # SQLALCHEMY_DATABASE_URI = "mysql://数据库的账号:密码@ip地址:端口/数据库名称"
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@192.168.146.135:3306/toutiao"

    # 能将orm转换出来的sql语句输出
    SQLALCHEMY_ECHO = True

    # 关闭数据库修改跟踪操作
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app = Flask(__name__)

app.config.from_object(MyConfig)

db = SQLAlchemy(app)


class User(db.Model):
    """
    用户基本信息
    """
    __tablename__ = 'user_basic'

    class STATUS:
        ENABLE = 1
        DISABLE = 0

    id = db.Column('user_id', db.Integer, primary_key=True, doc='用户ID')
    mobile = db.Column(db.String, doc='手机号')
    password = db.Column(db.String, doc='密码')
    name = db.Column('user_name', db.String, doc='昵称')
    profile_photo = db.Column(db.String, doc='头像')
    last_login = db.Column(db.DateTime, doc='最后登录时间')
    is_media = db.Column(db.Boolean, default=False, doc='是否是自媒体')
    is_verified = db.Column(db.Boolean, default=False, doc='是否实名认证')
    introduction = db.Column(db.String, doc='简介')
    certificate = db.Column(db.String, doc='认证')
    article_count = db.Column(db.Integer, default=0, doc='发帖数')
    following_count = db.Column(db.Integer, default=0, doc='关注的人数')
    fans_count = db.Column(db.Integer, default=0, doc='被关注的人数（粉丝数）')
    like_count = db.Column(db.Integer, default=0, doc='累计点赞人数')
    read_count = db.Column(db.Integer, default=0, doc='累计阅读人数')

    account = db.Column(db.String, doc='账号')
    email = db.Column(db.String, doc='邮箱')
    status = db.Column(db.Integer, default=1, doc='状态，是否可用')

    user_profile = db.relationship('UserProfile', primaryjoin='User.id==foreign(UserProfile.id)', uselist=False)

    following = db.relationship('Relation', primaryjoin='User.id==foreign(Relation.user_id)')


# 需求：当有一个User对象，根据User对象获取 UserProfile 用户资料表中的字段值

# 已知user对象查询用户资料表的性别：

# 需求：查询用户id为1，关注的每一个用户的昵称


class UserProfile(db.Model):
    """
    用户资料表
    """
    __tablename__ = 'user_profile'

    class GENDER:
        MALE = 0
        FEMALE = 1

    id = db.Column('user_id', db.Integer, primary_key=True, doc='用户ID')
    gender = db.Column(db.Integer, default=0, doc='性别')
    birthday = db.Column(db.Date, doc='生日')
    real_name = db.Column(db.String, doc='真实姓名')
    id_number = db.Column(db.String, doc='身份证号')
    id_card_front = db.Column(db.String, doc='身份证正面')
    id_card_back = db.Column(db.String, doc='身份证背面')
    id_card_handheld = db.Column(db.String, doc='手持身份证')
    ctime = db.Column('create_time', db.DateTime, default=datetime.now, doc='创建时间')
    utime = db.Column('update_time', db.DateTime, default=datetime.now, onupdate=datetime.now, doc='更新时间')
    register_media_time = db.Column(db.DateTime, doc='注册自媒体时间')

    area = db.Column(db.String, doc='地区')
    company = db.Column(db.String, doc='公司')
    career = db.Column(db.String, doc='职业')


class Relation(db.Model):
    """
    用户关系表
    """
    __tablename__ = 'user_relation'

    class RELATION:
        DELETE = 0
        FOLLOW = 1
        BLACKLIST = 2

    id = db.Column('relation_id', db.Integer, primary_key=True, doc='主键ID')
    user_id = db.Column(db.Integer, doc='用户ID')
    target_user_id = db.Column(db.Integer, doc='目标用户ID')
    relation = db.Column(db.Integer, doc='关系')
    ctime = db.Column('create_time', db.DateTime, default=datetime.now, doc='创建时间')
    utime = db.Column('update_time', db.DateTime, default=datetime.now, onupdate=datetime.now, doc='更新时间')


@app.route('/')
def index():
    try:
        user = User(mobile='15312345678', name='xiaoming')
        db.session.add(user)
        # db.session.flush()
        user_profile = UserProfile(id=user.id)
        db.session.add(user_profile)
        db.session.commit()
    except:
        db.session.rollback()

    return 'hello'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
