import datetime
import mongoengine

class Course(mongoengine.Document):
    sigle = mongoengine.StringField(unique=True)
    # group = mongoengine.StringField()
    name = mongoengine.StringField()
    # Dates : ex 110 lundi 10e periode dheure
    group = mongoengine.ListField()

    meta = {
        'db_alias': 'core',
        'collection': 'courses',
        'indexes': [
            'sigle',
            'name'
        ]
    }
