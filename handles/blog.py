from flask import Blueprint
from flask import g, request, flash, current_app, session,jsonify
from flask import render_template, redirect, url_for
from models import db,Dashboard,Submission
from utils.users import login_required,admin_required
import time

bp = Blueprint('blog', __name__)

@bp.route('/add')
@login_required
def blog_add():
    user_id = session['user_id']
    time_now = time.strftime('%Y%m%d%H%M%S')
    submission = Submission(suber_id=user_id,sub_time='',title='',content='',status=0)
    key = "create"
    return render_template('/blog/add.html',submission=submission,key=key)

@bp.route('/id/<blog_id>',methods=['POST','GET','UPDATE','DELETE'])
@login_required
def blog(blog_id):
    if request.method=='POST':
        time_now = time.strftime('%Y%m%d%H%M%S')

        data = request.get_json()
        suber_id=data['suber_id']
        sub_time=time_now
        title=data['title']
        content=data['content']
        status=0

        submission = Submission(suber_id=suber_id,sub_time=sub_time,title=title,content=content,status=status)

        db.session.add(submission)
        db.session.commit()

        return jsonify({'result':'success'})