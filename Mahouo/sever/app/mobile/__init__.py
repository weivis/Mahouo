__author__ = 'Ran'

from flask import Blueprint
mobile = Blueprint('mobile', __name__, template_folder='../templates',static_folder='../static')
from ..mobile import views