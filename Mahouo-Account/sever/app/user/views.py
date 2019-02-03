# -*- coding: utf-8 -*-
__author__ = 'Ran'

from ..user import user
from app import db, Flask
import os
from flask import render_template, request, abort
from flask_login import current_user, login_required
from app.Database import Account, Usersafe, Loginlog, Userdata
from app.cos import Get_uploadtoken, del_userhead, cover_transcoding
import hashlib
import json
import time
import base64


@user.route('/')
@login_required
#@cache.cached(timeout=3600, key_prefix='index')
def account_my():
    user = Account.query.filter_by(id=current_user.user_id).first()
    usersafe = user_safe_type(current_user.user_id)
    loginlog = account_my_loginlog(current_user.user_id)
    phone = str((base64.decodestring(str.encode(user.phone))),'utf-8')
    get = phone[0:5] + '******'
    return render_template('user/user-account.html',userphone=get, usersafe=usersafe, loginlog=loginlog)

def user_safe_type(id):
    user = Usersafe.query.filter_by(user_id=id).first()
    if user.email == 1:
        email = 'True'
    else:
        email = 'False'

    if user.phone == 1:
        phone = 'True'
    else:
        phone = 'False'

    if user.security == 1:
        security = 'True'
    else:
        security = 'False'

    if user.phone + user.email + user.security == 0:
        level = 0
    if user.phone == 1 or user.email == 1 or user.security ==1:
        level = 1
    if user.phone == 1 and user.email == 1 or user.security == 1:
        level = 2
    if user.phone == 1 and user.email == 1 and user.security == 1:
        level = 3

    data = {"level":level, "email":email, "phone":phone, "security":security}
    return data

def account_my_loginlog(userid):
    data = Loginlog.query.filter_by(user_id=userid).order_by(Loginlog.id.desc()).limit(5).all()
    return data


@user.route('/upload-head')
@login_required
#@cache.cached(timeout=3600, key_prefix='index')
def account_headup():
    return render_template('user/user-head.html', title='更换头像')

file_type = set([u'jpg',u'png',u'gif']) #这里可以限制上传文件格式



# 获取封面上传许可证
@user.route('/upload-token', methods=["GET", "POST"])
@login_required
def get_video_cover_upload_token():
    '''
        提取filename表单字段 filename 封面图源文件名
        提取key字段 key字段储存的是视频生成的key
    '''
    filename = request.args.get('filename')
    filetype = filename.split('.')[-1]

    if filetype in file_type:
        # 这一步很重要 如果key不存在表示用户未选择上传的文件 该情况下禁止上传封面图
        # 生成新的封面图 key
        generate_key = (hashlib.md5((current_user.user_email).encode()).hexdigest()) + time.strftime("%H%M%S", time.localtime()) + '.jpg'  # + filetype
        data = Get_uploadtoken(bucket_name='cache', key=generate_key, outtime='3600')
        print(generate_key)
        if (data):  # 判断token是否获取成功
            return json.dumps({'code': 'ok', 'text': '成功获取封面图上传许可证', 'covertoken': data, 'filetype': filetype,'key': generate_key})
        return json.dumps({'code': 'no', 'text': '封面图许可证生成失败', 'covertoken': '', 'filetype': filetype})
    return json.dumps({'code': 'no', 'text': '上传的文件类型不允许', 'covertoken': '', 'filetype': filetype})


# 发布视频
@user.route('/release', methods=["POST"])
def release_video():
    if request.method == 'POST':
        jsondata = request.json
        new_filename = jsondata['key']

        #查询用户是否存在头像(没有pass 有获取用户旧头像文件名传入对象存储删除)
        #if ifuserhead() == 0: #0=没有 1=有
        if current_user.head == '' or None:
            cover_transcoding(new_filename)
            new_head = db.session.query(Userdata).filter(Userdata.user_id == current_user.user_id).update(
                {Userdata.head: new_filename})
            db.session.commit()  # 保存至数据库
            return json.dumps({'code': 'error'})

        else:
            user = Userdata.query.filter_by(user_id = current_user.user_id).first()
            #print('存在旧图象执行删除旧头像')
            del_userhead(user.head)
            cover_transcoding(new_filename)

            new_head = db.session.query(Userdata).filter(Userdata.user_id == current_user.user_id).update(
                {Userdata.head: new_filename})
            db.session.commit()  # 保存至数据库
            return json.dumps({'code': 'ok'})


#查询是否存在头像
def ifuserhead():
    user = Userdata.query.filter_by(user_id = current_user.user_id).first()
    if user.head == '' or None:
        return 1
    else:
        return 0


@user.route('/profile')
@login_required
#@cache.cached(timeout=3600, key_prefix='index')
def account_profile():
    return render_template('user/user-infoset.html',title='更新个人信息')


@user.route('/security')
@login_required
#@cache.cached(timeout=3600, key_prefix='index')
def account_security():
    user = Account.query.filter_by(id=current_user.user_id).first()
    safedata = Usersafe.query.filter_by(user_id=current_user.user_id).first()
    phone = str((base64.decodestring(str.encode(user.phone))),'utf-8')
    get = phone[0:5] + '******'
    return render_template('user/user-safe.html', safedata=safedata, phone = get, email = user.personal_email, title = '安全')


@user.route('/activity')
@login_required
#@cache.cached(timeout=3600, key_prefix='index')
def account_loginlog():
    data = Loginlog.query.filter_by(user_id=current_user.user_id).all()
    return render_template('user/user-loginlog.html',data=data,title='账户活动')