from flask import Blueprint

index_api = Blueprint('index', __name__)

from . import views
