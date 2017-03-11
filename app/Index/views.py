from app.Index import index_api


@index_api.route('/group', methods=['GET'])
def all_group_details():
    pass


@index_api.route('/group/<int:group_id>', methods=['GET'])
def group_details(group_id):
    pass


@index_api.route('/group/participate', methods=['POST'])
def group_participate():
    pass
