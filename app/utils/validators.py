from wtforms.validators import ValidationError

from app.Models import Group
from app.constants import (GROUP_NOT_EXIST, PHONE_FORMAT_ERROR)


class FieldLengthValidators(object):

    def __init__(self, max_length, message=None):
        self.max_length = max_length
        self.message = message

    def __call__(self, form, field):
        raw_string = field.data
        if len(raw_string) > self.max_length:
            if self.message is None:
                self.message = "".join([field.short_name, "must less than ", str(self.max_length), "characters."])

            raise ValidationError(self.message)


class PhoneFormatValidators(object):

    def __call__(self, form, field):
        phone = field.data
        if not phone.isdigit() and len(phone) != 11:
            raise ValidationError(PHONE_FORMAT_ERROR)


class GroupExistValidators(object):

    def __call__(self, form, field):
        group_id = field.data
        group = Group.query.get(group_id)
        if not group:
            raise ValidationError(GROUP_NOT_EXIST)
