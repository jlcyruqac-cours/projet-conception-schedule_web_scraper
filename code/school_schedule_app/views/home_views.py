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
            courses = requests.get("http://localhost:6000/database/get_courses")

            courses_list = []
            for course in courses.json():
                courses_list.append(course)
            return render_template('home/index.html', name=session['fb_user']['name'],
                                   picture_url=session['fb_user']['picture']['data']['url'], courses=courses_list)

    except:
        return redirect('/login')


@blueprint.route('/', methods=['POST'])
def index_post():

    requests.post("http://localhost:6000/database/add_course_to_user/" + request.form['course_select'], session['fb_user'])
    return redirect("/")
