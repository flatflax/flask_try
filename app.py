# imports
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
import os


# grabs the folder where the script runs
basedir = os.path.abspath(os.path.dirname(__file__))


# configuration
DATABASE = 'dashboard.db'
DEBUG = True
SECRET_KEY = 'my_precious'
USERNAME = 'admin'
PASSWORD = 'admin'

# defines the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)

# database config
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
SQLALCHEMY_TRACK_MODIFICATIONS = False  # 跟踪记录修改：False

# create app
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
db = SQLAlchemy(app)

import models


@app.route('/')
def index():
    """display the iframe"""
    entries = models.Dashboard.query.all()
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
    if request.method == 'GET':
        if not session.get('logged_in'):
            flash('Please login first.')
            return redirect(url_for('login'))
        elif session['logged_in'] == True:
            dashboard = models.Dashboard.query.filter_by(post_id=post_id).first()
            entries = models.Dashboard.query.all()
            if dashboard is None:
                abort(404)
            return render_template('dashboard.html', dashboard=dashboard, entries=entries)


if __name__ == '__main__':
    app.run()
