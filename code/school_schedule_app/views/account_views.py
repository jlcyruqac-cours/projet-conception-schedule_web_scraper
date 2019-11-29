import os

import requests_oauthlib
from flask import render_template, Blueprint, redirect, session, request, make_response
from flask_login import login_manager

import school_schedule_app.infrastructure.cookie_auth as cookie_auth

FB_CLIENT_ID = ''
FB_CLIENT_SECRET = ''

FB_AUTHORIZATION_BASE_URL = "https://www.facebook.com/dialog/oauth"
FB_TOKEN_URL = "https://graph.facebook.com/oauth/access_token"

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

FB_SCOPE = ["email"]

blueprint = Blueprint('account', __name__, template_folder='templates')


# LOGIN
@blueprint.route('/login', methods=['GET'])
def login_get():
    if request.cookies:
        return redirect('/')

    else:
        return render_template('account/login.html', vm=None)


@blueprint.route('/fb_login', methods=['GET', 'POST'])
def fb_login_post():
    facebook = requests_oauthlib.OAuth2Session(
        FB_CLIENT_ID, redirect_uri="http://localhost:5000/fb_callback", scope=FB_SCOPE
    )
    authorization_url, _ = facebook.authorization_url(FB_AUTHORIZATION_BASE_URL)

    return redirect(authorization_url)


@blueprint.route('/fb_callback')
def callback(facebook_compliance_fix=None):
    facebook = requests_oauthlib.OAuth2Session(
        FB_CLIENT_ID, scope=FB_SCOPE, redirect_uri="http://localhost:5000/fb_callback"
    )
    print(facebook)
    # we need to apply a fix for Facebook here
    # facebook = facebook_compliance_fix(facebook)

    facebook.fetch_token(
        FB_TOKEN_URL,
        client_secret=FB_CLIENT_SECRET,
        authorization_response=request.url,
    )

    # Fetch a protected resource, i.e. user profile, via Graph API

    facebook_user_data = facebook.get(
        "https://graph.facebook.com/me?fields=id,name,email,picture{url}"
    ).json()

    email = facebook_user_data["email"]
    name = facebook_user_data["name"]
    picture_url = facebook_user_data.get("picture", {}).get("data", {}).get("url")

    session['fb_user'] = facebook_user_data

    return redirect('/')


# LOGOUT

@blueprint.route('/logout')
def logout():
    session.clear()

    return redirect('/login')
