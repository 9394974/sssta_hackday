import os

config = {

    'SQLALCHEMY_DATABASE_URI': ''.join(["sqlite:///", os.path.join(os.path.dirname(__file__), 'database.db')]),

    'SQLALCHEMY_TRACK_MODIFICATIONS': False,

    'JSON_AS_ASCII': False
}


test_config = {

    'SQLALCHEMY_DATABASE_URI': ''.join(["sqlite:///", os.path.join(os.path.dirname(__file__), 'test_database.db')]),

    'SQLALCHEMY_TRACK_MODIFICATIONS': False,

    'JSON_AS_ASCII': False
}

