from os import name

import pytest
import mongoengine as db
from mongoengine import connect, Document, IntField, StringField, EmbeddedDocument

from es4 import Author,Post,all_posts, author_of_post

@pytest.fixture
def db_es4():
    connect(db="learning_db", host="mongodb://localhost:27017/")
    Author.objects.delete()
    Post.objects.delete()
    a1 = Author(name="Mario Rossi").save()
    a2 = Author(name="Laura Bianchi").save()
    a3 = Author(name="Giovanni Verdi").save()
    Post(title="Intro a Python", body="Python è un linguaggio versatile", author=a1).save()
    Post(title="Flask base", body="Flask è un microframework", author=a1).save()
    Post(title="MongoDB guida", body="NoSQL e documenti", author=a2).save()
    Post(title="MongoEngine ORM", body="ODM per MongoDB", author=a2).save()
    Post(title="AI basics", body="Introduzione all'AI", author=a3).save()
    Post(title="Deep Learning", body="Reti neurali profonde", author=a3).save()
    yield
    Author.objects.delete()
    Post.objects.delete()

def test_all_posts(db_es4):
    posts_of_mario = all_posts(Author.objects(name= "Mario Rossi")[0])
    title_post_of_mario = []
    for p in posts_of_mario:
        title_post_of_mario.append(p.title)
    check = True
    if not "Intro a Python" in title_post_of_mario or not "Flask base" in title_post_of_mario:
        check =  False
    assert check

def test_author_of_post(db_es4):
    assert "Mario Rossi" == author_of_post(Post.objects(title = "Intro a Python")[0]).name
