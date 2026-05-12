import mongoengine as db
from mongoengine import connect, Document, IntField, StringField, EmbeddedDocument
import datetime

class Adress(EmbeddedDocument):
    street = db.StringField()
    city = db.StringField()
    zip_code = db.IntField()
    country = db.StringField()
    def to_json(self):
        return {'city': self.city, 'street': self.street, 'zip_code': self.zip_code, 'country': self.country}

class User(Document):
    email = db.StringField(required=True)  # unique= True
    username = db.StringField()
    age = IntField(max_value=99, min_value=0)
    created_at = db.DateTimeField(default=datetime.datetime.now)
    is_active = db.BooleanField(default=True)
    adresses = db.EmbeddedDocumentListField(Adress)

    def to_json(self):
        return {'email': self.email, 'username': self.username, 'age': self.age}


def es3():
    connect(db="learning_db", host="mongodb://localhost:27017/")
    User.objects().delete()
    ind1 = Adress(street="via Garbagnate", city="lainate", zip_code=20045, country="Italia")
    ind2 = Adress(street="via Garbagnate", city="lainate", zip_code=20020, country="Italia")
    User(email="simosoli==@gmail.com", username="simos", age=26, adresses=[ind1, ind2]).save()
    User(email="simosoli00@gmail.com", username="simos", age=26, adresses=[ind1, ind2]).save()
    User(email="crisoli00@gmail.com", username="cris", age=26).save()
    User(email="alesoli04@gmail.com", username="ales", age=22).save()
    for u in User.objects():
        print(u.to_json())
        print("ha i seguenti indirizzi")
        for ad in u.adresses:
            print(ad.to_json())
es3()