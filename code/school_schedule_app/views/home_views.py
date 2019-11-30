import json
import os

import requests
import requests_oauthlib
from flask import render_template, Blueprint, flash, redirect, request, session, url_for

blueprint = Blueprint('home', __name__, template_folder='templates')


@blueprint.route('/', methods=['GET'])
def index_get():
    try:
        if (session['fb_user']):
            # Get courses from database
            courses = requests.get("http://localhost:6000/database/get_courses")

            # Get user courses
            user_courses = requests.post("http://localhost:6000/database/get_user_courses", session['fb_user'])
            user_courses = user_courses
            print(json.dumps(user_courses))
            return render_template('home/index.html', name=session['fb_user']['name'],
                                   picture_url=session['fb_user']['picture']['data']['url'], courses=courses.json(),
                                   user_courses=user_courses)

    except:
        return redirect('/login')


@blueprint.route('/', methods=['POST'])
def index_post():
    requests.post("http://localhost:6000/database/add_course_to_user/" + request.form['course_select'],
                  session['fb_user'])
    return redirect("/")
