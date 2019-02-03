# -*- coding: utf-8 -*-
from flask import Flask, request
from app import db
import time

#应用列表
class App_list(db.Model):
    #表的名字
    __tablename__ = 'app_list'
    __bind_key__ = 'mahouo_api'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text) #应用名
    app_type = db.Column(db.Text) #应用状态 是否显示 0=不显示 1=显示
    ico_url = db.Column(db.Text) #应用图标
    url = db.Column(db.Text) #应用url
    sort = db.Column(db.Text) #app排序

    # 定义对象
    def __init__(self, name=name, app_type=0, ico_url=ico_url, url=url):
        self.name = name
        self.app_type = app_type
        self.ico_url = ico_url
        self.url = url
        self.update()  # 提交数据

    def update(self):
        db.session.add(self)
        db.session.commit()

#db.drop_all()
#db.create_all()