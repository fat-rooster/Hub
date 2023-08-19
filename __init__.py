from flask import Blueprint

hub = Blueprint('Hub', __name__)

from . import routes