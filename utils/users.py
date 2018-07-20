from functools import wraps
from flask import g, request, redirect, url_for, session, flash

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            flash('Sorry.Login Required.')
            return redirect(url_for('auth.login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session['right'] != 0:
            flash('Sorry.Admin Required.')
            return redirect(url_for('auth.index', next=request.url))
        return f(*args, **kwargs)
    return decorated_function