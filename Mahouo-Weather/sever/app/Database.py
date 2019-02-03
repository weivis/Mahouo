# -*- coding: utf-8 -*-
from flask import Flask, request
from app import db

class Usermap(db.Model):
    __tablename__ = 'usermap'

    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Text)
    mapid = db.Column(db.Text)
    mapname = db.Column(db.Text)
    countryName = db.Column(db.Text)

    def __init__(self, userid=None, mapid=None, mapname=None, countryName=None):
        self.countryName = countryName
        self.userid = userid
        self.mapid = mapid
        self.mapname = mapname
        update()

    def update(self):
        db.session.add(self)
        db.session.commit()

class City_code(db.Model):
    __tablename__ = 'city_code'

    ID = db.Column(db.Integer, primary_key=True)
    countryID = db.Column(db.Text)
    countryName = db.Column(db.Text)
    countryEN = db.Column(db.Text)
    areaID = db.Column(db.Text)
    areaName = db.Column(db.Text)
    areaEN = db.Column(db.Text)
    cityID = db.Column(db.Text)
    cityName = db.Column(db.Text)
    cityEN = db.Column(db.Text)
    townID = db.Column(db.Text)
    townName = db.Column(db.Text)
    townEN = db.Column(db.Text)

    def __init__(self, countryID=None, countryName=None, countryEN=None,
        areaID=None, areaName=None, areaEN=None,
        cityID=None, cityName=None, cityEN=None,
        townID=None, townName=None, townEN=None):
        self.countryID = countryID
        self.countryName = countryName
        self.countryEN = countryEN
        self.areaID = areaID
        self.areaName = areaName
        self.areaEN = areaEN
        self.cityID = cityID
        self.cityName = cityName
        self.cityEN = cityEN
        self.townID = townID
        self.townEN = townEN
        self.townName = townName

#db.drop_all()
#db.create_all()