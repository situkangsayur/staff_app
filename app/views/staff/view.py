from flask import request, jsonify, make_response
from flask_restx import Resource
# import StafDto yang merupakan struktur data json body request api staff
from app.utils.staf_dto import StaffDto

# import model mongoengine staff untuk berkomunikasi dengan mongoengine collection/table staff
from app.models import Staff

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
@api.route('/')
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

    @api.response(200, 'get all staff data')
    @api.doc('get all staff data from staff collection')
    def get(self):

        try:
            staf_list = list(Staff.objects())
            return make_response(jsonify(staf_list), 200)
        
        except Exception as es:
            # Logger.error(es, exc_info = 1)
            return make_response(jsonify({'message' : 'err when get all data', 'code' : 500}), 500)



@api.route('/<id>')
class StaffIDRoute(Resource):

    @api.response(200, 'data ditemukan')
    @api.doc('update  staff')
    def get(self, id):
       
        response = {'message' : 'data telah ditemukan', 'code' : 200}

        try:
            # ambil data json (request body) dari request yang masuk, dalam bentuk dict()
            data = request.json 

            # checking if the id of the staff is exists
            check = Staff.objects(id = id)[0]
            if len(check) == 0:
                response['message'] = 'data gagal diupdate, data tidak ditemukan'
                response['code'] = 404
            else:
                return make_response(jsonify(check), 200)

        except Exception as ex:
            # Logger.error('error gagal update ', exc_info = 1)
            response['message'] = 'error exception'
            response['code'] = 500

        # berikan response jika proses sudah selesai
        return make_response(response, response['code'])


    @api.response(200, 'add data success')
    @api.doc('update  staff')
    @api.expect(model)
    def put(self, id):
        
        response = {'message' : 'data telah diupdate', 'code' : 200}
        try:
            # ambil data json (request body) dari request yang masuk, dalam bentuk dict()
            data = request.json 

            # checking if the id of the staff is exists
            check = Staff.objects(id = id)[0]
            if len(check) > 0:
                # construct object staff dari class model Staff turunan kelas Document mongoengine
                # passing data sebagai parameters constructor Staff Model dengan menggunakan double *
                staff = Staff(**data)

                # panggil method save() untuk menyimpan data yang sudah dibangun sebelumnya
                staff.save()

                # logging pada flask app
                app.logger.debug(data)
            else:
                response['message'] = 'data gagal diupdate, data tidak ditemukan'
                response['code'] = 404

        except Exception as ex:
            #Logger.error('error gagal update ', exc_info = 1)
            response['message'] = 'error exception'
            response['code'] = 500

        # berikan response jika proses sudah selesai
        return make_response(response, response['code'])

    @api.response(200, 'delete data success')
    @api.doc('delte  staff')
    def delete(self, id):
        
        response = {'message' : 'data telah dihapus', 'code' : 200}
        try:
            # ambil data json (request body) dari request yang masuk, dalam bentuk dict()

            # checking if the id of the staff is exists
            check = Staff.objects(id = id)
            if len(check) > 0:
                staff = Staff.objects(id = id).delete()

            else:
                response['message'] = 'data gagal diupdate, data tidak ditemukan'
                response['code'] = 404

        except Exception as ex:
            # Logger.error('error gagal update ', exc_info = 1)
            app.logger.error(ex, exc_info= 1)
            response['message'] = 'error exception'
            response['code'] = 500

        # berikan response jika proses sudah selesai
        return make_response(response, response['code'])
