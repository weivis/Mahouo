from elasticsearch import Elasticsearch
from app.elastic import es
from datetime import datetime

res = es.index(index="mahouo_es_index", doc_type='tweet', body={
    'title': '登录你的Mahouo账号',
    'url': 'www.account.mahouo.com/sign-in',
    'info': '登录Mahouo账号以便同步数据和使用我们的应用',
    'keywords':'', #关键词
    'description':'', #网页描述
    'pic': 'mahoulogin',
    'deta': '0000-00-00',
    'tcp': 'http'+'://',
    'timestamp': datetime.now(),
})

res = es.index(index="mahouo_es_index", doc_type='tweet', body={
    'title': 'Mahouo',
    'url': 'www.mahouo.com',
    'info': 'Mahouo魔法搜索 快来变成魔法少女吧！',
    'keywords':'', #关键词
    'description':'', #网页描述
    'pic': 'mahou',
    'deta': '0000-00-00',
    'tcp': 'http'+'://',
    'timestamp': datetime.now(),
})

res = es.index(index="mahouo_es_index", doc_type='tweet', body={
    'title': 'Mahouo图站',
    'url': 'painting.mahouo.com',
    'info': '分享你的绘画作品 或者来欣赏别人的作品吧也',
    'keywords':'', #关键词
    'description':'', #网页描述
    'info': '能找壁纸哟 分享图包哟！',
    'pic': '',
    'deta': '0000-00-00',
    'tcp': 'http'+'://',
    'timestamp': datetime.now(),
})

res = es.index(index="mahouo_es_index", doc_type='tweet', body={
    'title': 'Mahouo天气',
    'url': 'www.weather.mahouo.com',
    'info': '关注天气信息 出门不用担心-说不定明天会下雨哟',
    'keywords':'', #关键词
    'description':'', #网页描述
    'pic': '',
    'deta': '0000-00-00',
    'tcp': 'http'+'://',
    'timestamp': datetime.now(),
})

res = es.index(index="mahouo_es_index", doc_type='tweet', body={
    'title': 'Mahouo番剧',
    'url': 'bangumi.mahouo.com',
    'info': '一起追番吧 米娜！',
    'keywords':'', #关键词
    'description':'', #网页描述
    'pic': '',
    'deta': '0000-00-00',
    'tcp': 'http'+'://',
    'timestamp': datetime.now(),
})

res = es.index(index="mahouo_es_index", doc_type='tweet', body={
    'title': 'Mahouo日历',
    'url': 'Calendar.mahouo.com',
    'info': '查看年历 给自己设定任务安排时间 并提醒你执行',
    'keywords':'', #关键词
    'description':'', #网页描述
    'pic': '',
    'deta': '0000-00-00',
    'tcp': 'http'+'://',
    'timestamp': datetime.now(),
})

res = es.index(index="mahouo_es_index", doc_type='tweet', body={
    'title': 'Mahouo Pro',
    'url': 'pro.mahouo.com',
    'info': 'Mahouo-Por 乐趣分享关 注新鲜事',
    'keywords':'', #关键词
    'description':'', #网页描述
    'pic': '',
    'deta': '0000-00-00',
    'tcp': 'http'+'://',
    'timestamp': datetime.now(),
})
#es.indices.refresh(index="mahouo_es_index")

#多域名格式
res = es.index(index="mahouo_es-son_link", doc_type='mc-link', id=1, body={

	#主域名
    'maintitle': 'Mahouo',
    'mainurl': 'www.mahouo.com',
    'maininfo': 'Mahouo-魔法搜索 快来变成魔法少女吧！',
    'mainpic': 'mahou',
    'maindeta': '0000-00-00',
    'tcp': 'http'+'://',

    #子域名
    'son1title': 'Mahouo-sgin-in',
    'son1info': '登录Mahou账号以便同步数据和使用我们的应用',
    'son1url': 'account.mahouo.com/sign-in',
    'tcp': 'http'+'://',

    'son2title': 'Mahouo图站',
    'son2info': '分享你的绘画作品 或者观赏别人的作品吧！',
    'son2url': 'painting.mahouo.com',
    'tcp': 'http'+'://',

    'son3title': 'Mahouo天气',
    'son3info': '我感觉明天会下雨',
    'son3url': 'weather.mahouo.com',
    'tcp': 'http'+'://',

    'son4title': 'Mahouo番剧',
    'son4info': '追番吧 追番吧！',
    'son4url': 'bangumi.mahouo.com',
    'tcp': 'http'+'://',

    'timestamp': datetime.now(),
})

#es.indices.refresh(index="mahouo_es-son_link")

#认证网站
res = es.index(index="authcom", doc_type='authcom', id=1, body={
    'cover':'mahouo.jpg',
    'title':'Mahouo',
    'info':'MAHOUO 生态 掌握核心科技',
    'com':'mahouo.com',
    'http':'1', #0=http , 1=https
})
#公司或组织
res = es.index(index="company", doc_type='company', id=1, body={
    'cover':'cover.jpg',
    'name':'Mahouo',
    'info':'Mahouo搜索引擎',
    'com':'mahouo.com',
    'the': 'Mahouo'
})
#人
res = es.index(index="people", doc_type='people', id=3, body={
    'cover': '123.jpg',
    'name': '阿基米德',
    'title': '伟大的古希腊哲学家',
    'the': 'scholar',
})

#es.indices.refresh(index="people")
#es.indices.refresh(index="company")
#es.indices.refresh(index="authcom")
#es.indices.refresh(index="mahouo_es-son_link")
#es.indices.refresh(index="mahouo_es_index")