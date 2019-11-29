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
    print(request.form)
    print(course_sigle)
    user = User.objects(email=request.form['email'])
    print(user)

    return "User successfully created"





