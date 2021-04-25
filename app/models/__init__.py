from ..app import db

class Staff(db.Document):
    nama = db.StringField()
    email = db.StringField()
    phone_number = db.StringField()
