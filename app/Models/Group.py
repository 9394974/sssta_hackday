from app import db


class Group(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    points = db.Column(db.Integer, default=0)

    def __init__(self, points=0):
        self.points = points



