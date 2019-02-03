__author__ = 'Ran'
from app import Flask #cache
from ..index import index
import hashlib
from flask import render_template
from datetime import datetime
from flask_login import current_user

#欢迎
@index.route('/')
#@cache.cached(timeout=3600, key_prefix='index-home')  #缓存
def i():
    return render_template('index/index.html', title='', page='index')

#提交页面
@index.route('/submit')
#@cache.cached(timeout=3600, key_prefix='index-home')  #缓存
def submit_ui():
    return render_template('index/submit.html', title='提交域名给我们/收录', page='submit')