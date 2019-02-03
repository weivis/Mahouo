# -*- coding: utf-8 -*-
__author__ = 'Ran'

from ..apilist import apilist
from flask import render_template
from app import Flask, db, cache
from app.Database import App_list
import json
from flask_cors import *

CORS(apilist, supports_credentials=True)

@apilist.route("/")
@cache.cached(timeout=36000, key_prefix='app-list')
def get_common_applist():
    app_list = App_list.query.filter_by(app_type=0).all()
    applist_data = [{
        'name': i.name,
        'img': i.ico_url,
        'url': i.url,
        'sort': i.sort,
    }for i in app_list]
    return json.dumps(sorted(applist_data, key=lambda x:x['sort'], reverse=True))