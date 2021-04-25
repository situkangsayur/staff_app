from .. import db

# membuat kelas Staff untuk model yang merepresentasikan struktu data di mongodb
# Class diturunkan dari kelas Document mongodb, sehingga class Staff model memiliki
# fitur seperti kelas Document
class Staff(db.Document):
    nama = db.StringField()
    email = db.StringField()
    phone_number = db.StringField()
