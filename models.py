from app import db


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