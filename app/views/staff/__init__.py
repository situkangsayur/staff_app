from flask import Blueprint
from flask_restx import Api
from .view import api as staff_api

blueprint = Blueprint('staff', __name__)

api = Api(blueprint,
          title = "Staff REST API",
          version = "1.0",
          description = "Sample Rest app")

api.add_namespace(staff_api, '/staff')

