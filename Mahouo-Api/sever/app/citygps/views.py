# -*- coding: utf-8 -*-
__author__ = 'Ran'

from ..citygps import citygps
from flask import render_template
from app import Flask, db, cache
import json
from flask_cors import *
import requests

CORS(citygps, supports_credentials=True)

@citygps.route("/")#getcity
def xinlang_gps():
	#url = "http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json"
	#jsonStr = requests.get(url).text
	return json.dumps({'type':'no','city':'未知','province':'未知','country':'未知'})
	#return json.dumps(json.loads(jsonStr))