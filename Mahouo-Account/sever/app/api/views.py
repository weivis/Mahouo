# -*- coding: utf-8 -*-
__author__ = 'Ran'


from ..api import api
from app import  db
from app.Database import Userdata, Account
from flask import Flask, jsonify, request
from flask_login import current_user
import json


#查询是否存在用户名
@api.route("/search-username", methods=["POST"])
def search_username():
    username = request.values.get('username')
    if Userdata.query.filter_by(username=username).first():
        return json.dumps({'type': '1'}) #有
    else:
        return json.dumps({'type': '0'}) #没有


#查询是否存该邮箱
@api.route("/search-mahouoemail", methods=["POST"])
def search_emailname():
    user_email = request.values.get('emailname')
    if Userdata.query.filter_by(user_email=user_email).first():
        return json.dumps({'type': '1'}) #有
    else:
        return json.dumps({'type': '0'}) #没有


#查询是否存该手机号
@api.route("/search-phone", methods=["POST"])
def search_phone():
    phone = request.values.get('phone')
    if Account.query.filter_by(phone=phone).first():
        return json.dumps({'type': '1'}) #有
    else:
        return json.dumps({'type': '0'}) #没有


#查询是否存该手机号
@api.route("/search-email", methods=["POST"])
def search_useremail():
    email = request.values.get('email')
    if Account.query.filter_by(personal_email=email).first():
        return json.dumps({'type': '1'}) #有
    else:
        return json.dumps({'type': '0'}) #没有


#修改生日日期
@api.route("/profile/birthday", methods=["GET","POST"])
def set_brday():
    if request.method == 'POST':
        if current_user.is_authenticated:
            brd = request.values.get('brd')
            user = Userdata.query.filter_by(user_id=current_user.user_id).first()
            if user.birthday == '' or None:
                user_newbrday = Userdata(birthday = brd)
                db.session.add(user_newbrday)
                db.session.commit() #保存至数据库
                return json.dumps({'type': '1'}) #ok
            else:
                newbrday = db.session.query(Userdata).filter(Userdata.user_id == current_user.user_id).update({Userdata.birthday:brd})
                db.session.commit() #保存至数据库
                return json.dumps({'type': '1'}) #ok
        else:
            return jsonify({'eat shit la you':'吔屎啦你'})
    else:
        return jsonify({'eat shit la you':'吔屎啦你'})


#修改性别
@api.route("/profile/gender", methods=["GET","POST"])
def set_gender():
    if request.method == 'POST':
        if current_user.is_authenticated:
            brd = request.values.get('brd')
            user = Userdata.query.filter_by(user_id=current_user.user_id).first()
            if user.gender == '' or None:
                user_newbrday = Userdata(gender = brd)
                db.session.add(user_newbrday)
                db.session.commit() #保存至数据库
                return json.dumps({'type': '1'}) #ok
            else:
                newbrday = db.session.query(Userdata).filter(Userdata.user_id == current_user.user_id).update({Userdata.gender:brd})
                db.session.commit() #保存至数据库
                return json.dumps({'type': '1'}) #ok
        else:
            return jsonify({'eat shit la you':'吔屎啦你'})
    else:
        return jsonify({'eat shit la you':'吔屎啦你'})


#修改性别
@api.route("/profile/region", methods=["GET","POST"])
def set_region():
    if request.method == 'POST':
        if current_user.is_authenticated:
            region = request.values.get('brd')
            user = Userdata.query.filter_by(user_id=current_user.user_id).first()
            if user.gender == '' or None:
                user_newbrday = Userdata(region = region)
                db.session.add(user_newbrday)
                db.session.commit() #保存至数据库
                return json.dumps({'type': '1'}) #ok
            else:
                newbrday = db.session.query(Userdata).filter(Userdata.user_id == current_user.user_id).update({Userdata.region:region})
                db.session.commit() #保存至数据库
                return json.dumps({'type': '1'}) #ok
        else:
            return jsonify({'eat shit la you':'吔屎啦你'})
    else:
        return jsonify({'eat shit la you':'吔屎啦你'})
