# -*- coding: utf-8 -*-
__author__ = 'Ran'

from ..auth import auth
from app import Flask, cache, login_manager, db
from flask import render_template
from flask import Flask, jsonify, request, redirect, url_for, session
from app.Database import Userdata, Account, Loginlog ,Sso_key
from flask_login import current_user, login_required, login_user, logout_user
from sqlalchemy import func
import hashlib
import time
import re
import json
import base64

@login_manager.user_loader
###加载用户的回调函数接收以Unicode字符串形式表示的用户标示符
###如果能找到用户，这个函数必须返回用户对象，否则返回None。
def load_user(user_id):
    return Userdata.query.get(int(user_id))


#首页
@auth.route('/')
#@cache.cached(timeout=3600, key_prefix='index')
def account_login():
    if current_user.is_authenticated:
        return redirect('https://www.mahouo.com')
    return render_template('auth/sign-in.html')


#登陆的账户验证api
@auth.route('/account-auth', methods=["POST"])
def login_authuser():
    userkey = request.values.get('key')
    email_type = re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", userkey)

    if(email_type):
        userloginauthemail = userkey.split('@')[0]
        user = Userdata.query.filter_by(user_email=userloginauthemail).first()
        #print ('邮箱', userloginauthemail)
        if(user):
            #print (user.user_id)
            authtpye = login_authaccount(user.user_id)
            return json.dumps(authtpye)
        else:
            return json.dumps({'type': '-1'})
    else:
        basphone = base64.encodestring(str.encode(userkey))
        user = Account.query.filter_by(phone=basphone).first()
        if(user):
            #print (user.id)
            authtpye = login_authaccount(user.id)
            return json.dumps(authtpye)
        else:
            return json.dumps({'type': '-1'})

    return ''


def login_authaccount(userid):
    #此处省略了验证用户是否处于禁止登陆期间
    data = {'type': 'ok'}
    return data


@auth.route('/sso')
def sso_auth():
    referer = request.args.get('request', None)
    if referer is not None:
        referer = referer.strip()
    if 'key' in session:
        if referer is not None:
            return redirect(referer + '?token=' +sso_auth_md5())
    return redirect(url_for("auth.account_login",referer=referer))

'''
@auth.route('/sso')
def sso_auth():
    try:
        if current_user.user_id is not None:
            userid = current_user.user_id
            referer = request.args.get('request', None)
            if referer is not None:
                referer = referer.strip()
                return redirect(referer + '?token=' + sso_auth_md5()) #referer=request sso请求头
            print(request)
            return ''
        else:
            return redirect(referer + '?token=' + 'fuck_you')
    except:
        referer = request.args.get('request', None)
        return redirect(referer + '?token=' + 'fuck_you')
'''

def sso_auth_md5():
    key = Sso_key.query.filter_by(user_id = current_user.user_id).first()
    return key.md5


@auth.route('/auth', methods=["POST"])
def account_auth():
    account = request.values.get('key')
    password = request.values.get('pass')
    sign_wp = request.values.get('wp')
    sign_ip = request.values.get('ip')
    sign_city = request.values.get('city')
    sign_long = request.values.get('long')
    account_type = re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", account)
    
    #如果用户输入的是邮箱
    if(account_type):
        emailname = account.split('@')[0]
        login_userdata = Userdata.query.filter_by(user_email=emailname).first()
        user = Account.query.filter_by(id=login_userdata.user_id).first()
        
        '''
        1.获取邮箱[的内容]@xxx.com
        2.在userdata里面找到该邮箱的用户id
        3.把找到的id传到account里面寻找出用户数据
        '''

        #自动化用户登陆记录储存
        sign_log(user_id=login_userdata.user_id, wp=sign_wp, ip=sign_ip, city=sign_city)

    else:
        basphone = base64.encodestring(str.encode(account))
        user = Account.query.filter_by(phone=basphone).first()
        #print(account,password,sign_wp,sign_ip,sign_city,sign_long)

        #自动化用户登陆记录储存
        sign_log(user_id=user.id, wp=sign_wp, ip=sign_ip, city=sign_city)

    if user.is_correct_password(password):
        userinfo_data = Userdata.query.filter_by(user_id=user.id).first()
        if(userinfo_data):
            session['key'] = user.id
            session.permanent = True
            login_user(userinfo_data, remember=sign_long)
            generate_ssokey()
            return json.dumps({'type':'ok'})
        else:
            print('系统错误')
    else:
        print('密码错误')
    
    return ''


def generate_ssokey():
    md5 = hashlib.md5((current_user.user_email).encode()).hexdigest()
    Sso_key().write_sso_key(user_id=current_user.user_id, md5=md5)

def sign_log(user_id, wp, ip, city):
    Loginlog().sign_log_up(user_id=user_id, ip=ip, platform=wp, region=city)

    user_signlog = Loginlog.query.filter_by(user_id=user_id).all() #获取所有登陆记录
    data1 = user_signlog[0]#获取列表第一条数据
    pcs = 0
    for list_pcs in user_signlog:
        pcs = pcs + 1

    if pcs>15:
        db.session.delete(data1)
        db.session.commit()
        #print('删除成功')
    else:
        pass
        #print('未达到15行')



@auth.route("/logout")
@login_required
def logout():
	try:
	    sso_delkey()
	    logout_user()
	    session.pop('key')
	    return redirect(url_for("auth.account_login"))
	except:
	    logout_user()
	    session.pop('key')
	    return redirect(url_for("auth.account_login"))

def sso_delkey():
	data = Sso_key.query.filter_by(user_id = current_user.user_id).first()
	db.session.delete(data)
	db.session.commit()