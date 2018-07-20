from flask import Blueprint
from flask import g, request, flash, current_app, session
from flask import render_template, redirect, url_for
from models import Dashboard
from utils.users import login_required,admin_required

bp = Blueprint('submit', __name__)

@bp.route('/add')
@login_required
def submit_add():
	'''
	富文本编辑器
	提供给right=1的用户编辑及投稿
	'''
	pass