from flask import Flask

from app.Admin import admin_api
from app.Index import index_api


def create_app():
    app = Flask(__name__)

    app.register_blueprint(admin_api)
    app.register_blueprint(index_api)

    return app
