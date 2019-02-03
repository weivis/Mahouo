__author__ = 'Ran'

from flask import Blueprint
citygps = Blueprint('citygps', __name__, template_folder='../templates',static_folder='../static')
from ..citygps import views