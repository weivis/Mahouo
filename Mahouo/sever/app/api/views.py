__author__ = 'Ran'
import json

from flask import request
from app import Flask, cache, db
from app.elastic import es
from datetime import datetime
from elasticsearch import Elasticsearch
from flask_login import current_user
from ..api import api
from app.Database import Report_index_data

#查询搜索数据类型
@api.route("/search-type/<content>")
@cache.cached(timeout=3600, key_prefix='search-type')
def search_type(content):
	body = {
	    "query":{
	        "match":{
	            "data": content
	        }
	    }
	}
	get = es.search(index="search-type",doc_type="data_type",body=body)
	out = get["hits"]["hits"]

	if(out):
		out_source = out[0]['_source']
		return json.dumps(out_source)
	else:
		return json.dumps(out)
		return '没有数据'


#搜索更多
@api.route("/get-more/<content>")
@cache.cached(timeout=36000, key_prefix='search_mvoe')
def search_more(content):
    peopledata = more_people(content)
    companydata = more_company(content)
    authcomdata = more_authcom(content)

    data = {'people':peopledata, 'company': companydata, 'authcom':authcomdata}
    return json.dumps(data)

    #查询人物
def more_people(content):
    timedata = (es.search(index="people", body={
            "size": 1,
                "query": {
                    "multi_match": {
                        "query": content,
                        "analyzer" : "ik_max_word",
                        "fields": ["name","info","keyword"],
                        },
                    },
                }))['hits']['hits']
    if (timedata):
        get = timedata[0]['_source']
        more_index = get['keyword']
        outmore = ((es.search(index="people", body={
            "size": 1,
                "query": {
                    "multi_match": {
                        "query": more_index,
                        "analyzer" : "ik_max_word",
                        "fields": ["name","info","keyword"],
                        },
                    },
                }))['hits']['hits'])

        data = [{'type': 'people','time':get, 'more':outmore }]#'more':outmore
    else: 
        data = ''
    return data

    #查询公司和组织
def more_company(content):
    timedata = (es.search(index="company", body={
            "size": 1,
                "query": {
                    "multi_match": {
                        "query": content,
                        "analyzer" : "ik_max_word",
                        "fields": ["name","info","search_keyword"],
                        },
                    },
                }))['hits']['hits']
    if (timedata):
        get = timedata[0]['_source']
        #more_index = get['people_keyword']
        #timedata_people_dict = ((es.search(index="people", body={'query': {'match': {'keyword': more_index}}}))['hits']['hits'])
        #timedata_people_dict = ''
        timedata_people_dict = ''
        data = [{'type': 'company', 'time': get, 'company_people': timedata_people_dict}]
        #print(timedata)
        #print(timedata_people_dict)
    else:
        data = ''
    return data

    #查询存在官网的
def more_authcom(content):
    timedata = (es.search(index="authcom", body={'query': {'match': {'keyword': content}}}))['hits']['hits']
    if (timedata):
        #print(timedata)
        data = [{'type': 'authcom','time': timedata}]
    else:
        data = ''
    return data

#举报请求
@api.route('/report', methods=["POST"])
def report_index():
    if request.method == 'POST':
        data_id = request.values.get('index-id')

        if data_id:
            if current_user.user_id:
                user = current_user.user_id
            else:
                user = ''

            if Report_index_data.query.filter_by(index_id = data_id, submit_userid = user).first():
                return json.dumps({'p': '你已提交过'})
                
            else:
                data = es.get(index='index', doc_type='index', id=data_id)
                sql = Report_index_data(index_id=data_id, index_name=data['_source']['title'], index_link=data['_source']['url'], submit_userid=user)
                db.session.add(sql) 
                db.session.commit()
                return json.dumps({'p': '感谢你的提交 我们将会在1-2个工作日内处理'})

        else:
            abort(404)
    else:
        abort(404)