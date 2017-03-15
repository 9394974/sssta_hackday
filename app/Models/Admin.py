from flask_login import UserMixin

from app import db, login_manager


class Admin(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    password = db.Column(db.String(200))

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def __repr__(self):
        return '<Admin %r>' % self.name


@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(user_id)
