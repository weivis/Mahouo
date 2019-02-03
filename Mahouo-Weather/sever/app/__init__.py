__author__ = 'Ran'

from app import config
from flask_login import LoginManager
from flask import Flask, redirect
from flask_cache import Cache
from datetime import timedelta
from flask_cors import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,
        template_folder='templates', #指定模板路径，可以是相对路径，也可以是绝对路径。 
        static_folder='static',  #指定静态文件前缀，默认静态文件路径同前缀
         )

CORS(app, supports_credentials=True)
app.config.from_object(config)

app.secret_key = '\x12my\x0bVO\xeb\xf8\x18\x15\xc5_?\x91\xd7h\x06AC'
app.permanent_session_lifetime = timedelta(seconds=24 * 60 * 60)

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'
login_manager.init_app(app=app)

db = SQLAlchemy(app)

cache = Cache(app)
cache.init_app(app)