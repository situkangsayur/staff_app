from flask import Flask
from flask_restx import Api
from flask_mongoengine import MongoEngine

# config untuk komunikasi dengan mongodb local
mongodb_config = {
        'db': 'sample',
        'host': 'localhost',
        'port': 27017
    }

# membuat objet MongoEngine (untuk koneksi)
db = MongoEngine()

# membuat restx api untuk nanti dihubungakan dengan flask app
# api = Api()

def create_app(mode):

    # inisialisasi aplikasi Flask (construct Flask object, name : app)
    app = Flask(__name__)

    '''
    uncomment baris dibawah untuk mengaktifkan mongodb
    tanpa mengaktifkan mongodb setting dibawah mongodb tidak terhubung
    '''
    # app.config['MONGODB_SETTINGS'] = mongodb_config
    
    # hubungkan mongoengine dengan flask app dengan method init_app pada mongoengine object
    db.init_app(app)

    # hubungkan restx api dengan flask app
    # api.init_app(app)

    # import view atau router untuk staff api rename atau beri nama alias staff api
    from .views.staff import blueprint as staff_api

    # add staff_api yang merupakan router ke restx api dengan method add_namespace
    app.register_blueprint(staff_api, url_prefix = '/api/v1/')

    # kembalikan flask app untuk dijalankan di tempat lain (file main.py)
    return app

