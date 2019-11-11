import os
from flask import render_template, Blueprint, flash, redirect, request, session, url_for

blueprint = Blueprint('home', __name__, template_folder='templates')


@blueprint.route('/', methods=['GET'])
def index_get():
    return render_template('home/index.html')


@blueprint.route('/', methods=['POST'])
def index_post():
     # Success
    return redirect("/")
