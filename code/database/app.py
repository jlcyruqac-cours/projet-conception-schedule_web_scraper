from flask import Flask, render_template
import os
import sys

from database.models import mongo_setup
from database.models.users import User
from models.courses import Course

app = Flask(__name__)

app.secret_key = 'super_awesome_project'

folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)


def main():
    configure()
    app.run(debug=True, port=6000)


def configure():
    print("Configuring Flask app:")

    register_blueprints()
    print("Registered blueprints")

    setup_db()

def setup_db():
    mongo_setup.global_init()
    # user = User()
    # user.first_name = "test3"
    # user.last_name = "test3_last"
    # user.email = "test3@gmail.com"
    # user.courses = ['5dd3047ff733ff70c1d9676a', '5dd304b5c6dc473f891ed4dd']
    # user.save()
    course = Course()
    course.sigle = '6GEI100'
    course.name = "Cours de marde 1"
    course.credit = 3.0
    course.days = ['mardi', 'jeudi']
    course.save()

def register_blueprints():
    from views import database_views

    app.register_blueprint(database_views.blueprint)


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('error/404.html', vm=None)


if __name__ == '__main__':
    main()
else:
    configure()
