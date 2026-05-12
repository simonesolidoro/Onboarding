import mongoengine as db
from mongoengine import connect, Document, IntField, StringField, EmbeddedDocument
import datetime
import email
from operator import index


class MongoengineEs1:
    class User(Document):
        email = db.StringField(required=True, unique=True)
        username = db.StringField()
        age = IntField(max_value=99, min_value=0)
        created_at = db.DateTimeField(default=datetime.datetime.now)
        is_active = db.BooleanField(default=True)
        def to_json(self):
            return {'email': self.email, 'username': self.username, 'age': self.age}





def mongoengine_es5():
    """
     post + comment (embedded and reference)
    """

    # #embedded
    # class Comment(EmbeddedDocument):
    #     body = db.StringField()
    # class Post(Document):
    #     title = db.StringField()
    #     coments = db.ListField(db.EmbeddedDocumentField(Comment))

    # reference
    class Post(db.Document):
        title = db.StringField()
    class Comment(db.Document):
        body = db.StringField()
        post = db.ReferenceField(Post, reverse_delete_rule=db.CASCADE)


    Post.objects().delete()
    Comment.objects().delete()
    p1 = Post(title= "vacanza")
    p1.save()
    p2 = Post(title= "scuola")
    p2.save()
    c1 = Comment(body = "che bello")
    c1.save()
    c2 = Comment(body = "che brutto")
    c2.save()
    c1.update(post = p1)
    c2.update(post = p2)

def mongoengine_es7():
    """
    ereditarietà
    """
    class Vehicle(db.Document):
        nome = db.StringField()
        ruote = db.IntField()
        peso = db.IntField()
        velocity = db.IntField(gt=0, lt=130)
        def to_json(self):
            return {"nome" : self.nome, "ruote" : self.ruote,"peso" : self.peso, "velocity" : self.velocity}
        meta = {'allow_inheritance': True}
    class Car(Vehicle):
        ruote = db.IntField(default=4)
        car_id = db.IntField()

    class Motorcycle(Vehicle):
        ruote = db.IntField(default=2)
        moto_id = db.IntField()

    class Truck(Vehicle):
        ruote = db.IntField(default=4)
        truck_id = db.IntField()

    c1 = Car(nome= "ford",peso = 1500, velocity = 100).save()
    m1 = Motorcycle(nome = "KTM", peso = 200, velocity = 130).save()
    t1 = Truck(nome = "range", peso = 3000, velocity= 90).save()

    print("print di Vehicle.objects():")
    for v in Vehicle.objects():
        print(v.to_json())
    print("print di car.objects():")
    for c in Car.objects():
        print(c.to_json())

def mongoengine_es8():
    class PostQueries:
        @staticmethod
        def published():
            # non capito
            pass

        @staticmethod
        def get_by_author(author_: str):
            return Post.objects(author = author_)

    class Post(Document):
        title = db.StringField()
        author = db.StringField()

    p1 = Post(title = "primoPost", author = "io").save()
    p2 = Post(title = "secondoPost", author = "io").save()
    p3 = Post(title = "terzoPost", author = "tu").save()
    p4 = Post(title = "quartoPost", author = "lui").save()
    post_io = PostQueries.get_by_author("io")
    for p in post_io:
        print(p.title)


if __name__ == '__main__':
    # pip install mongoengine
    import mongoengine as db
    from mongoengine import connect, Document, IntField, StringField, EmbeddedDocument
    import datetime

    connect(db="learning_db", host="mongodb://localhost:27017/")

    # mongoengine_es5()
    # mongoengine_es7()
    # mongoengine_es8()
