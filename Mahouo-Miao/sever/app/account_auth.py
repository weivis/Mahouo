# -*- coding: utf-8 -*-
from flask import Flask, request
from app import db, login_manager
from flask_login import UserMixin, current_user
import time
from flask_login import current_user

# -----------------------------------------------------------

# 用户数据表
class Userdata(db.Model, UserMixin):

    # 表的名字
    __tablename__ = 'userdata'
    __bind_key__ = 'account_userdata'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    user_email = db.Column(db.String(150), unique=True)
    head = db.Column(db.Text)
    reg_time = db.Column(db.String(100))
    reg_ip = db.Column(db.String(100))
    birthday = db.Column(db.String(100))
    gender = db.Column(db.String(100)) #1=男 2=女
    region = db.Column(db.Text)
    username_modify_overage = db.Column(db.Integer)

    # 定义对象
    def __init__(self, username=None, user_email=None, reg_ip=None, birthday=None, region=None, gender=None, head=None, username_modify_overage=2):
        self.username = username
        self.user_email = user_email
        self.reg_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.head = head
        self.reg_ip = reg_ip
        self.birthday = birthday
        self.region = region
        self.gender = gender
        self.username_modify_overage = username_modify_overage
        self.update()  # 提交数据

    # 提交数据函数
    def update(self):
        db.session.add(self)
        db.session.commit()

    def get_id(self):
        return self.user_id

# -----------------------------------------------------------
#db.drop_all()
#db.create_all()
#mysqlclient