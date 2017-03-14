from app.Admin import admin_api


@admin_api.route('/login', methods=['POST'])
def admin_login():
    pass


@admin_api.route('/logout', methods=['GET'])
def admin_logout():
    pass


@admin_api.route('/group/<int:group_id>/points', methods=['POST'])
def group_points(group_id):
    pass


@admin_api.route('/group/<int:group_id>', methods=['DELETE'])
def group_delete(group_id):
    pass
