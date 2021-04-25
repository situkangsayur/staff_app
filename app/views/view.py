from flask import request, jsonify, make_response
from flask_restx import Resource
from ..utils.staf_dto import StaffDto
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
api = StaffDto.api
model = StaffDto.model

@api.route('')
class StaffRoute(Resource):

    @api.response(201, 'add data success')
    @api.doc('crate new staff')
    @api.expect(model)
    def post(self):
        data = request.json 
        staff = Staff(**data)
        staff.save()
        return make_response(jsonify(data), 201)
