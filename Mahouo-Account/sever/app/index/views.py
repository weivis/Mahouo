# -*- coding: utf-8 -*-

__author__ = 'Ran'

from ..index import index
from app import Flask, cache
from flask import render_template
from flask_login import current_user

#首页
@index.route('/')
#@cache.cached(timeout=3600, key_prefix='index')
def account_index():
    return render_template('index/index.html')