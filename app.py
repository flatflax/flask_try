# -*- coding: UTF-8 -*- 
# imports
from flask import Flask
import os
import redis
from celery import Celery
from models import db


def create_app(config=None):
    app = Flask(__name__)
    app.config.from_pyfile('_settings.py')
    return(app)

def register_database(app):
    with app.app_context():
        db.init_app(app)

def register_admin(app):
    from flask_admin import Admin
    from models import User,Dashboard,Submission
    from modelview import BaseModelview
    admin = Admin(app, name='apps', template_mode='bootstrap3')
    admin.add_view(BaseModelview(User, db.session,name=u'用户管理'))
    admin.add_view(BaseModelview(Dashboard, db.session, name=u'标签管理'))
    admin.add_view(BaseModelview(Submission, db.session, name=u'投稿管理'))

def register_blueprint(app):
    from handles import manage,auth,short,dashboards,test,blog
    app.register_blueprint(manage.bp, url_prefix='/manage')
    app.register_blueprint(auth.bp, url_prefix='/')
    app.register_blueprint(short.bp, url_prefix='/short')
    app.register_blueprint(dashboards.bp, url_prefix='/dashboards')
    app.register_blueprint(test.bp, url_prefix='/test')
    app.register_blueprint(blog.bp, url_prefix='/blog')

def register_logger(app):
	pass

def register_celery(app):
    celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)


if __name__ == '__main__':
    app = create_app()
    register_database(app)
    register_admin(app)
    register_blueprint(app)
    # register_celery(app)
    app.run()
