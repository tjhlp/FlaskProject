from flask import Blueprint


user_bp = Blueprint('users', __name__)

from .views import *
