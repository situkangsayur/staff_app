from .view import api as staff_api

def add_namespace_staff(api):
    api.add_namespace(staff_api, path = '/api/staff')



