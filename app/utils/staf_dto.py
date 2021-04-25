from flask_restx import Namespace, fields


class Staff():

    api = Namespace('Staff API', description = 'sample api for staff')

    model = api.model('staff', {
        'nama' : fields.String(),
        'email' : fields.String(),
        'phone_number' : fields.String()
    })
