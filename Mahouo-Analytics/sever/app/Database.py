# -*- coding: utf-8 -*-
from app import db
from flask_login import current_user
import time

# 稿件表
class Submit_link(db.Model):

    # 表的名字
    __tablename__ = 'submit_link'

    id = db.Column(db.Integer, primary_key=True) #自增id
    link = db.Column(db.Text) #链接
    submit_userid = db.Column(db.Integer) #提交者id #有则储存 无则为空
    status = db.Column(db.Integer) #是否可用状态 0=未审核 1=通过
    time = db.Column(db.String(100)) #提交时间

    # 定义对象
    def __init__(self, link=None, submit_userid=None):
        self.link = link
        self.submit_userid = submit_userid
        self.status = 0
        self.time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.update()  # 提交数据

    # 提交数据函数
    def update(self):
        db.session.add(self)
        db.session.commit()


#db.drop_all()
#db.create_all()