import datetime
import mongoengine

class Course(mongoengine.Document):
    sigle = mongoengine.StringField(unique=True)
    group = mongoengine.StringField()
    name = mongoengine.StringField()
    credit = mongoengine.FloatField()
    dates = mongoengine.ListField()

    meta = {
        'db_alias': 'core',
        'collection': 'courses',
        'indexes': [
            'sigle',
            'name',
            'credit'
        ]
    }
    # TODO convertir jour/heure en code ex 101 = lundi am a 8h00 10 = 8h am 3 0 = 5 pm