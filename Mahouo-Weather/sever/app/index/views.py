__author__ = 'Ran'
from app import Flask, cache
from ..index import index
from flask import render_template, request, url_for, jsonify, redirect, session
from datetime import datetime
from flask_login import current_user

#搜索
@index.route('/index/')
@index.route('/index')
@index.route('/')
@cache.cached(timeout=3600, key_prefix='index')  #缓存
def search():
    useremailsession = None
    if(useremailsession):
    	user = useremailsession
    	return render_template('index.html',user = user)
    else:
    	user = ""
    	return render_template('index.html',user = user)