import mongoengine as db
from mongoengine import connect, Document, IntField, StringField, EmbeddedDocument

class Post(Document):
    title = db.StringField()
    body = db.StringField()
    tags = db.ListField(StringField())
    views = db.IntField(default=0)


def increment_views(doc: Post):
    doc.update(inc__views=1)
    doc.reload()
    pass


def find_post(tag : str):
    return Post.objects(tags__in=[tag])


def sort_by_views_dec():
    return Post.objects().order_by("-views")