from flask import Blueprint

api = Blueprint('staff', __name__)

from . import view

