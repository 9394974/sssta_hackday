from app import db


class Members(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(20))

    college = db.Column(db.Integer)

    grade = db.Column(db.Integer)

    qq = db.Column(db.String(20))

    phone = db.Column(db.String(11))

    email = db.Column(db.String(50))

    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))

    captain = db.relationship('Group', backref='captain', lazy='dynamic')
