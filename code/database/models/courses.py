import datetime
import mongoengine

class Course(mongoengine.Document):
    sigle = mongoengine.StringField(unique=True)
    group = mongoengine.StringField()
    name = mongoengine.StringField()
    local = mongoengine.StringField()
    # Dates : ex 110 lundi 10e periode dheure
    dates = mongoengine.ListField()

    meta = {
        'db_alias': 'core',
        'collection': 'courses',
        'indexes': [
            'sigle',
            'name'
        ]
    }