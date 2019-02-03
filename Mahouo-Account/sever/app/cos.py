# -*- coding: utf-8 -*-

import re
from qiniu import Auth, put_file, etag, urlsafe_base64_encode, BucketManager, PersistentFop
import qiniu.config

access_key = ''
secret_key = ''

def Get_uploadtoken(bucket_name, key, outtime):
    q = Auth(access_key, secret_key)
    token = q.upload_token(bucket_name, key, int(outtime))
    return token

#删除头像
def del_userhead(user_oldhead):
    q = Auth(access_key, secret_key)
    bucket = BucketManager(q)
    bucket_name = 'mhcdn-ssl-img' #需要删除的储存桶
    key = user_oldhead #被删除的文件名
    ret, info = bucket.delete(bucket_name, 'head/'+str(key))
    #print('对象存储删除被执行')
    #print('被删除的文件是',user_oldhead)
    #print(info)
    return True

def cover_transcoding(key):
    q = Auth(access_key, secret_key)

    # 要转码的文件所在的空间和文件名。
    bucket = 'cache'
    overname = 'head/' + str(key)

    # 转码是使用的队列名称。
    # pipeline = 'mpsdemo'

    # 要进行转码的转码操作。
    fops = 'imageView2/1/w/180/h/180/q/100|imageslim'
    # 可以对转码后的文件进行使用saveas参数自定义命名，当然也可以不指定文件会默认命名并保存在当前空间
    saveas_key = urlsafe_base64_encode('mhcdn-ssl-img:' + overname)

    fops = fops + '|saveas/' + saveas_key
    pfop = PersistentFop(q, bucket)  # , pipeline

    ops = []
    ops.append(fops)
    ret, info = pfop.execute(key, ops, 1)
    print(info)
    assert ret['persistentId'] is not None