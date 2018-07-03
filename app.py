# -*- coding: UTF-8 -*- 
# imports
from flask import Flask, request, session, g, redirect, \
     abort, flash, jsonify
from sqlalchemy.sql import func
import os
import redis
from models import db,Dashboard


# grabs the folder where the script runs
basedir = os.path.abspath(os.path.dirname(__file__))


# configurationb
DATABASE = 'dashboard.db'
DEBUG = True
SECRET_KEY = 'my_precious'
USERNAME = 'admin'
PASSWORD = 'admin'

# REDIS_HOST = '43.82.163.74'
# REDIS_PORT = 6379

# defines the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)

# database config
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
SQLALCHEMY_TRACK_MODIFICATIONS = False  # 跟踪记录修改：False

# REDIS = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)

# create app
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

db.init_app(app)

from handles import manage,admin,short,dashboard
app.register_blueprint(manage.bp, url_prefix='/manage')
app.register_blueprint(admin.bp, url_prefix='/')
app.register_blueprint(short.bp, url_prefix='/short')
app.register_blueprint(dashboard.bp, url_prefix='/dashboard')



if __name__ == '__main__':
    app.run()
