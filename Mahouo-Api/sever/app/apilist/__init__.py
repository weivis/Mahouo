__author__ = 'Ran'

from flask import Blueprint
apilist = Blueprint('apilist', __name__, template_folder='../templates',static_folder='../static')
from ..apilist import views