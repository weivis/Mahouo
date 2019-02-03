from app import app
from app.index import index
from app.api import api
import hashlib
import base64
from datetime import timedelta
from flask import render_template, session, request, redirect, url_for
from flask_login import current_user, login_required, login_user
from app.account_auth import Userdata
import urllib
from app import login_manager

app.config['SERVER_NAME'] = 'mahouo.com'
app.register_blueprint(index, subdomain='weather')  # search-index
app.register_blueprint(api, subdomain='weather', url_prefix='/api') #user

@login_manager.user_loader
def load_user(user_id):  
    return Userdata.query.get(int(user_id))