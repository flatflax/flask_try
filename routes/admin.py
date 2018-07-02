from flask import Blueprint
from flask import g, request, flash, current_app, session
from flask import render_template, redirect, url_for
from models import Dashboard

bp = Blueprint('admin', __name__)

@bp.route('/update/<post_id>')
def manage_update(post_id):
    if not session.get('logged_in'):
        flash('Please login first.')
        return redirect(url_for('login'))
    elif session['logged_in'] == True:
        entries = Dashboard.query.all()
        entry = Dashboard.query.filter_by(post_id=post_id).first()
        # set key:Update
        key = {}
        key['value'] = 'Update'
        key['method'] = 'PUT'
        return render_template('/admin/linkinfo.html', entry=entry, entries=entries, key=key)

@bp.route('/add')
def manage_add():
    if not session.get('logged_in'):
        flash('Please login first.')
        return redirect(url_for('login'))
    elif session['logged_in'] == True:
        # create new blank entry
        entry = Dashboard(title='',url='')
        entries = Dashboard.query.all()
        # set key:Add
        key = {}
        key['value'] = 'Add'
        key['method'] = 'POST'
        return render_template('/admin/linkinfo.html', key=key, entry=entry, entries=entries)

@bp.route('/')
def manage():
    """User manage link of iframe"""
    if not session.get('logged_in'):
        flash('Please login first.')
        return redirect(url_for('login'))
    elif session['logged_in'] == True:
        entries = Dashboard.query.all()
        return render_template('/admin/manage.html', entries=entries)

@bp.route('/id/<post_id>', methods=['POST','DELETE'])
def link_post_id(post_id):
    """
    POST : Add new link
    PUT : Modify existed link
    GET : Get more info the link
    DELETE : Delete the link
    """
    from models import db
    if request.method == 'POST':
        if request.form["_method"] == 'DELETE':
            d = Dashboard.query.filter_by(post_id=post_id).first_or_404()
            db.session.delete(d)
            db.session.commit()
            flash('Delete Success.')
            return redirect('/manage')
        if request.form["_method"] == 'PUT':
            d = Dashboard.query.filter_by(post_id=post_id).first_or_404()
            d.title = request.form["title"]
            d.url = request.form["url"]
            db.session.add(d)
            db.session.commit()
            flash('Update Success.')
            return redirect('/manage')
        else :
            d = Dashboard(title=request.form["title"], url=request.form["url"])
            db.session.add(d)
            db.session.commit()
            flash('Add Success.')
            return redirect('/manage')
    if request.method == 'PUT':
        entry = Dashboard.query.filter_by(post_id=post_id).first().update(title=request.form["title"],url=request.form["url"])
        flash('Update Success.')
        return redirect('/manage')