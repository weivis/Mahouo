__author__ = 'Ran'
from app import Flask, cache
from ..mobile import mobile
import hashlib
from flask import render_template, request, url_for, jsonify, redirect
from elasticsearch import Elasticsearch
from datetime import datetime
from app.elastic import es
from flask_login import current_user
from app.proxy.search import getsearch


#搜索
@mobile.route('/index/')
@mobile.route('/index')
@mobile.route('/')
@cache.cached(timeout=3600, key_prefix='mobile-home')  #缓存
def search():
    return render_template('mobile/index.html')


#搜索返回
@mobile.route('/search')
@cache.cached(timeout=3600, key_prefix='mobile-out')
def mobile_out():

    #搜索内容
    search_content = request.args.get('s')

    page = request.args.get('page')#页数
    #spage = request.args.get('page')#上一个页数
    charted = request.args.get('charted')#是否精准搜索
    st = request.args.get('st') #开始条数
    er = request.args.get('er') #结束条数
    optime = request.args.get('optime')#时间分类 开始时间
    ertime = request.args.get('ertime')#时间分类 结束时间
    cacheid = request.args.get('cacheid')#时间分类 结束时间

    if search_content is None or search_content == '':
        return redirect(url_for('mobile.search'))

    if(search_content):
        start_time = datetime.now()

        try:
           page = int(page)
        except:
            page = 1

        '''
        results = es.search(index="index",
        body={
        "size": 10, "from":(page-1)*10,
            "query": {
                "multi_match": {
                    "query": search_content,
                    "analyzer" : "ik_max_word",
                    "fields": ["title","keywords","description"],
                    },
                },
            }
        ) #主域名
        '''

        try:
            results = getsearch(content=search_content, page=page)
        except:
            results = ''

        end_time = datetime.now()
        last_seconds = (end_time - start_time).total_seconds()

        total_nums = results["hits"]["total"]
        #scroll_id = results['_scroll_id']

        page_nums = 0

        '''
        if (page % 10) > 0:
            page_nums = int(total_nums / 10) + 1
        else:
            page_nums = int(total_nums / 10)
        '''

        #print(scroll_id)
        #print('列队开始数',(page-1)*10)

    return render_template('mobile/search-out.html', results=results, s=search_content, total_nums=total_nums, page=page, page_nums=page_nums, end_time=last_seconds,)