from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DEBUG = True

# Flask Sqlalchemy Setting
SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost:3307/mahouo_account?charset=utf8'
SQLALCHEMY_BINDS = {
    'mahouo_sso':        'mysql://root:@localhost:3307/mahouo_sso?charset=utf8',
}
SQLALCHEMY_TRACK_MODIFICATIONS = True

# Flask Bcrypt Setting
BCRYPT_LOG_ROUNDS = 1