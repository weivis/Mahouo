from app import app
from app.index import index
from app.api import api

from flask_login import current_user, login_required, login_user
from app.account_auth import Userdata
from app import login_manager
#from app.error import *

app.config['SERVER_NAME'] = 'mahouo.com'
app.register_blueprint(index, subdomain='analytics')
app.register_blueprint(api, subdomain='analytics', url_prefix='/api')

@login_manager.user_loader
def load_user(user_id):  
    return Userdata.query.get(int(user_id))