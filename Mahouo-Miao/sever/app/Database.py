# -*- coding: utf-8 -*-
from app import db
from flask_login import UserMixin, current_user
from flask_bcrypt import check_password_hash, generate_password_hash
import time


# 热门uc标题部
class Carousel_module(db.Model):

    # 表的名字
    __tablename__ = 'carousel_module'

    id = db.Column(db.Integer, primary_key=True) #自增id
    cover = db.Column(db.Text) #封面
    classification = db.Column(db.Integer) #类型
    name = db.Column(db.Text) #网站名字
    url = db.Column(db.Text) #url
    status = db.Column(db.Integer) #状态
    sorll = db.Column(db.Integer) #排序

    # 定义对象
    def __init__(self, name=None, cover=None, url=None, status=None, sorll=None, classification=None):
        self.name = name
        self.cover = cover
        self.classification = classification
        self.url = url
        self.status = status
        self.sorll = sorll
        self.update()  # 提交数据

    # 提交数据函数
    def update(self):
        db.session.add(self)
        db.session.commit()


# 热门uc标题部
class Uc_page(db.Model):

    # 表的名字
    __tablename__ = 'uc_page'

    id = db.Column(db.Integer, primary_key=True) #自增id
    classification = db.Column(db.Integer) #类型
    name = db.Column(db.Text) #网站名字
    url = db.Column(db.Text) #url
    status = db.Column(db.Integer) #状态
    sorll = db.Column(db.Integer) #排序

    # 定义对象
    def __init__(self, name=None, url=None, status=None, sorll=None, classification=None):
        self.name = name
        self.classification = classification
        self.url = url
        self.status = status
        self.sorll = sorll
        self.update()  # 提交数据

    # 提交数据函数
    def update(self):
        db.session.add(self)
        db.session.commit()


# 首页常用网站
class Index_commonly_com(db.Model):

    # 表的名字
    __tablename__ = 'index_commonly_com'

    id = db.Column(db.Integer, primary_key=True) #自增id
    name = db.Column(db.Text) #网站名字
    ico = db.Column(db.Text) #图标
    url = db.Column(db.Text) #url
    status = db.Column(db.Integer) #状态
    sorll = db.Column(db.Integer) #排序

    # 定义对象
    def __init__(self, name=None, ico=None, url=None, status=None, sorll=None):
        self.name = name
        self.ico = ico
        self.url = url
        self.status = status
        self.sorll = sorll
        self.update()  # 提交数据

    # 提交数据函数
    def update(self):
        db.session.add(self)
        db.session.commit()


# 网站类目
class Classification_com(db.Model):

    # 表的名字
    __tablename__ = 'classification_com'

    id = db.Column(db.Integer, primary_key=True) #自增id
    classification = db.Column(db.Integer) #类目id
    name = db.Column(db.Text) #网站名字
    ico = db.Column(db.Text) #图标
    url = db.Column(db.Text) #url
    status = db.Column(db.Integer) #状态
    sorll = db.Column(db.Integer) #排序

    # 定义对象
    def __init__(self, name=None, ico=None, url=None, status=None, sorll=None, classification=None):
        self.name = name
        self.classification = classification
        self.ico = ico
        self.url = url
        self.status = status
        self.sorll = sorll
        self.update()  # 提交数据

    # 提交数据函数
    def update(self):
        db.session.add(self)
        db.session.commit()


# 连载番剧
class Bangumi(db.Model):

    # 表的名字
    __tablename__ = 'bangumi'

    id = db.Column(db.Integer, primary_key=True) #自增id
    day = db.Column(db.Integer) #更新周期
    name = db.Column(db.Text) #番剧名称
    cover = db.Column(db.Text) #封面图
    url = db.Column(db.Text) #url

    # 定义对象
    def __init__(self, name=None, ico=None, url=None, day=None):
        self.name = name
        self.classification = classification
        self.ico = ico
        self.url = url
        self.day = day
        self.update()  # 提交数据

    # 提交数据函数
    def update(self):
        db.session.add(self)
        db.session.commit()


#db.drop_all()
#db.create_all()