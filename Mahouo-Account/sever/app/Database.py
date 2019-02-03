# -*- coding: utf-8 -*-
from app import db
from flask_login import UserMixin, current_user
from flask_bcrypt import check_password_hash, generate_password_hash
import time
import hashlib
import base64


# 用户表
class Account(db.Model):

    # 表的名字
    __tablename__ = 'account'

    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(100), unique=True)
    personal_email = db.Column(db.String(150), unique=True)
    phone = db.Column(db.String(100), unique=True)
    violation_count = db.Column(db.Integer)
    status = db.Column(db.Integer)

    # 定义对象
    def __init__(self, password=None, personal_email=None, phone=None, violation_count=0, status=0):
        self.password = password
        self.personal_email = personal_email
        self.phone = phone
        self.violation_count = violation_count
        self.status = status
        self.update()  # 提交数据

    # 提交数据函数
    def update(self):
        db.session.add(self)
        db.session.commit()

    def is_correct_password(self, plaintext):
        if check_password_hash(self.password, plaintext):
            return True

    #查询是否存在这个手机号
    def is_correct_phone(self, plaintext):
        base64_phone = base64.encodestring(str.encode(plaintext))
        if Account.query.filter_by(phone=base64_phone).first():
            return True

    #获取用户手机号
    def _get_user_phone(self):
        user = Account.query.filter_by(id = current_user.user_id).first()
        phone = base64.decodestring(str.encode(user.phone))
        return phone

    #获取手机号
    def _get_phone(self):
        phone = base64.decodestring(str.encode(self.phone))
        return phone

    def _set_info(self, phone=None, password=None, personal_email=None):
        if phone: #传入account表下的用户id
            self.phone = base64.encodestring(str.encode(phone))
        if password: #用户名
            self.password = generate_password_hash(password)
        if personal_email: #邮箱名
            self.personal_email = personal_email
        self.update()

# -----------------------------------------------------------


# 用户数据表
class Userdata(db.Model, UserMixin):

    # 表的名字
    __tablename__ = 'userdata'

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

    # 初始化用户
    def initialization_userdata(self, user_id=None, username=None, user_email=None):
        if user_id: #传入account表下的用户id
            self.user_id = user_id
        if username: #用户名
            self.username = username
        if user_email: #邮箱名
            self.user_email = user_email
        self.update()
        '''
        初始化用户信息
        initialization_userdata(user_id, username, user_email)
        initialization_userdata用于注册完成account后初始化用户信息传入用户名
        '''

    def get_id(self):
        return self.user_id

# -----------------------------------------------------------

# 用户安全表
class Usersafe(db.Model):

    # 表的名字
    __tablename__ = 'usersafe'

    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Integer)   #常用邮箱是否已验证
    phone = db.Column(db.Integer)   #手机号是否已经验证
    security = db.Column(db.Integer) #是否存在密保

    # 定义对象
    def __init__(self, email=0, phone=0, security=0):
        self.email = email
        self.phone = phone
        self.security = security
        self.update()  # 提交数据

    # 提交数据函数
    def update(self):
        db.session.add(self)
        db.session.commit()

    # 初始化用户
    def initialization_usersafe(self, user_id=None):
        if user_id: #传入account表下的用户id
            self.user_id = user_id
            self.email = 0
            self.phone = 0
            self.security = 0
        self.update()

# -----------------------------------------------------------

#密保表
class Security(db.Model):

    # 表的名字
    __tablename__ = 'security'

    user_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(100))
    problem1 = db.Column(db.Text)
    problem2 = db.Column(db.Text)
    problem3 = db.Column(db.Text)
    answer1 = db.Column(db.Text)
    answer2 = db.Column(db.Text)
    answer3 = db.Column(db.Text)

    # 定义对象
    def __init__(self, problem1=None, problem2=None, problem3=None, answer1=None, date=None, answer2=None, answer3=None):
        #self.user_id = user_id
        self.date = date #time.strftime("%Y-%m-%d", time.localtime())
        self.problem1 = problem1
        self.problem2 = problem2
        self.problem3 = problem3
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.update()  # 提交数据

    # 提交数据函数
    def update(self):
        db.session.add(self)
        db.session.commit()

    def _stdata(self, problem1=None, problem2=None, problem3=None,answer1=None, answer2=None, answer3=None):
        self.user_id = current_user.user_id
        self.date = time.strftime("%Y-%m-%d", time.localtime())
        if problem1:
            self.problem1 = problem1
        if problem2:
            self.problem2 = problem2
        if problem3:
            self.problem3 = problem3
        if answer1:
            self.answer1 = answer1
        if answer2:
            self.answer2 = answer2
        if answer3:
            self.answer3 = answer3
        self.update()

# -----------------------------------------------------------

#敏感词汇表
class Reg_ban_vocabulary(db.Model):

    # 表的名字
    __tablename__ = 'reg_ban_vocabulary'

    id = db.Column(db.Integer, primary_key=True)
    vocabulary = db.Column(db.String(100))

    # 定义对象
    def __init__(self, vocabulary=None):
        self.vocabulary = vocabulary
        self.update()  # 提交数据

    # 提交数据函数
    def update(self):
        db.session.add(self)
        db.session.commit()

# -----------------------------------------------------------

#用户违规记录表
class User_violation_log(db.Model):

    # 表的名字
    __tablename__ = 'user_violation_log'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    vocabulary = db.Column(db.String(100))
    violation_type = db.Column(db.Integer)
    prohibit_time = db.Column(db.String(100))
    effective = db.Column(db.Integer)
    date = db.Column(db.String(100))
    text = db.Column(db.Text)


    # 定义对象
    def __init__(self, user_id=None, vocabulary=None, violation_type=None, prohibit_time=None, effective=None, date=None, text=None):
        self.user_id = user_id
        self.vocabulary = vocabulary
        self.violation_type = violation_type
        self.prohibit_time = prohibit_time
        self.effective = effective
        self.date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.text = text
        self.update()  # 提交数据

    # 提交数据函数
    def update(self):
        db.session.add(self)
        db.session.commit()

# -----------------------------------------------------------

#敏感词汇表
class Loginlog(db.Model):

    # 表的名字
    __tablename__ = 'loginlog'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    date = db.Column(db.String(100))
    time = db.Column(db.String(100))
    ip = db.Column(db.String(100))
    platform = db.Column(db.Text)
    region = db.Column(db.String(100))

    # 定义对象
    def __init__(self, user_id=None, ip=None, platform=None, region=None):
        self.user_id = user_id
        self.date = time.strftime("%Y-%m-%d", time.localtime())
        self.time = time.strftime("%H:%M:%S", time.localtime())
        self.ip = ip
        self.platform = platform
        self.region = region
        self.update()  # 提交数据

    # 提交数据函数
    def update(self):
        db.session.add(self)
        db.session.commit()

    def sign_log_up(self, user_id=None, ip=None, platform=None, region=None):
        if user_id:
            self.user_id = user_id
        if ip:
            self.ip = ip
        if platform:
            self.platform = platform
        if region:
            self.region = region
        self.update()


# -----------------------------------------------------------

#SSO记录
class Sso_key(db.Model):

    # 表的名字
    __tablename__ = 'sso_key'
    __bind_key__ = 'mahouo_sso'

    id = db.Column(db.Integer, primary_key=True)
    md5 = db.Column(db.Text)
    user_id = db.Column(db.Integer)

    # 定义对象
    def __init__(self, md5=None, user_id=None):
        md5 = md5
        user_id = user_id
        self.update()  # 提交数据

    # 提交数据函数
    def update(self):
        db.session.add(self)
        db.session.commit()

    def write_sso_key(self, md5=None,user_id=None):
        if md5:
            self.md5 = md5
        if user_id:
            self.user_id = user_id
        self.update()