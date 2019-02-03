from app import app
from app.auth import auth
from app.index import index
from app.user import user
from app.register import register
from app.safe import safe
from app.api import api
#from app.error import *

app.config['SERVER_NAME'] = 'mahouo.com'

#index(域名主页和账户异常页面)首页
app.register_blueprint(index, subdomain='account')

#register注册
app.register_blueprint(register, subdomain='account', url_prefix='/register')

#auth(sgin-in,sso-rload)登陆认证和sso回调
app.register_blueprint(auth, subdomain='account', url_prefix='/sign-in')

#user(user,upload-head,profile,security,account-activity)用户中心
app.register_blueprint(user, subdomain='account', url_prefix='/user')

#api
app.register_blueprint(api, subdomain='account', url_prefix='/api')

#账户安全修改页面(更换密码,更换手机号,更换密保)
app.register_blueprint(safe, subdomain='account', url_prefix='/safe')