# -*- coding: utf-8 -*-
from app import db
from flask_login import current_user
import time

# 稿件表
class Report_index_data(db.Model):

    # 表的名字
    __tablename__ = 'report_index_data'

    id = db.Column(db.Integer, primary_key=True) #自增id

    index_id = db.Column(db.Text) #被举报的数据id
    index_name = db.Column(db.Text)#被举报的数据名
    index_link = db.Column(db.Text)#被举报的数据url

    submit_userid = db.Column(db.Integer) #提交者id #有则储存无则为空
    status = db.Column(db.Integer) #是否可用状态 0=未处理 1=完成
    
    admin_id = db.Column(db.Integer) #处理的管理员id

    time = db.Column(db.String(100)) #提交时间

    # 定义对象
    def __init__(self, index_id=None, index_name=None, index_link=None, submit_userid=None, status=None, admin_id=None):
        self.index_id = index_id
        self.index_name = index_name
        self.index_link = index_link
        self.submit_userid = submit_userid
        self.status = 0
        self.admin_id = admin_id
        self.time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.update()  # 提交数据

    # 提交数据函数
    def update(self):
        db.session.add(self)
        db.session.commit()


#db.drop_all()
#db.create_all()