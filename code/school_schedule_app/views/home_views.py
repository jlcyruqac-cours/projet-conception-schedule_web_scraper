import os

import requests_oauthlib
from flask import render_template, Blueprint, flash, redirect, request, session, url_for
from requests_oauthlib.compliance_fixes import facebook_compliance_fix, facebook

blueprint = Blueprint('home', __name__, template_folder='templates')

@blueprint.route('/', methods=['GET'])
def index_get():
    try:
        if (session['fb_user']):
            return render_template('home/index.html', name=session['fb_user']['name'],
                                   picture_url=session['fb_user']['picture']['data']['url'])

    except:
        return redirect('/login')


@blueprint.route('/', methods=['POST'])
def index_post():
     # Success
    return redirect("/")
