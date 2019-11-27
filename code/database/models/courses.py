import datetime
import mongoengine

class Course(mongoengine.Document):
    sigle = mongoengine.StringField(primary_key=True)
    name = mongoengine.StringField()
    credit = mongoengine.FloatField()
    days = mongoengine.ListField()
    start_time = mongoengine.ListField()
    end_time = mongoengine.ListField()

    meta = {
        'db_alias': 'core',
        'collection': 'courses',
        'indexes': [
            '',
            'name',
            'credit'
        ]
    }
    # TODO convertir jour/heure en code ex 101 = lundi am a 8h00 10 = 8h am 30 = 5 pm