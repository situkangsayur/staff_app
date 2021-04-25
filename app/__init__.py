from flask import Flask
from flask_restx import Api
from flask_mongoengine import MongoEngine

mongodb_config = {
        'db': 'sample',
        'host': 'localhost',
        'port': 27017
    }
db = MongoEngine()

api = Api()

def create_app(mode):

    app = Flask(__name__)
    # uncomment baris dibawah untuk mengaktifkan mongodb
    # tanpa mengaktifkan mongodb setting dibawah mongodb tidak terhubung
    # app.config['MONGODB_SETTINGS'] = mongodb_config

    db.init_app(app)
    api.init_app(app)

    from .views.view import api as staff_api
    api.add_namespace(staff_api, path = '/api/staff')

    return app

