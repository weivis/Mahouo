__author__ = 'Ran'

from flask import Flask  # flask
from flask_cors import *
from flask_sqlalchemy import SQLAlchemy  # sql
from flask_login import LoginManager
from flask_cache import Cache
from app import config  # config


#实例化app
app = Flask(__name__)

CORS(app, supports_credentials=True)

#引入全局配置
app.config.from_object(config)

#跨域密匙
app.secret_key = '\x12my\x0bVO\xeb\xf8\x18\x15\xc5_?\x91\xd7h\x06AC'

#回调
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'
login_manager.init_app(app=app)

#绑定对象
db = SQLAlchemy(app)
cache = Cache(app,config={'CACHE_TYPE': 'simple'})
cache.init_app(app)