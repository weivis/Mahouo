__author__ = 'Ran'

from flask import Blueprint
api = Blueprint('api', __name__, template_folder='../templates', static_folder='../static')
from ..api import views