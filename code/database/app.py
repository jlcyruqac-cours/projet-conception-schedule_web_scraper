from flask import Flask, render_template, make_response, jsonify
import os
import sys
import re

from database.models import mongo_setup
from database.models.users import User
from models.courses import Course

app = Flask(__name__)

app.secret_key = 'super_awesome_project'

folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)


def load_courses():
    courses_list = []
    with open('courses_list.txt', 'r', encoding='iso-8859-1') as scraped_data:
        line = scraped_data.readline()
        cnt = 1
        while line:
            # print("Line {}: {}".format(cnt, line.strip()))
            course = Course()
            sigle = re.search('\d\w\w\w\d\d\d', line)
            line_without_sigle = line[8:]

            splited_line = line_without_sigle.split('(')
            # print(result)
            if sigle:
                course.sigle = (sigle.group())
                course.name = splited_line[0]

                print(course.sigle)
                print(course.name)
                course.save()


            else:
                if line.strip() == "du":
                    for index in range(12):
                        if index == 1 or index == 2 or index == 4 or index == 5 or index == 7 or index == 9 or index == 11:
                            # print(line)
                            a=1
                        line = scraped_data.readline()
            courses_list.append(course)
            line = scraped_data.readline()


def main():
    configure()
    app.run(debug=True, port=6000)


def configure():
    print("Configuring Flask app:")

    register_blueprints()
    print("Registered blueprints")

    setup_db()
    # load_courses()

def setup_db():
    mongo_setup.global_init()

    course = Course()
    # course.sigle = "6GEI445"
    # course.group = "0"
    # course.name = "Infographie"
    # course.local = "P2-1050"
    # course.dates = ["511", "512"]
    # course.save()
    #
    # course.sigle = "6GEI676"
    # course.group = "0"
    # course.name = "Circuit électrique"
    # course.local = "P1-5010"
    # course.dates = ["401", "402"]
    # course.save()


def register_blueprints():
    from views import database_views

    app.register_blueprint(database_views.blueprint)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    main()
else:
    configure()