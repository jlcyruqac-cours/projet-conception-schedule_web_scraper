from typing import Optional

import bson
import bson.json_util
import json
from flask import render_template, Blueprint, redirect, session, jsonify, request

from database.models.users import User
from database.models.courses import Course

blueprint = Blueprint('account', __name__, template_folder='templates')


@blueprint.route('/database/get_courses', methods=['GET'])
def get_courses():
    result = Course.objects().all()

    result = result.to_json()

    return result


@blueprint.route('/database/get_user_courses', methods=['POST'])
def get_user_courses():
    user = User.objects(email=request.form['email']).first()

    courses_list = []

    if user:
        for course in user.courses:
            course_to_json = (Course.objects(id=course).first())
            course_to_json = course_to_json.to_json()
            courses_list.append(course_to_json)
        courses_list = json.dumps(courses_list)

    return courses_list

@blueprint.route('/database/create_user', methods=['POST'])
def create_user():
    # If no user with same email, add
    if not User.objects(email=request.form['email']):
        user = User()
        user.name = request.form['name']
        user.email = request.form['email']
        user.save()
        return "User successfully created"
    return "User already exist"


@blueprint.route('/database/add_course_to_user/<course_sigle>', methods=['POST'])
def add_course_to_user(course_sigle):
    # If no user with same email, add

    user = User.objects(email=request.form['email']).first()
    course = Course.objects(sigle=course_sigle).first()

    user.update(add_to_set__courses=course.id)

    return "User successfully created"

@blueprint.route('/database/update_courses_data', methods=['POST'])
def update_courses_data():
    courses = requests.post("http://localhost:7000/scraper/get_courses")

    courses = courses.json()
    for course in courses:
        mongo_course = Course()
        group = []
        group_index = []

        tmp_course_sigle_title = course[0].split(' ', 1)
        sigle = tmp_course_sigle_title[0]
        title = tmp_course_sigle_title[1].split('(', 1)[0]

        for index in range(len(course)):
            if 'Group' in course[index]:
                group_index.append(index)

        for index in group_index:

            group.append(course[index].split(' ')[1])

            group.append([])
            if len(course) > (index + 1):
                if 'Groupe' not in course[2]:
                    group[len(group) - 1].append(course[index + 1])
            if len(course) > (index + 2):
                if 'Groupe' not in course[3]:
                    group[len(group) - 1].append(course[index + 2])
            if len(course) > (index + 3):
                if 'Groupe' not in course[4]:
                    group[len(group) - 1].append(course[index + 3])

        mongo_course.sigle = sigle
        mongo_course.name = title
        mongo_course.group = group
        mongo_course.save()

    return "Success"
