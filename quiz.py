from mongoengine import Document, StringField, ListField, IntField, ReferenceField, DictField

class Answer(Document):
    name = StringField()
    link = StringField()
    point = IntField()

class Question(Document):
    question = ListField(ReferenceField(Answer))

class PersonType(Document):
    name = StringField()
    des = StringField()
    suited = StringField()
    total_points = IntField()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
