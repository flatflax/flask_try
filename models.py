from exts import db

class Dashboard(db.Model):

    __tablename__ = "dashboard"

    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)

    def __init__(self, title, url):
        self.title = title
        self.url = url

    def __repr__(self):
        return '<title %r>' % self.title

class User(db.Model):
    
    __tablename__ = 'user'

    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return '<title %r>' % self.username