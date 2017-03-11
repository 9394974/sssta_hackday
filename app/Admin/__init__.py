from flask import Blueprint

admin_api = Blueprint('admin', __name__)

from . import views
