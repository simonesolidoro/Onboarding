import email
from operator import index


def mongoengine_es1():
    class User(Document):
        email = db.StringField(required=True, unique=True)
        username = db.StringField()
        age = IntField(max_value=99, min_value=0)
        created_at = db.DateTimeField(default=datetime.datetime.now)
        is_active = db.BooleanField(default=True)
        def to_json(self):
            return {'email': self.email, 'username': self.username, 'age': self.age}
    User.objects().delete()
    simo = User(email="simosoli00@gmail.com", username = "simos", age = 26)
    cri =  User(email ="crisoli00@gmail.com",username = "cris",age = 26)
    ale = User(email = "alesoli04@gmail.com", username = "ales", age =22)
    simo.save()
    ale.save()
    cri.save()

    for user in User.objects():
        print(user.to_json())

def mongoengine_es2 ():
    class Post(Document):
        title = db.StringField()
        body = db.StringField()
        tags = db.ListField(StringField())
        views = db.IntField(default=0)
    Post.objects().delete()
    p1 = Post(title = "My first post", body = "hello world", tags = ["primo","test"])
    p1.save()
    p2 = Post(title="My second post", body="hello world2", tags=["second", "test"])
    p2.save()
    def increment_views(doc):
        doc.update(inc__views = 1)
    def find_post (tag):
        return Post.objects(tags__in = [tag])
    def sort_by_views_dec():
        Post.objects().order_by("-views")

    posts = find_post("primo")
    for p in posts:
        increment_views(p)

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

if __name__ == '__main__':
    # pip install mongoengine
    import mongoengine as db
    from mongoengine import connect, Document, IntField, StringField, EmbeddedDocument
    import datetime

    connect(db="learning_db", host="mongodb://localhost:27017/")

    # mongoengine_es2()
    # mongoengine_es1()
    # mongoengine_es3()
    mongoengine_es4()



