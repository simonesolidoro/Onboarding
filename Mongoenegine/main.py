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






def mongoengine_es3 ():
    """
    embedded document e list of embedded documents

    """
    class Adress(EmbeddedDocument):
        street = db.StringField()
        city = db.StringField()
        zip_code = db.IntField()
        country = db.StringField()
    class User(Document):
        email = db.StringField(required=True)#unique= True
        username = db.StringField()
        age = IntField(max_value=99, min_value=0)
        created_at = db.DateTimeField(default=datetime.datetime.now)
        is_active = db.BooleanField(default=True)
        adresses = db.EmbeddedDocumentListField(Adress)
        def to_json(self):
            return {'email': self.email, 'username': self.username, 'age': self.age}
    User.objects().delete()
    ind1 = Adress(street = "via Garbagnate", city = "lainate", zip_code= 20045, country= "Italia")
    ind2 = Adress(street="via Garbagnate", city="lainate", zip_code=20020, country="Italia")
    simo = User(email= "simosoli==@gmail.com", username = "simos", age = 26, adresses = [ind1, ind2])
    simo.save()
    simo2 = User(email= "simosoli00@gmail.com", username = "simos", age = 26, adresses = [ind1, ind2])
    simo2.save()
    cri = User(email="crisoli00@gmail.com", username="cris", age=26)
    cri.save()
    ale = User(email="alesoli04@gmail.com", username="ales", age=22)
    ale.save()

    us = []
    for u26 in User.objects(age = 26):
        us.append(u26)
    for u in us:
        print(u.to_json())

    print(User.objects().count())
    for i in User.objects(adresses__country="Italia"):
        print( i.to_json())

def mongoengine_es4():
    class Author(Document):
        name = db.StringField()
    class Post(Document):
        title = db.StringField()
        body = db.StringField()
        author = db.ReferenceField(Author, reverse_delete_rule=db.CASCADE) # cancelando autore si caneclla anche il post 
    Author.objects.delete()
    Post.objects.delete()
    # creto dataset con chatgpt
    a1 = Author(name="Mario Rossi").save()
    a2 = Author(name="Laura Bianchi").save()
    a3 = Author(name="Giovanni Verdi").save()
    Post(title="Intro a Python", body="Python è un linguaggio versatile", author=a1).save()
    Post(title="Flask base", body="Flask è un microframework", author=a1).save()
    Post(title="MongoDB guida", body="NoSQL e documenti", author=a2).save()
    Post(title="MongoEngine ORM", body="ODM per MongoDB", author=a2).save()
    Post(title="AI basics", body="Introduzione all'AI", author=a3).save()
    Post(title="Deep Learning", body="Reti neurali profonde", author=a3).save()

    #tutti i post di a1
    id_a1 = a1.id
    post_of_a1 = []
    for p in Post.objects(author=a1):
        post_of_a1.append(p.title)
        print(p.title)
    print(Post.objects.count())
    a1.delete()
    print(Post.objects.count())

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
def mongoengine_es6():
    """
    many-to-many
    """
    class Course(db.Document):
        title = db.StringField()
        code = db.IntField(required=True, unique=True)
        def __str__(self):
            return self.title

    class Student(db.Document):
        nome = db.StringField()
        matricola = db.IntField(unique=True)
        courses = db.ListField(db.ReferenceField(Course))
        def to_json(self):
            return {"name" : self.nome, "matricola" : self.matricola}

    Course.objects().delete()
    Student.objects().delete()
    def iscrivi(studente: Student, course: Course):
        # if course in studente.courses:
        #     raise ValueError("studente gia iscritto al corso")
        studente.courses.append(course)
        studente.save()
    def lista_corsi_di_studente(studente: Student) -> list[Course]:
        crs = []
        for c in studente.courses:
            crs.append(c)
            print(c)
        return crs
    def studenti_iscritti(corso: Course):
        listas=[]
        for s in Student.objects(courses = corso):
            print(s.to_json())
            listas.append(s)
        return listas


    s1 = Student(nome= "simo", matricola = "10656115").save()
    s2 = Student(nome= "cri", matricola = "10656114").save()
    c1 = Course(title = "analisi1", code = 1).save()
    c2 = Course(title = "analisi2", code = 2).save()
    c3 = Course(title = "analisi3", code = 3).save()
    c4 = Course(title = "economia1", code = 4).save()
    c5 = Course(title = "economia2", code = 5).save()

    iscrivi(s1,c1)
    iscrivi(s1,c2)
    iscrivi(s1,c3)
    iscrivi(s2,c4)
    iscrivi(s2,c5)
    iscrivi(s1,c4)
    lista_corsi_di_studente(s1)
    studenti_iscritti(c4)

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
        def get_by_author(author: str):
            return Post.objects(author = author)

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

    # mongoengine_es2()
    mongoengine_es1()
    # mongoengine_es3()
    # mongoengine_es4()
    # mongoengine_es5()
    # mongoengine_es6()
    # mongoengine_es7()
    # mongoengine_es8()
