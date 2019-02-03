__author__ = 'Ran'
from app import Flask, cache
from ..index import index
import hashlib
from flask import render_template, request, url_for, jsonify, redirect
from elasticsearch import Elasticsearch
from datetime import datetime
from app.elastic import es
from flask_login import current_user
from app.proxy.search import getsearch


#搜索
@index.route('/index/')
@index.route('/index')
@index.route('/')
def search():
    return render_template(
        #页面html文件
        'index.html',

        newpage='',

        page_nums=0,

        page = 0,

        results = '',
        )


#搜索返回
@index.route('/search')
def search_out():

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

    #上一个搜索内容
    otcon = search_content

    #print('搜索的内容为:',search_content)
    #print('上一个搜索内容:',otcon)
    #print('页数:',page)
    #print('是否精准搜索:',charted)

    #是否存在搜索内容
    if search_content is None or search_content == '':
        return redirect(url_for('index.search'))

    if(search_content):
        start_time = datetime.now()

        try:
           page = int(page)
        except:
            page = 1

        #子域名搜索
        if page == 1:
            sonlink = es.search(index="subindex", body={'query': {'match': {'maintitle': search_content}}}) #主域名带子域名
        else:
            sonlink = ''

        try:
            results = getsearch(content=search_content, page=page)
        except:
            results = ''

        #print(results)

        end_time = datetime.now()
        last_seconds = (end_time - start_time).total_seconds()
        total_nums = results["hits"]["total"]
        page_nums = 10

    return render_template("index.html",
    s=search_content, #搜索内容
    results=results, #搜索返回内容
    sonlink=sonlink, #子域名
    end_time=last_seconds, #搜索时间
    otcon=otcon, #上一个搜索内容
    page=page, #当前搜索页数
    page_nums=page_nums, #页数
    total_nums=total_nums, #结果大概数据量
    newpage='ture')