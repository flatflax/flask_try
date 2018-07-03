from flask import Blueprint
from flask import g, request, flash, current_app, session
from flask import render_template, redirect, url_for
from models import Dashboard

bp = Blueprint('short', __name__)

@bp.route('/get')
def getShortLink():
    if not session.get('logged_in'):
        flash('Please login first.')
        return redirect(url_for('admin.login'))
    key = {}
    key['longlink'] = ''
    key['shortlink'] = ''
    key['value'] = 'getShortLink'
    return render_template('/short/getshort.html', key=key)  

@bp.route('/link/<link_id>', methods=['POST','GET'])
def ShortLink(link_id):
    if not session.get('logged_in'):
        flash('Please login first.')
        return redirect(url_for('admin.login'))
    if request.method == 'POST':
        pass