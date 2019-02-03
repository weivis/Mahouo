# -*- coding: utf-8 -*-
__author__ = 'Ran'

from ..safe import safe
from app import app, Flask, db
from flask import render_template, request, redirect, url_for
from flask_login import current_user
from app.Database import Security, Usersafe

safe_problem = [
    '你喜欢女装吗?',
    '你喜不喜欢搞基?',
    '如果你突然发现你的老婆是可爱的男孩子你会怎么办?',
    '如果你老妈突然告诉你你有个亲妹妹你会怎么处理?',
    '你觉得以后你能变成富豪吗?',
    '如果你某天起床发现你突然变成女孩子了你会做的第一件事是什么?',
    '如果你的房间里面有鬼你会怎么办?',
    '你的钱包突然空了又没地方住又没朋友你会怎么做?(而且还没饭吃)',
    '你喜欢萝莉吗?',
    '你觉得你们班主任可不可爱?',
    '想象一下你让你们班主任女装的看后感',
    '如果你老爸叫你亲他一口你会怎么做?',
    '万一你的心爱的女儿那天有男朋友你会怎么做?',
    '你学号是多少?(这个问题太没安全性了纯属筹数)',
    '你喜欢带套吗?',
]


@safe.route('/security')
def security_atuh():
    if Security.query.filter_by(user_id=current_user.user_id).first():
        #存在则要验证
        return render_template('safe/security-auth.html',title='设置密保问题和答案')
    else:
        #不存在密保记录直接跳转至设置页面
        return redirect(url_for("safe.security_update_page"))

@safe.route('/security/update')
def security_update_page():
    return render_template('safe/security-set.html', title='设置密保问题和答案')

@safe.route('/security/auth',methods=['GET','POST'])
def security_atuh_post():
    if request.method == 'POST':
        wenti = request.form.get('select')
        out = request.form.get('out')
        # 判断问题是否存在于列表中
        if wenti in safe_problem:
            #查询该用户是否存在密保记录
            usersafedata = Security.query.filter_by(user_id=current_user.user_id).first()
            if(usersafedata):
            	if usersafedata.problem1 == wenti or usersafedata.problem2 == wenti or usersafedata.problem3 == wenti:
            		if usersafedata.answer1 == out or usersafedata.answer2 == out or usersafedata.answer3 == out:
            			return redirect(url_for("safe.security_update_page"))
            		else:
            			return '问题或答案不正确'
            	else:
            		return '问题或答案不正确'
            else:
                return ''
        else:
            return '密保问题不存在'
    else:
        return '非法请求'

@safe.route('/security/update-post',methods=['POST'])
def security_update():
    if request.method == 'POST':
        problem1 = request.form.get('pr1')
        problem2 = request.form.get('pr2')
        problem3 = request.form.get('pr3')
        answer1 = request.form.get('ans1')
        answer2 = request.form.get('ans2')
        answer3 = request.form.get('ans3')

        auth_data = auth_security_data(problem1, problem2, problem3, answer1, answer2, answer3)
        if auth_data['type'] == 'ok':
            if Security.query.filter_by(user_id=current_user.user_id).first():
                newdata = db.session.query(Security).filter(Security.user_id == current_user.user_id).update({Security.problem1:problem1, Security.problem2:problem2, Security.problem3:problem3,
                Security.answer1:answer1, Security.answer2:answer2, Security.answer3:answer3})
                db.session.commit() #保存至数据库
                security_auth_ok()
                return redirect(url_for("user.account_my"))
                return ''
            else:
                Security()._stdata(problem1=problem1, problem2=problem2, problem3=problem3, answer1=answer1, answer2=answer2, answer3=answer3)
                security_auth_ok()
                return redirect(url_for("user.account_my"))
                return ''
        else:
            return '输入有误'
    else:
        return '非法请求'

def security_auth_ok():
    new_security_type = db.session.query(Usersafe).filter(Usersafe.user_id == current_user.user_id).update({Usersafe.security:1})
    db.session.commit() #保存至数据库

def auth_security_data(problem1, problem2, problem3, answer1, answer2, answer3):
    if problem1 == None or '请选择':
        if problem1 in safe_problem:
            problem1auth = 1
        else:
            jsdata = {'type':'error','info':'该问题不存在于系统中'}
            return jsdata
    else:
        jsdata = {'type':'error','info':'问题为空'}
        return jsdata

    if problem2 == None or '请选择':
        if problem2 in safe_problem:
            problem2auth = 1
        else:
            jsdata = {'type':'error','info':'该问题不存在于系统中'}
            return jsdata
    else:
        jsdata = {'type':'error','info':'问题为空'}
        return jsdata

    if problem3 == None or '请选择':
        if problem3 in safe_problem:
            problem3auth = 1
        else:
            jsdata = {'type':'error','info':'该问题不存在于系统中'}
            return jsdata
    else:
        jsdata = {'type':'error','info':'问题为空'}
        return jsdata

    if problem3auth + problem2auth + problem1auth == 3:
        if (answer1 and answer2 and answer3):
            jsdata = {'type':'ok','info':''}
            return jsdata
        else:
            jsdata = {'type':'error','info':'答案有误'}
            return jsdata
    else:
        jsdata = {'type':'error','info':'问题为空'}
        return jsdata