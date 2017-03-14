from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os


db = SQLAlchemy()


def create_app(test=False):
    app = Flask(__name__)

    from config import config, test_config
    if test:
        app.config.update(test_config)
    else:
        app.config.update(config)

    db.init_app(app)

    from app.Admin import admin_api
    app.register_blueprint(admin_api)

    from app.Index import index_api
    app.register_blueprint(index_api)

    return app
