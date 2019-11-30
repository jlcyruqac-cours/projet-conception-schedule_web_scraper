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

    # print(bson.json_util.dumps(result))
    return result


@blueprint.route('/database/get_user_courses', methods=['POST'])
def get_user_courses():
    user = User.objects(email=request.form['email']).first()

    courses_list = []

    if user:
        print(user.courses)
        for course in user.courses:
            course_to_json = (Course.objects(id=course).first()).to_json()
            courses_list.append(course_to_json)

    return json.dumps(courses_list)

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
    # test = Course.objects(id=user.courses[0]).first()
    # print(test.name)
    user.update(add_to_set__courses=course.id)
    # user.save()
    return "User successfully created"
