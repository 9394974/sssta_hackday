from app import db


class Group(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    captain = db.Column(db.Integer, db.ForeignKey('members.id'))

    points = db.Column(db.Integer, default=0)

    members = db.relationship('Members', backref='group', lazy='dynamic')
