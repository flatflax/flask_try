# create_db.py

from app import app
from models import *


db.init_app(app)
with app.app_context():
    # create the database and the db table
    db.drop_all()
    db.create_all()

    title1 = Dashboard(title="【赤ティン】局外人",url="//player.bilibili.com/player.html?aid=21938672&cid=36235459&page=1")
    title2 = Dashboard(title='【赤ティン】梦中之梦',url='//player.bilibili.com/player.html?aid=20992195&cid=34418092&page=1')
    title3 = Dashboard(title='【赤ティン】只为生命',url='//player.bilibili.com/player.html?aid=19315003&cid=31498603&page=1')

    admin = User(username='admin',password='admin',email='admin@example.com',right=0)

    db.session.add(title1)
    db.session.add(title2)
    db.session.add(title3)
    db.session.add(admin)

    # commit the changes
    db.session.commit()
'''

# create the database and the db table
db.create_all()

# commit the changes
db.session.commit()
'''