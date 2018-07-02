# -*- coding: UTF-8 -*- 
# imports
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, jsonify
from sqlalchemy.sql import func
import os
import redis
from models import db,Dashboard


# grabs the folder where the script runs
basedir = os.path.abspath(os.path.dirname(__file__))


# configuration
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

from routes import admin
app.register_blueprint(admin.bp, url_prefix='/manage')

@app.route('/')
def index():
    """display the iframe"""
    entries = Dashboard.query.all()
    return render_template('index.html', entries=entries)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login/authentication/session management."""
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    """User logout/authentication/session management."""
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('index'))


@app.route('/dashboard/<post_id>', methods=['GET','POST'])
def show_dashboard(post_id):
    """Show iframe"""
    if request.method == 'GET':
        if not session.get('logged_in'):
            flash('Please login first.')
            return redirect(url_for('login'))
        elif session['logged_in'] == True:
            dashboard = Dashboard.query.filter_by(post_id=post_id).first()
            entries = Dashboard.query.all()
            if dashboard is None:
                abort(404)
            return render_template('dashboard.html', dashboard=dashboard, entries=entries)


@app.route('/getShort')
def getShortLink():
    if not session.get('logged_in'):
        flash('Please login first.')
        return redirect(url_for('login'))
    entries = Dashboard.query.all()
    key = {}
    key['longlink'] = ''
    key['shortlink'] = ''
    return render_template('getshort.html', entries=entries, key=key)  

@app.route('/link/<link_id>', methods=['POST','GET'])
def ShortLink(link_id):
    if not session.get('logged_in'):
        flash('Please login first.')
        return redirect(url_for('login'))
    if request.method == 'POST':
        pass


if __name__ == '__main__':
    app.run()
