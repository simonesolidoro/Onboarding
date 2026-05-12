import mongoengine as db
from mongoengine import connect, Document, IntField, StringField, EmbeddedDocument
from typing import List

class Author(Document):
    name = db.StringField()

class Post(Document):
    title = db.StringField()
    body = db.StringField()
    author = db.ReferenceField(Author, reverse_delete_rule=db.CASCADE) # cancelando autore si caneclla anche il post

def all_posts(author_ : Author) -> List[Post]:
    post_of_a = []
    for p in Post.objects(author = author_):
        post_of_a.append(p)
    return post_of_a

def author_of_post(post : Post):
    return post.author
