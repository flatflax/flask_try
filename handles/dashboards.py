from flask import Blueprint
from flask import g, request, flash, current_app, session
from flask import render_template, redirect, url_for
from models import Dashboard

bp = Blueprint('dashboards', __name__)

@bp.route('/<post_id>', methods=['GET','POST'])
def show(post_id):
    """Show iframe"""
    if request.method == 'GET':
        if not session.get('logged_in'):
            flash('Please login first.')
            return redirect(url_for('login'))
        elif session['logged_in'] == True:
            dashboard = Dashboard.query.filter_by(post_id=post_id).first()
            if dashboard is None:
                abort(404)
            return render_template('dashboards/dashboard.html', dashboard=dashboard)