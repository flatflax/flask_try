from flask import Blueprint
from flask import g, request, flash, current_app, session,jsonify
from flask import render_template, redirect, url_for
from models import db,Dashboard,Submission,User
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
    if request.method == 'POST':
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

    if request.method == 'GET':
        submission = Submission.query.filter_by(sub_id=blog_id).first_or_404()
        user = User.query.filter_by(userid=submission.suber_id).first_or_404()
        result = {
            'sub_id' : submission.sub_id,
            'suber_id' : user.username,
            'title' : submission.title,
            'content' : submission.content
        }
        return jsonify(result)

    if request.method == 'UPDATE':
        data = request.get_json()
        time_now = time.strftime('%Y%m%d%H%M%S')

        title=data['title']
        content=data['content']
        suber_id=data['suber_id']
        aud_id=data['aud_id']
        status=data['status']

        submission = Submission.query.filter_by(sub_id=blog_id).first_or_404()
        submission.title = title if title else submission.title
        submission.content = content if content else submission.content
        submission.aud_id = aud_id if aud_id else submission.aud_id
        submission.aud_time = time_now if aud_id else submission.aud_time
        submission.suber_id = suber_id if suber_id else submission.suber_id
        submission.sub_time = time_now if suber_id else submission.sub_time
        submission.status = status if status else submission.status

        db.session.add(submission)
        db.session.commit()
        return jsonify({'result':'success'})

    if request.method == 'DELETE':
        submission = Submission.query.filter_by(sub_id=blog_id).first_or_404()
        db.session.delete(submission)
        db.session.commit()
        return jsonify({'result':'success'})

@bp.route('/main')
@login_required
def blog_main():
    user = User.query.filter_by(userid=session['user_id']).first_or_404()
    if user.right == 1:
        entries = Submission.query.filter_by(status=0).all()
    else:
        entries = Submission.query.filter_by(suber_id=session['user_id']).all()
    return render_template('/blog/main.html',entries=entries)