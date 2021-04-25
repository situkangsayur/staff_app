from flask import Flask
from flask_restx import Api
from .views.view import api as staff_api
from .views import  api
from flask_mongoengine import MongoEngine

db = MongoEngine()

def create_app(mode):
   app = Flask(__name__)
   db.init_app(app)
   # app.register_blueprint(api, url_prefix = '/api/')
   api = Api(app)

   from .views.view import Staff
   api.add_namespace(staff_api, path = '/api/staff')

   return app

