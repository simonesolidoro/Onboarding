import pytest
import mongoengine as db
from mongoengine import connect, Document, IntField, StringField, EmbeddedDocument

from es6 import Course,Student,iscrivi,lista_corsi_di_studente,studenti_iscritti

@pytest.fixture
def db_es6():
    connect(db="learning_db", host="mongodb://localhost:27017/")
    Course.objects.delete()
    Student.objects.delete()
    Student(nome="simo", matricola="10656115").save()
    Student(nome="cri", matricola="10656114").save()
    Course(title="analisi1", code=1).save()
    Course(title="analisi2", code=2).save()
    Course(title="analisi3", code=3).save()
    Course(title="economia1", code=4).save()
    Course(title="economia2", code=5).save()
    yield
    Course.objects().delete()
    Student.objects().delete()

def test_iscrivi(db_es6):
    s = Student.objects(nome = "simo").first()
    c =  Course.objects(title="analisi1").first()
    iscrivi(s,c)
    assert c in s.courses

def test_lista_corsi_di_studente(db_es6):
    s = Student.objects(nome="simo").first()
    c = Course.objects(title="analisi1").first()
    c1 = Course.objects(title="analisi2").first()
    c2 = Course.objects(title="analisi3").first()
    iscrivi(s, c)
    iscrivi(s, c1)
    iscrivi(s, c2)
    lista_corsi = lista_corsi_di_studente(s)
    check = True
    if not c in lista_corsi or not c1 in lista_corsi or not c2 in lista_corsi:
        check = False
    assert check

def test_studenti_iscritti(db_es6):
    s = Student.objects(nome="simo").first()
    s1 = Student.objects(nome="cri").first()
    c = Course.objects(title="analisi1").first()
    iscrivi(s,c)
    iscrivi(s1,c)
    list_stud = studenti_iscritti(c)
    check = True
    if not s in list_stud or not s1 in list_stud:
        check = False
    assert check