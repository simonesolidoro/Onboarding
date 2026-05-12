import mongoengine as db
from mongoengine import connect, Document, IntField, StringField, EmbeddedDocument
from datetime import datetime, timedelta
from Mongoenegine.es4 import Author


class Profile(EmbeddedDocument):
    id = db.IntField(gt = 0)
    username = db.StringField()

class Adress(EmbeddedDocument):
    street = db.StringField()
    city = db.StringField()
    zip_code = db.IntField()
    country = db.StringField()

class User(Document):
    email = db.StringField(required=True)  # unique= True
    username = db.StringField()
    age = IntField(max_value=99, min_value=0)
    created_at = db.DateTimeField(default=datetime.datetime.now)
    is_active = db.BooleanField(default=True)
    adresses = db.EmbeddedDocumentListField(Adress)
    profile = db.EmbeddedDocument(Profile)

class Comment(EmbeddedDocument):
    body = db.StringField()
    author = db.ReferenceField(User)
class Post(Document):
    title = db.StringField()
    body = db.StringField()
    tags = db.ListField(StringField())
    created_at = db.DateTimeField(default=datetime.utcnow)
    views = db.IntField(default=0)
    author = db.ReferenceField(User, reverse_delete_rule=db.CASCADE) # cancelando autore si caneclla anche il post
    comments = db.EmbeddedDocumentListField(Comment)

class Category(Document):
    nome = db.StringField()
    posts = db.ListField(db.ReferenceField(Post))

class QuerySet:

    def by_tag(self, tag : str):
        return Post.objects(tags__in = [tag])

    def recent(self, days):
        limite = datetime.utcnow() - timedelta(days=days)
        return Post.objects(created_at__gte=limite)

class PostRepository:
    # non capito
    pass