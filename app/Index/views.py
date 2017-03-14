from flask import jsonify, request

from werkzeug.datastructures import MultiDict

from app.Index import index_api
from app.Index.queries import (get_all_group_information,get_one_group_information )
from app.Index.forms import (GroupCheckForm, GroupCreateForm)

from app.utils.utils import response_dict

from app.constants import (SUCCESS, )


@index_api.route('/group', methods=['GET'])
def all_group_details():
    data = get_all_group_information()
    return jsonify(response_dict(SUCCESS, data=data))


@index_api.route('/group/<int:group_id>', methods=['GET'])
def group_details(group_id):
    form = GroupCheckForm(MultiDict([('group_id', group_id), ]), csrf_enabled=False)
    if form.validate():
        data = get_one_group_information(form.group_id.data)
        return jsonify(response_dict(SUCCESS, data=data))
    else:
        return jsonify(form.error_detail())


@index_api.route('/group/participate', methods=['POST'])
def group_participate():
    form = GroupCreateForm(request.form, csrf_enabled=False)
    if form.validate():
        data = form.create_group()
        return jsonify(response_dict(SUCCESS, data=data))
    else:
        return jsonify(form.error_detail())
