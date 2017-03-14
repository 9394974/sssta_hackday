# -*- coding: utf-8 -*-

from wtforms.fields import IntegerField, StringField, SelectField
from wtforms.validators import InputRequired, Optional, Email

from app import db

from app.constants import EMAIL_FORMAT_ERROR, CALL_NOT_NULL

from app.Models import Members, Group

from app.utils.forms import BaseForm
from app.utils.validators import (GroupExistValidators, FieldLengthValidators, PhoneFormatValidators, )


NAME_LENGTH = 20

QQ_LENGTH = 11

EMAIL_LENGTH = 50


college_choices = [
    (0, '软院'),
    (1, '计院')
]

grade_choices = [
    (0, '15级'),
    (1, '16级')
]


class GroupCheckForm(BaseForm):

    group_id = IntegerField(validators=[InputRequired("Group id is required."), GroupExistValidators()])


class GroupCreateForm(BaseForm):

    name = StringField(validators=[InputRequired("Name is required."), FieldLengthValidators(NAME_LENGTH)])

    college = SelectField(validators=[InputRequired("college is required.")], choices=college_choices, coerce=int)

    grade = SelectField(validators=[InputRequired('grade is required')], choices=grade_choices, coerce=int)

    qq = StringField(validators=[Optional(), FieldLengthValidators(QQ_LENGTH)])

    email = StringField(validators=[Optional(), FieldLengthValidators(EMAIL_LENGTH), Email(message=EMAIL_FORMAT_ERROR)])

    phone = StringField(validators=[Optional(), PhoneFormatValidators()])

    def validate(self):
        if not super(GroupCreateForm, self).validate():
            return False

        call_field = [self.qq, self.email, self.phone]
        if not any([bool(field.data.strip()) for field in call_field]):
            self.phone.errors.append(CALL_NOT_NULL)
            return False

        return True

    def create_group(self):
        group = Group()
        db.session.add(group)

        members = Members(name=self.name.data,
                          college=self.college.data,
                          grade=self.grade.data,
                          qq=self.qq.data,
                          email=self.email.data,
                          phone=self.phone.data,
                          group=group)
        db.session.add(members)
        db.session.commit()

        return {'group_id': group.id}



