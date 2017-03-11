from flask import Flask
from flask import request

app = Flask(__name__)

# Index api


@app.route('/group', methods=['GET'])
def all_group_details():
    pass


@app.route('/group/<int:group_id>', methods=['GET'])
def group_details(group_id):
    pass


@app.route('/group/participate', methods=['POST'])
def group_participate():
    pass


# Admin api

@app.route('/login', methods=['POST'])
def admin_login():
    pass


@app.route('/logout', methods=['GET'])
def admin_logout():
    pass


@app.route('/group/<int:group_id>/points', methods=['POST'])
def group_points(group_id):
    pass


@app.route('/group/<int:group_id>/delete', methods=['DELETE'])
def group_delete(group_id):
    pass


if __name__ == '__main__':
    app.debug = True
    app.run()
