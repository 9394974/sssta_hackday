from flask import request, jsonify
from flask_login import login_required, logout_user

from werkzeug.datastructures import MultiDict

from app.Admin import admin_api
from app.Admin.forms import GroupPointsForm, GroupDeleteForm, AdminLoginForm

from app.utils.utils import response_dict

from app.constants import SUCCESS


@admin_api.route('/login', methods=['POST'])
def admin_login():
    form = AdminLoginForm(request.form)
    if form.validate():
        form.login()
        return jsonify(response_dict(SUCCESS))
    else:
        return jsonify(form.error_detail())


@admin_api.route('/logout', methods=['GET'])
@login_required
def admin_logout():
    logout_user()
    return jsonify(response_dict(SUCCESS))


@admin_api.route('/group/<int:group_id>/points', methods=['POST'])
@login_required
def group_points(group_id):
    post_data = MultiDict({
        'group_id': group_id,
        'points': request.form.get('points', None)
    })
    form = GroupPointsForm(post_data)
    if form.validate():
        form.set_group_points()
        return jsonify(response_dict(SUCCESS))
    else:
        return jsonify(form.error_detail())


@admin_api.route('/group/<int:group_id>', methods=['DELETE'])
@login_required
def group_delete(group_id):
    form = GroupDeleteForm(MultiDict({'group_id': group_id}))
    if form.validate():
        form.delete_group()
        return jsonify(response_dict(SUCCESS))
    else:
        return jsonify(form.error_detail())
