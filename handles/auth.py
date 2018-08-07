from flask import Blueprint
from flask import g, request, flash, current_app, session
from flask import render_template, redirect, url_for
from models import db,Dashboard,User,Submission

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
            session['right'] = user.right
            session['username'] = username
            session['user_id'] = user.userid
            session['blog_num'] = Submission.query.filter_by(suber_id=user.userid).count()
            flash('You were logged in')
            return redirect(url_for('auth.index'))
    return render_template('/auth/login.html', error=error)


@bp.route('logout/')
def logout():
    """User logout/authentication/session management."""
    session.pop('logged_in', None)
    session.pop('username', None)
    session.pop('user_id', None)
    session.pop('blog_num', None)
    flash('You were logged out')
    return redirect(url_for('auth.index'))

@bp.route('/')
def index():
    """display the iframe"""
    entries = Dashboard.query.all()
    return render_template('auth/index.html', entries=entries)

@bp.route('register/', methods=['POST','GET'])
def register():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        user = User(username=username,password=password,email=email,right=1)
        
        # if fliter error, return to register page
        fliter_result = register_fliter(user)
        if fliter_result:
            flash(fliter_result)
            entries = Dashboard.query.all()
            user = User(username='',password='',email='',right=1)
            return render_template('auth/register.html', entries=entries, user=user)

        db.session.add(user)
        db.session.commit()
        flash('You have register success.Please login.')
        return redirect(url_for('auth.index'))
    entries = Dashboard.query.all()
    user = User(username='',password='',email='',right=1)
    return render_template('auth/register.html', entries=entries, user=user)

def register_fliter(user):
    if User.query.filter_by(username=user.username).first():
        return "The username has been existed."
    return ""