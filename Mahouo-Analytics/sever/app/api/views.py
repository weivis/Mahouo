__author__ = 'Ran'
from app import Flask, db #cache
from ..api import api
import hashlib
from flask import render_template, request
from datetime import datetime
from flask_login import current_user
from app.Database import Submit_link
import json

#获取上传的url
@api.route('/submit_url', methods=["POST"])
def submit_url():
    if request.method == 'POST':
        url = request.values.get('url')
        if url:
            if current_user.user_id:
                userid = current_user.user_id
            else:
                userid = ''

            if Submit_link.query.filter_by(link = url, submit_userid = userid).first():
                return json.dumps({'t': '你已提交过该URL'})
            else:
                data = Submit_link(link=url,submit_userid=userid) 
                db.session.add(data) 
                db.session.commit()
                return json.dumps({'t': '0'})
        else:
            return json.dumps({'t': '1'})
    else:
        return '404'