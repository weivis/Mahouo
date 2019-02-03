# -*- coding: utf-8 -*-
__author__ = 'Ran'

from ..register import register
from app import Flask, cache
from flask import render_template, request, redirect
from app.Database import Userdata, Account, Reg_ban_vocabulary, Usersafe
from flask_login import current_user
import json

'''
#首页
@register.route('/auth')
#@cache.cached(timeout=3600, key_prefix='index')
def passauth():
    password = word = '.1889394'
    phone = ''
    useremail = '442981412@qq.com'
    user = Account.query.filter_by(id=2).first()
    if user.is_correct_password(word):
        authreg = auth_register(phone=phone, personal_email=useremail, password=password)
        if (authreg):
            print (authreg.id)
            return ''
    else:
        return 'no'
'''

#首页
@register.route('/')
#@cache.cached(timeout=3600, key_prefix='index')
def reg():
    if current_user.is_authenticated:
        return redirect('https://mahouo.com')
    return render_template('register/register.html')


#首页
@register.route('/post', methods=["POST"])
#@cache.cached(timeout=3600, key_prefix='index')
def reg_api():

    username = request.values.get('reg_name')
    email_name = request.values.get('reg_emailname')
    phone = request.values.get('reg_phone')
    password = request.values.get('reg_pass')
    useremail = request.values.get('reg_useremail')

    #验证注册信息 (返回值为0/1 0表示通过)
    regauth = auth_reginfo(username, email_name, phone, useremail)

    if regauth.get('out_type') == 0: #注册内容是否可用

        print ('注册信息没问题')

        # 传入注册信息(account)
        Account()._set_info(phone=phone, password=password, personal_email=useremail) #传入值(密码 手机号 个人常用邮箱)

        # 检验是否成功注册用户账户信息(密码 用户个人邮箱 手机)
        authreg = auth_register(phone=phone, personal_email=useremail, password=password)

        if (authreg.id):#判断是否存在UserID 不存在则创建出错 执行回调删除出错注册数据

            #初始化用户
            #用户数据表初始化
            Userdata().initialization_userdata(user_id=authreg.id, username=username, user_email=email_name)

            #用户安全表初始化
            Usersafe().initialization_usersafe(user_id=authreg.id)

            #用户密保表初始化 (废弃)
            #Security().initialization_security(user_id=authreg.id)

            '''
                写入用户数据表(账户id 帐户名 账户邮箱名(mahouo邮箱))
            '''
            return  json.dumps({'out_type': 'ok'})

        else:
            error_password = generate_password_hash(password)
            Account_register_error_data = Account(phone = phone, password = error_password, personal_email = useremail)
            db.session.add(Account_register_error_data)
            db.session.commit()
            return '系统出错'

            # 注册失败后立刻执行清除删除该注册信息所创建的记录
            #print (username, email_name, phone, password, useremail)
            #return ''
    else:
        return json.dumps({'out_type': regauth.get('out_type'), 'out': regauth.get('out')})#{'out_type': regauth.out_type, 'out': regauth.out}


def auth_register(phone, personal_email, password):
    if(password and personal_email or phone):
        user = Account.query.filter_by(personal_email=personal_email).first()
        if user: # Account.query.filter_by(personal_email = personal_email).first():
            return user
        elif Account.query.filter_by(phone = phone).first():
            return user
        elif user.is_correct_password(password):
            return user
        else:
            return False


def auth_reginfo(username, email_name, phone, useremail):

    if Account.query.filter_by(phone=phone).first():
        auth_type = {'out_type': 1, 'out': '该手机号已被注册'}
        return auth_type

    #是否允许注册
    elif 1 == 0: #Reg_ban_vocabulary
        auth_type = {'out_type': 1, 'out': '非开放注册'}
        return auth_type

    #查询用户名是否存在非法字段
    elif Reg_ban_vocabulary.query.filter_by(vocabulary=useremail).first(): #Reg_ban_vocabulary
        auth_type = {'out_type': 1, 'out': '非法字段'}
        return auth_type

    elif Account.query.filter_by(personal_email=useremail).first(): #Account
        auth_type = {'out_type': 1, 'out': '该邮箱以使用过'}
        return auth_type

    elif Userdata.query.filter_by(username=username).first(): #Userdata
        auth_type = {'out_type': 1, 'out': '用户名已存在'}
        return auth_type

    elif Userdata.query.filter_by(user_email=email_name).first(): #Userdata
        auth_type = {'out_type': 1, 'out': '该邮箱名已被使用'}
        return auth_type

    elif username == '' or None:
        auth_type = {'out_type': 1, 'out': '用户名为空'}
        return auth_type

    elif email_name == '' or None:
        auth_type = {'out_type': 1, 'out': '邮箱名为空'}
        return auth_type

    elif phone == '' or None:
        auth_type = {'out_type': 1, 'out': '手机空'}
        return auth_type

    elif useremail == '' or None:
        auth_type = {'out_type': 1, 'out': '用户邮箱为空'}
        return auth_type

    else:
        auth_type = {'out_type': 0, 'out': ''}
        return auth_type
