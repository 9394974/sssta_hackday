from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS


db = SQLAlchemy()
login_manager = LoginManager()


def create_app(test=False):
    app = Flask(__name__)

    from config import config, test_config
    if test:
        app.config.update(test_config)
    else:
        app.config.update(config)

    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

    db.init_app(app)
    login_manager.init_app(app)
    CORS(app)

    from app.Admin import admin_api
    app.register_blueprint(admin_api, url_prefix='/api')

    from app.Index import index_api
    app.register_blueprint(index_api, url_prefix='/api')

    from app.constants import USER_NOT_LOGIN
    from app.utils.utils import response_dict

    @app.errorhandler(401)
    def user_not_login(e):
        return jsonify(response_dict(USER_NOT_LOGIN))

    # account for test
    from app.Models import Admin
    with app.app_context():
        db.create_all()
        if Admin.query.filter_by(name='sssta_admin').first() is None:
            admin = Admin(name='sssta_admin', password='2333')
            db.session.add(admin)
            db.session.commit()

    return app

