from app import app, Flask
from flask import session, redirect
from app.index import index
from app.api import api
from flask_login import current_user, login_required, login_user
from app.account_auth import Userdata
from app import login_manager

@login_manager.user_loader
def load_user(user_id):
    return Userdata.query.get(int(user_id))

app.config['SERVER_NAME'] = 'mahouo.com'
app.register_blueprint(index, subdomain='miao') #index
app.register_blueprint(api, subdomain='miao', url_prefix='/index-api')