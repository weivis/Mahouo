from app import app
from app.api import api
from app.index import index
from app.mobile import mobile

from flask_login import current_user, login_required, login_user
from app.account_auth import Userdata
from app import login_manager
from app.error import *

app.config['SERVER_NAME'] = 'mahouo.com'
app.register_blueprint(index, subdomain='www') #index
app.register_blueprint(api, subdomain='www', url_prefix='/api')
app.register_blueprint(mobile, subdomain='m')

@login_manager.user_loader
def load_user(user_id):  
    return Userdata.query.get(int(user_id))

'''
@login_manager.user_loader
def load_user(id):
    user = User.query.filter_by(id=id).first()
    return user

@index.route('/')
def index():
    #表示存活期为浏览器进程的存活期
    session.permanent = False
    ticket = request.args.get('ticket', None)
    if ticket is not None:
        session['user_email'] = ticket.strip()
    #检测登录态
    if 'username' in session:
        return redirect(url_for("index.index"))
    return "未登录"

'''