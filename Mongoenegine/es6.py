import mongoengine as db
from mongoengine import connect, Document, IntField, StringField, EmbeddedDocument
from typing import List

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

def iscrivi(studente: Student, course: Course):
    if course in studente.courses:
        raise ValueError("studente gia iscritto al corso")
    studente.courses.append(course)
    studente.save()

def lista_corsi_di_studente(studente: Student) -> list[Course]:
    crs = []
    for c in studente.courses:
        crs.append(c)
    return crs

def studenti_iscritti(corso: Course):
    listas=[]
    for s in Student.objects(courses = corso):
        listas.append(s)
    return listas

