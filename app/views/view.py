from . import api
from flask import request, jsonify, make_response
from flask_restx import Resource
from ..utils.staf_dto import Staff
from ..models import Staff
import logging

'''
@api.route('/')
def hello():
    return 'hello world'


@api.route('/staff')
def staff():
    return 'hello staff'
'''
api = Staff.api
model = Staff.model

@api.route('')
class Staff(Resource):

    @api.response(201, 'add data success')
    @api.doc('crate new staff')
    @api.expect(model)
    def post(self):
        data = request.json 
        logging.debug(data) 
        staff = Staff(**data)
        staff.save()
        # process
        return make_response(jsonify(data), 201)
