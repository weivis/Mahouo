__author__ = 'Ran'
from app import Flask, cache
from ..api import api
from flask import render_template, request, url_for, jsonify, redirect, session
from datetime import datetime
from flask_login import current_user
from app.Database import Usermap, City_code
import json
import requests


#分类-国家
@api.route("/country=<country>")
@cache.cached(timeout=80000, key_prefix='country')
def get_country_all(country):
	country_list = City_code.query.filter_by(countryName=country).with_entities(City_code.areaID, City_code.areaName).all()
	new_country_list = list(set(country_list))
	country_data = [{
		'areaname':i.areaName,
		'areaid':i.areaID
	}for i in new_country_list]

	return json.dumps(country_data)


#分类-海外国家
@api.route("/country-haiwai=<city>")
@cache.cached(timeout=80000, key_prefix='country-haiwai')
def get_country_haiwai_all(city):
	country_list = country_list = City_code.query.filter_by(cityName=city).all()
	new_country_list = list(set(country_list))
	for i in (new_country_list):
		print(i.cityName, i.areaName, i.townName, i.townID)
	return ''


#分类-省
@api.route("/city=<city>")
@cache.cached(timeout=80000, key_prefix='city')
def get_city_all(city):
	country_list = City_code.query.filter_by(areaName=city).all()
	city_data = [{
		'cityname':i.townName,
		'cityid':i.townID
	}for i in country_list]
	return json.dumps(city_data)


#获取id
@api.route("/city-id=<city>")
@cache.cached(timeout=80000, key_prefix='city-id')
def get_cityid_all(city):
	cityid = City_code.query.filter_by(townName=city).first()
	cityiddata = cityid.townID
	return json.dumps(cityiddata)


#获取城市天气消息
@api.route("/weather=<city>")
def weather_data(city):
	url = "http://tj.nineton.cn/Heart/index/all?city=" + city
	jsonStr = requests.get(url).text
	return json.dumps(json.loads(jsonStr))


#获取用户设置的地址
@api.route("/user-map")
def user_map():
	if current_user.is_authenticated:
		return json.dumps({'type':'1', 'mapname':'', 'mapid':''})
		if Usermap.query.filter_by(userid=current_user.id).first(): #是否存在该数据行
			usermap_data = Usermap.query.filter_by(userid=current_user.id).first() #获取该行
			return json.dumps({'type':0,'countryName':usermap_data.countryName, 'mapname':usermap_data.mapname, 'mapid':usermap_data.mapid})  #, key=lambda x:x['sort'], reverse=True
		else:
			return json.dumps({'type':'1', 'mapname':'', 'mapid':''})
	else:
		return json.dumps({'type':'1', 'mapname':'', 'mapid':''})