import pytest
import mongoengine as db
from mongoengine import connect, Document, IntField, StringField, EmbeddedDocument
from es2 import Post,find_post,increment_views,sort_by_views_dec

@pytest.fixture
def db_es2():
    connect(db="learning_db", host="mongodb://localhost:27017/")
    Post.objects().delete()
    p1 = Post(title="My first post", body="hello world", tags=["primo", "test"]).save()
    p2 = Post(title="My second post", body="hello world2", tags=["second", "test"]).save()
    yield
    Post.objects().delete()

def test_find_post(db_es2):
    post = find_post("primo")[0]
    assert post.title == "My first post"

@pytest.mark.parametrize("n",[1,2,3,4,5])
def test_increment_views(db_es2,n):
    post = find_post("primo")[0]
    for _ in range(n):
        increment_views(post)
    #post.reload() #inserito in increment_view()
    assert post.views == n

def test_sort_decreasing_order(db_es2):
    increment_views(find_post("second")[0])
    increment_views(find_post("second")[0])
    sortdb = sort_by_views_dec()
    check = True
    for i in range(Post.objects.count()-1):
        if sortdb[i].views < sortdb[i+1].views:
            check = False
    assert check



