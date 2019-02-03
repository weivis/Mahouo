__author__ = 'Ran'

from flask import Blueprint
safe = Blueprint('safe', __name__, template_folder='../templates', static_folder='../static')
from ..safe import views