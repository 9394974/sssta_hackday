from app import db


class Members(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(20))

    college = db.Column(db.Integer)

    grade = db.Column(db.Integer)

    qq = db.Column(db.String(20), default='')

    phone = db.Column(db.String(11), default='')

    email = db.Column(db.String(50), default='')

    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))

    group = db.relationship('Group', backref=db.backref('members', lazy='dynamic'))

    def __init__(self, name, college, grade, group, qq='', phone='', email=''):
        self.name = name
        self.college = college
        self.grade = grade
        self.group = group

        self.qq = qq
        self.phone = phone
        self.email = email

    def __repr__(self):
        return '<Members %s >' % self.name

