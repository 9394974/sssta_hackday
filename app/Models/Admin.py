from app import db


class Admin(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(200))

    def __init__(self, name, password):
        self.name = name
        self.ps = password

    def __repr__(self):
        return '<Admin %r>' % self.name
