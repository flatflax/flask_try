from flask import Blueprint
from flask import g, request, flash, current_app, session
from flask import render_template, redirect, url_for
from models import db,Dashboard,User

bp = Blueprint('auth', __name__)

@bp.route('login/', methods=['GET', 'POST'])
def login():
    """User login/authentication/session management."""
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user is None :
            error = 'Invalid username'
        elif user.password != password :
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            session['username'] = username
            flash('You were logged in')
            return redirect(url_for('auth.index'))
    return render_template('/auth/login.html', error=error)


@bp.route('logout/')
def logout():
    """User logout/authentication/session management."""
    session.pop('logged_in', None)
    session.pop('username', None)
    flash('You were logged out')
    return redirect(url_for('auth.index'))

@bp.route('/')
def index():
    """display the iframe"""
    entries = Dashboard.query.all()
    return render_template('auth/index.html', entries=entries)

@bp.route('register/', methods=['POST','GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        user = User(username=username,password=password,email=email)
        db.session.add(user)
        db.session.commit()
        flash('You have register success.Please login.')
        return redirect(url_for('auth.index'))
    entries = Dashboard.query.all()
    user = User(username='',password='',email='')
    return render_template('auth/register.html', entries=entries, user=user)

def register_fliter(user):
    # 用户名是否重复
    pass