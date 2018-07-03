from flask import Blueprint
from flask import g, request, flash, current_app, session
from flask import render_template, redirect, url_for
from models import Dashboard

bp = Blueprint('admin', __name__)

@bp.route('login/', methods=['GET', 'POST'])
def login():
    """User login/authentication/session management."""
    error = None
    if request.method == 'POST':
        if request.form['username'] != current_app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != current_app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('admin.index'))
    return render_template('/admin/login.html', error=error)


@bp.route('logout/')
def logout():
    """User logout/authentication/session management."""
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('admin.index'))

@bp.route('/')
def index():
    """display the iframe"""
    entries = Dashboard.query.all()
    return render_template('admin/index.html', entries=entries)