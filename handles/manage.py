from flask import Blueprint
from flask import g, request, flash, current_app, session
from flask import render_template, redirect, url_for
from models import Dashboard
from utils.users import login_required,admin_required

bp = Blueprint('manage', __name__)

@bp.route('/update/<post_id>')
@login_required
@admin_required
def manage_update(post_id):
    entry = Dashboard.query.filter_by(post_id=post_id).first()
    # set key:Update
    key = {}
    key['value'] = 'Update'
    key['method'] = 'PUT'
    return render_template('/manage/linkinfo.html', entry=entry, key=key)

@bp.route('/add')
@login_required
@admin_required
def manage_add():
    # create new blank entry
    entry = Dashboard(title='',url='')
    # set key:Add
    key = {}
    key['value'] = 'Add'
    key['method'] = 'POST'
    return render_template('/manage/linkinfo.html', key=key, entry=entry)

@bp.route('/')
@login_required
@admin_required
def manage():
    """User manage link of iframe"""
    entries = Dashboard.query.all()
    return render_template('/manage/manage.html', entries=entries)

@bp.route('/id/<post_id>', methods=['POST','DELETE'])
@login_required
@admin_required
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