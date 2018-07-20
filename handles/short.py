from flask import Blueprint
from flask import g, request, flash, current_app, session
from flask import render_template, redirect, url_for
from models import Dashboard
from utils.users import login_required

bp = Blueprint('short', __name__)

@bp.route('/get')
@login_required
def getShortLink():
    key = {}
    key['longlink'] = ''
    key['shortlink'] = ''
    key['value'] = 'getShortLink'
    return render_template('/short/getshort.html', key=key)  

@bp.route('/link/<link_id>', methods=['POST','GET'])
@login_required
def ShortLink(link_id):
    pass