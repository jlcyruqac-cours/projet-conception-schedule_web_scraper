import datetime
import mongoengine

class User(mongoengine.Document):
    first_name = mongoengine.StringField()
    last_name = mongoengine.StringField()
    perm_code = mongoengine.StringField()
    hashed_password = mongoengine.StringField()
    email = mongoengine.StringField(unique=True)
    created_date = mongoengine.DateTimeField(default=datetime.datetime.now())
    courses = mongoengine.ListField(mongoengine.ObjectIdField())

    meta = {
        'db_alias' : 'core',
        'collection': 'users',
        'indexes': [
            'email',
            'hashed_password',
            'created_date'
        ]
    }