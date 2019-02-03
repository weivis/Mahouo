from flask import Flask

SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost:3307/account?charset=utf8'
SQLALCHEMY_BINDS = {
    'mahouo_api':        'mysql://root:@localhost:3307/mahouo_api?charset=utf8',
}
DEBUG = True