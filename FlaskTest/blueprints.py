from flask import Blueprint

# register blueprint
user = Blueprint('users', __name__)


# register route
@user.route('/users')
def get_username():
    return 'xiaoming'
