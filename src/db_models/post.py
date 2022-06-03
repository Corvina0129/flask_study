from settings import db


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    body = db.Column(db.String(255))

    def __init__(self, title, body):
        self.title = title
        self.body = body

    def __repr__(self):
        return f'Title: {self.title}, body: {self.body}'
