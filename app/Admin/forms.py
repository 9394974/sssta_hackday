from wtforms.fields import IntegerField, StringField, PasswordField
from wtforms.validators import InputRequired

from flask_login import login_user

from app import db

from app.constants import PASSWORD_WRONG

from app.Models import Group, Admin

from app.Index.forms import GroupCheckForm

from app.utils.forms import BaseForm
from app.utils.validators import PositiveFieldValidators, FieldLengthValidators


NAME_LENGTH = 20


class AdminLoginForm(BaseForm):

    def __init__(self, *args, **kwargs):
        super(AdminLoginForm, self).__init__(*args, **kwargs)
        self.user = None

    username = StringField(validators=[InputRequired("username is required."), FieldLengthValidators(NAME_LENGTH)])
    password = PasswordField(validators=[InputRequired("password is required.")])

    def validate(self):
        if not super(AdminLoginForm, self).validate():
            return False

        self.user = Admin.query.filter_by(name=self.username.data, password=self.password.data).first()

        if self.user is None:
            self.password.errors.append(PASSWORD_WRONG)
            return False

        return True

    def login(self):
        login_user(self.user)


class GroupPointsForm(GroupCheckForm):

    points = IntegerField(validators=[InputRequired("points is required."), PositiveFieldValidators()])

    def set_group_points(self):
        group = Group.query.get(self.group_id.data)
        group.points = self.points.data

        db.session.add(group)
        db.session.commit()


class GroupDeleteForm(GroupCheckForm):

    def delete_group(self):
        group = Group.query.get(self.group_id.data)

        db.session.delete(group)
        db.session.commit()

