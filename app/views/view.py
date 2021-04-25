from flask import request, jsonify, make_response
from flask_restx import Resource
# import StafDto yang merupakan struktur data json body request api staff
from ..utils.staf_dto import StaffDto

# import model mongoengine staff untuk berkomunikasi dengan mongoengine collection/table staff
from ..models import Staff

# import app context dari flask untuk dapat memanfaatkan fitur yang ada app flask
from flask import current_app as app

# url rest tanpa menggunakan flask_restx
'''
@api.route('/')
def hello():
    return 'hello world'


@api.route('/staff')
def staff():
    return 'hello staff'
'''
# ampbil restx api yang terbentuk di StafffDto
api = StaffDto.api

# ambil mode rest json yang ada pada class StaffDto
model = StaffDto.model

# url atau endpoint untuk api staff di definisikan di decorator @api.route()
@api.route('')
class StaffRoute(Resource):

    '''
        decorator untuk dokumentasi dan validasi:
        api.response: mendefinisikan berbagai informasi message code, 201 untuk success
        api.doc : dokumen informasi atau descripsi endpoint 
        api.expect : structure data yang diharapkan diberikan saat request dibuat
            api.exect memilik parameter validate untuk memvalidasi berbagai kondisi 
                seprti tidak boleh null, tidak boleh tidak diisi, atau tipe data sesuai
            @api.expect(model, validate = True)
    '''
    @api.response(201, 'add data success')
    @api.doc('crate new staff')
    @api.expect(model)
    def post(self):
        
        # ambil data json (request body) dari request yang masuk, dalam bentuk dict()
        data = request.json 

        # construct object staff dari class model Staff turunan kelas Document mongoengine
        # passing data sebagai parameters constructor Staff Model dengan menggunakan double *
        staff = Staff(**data)

        # panggil method save() untuk menyimpan data yang sudah dibangun sebelumnya
        staff.save()

        # logging pada flask app
        app.logger.debug(data)

        # berikan response jika proses sudah selesai
        return make_response(jsonify(data), 201)
