__author__ = 'Ran'

from app import config
from flask import Flask, redirect
from flask_cache import Cache
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(config)
app.secret_key = '\x12my\x0bVO\xeb\xf8\x18\x15\xc5_?\x91\xd7h\x06AC'

db = SQLAlchemy(app)
cache = Cache(app)
cache.init_app(app)

CORS(app)