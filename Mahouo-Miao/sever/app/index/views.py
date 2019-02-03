__author__ = 'Ran'
from app import Flask
from ..index import index
from flask import render_template, session, redirect, abort, request
from flask_login import current_user
import json

@index.route('/')
def view_index():
    return render_template('index.html')