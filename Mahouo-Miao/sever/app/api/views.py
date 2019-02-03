__author__ = 'Ran'
from app import Flask, db, cache
from ..api import api
from flask import render_template, session, redirect, abort, request, jsonify
from flask_login import current_user
from app.Database import Index_commonly_com, Classification_com, Uc_page, Bangumi

@api.route('/bangumi', methods=["POST"])
@cache.cached(timeout=50 * 60)
def bangumi():
    data = Bangumi.query.filter_by().all()
    all_day = [{
        'name':i.name,
        'cover':i.cover,
        'url':i.url,
        'zhou':i.day,
    }for i in data]
    day1 = [{
        'name':i.name,
        'cover':i.cover,
        'url':i.url,
        'zhou':i.day,
    }for i in data if i.day == 1]

    day2 = [{
        'name':i.name,
        'cover':i.cover,
        'url':i.url,
        'zhou':i.day,
    }for i in data if i.day == 2]

    day3 = [{
        'name':i.name,
        'cover':i.cover,
        'url':i.url,
        'zhou':i.day,
    }for i in data if i.day == 3]

    day4 = [{
        'name':i.name,
        'cover':i.cover,
        'url':i.url,
        'zhou':i.day,
    }for i in data if i.day == 4]

    day5 = [{
        'name':i.name,
        'cover':i.cover,
        'url':i.url,
        'zhou':i.day,
    }for i in data if i.day == 5]

    day6 = [{
        'name':i.name,
        'cover':i.cover,
        'url':i.url,
        'zhou':i.day,
    }for i in data if i.day == 6]

    day7 = [{
        'name':i.name,
        'cover':i.cover,
        'url':i.url,
        'zhou':i.day,
    }for i in data if i.day == 7]

    daylist = {
        'all':all_day,
        'day1':day1,
        'day2':day2,
        'day3':day3,
        'day4':day4,
        'day5':day5,
        'day6':day6,
        'day7':day7,
    }
    return jsonify(daylist)


@api.route('/hot-uc', methods=["POST"])
@cache.cached(timeout=5 * 60)
def hot_uc():
    data = Uc_page.query.filter_by(status=1).all()
    json = [{
        'name':i.name,
        'url':i.url,
        'sort':i.sorll,
    }for i in data]
    return jsonify(sorted(json, key=lambda x:x['sort'], reverse=True))


@api.route('/commonly-com', methods=["POST"])
@cache.cached(timeout=120 * 60)
def commonly_com():
    data = Index_commonly_com.query.filter_by(status=1).all()
    json = [{
        'name':i.name,
        'ico':i.ico,
        'url':i.url,
        'sort':i.sorll,
    }for i in data]
    return jsonify(sorted(json, key=lambda x:x['sort'], reverse=True))


@api.route('/classification-comlist', methods=["POST"])
@cache.cached(timeout=120 * 60)
def classification_com():
    data1 = Classification_com.query.filter_by(classification=1 ,status=1).all()
    data2 = Classification_com.query.filter_by(classification=2 ,status=1).all()
    data3 = Classification_com.query.filter_by(classification=3 ,status=1).all()
    data4 = Classification_com.query.filter_by(classification=4 ,status=1).all()
    tp1 = [{
        'name':i.name,
        'ico':i.ico,
        'url':i.url,
        'sort':i.sorll,
    }for i in data1]
    tp2 = [{
        'name':i.name,
        'ico':i.ico,
        'url':i.url,
        'sort':i.sorll,
    }for i in data2]
    tp3 = [{
        'name':i.name,
        'ico':i.ico,
        'url':i.url,
        'sort':i.sorll,
    }for i in data3]
    tp4 = [{
        'name':i.name,
        'ico':i.ico,
        'url':i.url,
        'sort':i.sorll,
    }for i in data4]

    jsdata = {
        'data1':sorted(tp1, key=lambda x:x['sort'], reverse=True),
        'data2':sorted(tp2, key=lambda x:x['sort'], reverse=True),
        'data3':sorted(tp3, key=lambda x:x['sort'], reverse=True),
        'data4':sorted(tp4, key=lambda x:x['sort'], reverse=True),
    }
    return jsonify(jsdata)