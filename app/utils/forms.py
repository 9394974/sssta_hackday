from flask_wtf import Form

from app.utils.utils import response_dict
from app.constants import PARM_FORMAT_ERROR


class BaseForm(Form):

    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)

    def error_detail(self):

        # only return the first error
        for field in self.errors:
            for error in self.errors[field]:
                if isinstance(error, int):
                    return response_dict(error)
                elif isinstance(error, str):
                    return response_dict(PARM_FORMAT_ERROR, message=error)

    class Meta:
        csrf = False
