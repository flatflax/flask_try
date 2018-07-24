from flask import Blueprint
from flask import g, request, flash, current_app, session,jsonify
from flask import render_template, redirect, url_for
from models import Dashboard

bp = Blueprint('test', __name__)

@bp.route('/_add_numbers', methods=['POST','GET','DELETE'])
def add_numbers():
	data = request.get_json()
	result = int(data['a']) + int(data['b'])
	return jsonify({"result":result})

@bp.route('/')
def index():
	return render_template('/test/index.html')
