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
    right = db.Column(db.Integer, default=1)

    '''
    user right
    0:admin
    1:common user
    2:guess?
    '''

    def __init__(self, username, password, email, right):
        self.username = username
        self.password = password
        self.email = email
        self.right = right

    def __repr__(self):
        return '<title %r>' % self.username

class Submission(db.Model):

    __tablename__ = 'submission'

    '''
    submission
    audit
    '''
    sub_id = db.Column(db.Integer, primary_key=True)
    suber_id = db.Column(db.Integer, nullable = False)
    auder_id = db.Column(db.Integer)
    sub_time = db.Column(db.String, nullable = False)
    aud_time = db.Column(db.String, nullable = False)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    status = db.Column(db.Integer, nullable = False)

    def __init__(self, suber_id, sub_time, title, content, status):
        self.suber_id = suber_id
        self.sub_time = sub_time
        self.auder_id = 0
        self.aud_time = ''
        self.title = title
        self.content = content
        self.status = status

    def __repr__(self):
        return '<title %r>' % self.title