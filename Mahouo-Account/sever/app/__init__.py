__author__ = 'Ran'

from flask import Flask  # flask
from flask_cache import Cache  # cache
from flask_login import LoginManager
from flask_cors import *
from flask_sqlalchemy import SQLAlchemy  # sql
from datetime import timedelta

from app import config  # config
#实例化app
app = Flask(__name__,
        template_folder='templates', #指定模板路径，可以是相对路径，也可以是绝对路径。 
        static_folder='static',  #指定静态文件前缀，默认静态文件路径同前缀
         )

#引入全局配置
app.config.from_object(config)
app.permanent_session_lifetime = timedelta(days=7)

#跨域密匙
app.secret_key = '\x12my\x0bVO\xeb\xf8\x18\x15\xc5_?\x91\xd7h\x06AC'

#配置flasklogin
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.account_login'
login_manager.init_app(app=app)

#绑定对象
db = SQLAlchemy(app)

cache = Cache(app)
cache.init_app(app)